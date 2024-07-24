from fastapi import Body, FastAPI
# from server.routes.index import router as CrashReportRouter
from server.database import add_crashReports
from server.models.crashreports import CrashReportSchema, ResponseModel
from fastapi.encoders import jsonable_encoder


app = FastAPI()

# app.include_router(CrashReportRouter, tags=["CrashReport"], prefix="/crashreports")

@app.post("/saveCrashReports")
async def read_root(reports: CrashReportSchema = Body(...)):
    print("this is app directory...")
    reports = jsonable_encoder(reports)
    new_student = await add_crashReports(reports)
    return ResponseModel(new_student, "Crash Reports added successfully..")