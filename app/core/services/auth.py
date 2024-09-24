import jwt
from datetime import datetime, timedelta
from ..models.auth import Auth
from ...database.database import session


SECRET_KEY = "ec07c9f2c5894cf2779b6e5e81d7ba793e9cb0e9a84370f99cd3fc1e8b591e5f"
ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    add_token_to_db(encoded_jwt, expire)
    return encoded_jwt


def add_token_to_db(token: str, expire_time: datetime):
    auth_obj = Auth(token=token, expire_time=expire_time)
    session.add(auth_obj)
    session.commit()
