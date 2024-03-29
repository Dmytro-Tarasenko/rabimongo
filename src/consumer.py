import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='avg_book_price_queue')

    channel.basic_consume(queue='avg_book_price_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
