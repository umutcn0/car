from fastapi import APIRouter, UploadFile, Depends, File
from ...core.services import car as service
from ...schemas import CarSchema
from ...middleware.cache import cache_response
from ...api.routes.auth import auth_scheme

router = APIRouter(prefix="/car", tags=["Car"], dependencies=[Depends(auth_scheme)])


@router.get("/car-info")
async def car_info(car_id: int):
    """
    Get car info
    :param car_id: id of the car
    :return: vehicle information
    """
    return service.get_car_info(car_id)


@router.post("/update")
async def update_car(car_id: int, car_data: CarSchema):
    """
    Update car information
    :param car_id:  id of the car
    :param car_data: attributes to update
    :return: updated vehicle information
    """
    return service.update_car(car_id, car_data.model_dump())


@router.delete("/delete")
async def delete_car(car_id: int):
    """
    Delete car
    :param car_id: id of the car
    :return: vehicle information
    """
    return service.delete_car(car_id)


@router.get("/list")
async def list_car(page: int = 1, size: int = 25, filters: dict = Depends(CarSchema)):
    """
    List cars
    :param page: current page
    :param size: objects per page
    :param filters:  filters to apply
    :return: list of vehicles
    """
    return await service.list_car(page, size, filters.model_dump())


@router.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    """
    Upload data
    :param file: file to upload
    :return:
    """
    return service.upload_data(file)


@router.post("/add")
async def add_car(car_data: CarSchema):
    """
    Add car
    :param car_data: car information
    :return: new vehicle information
    """
    return service.add_car(car_data.model_dump())
