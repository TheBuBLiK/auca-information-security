from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345admin"

TARGET_USERNAME = "amantai"
TARGET_PASSWORD = "Amantai2005!"

@app.post('/login')
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return "secret token"
    return "Invalid credentials"

@app.post('/login_target')
def login_target(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username == TARGET_USERNAME and password == TARGET_PASSWORD:
        return "target token"
    return "Invalid credentials"
