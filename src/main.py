from fastapi import FastAPI
import uvicorn

from modules.auth.presenter.auth_controller import auth_router

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
