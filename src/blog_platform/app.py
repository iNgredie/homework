from fastapi import FastAPI

from .api import router

app = FastAPI(
    title='Blog platform',
    desctiption='Платформа для размещения блогов',
    version='0.0.1'
)


app.include_router(router)
