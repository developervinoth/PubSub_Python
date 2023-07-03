from google.cloud import pubsub_v1
from project_config import project_id, topic_id
import time
import random
import json
import datetime


publisher = pubsub_v1.PublisherClient()


topic_path = publisher.topic_path(project_id, topic_id)


while True:
    time.sleep(10)
    my_val = round(random.random()*1000,2)
    timestamp = datetime.datetime.now()
    data_str = {
    "sensor_name": "CO2",
    "value": my_val,
    "device_id": "CLUSTER_001",
    "time_stamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")
    }
    json_data = json.dumps(data_str)
    data = json_data.encode("utf-8")
    future = publisher.publish(topic_path, data)
    print(json_data, 'was published Sucessfully at', time.time())
