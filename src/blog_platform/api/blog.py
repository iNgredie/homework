from typing import Optional

from fastapi import APIRouter, Depends

from ..schemas import Blog, BlogCreate, User
from ..services.blog import BlogService
from ..services.user import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/', response_model=Blog)
def create_blog(
    blog_data: BlogCreate,
    user: User = Depends(get_current_user),
    service: BlogService = Depends(),
):
    return service.create(user_id=user.id, blog_data=blog_data)


@router.get('/{blog_id}', response_model=Blog)
def get_blog(
    blog_id: int,
    user: User = Depends(get_current_user),
    service: BlogService = Depends(),
):
    return service.get(user_id=user.id, blog_id=blog_id)


@router.delete('/{blog_id}', response_model=Blog)
def delete_blog(
    blog_id: int,
    user: User = Depends(get_current_user),
    service: BlogService = Depends(),
):
    return service.delete(user_id=user.id, blog_id=blog_id)


@router.get('/blogs', response_model=Blog)
def get_blog_list(
    amount: Optional[int] = None,
    user: User = Depends(get_current_user),
    service: BlogService = Depends(),
):
    return service.get_list(user_id=user.id, amount=amount)