import os
import sys
from concurrent import futures
import json
import logging

import grpc
from protobuf import location_pb2
from protobuf import location_pb2_grpc
from kafka import KafkaProducer
from datetime import datetime
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError


LOCATION_KAFKA_TOPIC = "location_processing"

producer = KafkaProducer(
    bootstrap_servers="kafka.default.svc.cluster.local:9092"
)


def push_to_kafka(payload):
    res = producer.send(LOCATION_KAFKA_TOPIC, json.dumps(payload).encode("utf-8"))
    print("Pushed payload to kafka..", payload)


class LocationServicer(location_pb2_grpc.LocationServicer):
    def AddLocation(self, request, context):
        payload = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "creation_time": datetime.now()
        }
        push_to_kafka(payload)
        payload.pop('creation_time')
        return location_pb2.LocationItem(**payload)


def serve():
    port = "5002"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServicer_to_server(LocationServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Grpc server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

