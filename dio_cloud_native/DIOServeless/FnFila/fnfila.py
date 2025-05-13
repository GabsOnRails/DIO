from azure.servicebus import ServiceBusClient
from dotenv import load_dotenv
import os


# ... suas configurações do .env ...

def peek_queue_messages(servicebus_client, queue_name, max_messages=5):
    with servicebus_client.get_queue_receiver(queue_name=queue_name) as receiver:
        messages = receiver.peek_messages(max_message_count=max_messages)
        if messages:
            print(f"As últimas {len(messages)} mensagens na fila '{queue_name}':")
            for message in messages:
                print(f"  Message ID: {message.message_id}")
                print(f"  Body: {str(message)}")
                print(f"  Properties: {message.application_properties}")
                print("-" * 20)
        else:
            print(f"Não há mensagens para espiar na fila '{queue_name}'.")

if __name__ == "__main__":
    load_dotenv()
    NAMESPACE = os.getenv("NAMESPACE")
    KEY_NAME = os.getenv("KEY_NAME")
    KEY_VALUE = os.getenv("KEY_VALUE")
    QUEUE_NAME = os.getenv("QUEUE_NAME")

    connection_str = f"Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={KEY_NAME};SharedAccessKeyValue={KEY_VALUE}"

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connection_str)

    peek_queue_messages(servicebus_client, QUEUE_NAME)