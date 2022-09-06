import pytest_asyncio
import asyncio
from data_test import s


@pytest_asyncio.fixture
async def run_client(HOST='0.0.0.0', PORT=8888):
    reader, writer = await asyncio.open_connection(HOST, PORT)
    writer.write(b"next")
    data = await reader.read(2048)
    yield data

def test_server(run_client):
    assert run_client[:100] == s[:100]
