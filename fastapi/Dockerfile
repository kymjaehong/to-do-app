FROM python:3.11.5

WORKDIR /usr/src/workspace

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["uvicorn", "main:app", "--reload"]
