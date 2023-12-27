from kafka import KafkaConsumer
import os
import logging
import json
import psycopg2


DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


LOCATION_KAFKA_TOPIC = "location_processing"
consumer = KafkaConsumer(
    LOCATION_KAFKA_TOPIC, 
    bootstrap_servers="kafka.default.svc.cluster.local:9092"
)

def add_location(payload):
    connection = psycopg2.connect(
        dbname=DB_NAME,
        port=DB_PORT,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    query = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}));".format(
        int(payload["person_id"]),
        float(payload["latitude"]),
        float(payload["longitude"]),
    )

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def serve():
    while True:
        for message in consumer:
            print("Kafka payload received: {}".format(message))
            consumed_message = json.loads(message.value.decode("utf-8"))
            add_location(consumed_message)


if __name__ == "__main__":
    logging.basicConfig()
    serve()

