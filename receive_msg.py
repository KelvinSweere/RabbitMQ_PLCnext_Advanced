import pika, os, sys
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.137.13',port=5672))

def main():    
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(" [x] Received "+ str(body))

    channel.basic_consume(queue='A', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)