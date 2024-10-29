# app/api/v1/endpoints/visualize.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.script_executor import execute_script

router = APIRouter()

class ScriptRequest(BaseModel):
    code: str

@router.post("/visualize")
async def visualize_script(request: ScriptRequest):
    code = request.code
    try:
        steps = execute_script(code)
        return {"steps": steps}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error executing script")
