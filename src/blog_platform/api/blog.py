from fastapi import APIRouter, Depends

from ..schemas import Blog, BlogCreate
from ..services.blog import BlogService

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/', response_model=Blog)
def create_blog(
    blog_data: BlogCreate,
    service: BlogService = Depends(),
):
    return service.create(blog_data=blog_data)


@router.get('/{blog_id}', response_model=Blog)
def get_blog(
    blog_id: int,
    service: BlogService = Depends(),
):
    return service.get(blog_id=blog_id)


@router.delete('/{blog_id}', response_model=Blog)
def delete_blog(
    blog_id: int,
    service: BlogService = Depends(),
):
    return service.delete(blog_id=blog_id)
