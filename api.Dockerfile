# pull the official docker image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# install python dependencies
# copy the file with the requirements to the /backend then install it with pip
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
# copy project
ADD ./app /app/app