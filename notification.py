# 
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()


session = boto3.session.Session(profile_name='Account_Name')   
sns_client=boto3.client('sns')
codestar_notification = boto3.client('codestar-notifications')

# creating subscription

def subscribe(topic, protocol, endpoint):
    
    subscriptions = [0 for x in range(len(endpoint))]

    try:
        for i in range(len(endpoint)): 
            subscriptions[i] = sns_client.subscribe(
            TopicArn=topic['TopicArn'],   Protocol=protocol, Endpoint=endpoint[i], ReturnSubscriptionArn=True)
            logger.info("Subscribed %s %s to topic %s.", protocol, endpoint[i], topic)
           
    except ClientError:
        logger.exception(
            "Couldn't subscribe %s %s to topic %s.", protocol, endpoint, topic)
        raise
    
    else:
        return subscriptions

    
# creating topic 

def create_topic(name):

    try:
       
        topic = sns_client.create_topic(Name=name)
        logger.info("Created topic %s with ARN %s.", name, topic)

    except ClientError:
        logger.exception("Couldn't create topic %s.", name)
        raise
    
    else:
        return topic
    
# function calling 

topic_name = f'{topic-name}-new-topic'
print(f"Creating topic {topic_name}.")
topicArn = create_topic(topic_name)
subscribe(topicArn, "email", ["example1.com", "example2.com"])
