from fastapi import APIRouter, Depends
from typing import Optional
from app.dependencies import get_db
from app.db.models import UserRequest
from sqlalchemy.orm import Session
from app.schemas.schema_request import RequestModel, RequestSearchResultsModel

# instantiate an APIRouter which is how we can group our API endpoints
request_route = APIRouter()


# By adding the @request_route.get("/") decorator to the root function, we define a basic GET endpoint for our API
@request_route.get("/")
def get_all_requests(db_session: Session = Depends(get_db)):
    return db_session.query(UserRequest).all()


@request_route.post("/create_new_request")
def create_request(request_data: RequestModel, db_session: Session = Depends(get_db)):
    for element in request_data.list_str_input:
        request_record = UserRequest(
            str_input=request_data.str_input,
            str2_input=element,
            opt_str_input=request_data.opt_str_input,
            float_input=request_data.float_input,
        )
        db_session.add(request_record)
    result = db_session.commit()
    # db.refresh(request_record)
    return result


# url path parameter
# a new GET endpoint /requests/{str_input} where the curly braces indicate the parameter value,
# which needs to match one of the arguments taken by the endpoint function get_request_by_str1.
# The data is then serialized and returned as JSON by FastAPI.
# @request_route.get("/requests/{request_id}", response_model = RequestModel)
# def fetch_request_by_str1(request_id: int, db_session: Session = Depends(get_db), limit: int = 5) -> dict:
#     """
#     Fetch a single request by request_id
#     """
#     return db_session.query(RequestModel).filter(RequestModel.id == request_id).limit(limit).all()


# created a new GET endpoint /search/
@request_route.get("/search/", response_model=RequestSearchResultsModel)
def search_requests(str_input: Optional[str] = None, db_session: Session = Depends(get_db), limit: int = 5) -> dict:
    """
    search for request(s) based on input_str
    After the search is complete the data is serialized to JSON by the framework.
    """
    if not str_input:
        # based on the limit query parameter we limit results
        return {"results": db_session.query(RequestModel).limit(limit).all()}

    return db_session.query(RequestModel).filter(RequestModel.str_input == str_input).limit(limit).all()
