## Running a simple example of gRPC

From directory EasygRPC:

1. Generate code for services: 

    $ python3 -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/requests.proto

2. Run server in one terminal

    $ python3 ingredient_server.py


3. Run client in another one:

    $ python3 ingredient_client.py