from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from blog_platform.schemas import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def fake_decode_token(token):
    return User(
        username=token + 'fakedecoded', email='john@example.com', full_name='John Doe'
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
