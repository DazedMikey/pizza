import dacite
import json

from pizza.pizza_delivery_service import DeliveryService, Customer
from pizza.grpc_outputs import pizza_deliver_pb2_grpc, pizza_deliver_pb2


class PizzaService(pizza_deliver_pb2_grpc.PizzaDeliveryServicer):

    def deliver_pizza(self, request_iterator, context):
        ds = DeliveryService()
        for request in request_iterator:
            try:
                print(request)
                req = json.loads(request.customer)
                c = dacite.from_dict(Customer, req)
                response = ds.deliver_pizza(c)
                print(response)
                yield pizza_deliver_pb2.PizzaResponse(rsp=response)
            except Exception as e:
                print(f"Nope: {e}")
