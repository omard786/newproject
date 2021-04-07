FROM python:3.7
WORKDIR /service2_letters
COPY . . 
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT ["python", "app.py"]