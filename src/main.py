from fastapi import FastAPI, Depends

from src.modules.auth.presenter.auth_controller import auth_router
from src.modules.users.presenter.users_controller import users_router

from fastapi.security import HTTPBearer

http_bearer = HTTPBearer(auto_error=False)

app = FastAPI(title="Road Vision Core API", dependencies=[Depends(http_bearer)])
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
