__author__ = 'Ahmad Syarif'
import Data
from Data import DataHandler
import Command
from Command import CommandHandler
from multiprocessing import Process
from pydispatch import dispatcher
command = None
def startWelcomingBehavior():
    VISUAL_FACE_DETECTION = Data.VISUAL_FACE_DETECTION
    AVATAR_DATA_TACTILE = Data.AVATAR_DATA_TACTILE
    global command
    command = CommandHandler()
    dataProcessing = Process(target=startQueryData,args=())
    dataProcessing.start()
    dispatcher.connect(faceDetectionCallback,signal=VISUAL_FACE_DETECTION,sender=dispatcher.Any)
    dispatcher.connect(tactileDataCallback,signal=AVATAR_DATA_TACTILE,sender=dispatcher.Any)
    print 'hello'
def startQueryData():
    data = DataHandler()
    data.start()
def faceDetectionCallback(sender,result):
    print 'dispatcher : ',sender
    pass
def tactileDataCallback(sender,result):
    print 'dispatcher :', result[3]
    pass
pass
