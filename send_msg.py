# Testing RabbitMQ infrastructure by posting three different kind of binding keys:
#   * info          -> Queue 'A'
#   * warning       -> Queue 'A'
#   * error         -> Queue 'B'
#
# Made by MA-IT for the course: Advanced PLCnext with C++.

#make sure that you activated the venv.
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.137.13',port=5672))
channel = connection.channel()

#Only run when the channel is open.
while(channel.is_open):

    #Write as input the routing key
    r_key = input("routing key: ")
    if(r_key == 'c'):
        break

    #Write as input the message that will be send.
    msg = input("message: ")

    if(msg == 'c'):
        break

    channel.basic_publish(exchange='ErrorExchange', #ErrorExchange
                        routing_key=r_key,          #routing key
                        body=msg)                   #message

    print("message: " + msg + " is send to " + r_key) 

channel.close()
connection.close()
