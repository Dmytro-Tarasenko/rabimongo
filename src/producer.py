from .select_data import select_avg_price_per_author
import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='avg_book_price_queue')

    query_result = select_avg_price_per_author()
    channel.basic_publish(exchange='',
                routing_key='avg_price',
                body=str(query_result).encode())
    
    channel.queue_declare(queue='sms')
    channel.basic_publish(exchange='',
                routing_key='avg_price',
                body=str(query_result).encode())
    
    connection.close()

if __name__ == '__main__':
    main()
