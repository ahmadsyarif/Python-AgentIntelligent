__author__ = 'Ahmad Syarif'
import pika
import json
class CommandHandler(object):
    avatarKey = 'avatar.NAO.command'
    def __init__(self):
        credential = pika.PlainCredentials('lumen', 'lumen')
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credential))
        self.channel = connection.channel()
        pass
    def sendCommand(self,command):
        self.channel.basic_publish(exchange='amq.topic',routing_key=CommandHandler.avatarKey,body=command)
        pass
    def LS_say(self,toSay):
        par = json.dumps({'text':toSay})
        com = json.dumps({'type':'texttospeech','method':'say','parameter':{'text':toSay}})
        self.sendCommand(command=com)
        pass
    def LS_goToPosture(self,posture,speed):
        com = json.dumps({'type':'posture','method':'goToPosture','parameter':{'postureName':posture,'speed':speed}})
        self.sendCommand(command=com)
        pass
    def LS_wakeUp(self):
        com = json.dumps({'type':'motion','method':'wakeUp'})
        self.sendCommand(command=com)
        pass
    def LS_rest(self):
        com = json.dumps({'type':'motion','method':'rest'})
        self.sendCommand(command=com)
        pass
    pass
