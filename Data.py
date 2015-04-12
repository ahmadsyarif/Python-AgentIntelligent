__author__ = 'Ahmad Syarif'
import pika
import json
from pydispatch import dispatcher

VISUAL_FACE_DETECTION = 'VISUAL_FACE_DETECTION'
VISUAL_FACE_DETECTION = 'VISUAL_FACE_DETECTION'
VISUAL_FACE_RECOGNITION ='VISUAL_FACE_RECOGNITION'
VISUAL_FACE_TRACKING = 'VISUAL_FACE_TRACKING'
VISUAL_HUMAN_TRACKING = 'VISUAL_HUMAN_TRACKING'
AUDIO_SPEECH_RECOGNITION = 'AUDIO_SPEECH_RECOGNITION'
AUDIO_TEXT_TO_SPEECH = 'AUDIO_TEXT_TO_SPEECH'
AUDIO_GENDER_RECOGNITION = 'AUDIO_GENDER_RECOGNITION'
AVATAR_DATA_TACTILE = 'AVATAR_DATA_TACTILE'
class DataHandler(object):
    'class to control connection'
    credential = pika.PlainCredentials('lumen', 'lumen')
    isConnected = None

    def __init__(self):
        try:
            self.connection = pika.SelectConnection(parameters=pika.ConnectionParameters('localhost', 5672, '/', DataHandler.credential),on_open_callback=self.on_connected)
            DataHandler.isConnected = True
        except RuntimeError as e:
            print 'unable to connect', e
        pass

    def start(self):
        self.connection.ioloop.start()
        pass
    def on_connected(self,connection):
        connection.channel(self.on_channel_open,channel_number=1)
        connection.channel(self.on_channel_open,channel_number=2)
        #connection.channel(self.on_channel_open,channel_number=3)
        #connection.channel(self.on_channel_open,channel_number=4)
        #connection.channel(self.on_channel_open,channel_number=5)
        #connection.channel(self.on_channel_open,channel_number=6)
        #connection.channel(self.on_channel_open,channel_number=7)
        connection.channel(self.on_channel_open,channel_number=8)
        pass
    def on_channel_open(self,channel):
        if channel.channel_number ==1:
            self.channelVisualFaceDetection = channel
            self.channelVisualFaceDetection.queue_declare(self.on_queue_declareOk,queue='lumen.visual.face.detection',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==2:
            self.channelVisualFaceRecognition = channel
            self.channelVisualFaceRecognition.queue_declare(self.on_queue_declareOk,queue='lumen.visual.face.recognition',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==3:
            self.channelVisualFaceTracking = channel
            self.channelVisualFaceTracking.queue_declare(self.on_queue_declareOk,queue='lumen.visual.face.tracking',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==4:
            self.channelVisualHumanDetection = channel
            self.channelVisualHumanDetection.queue_declare(self.on_queue_declareOk,queue='lumen.visual.human.detection',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==5:
            self.channelAudioSpeechRecognition = channel
            self.channelAudioSpeechRecognition.queue_declare(self.on_queue_declareOk,queue='lumen.audio.speech.recognition',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==6:
            self.channelAudioTextToSpeech = channel
            self.channelAudioTextToSpeech.queue_declare(self.on_queue_declareOk,queue='lumen.audio.text.to.speech',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==7:
            self.channelAudioGenderRecognition = channel
            self.channelAudioGenderRecognition.queue_declare(self.on_queue_declareOk,queue='lumen.audio.gender.recognition',durable=True,exclusive=False,auto_delete=True)
        elif channel.channel_number==8:
            self.channelAvatarDataTactile = channel
            self.channelAvatarDataTactile.queue_declare(self.on_queue_declareOk,queue='avatar.NAO.data.tactile',durable=True,exclusive=False,auto_delete=True)
        else:
            print 'print do nothing'
            pass
        pass
    def on_queue_declareOk(self,workQueue):
        if workQueue.channel_number == 1:
            self.channelVisualFaceDetection.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 2:
            self.channelVisualFaceRecognition.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 3:
            self.channelVisualFaceTracking.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 4:
            self.channelVisualHumanDetection.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 5:
            self.channelAudioSpeechRecognition.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 6:
            self.channelAudioTextToSpeech.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 7:
            self.channelAudioGenderRecognition.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        elif workQueue.channel_number == 8:
            self.channelAvatarDataTactile.queue_bind(self.on_bindOK,queue=workQueue.method.queue,exchange='amq.topic',routing_key=workQueue.method.queue)
        else:
            pass
        pass
    def on_bindOK(self,frame):
        if frame.channel_number == 1:
            self.channelVisualFaceDetection.basic_consume(self.faceDetectionCallback,queue='lumen.visual.face.detection',no_ack=True)
        elif frame.channel_number==2:
            self.channelVisualFaceRecognition.basic_consume(self.faceRecognitionCallback,queue='lumen.visual.face.recognition',no_ack=True)
        elif frame.channel_number==3:
            self.channelVisualFaceTracking.basic_consume(self.faceTrackingCallback,queue='lumen.visual.face.tracking',no_ack=True)
        elif frame.channel_number==4:
            self.channelVisualHumanDetection.basic_consume(self.humanDetectionCallback,queue='lumen.visual.human.detection',no_ack=True)
        elif frame.channel_number==5:
            self.channelAudioSpeechRecognition.basic_consume(self.speechRecognitionCallback,queue='lumen.audio.speech.recognition',no_ack=True)
        elif frame.channel_number==6:
            self.channelAudioTextToSpeech.basic_consume(self.textToSpeechCallback,queue='lumen.audio.text.to.speech',no_ack=True)
        elif frame.channel_number==7:
            self.channelAudioGenderRecognition.basic_consume(self.genderRecognitionCallback,queue='lumen.audio.gender.recognition',no_ack=True)
        elif frame.channel_number==8:
            self.channelAvatarDataTactile.basic_consume(self.tactileDataCallback,queue='avatar.NAO.data.tactile',no_ack=True)
        else:
            pass
        pass

    # defenition of event handler
    def faceDetectionCallback(self,ch, method, property, body):
        result = json.loads(body)
        faceLocation = [result['x'],result['y']]
        dispatcher.send(signal=VISUAL_FACE_DETECTION,sender=self,result=faceLocation)
        pass
    def faceRecognitionCallback(self,ch, method, property, body):
        result = json.loads(body)
        faceName = result['name']
        dispatcher.send(signal=VISUAL_FACE_RECOGNITION,sender=self,result = faceName)
        pass
    def faceTrackingCallback(self,ch, method, property, body):
        dispatcher.send(signal=VISUAL_FACE_TRACKING,sender=self,result = body)
        pass
    def humanDetectionCallback(self,ch, method, property, body):
        result = json.loads(body)
        humanLocation = [result['x'],result['y']]
        dispatcher.send(signal=VISUAL_HUMAN_TRACKING,sender=self,result = humanLocation)
        pass
    def speechRecognitionCallback(self,ch, method, property, body):
        result = json.loads(body)
        recognizedWord = result['result']
        dispatcher.send(signal=AUDIO_SPEECH_RECOGNITION,sender=self,result = recognizedWord)
        pass
    def textToSpeechCallback(self,ch, method, property, body):
        result = json.loads(body)
        sound = result['sound']
        dispatcher.send(signal=AUDIO_TEXT_TO_SPEECH,sender=self,result = sound)
        pass
    def genderRecognitionCallback(self,ch, method, property, body):
        result = json.loads(body)
        gender = result['gender']
        dispatcher.send(signal=AUDIO_GENDER_RECOGNITION,sender=self,result = gender)
        pass
    def tactileDataCallback(self,ch, method, property, body):
        result = json.loads(body)
        value = result['value']
        dispatcher.send(signal=AVATAR_DATA_TACTILE,sender=self,result = value)
        pass
    pass


