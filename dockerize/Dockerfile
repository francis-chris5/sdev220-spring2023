FROM python:3

WORKDIR /opt/payroll

COPY paycheck.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./paycheck.py"]
