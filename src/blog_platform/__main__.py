import uvicorn

from blog_platform.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'blog_platform.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True
    )
