from fastapi import APIRouter
from service import role_service
from model.role_model import Role
from fastapi import HTTPException
from fastapi.param_functions import Body

router = APIRouter(prefix="/roleService", tags=["role"])


@router.get("/findAll")
async def find_all():
    return await role_service.find_all()


@router.get("/findByRoleName/{role_name}")
async def find_by_role_name(role_name):
    return await role_service.find_by_role_name(role_name)


@router.post("/saveNewRole")
async def save_new_role(role: Role = Body(...)):
    if role is None:
        raise HTTPException(status_code=400, detail="Role object is required")
    result = await role_service.save_new_role(role)
    return {"message": "Role saved successfully", "inserted_id": str(result)}
