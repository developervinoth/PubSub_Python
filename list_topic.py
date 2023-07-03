from google.cloud import pubsub_v1
from create_topic import project_id
# TODO(developer)
# project_id = "your-project-id"

publisher = pubsub_v1.PublisherClient()
project_path = f"projects/{project_id}"

for topic in publisher.list_topics(request={"project": project_path}):
    print(topic)