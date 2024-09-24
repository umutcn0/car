from fastapi import APIRouter
from ...core.services import auth as service
from fastapi.security import HTTPBearer
from typing import Optional
from fastapi import Depends, HTTPException, Request
from ...database.database import session
from ...core.models import Auth
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["Auth"])


class OptionalHTTPBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        from fastapi import status

        try:
            r = await super().__call__(request)
            token = r.credentials
            auth = session.query(Auth).filter_by(token=token).first()

            if not auth:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token"
                )

            expire_time = auth.expire_time
            if expire_time < datetime.now():
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Token expired"
                )

        except HTTPException as ex:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token"
            )
        return token


auth_scheme = OptionalHTTPBearer()


@router.get("/token")
async def token(username: str):
    """
    Get token
    :param username: username could be dummy
    :return: token
    """
    token = service.create_access_token(data={"sub": username})
    return {"access_token": token, "token_type": "bearer"}
