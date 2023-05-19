FROM python:3
WORKDIR /flask_application
COPY requirements.txt /flask_application
RUN pip install -U pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
COPY . /flask_application
CMD [ "python3", "run.py" ]