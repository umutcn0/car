from fastapi import APIRouter
from app.api.routes.services import router as services_router
from .routes.auth import router as auth_router
from .routes.auth import auth_scheme


router = APIRouter(prefix="/api")
router.include_router(services_router)
router.include_router(auth_router)
