### Libs installation
```bash
pip3 install -r requirements.txt
```

### Run the server:
```bash
python3 server/server.py
```

### Run the client:
```bash
python3 client/client.py
```

### Run the PySide2 widget:
```bash
python3 client/__main__.py
```

### Run the test:
```bash
pytest tests/test_server.py
```

### Building and launching the project:
```bash
sudo docker-compose build
sudo docker-compose up
```

### Stop Docker resources:
```bash
sudo docker-compose down
```

### TASK
Create TCP client which gets pictures from the TCP server(port 8888)

Description:
	When the client connects to the server, it should send the command “next”(N times). The server returns chunks (max size 2048 bytes), where a first byte is a serial number(max 256 chunks). When all chunks are returned - the server closes the connection. 
	It is needed to remove the serial numbers, glue all chunks in the correct order in the one picture, and return the path to the picture from function “client”. After this QT application will be opened with the picture.