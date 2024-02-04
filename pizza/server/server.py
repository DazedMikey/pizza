from concurrent import futures
import grpc
from pizza.server.pizza_server import PizzaService
from pizza.grpc_outputs import pizza_deliver_pb2, pizza_deliver_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pizza_deliver_pb2_grpc.add_PizzaDeliveryServicer_to_server(PizzaService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
