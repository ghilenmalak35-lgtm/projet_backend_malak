from fastapi import FastAPI
from user.user_controller import router
from client.client_controller import router
app = FastAPI()
app.include_router(router)