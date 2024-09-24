from ...database.database import session
from ..models.car import Car
import pandas as pd
from ...schemas import CarSchema
from ...middleware.cache import cache_response
from sqlalchemy.exc import SQLAlchemyError

def get_car_info(car_id: int):
    car = session.query(Car).filter(Car.id == car_id).first()

    if not car:
        return None

    return car.to_dict()


def update_car(car_id: int, car_data: dict):
    car = session.query(Car).filter(Car.id == car_id).first()
    if not car:
        return None

    for key, value in car_data.items():
        if value:
            setattr(car, key, value)

    session.commit()
    return car.to_dict()


def delete_car(car_id: int):
    car = session.query(Car).filter(Car.id == car_id).first()

    if not car:
        return None

    car.deleted = True
    session.commit()
    return car.to_dict()


@cache_response(endpoint="list_car", cache_time=60)
async def list_car(page: int, size: int, filters):
    cars = session.query(Car)

    for key, value in filters.items():
        if value:
            cars = cars.filter(getattr(Car, key) == value)

    cars = cars.limit(size).offset((page - 1) * size).all()
    return [car.to_dict() for car in cars]


def upload_data(file):
    selected_columns = [
        "year",
        "make",
        "model",
        "trim",
        "body",
        "transmission",
        "state",
        "condition",
        "odometer",
        "color",
        "interior",
        "price",
    ]

    try:
        data = pd.read_csv(file.file, on_bad_lines="skip")

        data = data.rename(columns={"sellingprice": "price"})
        data = data.astype({"condition": "str"})
        data.ffill(inplace=True)
        data = data[selected_columns]

        chunk_size = 200
        for start in range(0, len(data), chunk_size):
            end = start + chunk_size
            chunk = data.iloc[start:end]

            bulk_data = []
            for _, row in chunk.iterrows():
                car = CarSchema(**row)
                bulk_data.append(car)

            session.bulk_insert_mappings(Car, bulk_data)
            session.commit()

        return {"message": "Data uploaded successfully"}

    except SQLAlchemyError as e:
        session.rollback()
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def add_car(car_data: dict):
    car = Car(**car_data)
    session.add(car)
    session.commit()
    return car.to_dict()
