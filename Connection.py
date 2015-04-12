__author__ = 'Ahmad Syarif'
import pika

class connection(object):
    credential = pika.PlainCredentials('lumen', 'lumen')
    connection = None
    def __init__(self):
        try:
            connection.connection = pika.SelectConnection(parameters=pika.ConnectionParameters('localhost', 5672, '/', connection.credential),on_open_callback=self.on_connected)
        except:
            print 'sesuatu'
        pass
    pass
