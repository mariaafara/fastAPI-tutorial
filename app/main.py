from fastapi import FastAPI
import logging
from app.db import base_class, db_session

from app.routes.route_request import request_route

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S')

# This will bind our models to the created database
base_class.Base.metadata.create_all(bind=db_session.engine)

app = FastAPI(title="Simple Requests API", openapi_url="/openapi.json")  # create a FastAPI instance

# we use the include_router method of the app object to register the router we created in app.routes.route_request on
# the FastAPI object
app.include_router(request_route, prefix="/request")


@app.get("/")
def welcome():
    return "Welcome to Maria API"
