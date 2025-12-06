import azure.functions as func
from api.wsgi import application

# The 'VortfolioHandler' directory is at the same level as 'api',
# so we can import from 'api.wsgi'.
# This wrapper converts the WSGI app to an ASGI app that Azure Functions can handle.
wsgi_app = func.WsgiMiddleware(application)

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await wsgi_app.main(req, context)