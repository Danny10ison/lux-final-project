FROM python:3.9
COPY . .
COPY ./requirements.txt ./requirements.txt
WORKDIR /.

EXPOSE 8000:8000
RUN pip3 install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]