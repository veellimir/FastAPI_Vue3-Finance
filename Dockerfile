FROM python:3.12.7

RUN mkdir /project

WORKDIR /project

COPY requirements.in .

RUN pip install --upgrade pip
RUN pip install -r requirements.in

COPY . .

RUN chmod a+x /booking/docker/*.sh

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]



