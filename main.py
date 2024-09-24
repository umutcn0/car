import uvicorn
from app.database.database import init_db, session

if __name__ == "__main__":
    init_db()
    #upload_data()
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
