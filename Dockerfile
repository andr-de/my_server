FROM python:3

COPY my_server.py /

EXPOSE 65432
ENTRYPOINT ["python", "my_server.py"]
