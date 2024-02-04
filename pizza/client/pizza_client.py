import grpc
import json
import time

from pizza.pizza_delivery_service import Customer
from pizza.grpc_outputs import pizza_deliver_pb2, pizza_deliver_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = pizza_deliver_pb2_grpc.PizzaDeliveryStub(channel)

def get_client_stream_requests():
    while True:
        name = input("Customer name? ")
        distance = input("Customer distance? ")

        if name == "":
            break

        try:
            customer = json.dumps({"name": name, "distance": int(distance)})
        except Exception as e:
            print(f"nope: {e}")

        pizza_request = pizza_deliver_pb2.PizzaRequest(customer=customer)
        yield pizza_request
        time.sleep(1)

def pizza_request_chat():
    responses = stub.deliver_pizza(get_client_stream_requests())

    for response in responses:
        print(response)

def pizza_request():
    name = input("Customer name? ")
    distance = input("Customer distance? ")
    try:
        customer = json.dumps({"name": name, "distance": int(distance)})
        rsp = stub.deliver_pizza(pizza_deliver_pb2.PizzaRequest(customer=customer))
        print(rsp.rsp)
    except Exception as e:
        print(f"nope: {e}")

def main():
    while True:
        c = input("Choice?\n1.Pizza Request\n2.Pizza Chat\n")
        if c == "1":
            pizza_request()
        if c == "2":
            pizza_request_chat()

if __name__ == "__main__":
    main()
