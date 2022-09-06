FROM python:3.7

RUN pip3 install pytest_asyncio

ADD data_test.py /tests/
ADD test_server.py /tests/

WORKDIR /tests/

