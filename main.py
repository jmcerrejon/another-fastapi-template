import uvicorn
from fastapi import FastAPI

app = FastAPI()


# Health API Endpoint
@app.get("/health")
async def server_health():
    return {"status": "OK", "message": "Server is up and running."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
