
from concurrent import futures
import logging

import grpc
import requests_pb2
import requests_pb2_grpc

# The 2 in pb2 indicates that the generated code is following Protocol Buffers Python API version 2. 
# Version 1 is obsolete. It has no relation to the Protocol Buffers Language version, which is 
# the one indicated by syntax = "proto3" or syntax = "proto2" in a .proto file.




def runSingle() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = requests_pb2_grpc.RestaurantStub(channel)

        # Direct read from the stub
        response_stream = stub.respondRequest(
            requests_pb2.FoodRequest(name="Pizza",num_times=2))
        for response in response_stream:
            print("Greeter client received: " +
                  response.message)
            
            

#################################################################
## Part 2
#################################################################

# Bidirectional streaming RPCs where both sides send a sequence 
# of messages using a read-write stream. The two streams operate 
# independently, so clients and servers can read and write in 
# whatever order they like

def generate_requests():
    messages = [
        requests_pb2.FoodRequest(name="Pizza", num_times=1),
        requests_pb2.FoodRequest(name="Patata", num_times=2),
        requests_pb2.FoodRequest(name="Tomato", num_times=3),
        requests_pb2.FoodRequest(name="Chicken", num_times=4),
    ]
    for msg in messages:
        yield msg



def runMultiple() -> None:       
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = requests_pb2_grpc.RestaurantStub(channel)
    # Direct read from the stub

        response_stream = stub.respondMultipleRequests(
            generate_requests())
        
        for response in response_stream:
            print("Greeter client received: " +
                  response.message)


if __name__ == "__main__":
    logging.basicConfig()
    runMultiple()
