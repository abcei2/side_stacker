FROM python:3
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /opt/app/
WORKDIR /opt/app/
RUN pip install -r requirements.txt
WORKDIR /opt/app/side_stacker_app