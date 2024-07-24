from motor.motor_asyncio import AsyncIOMotorClient

# Db Connection
async def db_conn():
    conn_str = "mongodb+srv://kalyankalyan8324:9676153319@cluster0.3tps0ne.mongodb.net/"
    client = AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    database = client.test
    crashRepCol = database.get_collection("CrashReports")
    try:
        print(await client.server_info())
    except Exception as e:
        print(f"Unable to connect to the server: {e}")
    return crashRepCol


# helpers
def crash_rep_helper(crash_report) -> dict:
    return {
        "id": str(crash_report["_id"]),
        "TIMESTAMP": crash_report["TIMESTAMP"],
        "ERROR": crash_report["ERROR"],
        "FILE": crash_report["FILE"],
        "LINE": crash_report["LINE"],
        "COLUMN": crash_report["COLUMN"],
        "STACK": crash_report["STACK"],
        "SERVICE": crash_report["SERVICE"],
        "EMBEDDING": crash_report["EMBEDDING"],
        "CREATED_DATE": crash_report["CREATED_DATE"],
    }


# Add a new crash report into the database
async def add_crashReports(crashData: dict) -> dict:
    crashRepCol = await db_conn()
    new_crash = await crashRepCol.insert_one(crashData)
    created_crash = await crashRepCol.find_one({"_id": new_crash.inserted_id})
    return crash_rep_helper(created_crash)
