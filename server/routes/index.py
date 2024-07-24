from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import add_crashReports
from server.models.crashreports import CrashReportSchema, ResponseModel

router = APIRouter()

@router.post("/saveCrashReports", response_description="CrashReports added into the database",tags=["CrashReport"])
async def addCrashReports(reports: CrashReportSchema = Body(...)):
    print("this is route directoiry...")
    reports = jsonable_encoder(reports)
    new_student = await add_crashReports(reports)
    return ResponseModel(new_student, "Crash Reports added successfully..")