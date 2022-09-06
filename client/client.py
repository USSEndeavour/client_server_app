import asyncio
import base64
import logging


"""
This module contains the run_client() function that connects to the server, obtains chunked bytestring data from server
and writes it to the picture_file.py. 

The convert_picture() function reads bytestring data from the picture_file.py, converts it to base64
and writes it to the encoded.bin file. After that the base64 data is being rewritten to the image.jpeg file.
"""

logging.basicConfig(level=logging.DEBUG)

HOST = "0.0.0.0"
PORT = 8888

file = open('picture_file.py', 'wb')

async def run_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    while True:
        writer.write(b"next")
        data = await reader.read(2048)
        file.write(data[1:])
        if not data:
            break

    logging.debug('The client has successfully obtained the data')
    await convert_picture()


async def convert_picture():
    with open('picture_file.py', 'rb') as file:
        encoded = base64.b64encode(file.read())

    with open('encoded.bin', 'wb') as write_binary:
        write_binary.write(encoded)

    with open('encoded.bin', 'rb') as read_binary:
        byte = read_binary.read()
        read_binary.close()

    with open('image.jpeg', 'wb') as decodeit:
        decodeit.write(base64.b64decode((byte)))

    logging.debug('file image.jpeg was successfully created')

if __name__ == "__main__":
    asyncio.run(run_client())

