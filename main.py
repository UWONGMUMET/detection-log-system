from fastapi import FastAPI
from routers import auth, user
from core.config import settings

app = FastAPI(debug=settings.DEBUG)

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Detection Log System API"}