FROM python:3.7
WORKDIR /service1_frontend
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]