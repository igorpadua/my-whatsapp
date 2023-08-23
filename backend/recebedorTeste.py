from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.spec import CHANNEL_ERROR


def on_message(channel, method_frame, header_frame, body):
    print(body)

connection = BlockingConnection(ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='logs', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, on_message_callback=on_message, auto_ack=True)

channel.start_consuming()
