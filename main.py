__author__ = 'Ahmad Syarif'
import Data
from Data import DataHandler
import Command
from pydispatch import dispatcher
from Command import CommandHandler
from multiprocessing import Process
import welcoming
from welcoming import startWelcomingBehavior
def testData():
    Data = DataHandler()
    Data.start()
    pass
def testCommand():
    command = CommandHandler()
    pass
def welcoming():
    startWelcomingBehavior()
    pass
def testDispatcher():
    dispatcher.send(signal=Data.AVATAR_DATA_TACTILE,result='hello')
    pass
if __name__ == '__main__':
    welcoming()
    testData()
    
    #data = Process(target=testData,args=())
    #data.start()
    #dis = Process(target=testDispatcher,args=())
    #dis.start()
    #testCommand()