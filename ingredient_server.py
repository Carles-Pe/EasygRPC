

from concurrent import futures
import logging

import grpc
from requests_pb2 import FoodRequest
from requests_pb2 import FoodReply
from requests_pb2_grpc import RestaurantServicer
from requests_pb2_grpc import add_RestaurantServicer_to_server



class BigAls(RestaurantServicer):

    def respondRequest(self, request: FoodRequest,
                       context: grpc.aio.ServicerContext) -> FoodReply:
        logging.info("Serving single request \n%s", request)
        for i in range(request.num_times):
            yield FoodReply(message=f"You requested: {request.name}, and this is the {i}th i give it to you!")


    def respondMultipleRequests(self, multiple_request,
                       context: grpc.aio.ServicerContext):
        
        logging.info("Serving Compund Request")
        for req in multiple_request:
            for i in range(req.num_times):
                yield FoodReply(message=f"You requested: {req.name}, and this is the {i}th i give it to you!")
            
        
        



def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RestaurantServicer_to_server(BigAls(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    logging.info("\n")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
