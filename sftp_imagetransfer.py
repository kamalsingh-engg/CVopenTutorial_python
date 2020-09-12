from datetime import datetime
#from picamera import PiCamera
from datetime import datetime,timedelta
import pysftp
import os
import time
from time import asctime
from time import sleep
import threading
camera = PiCamera()
def image_capture():
    while True:
        now=datetime.now()
        file1='image{}_{}_{}'.format(now.date(),now.hour,now.minute)
        filename1=file1+'.jpg'
        camera.resolution = (500,400)
        camera.capture(filename1)
        print('image has been captured')
        sleep(60)

def sftp_loop_transfer():
    while True:
        try:
            now=datetime.now()
            t1=datetime.today()-timedelta(minutes=1)
            cnopts=pysftp.CnOpts()
            cnopts.hostkeys=None
            with pysftp.Connection('sb-emea.avl.com',username='abhishek.hingwasia@avl.com',password='AvlAvl2931!!',cnopts=cnopts) as sftp:
                print('connection has been established')
                file1='image{}_{}_{}'.format(now.date(),now.hour,now.minute)+'.jpg'
                localFilePath='/home/pi/image{}_{}_{}'.format(now.date(),now.hour,t1.minute)+'.jpg'
                if os.path.exists(localFilePath):
                    remoteFilePath='/Cummins_CTCI_NB/image{}_{}_{}'.format(now.date(),now.hour,t1.minute)+'.jpg'
                    sftp.put(localFilePath,remoteFilePath)
                    print('file has been transferred')
                    sleep(30)
                else:
                    print('wait for the file')
                    sleep(10)
        except:
            print('it is continuously run the file')
            os.popen('python sftp_imagetransfer.py')
            sleep(5)
        
if __name__=="__main__":
    t1=threading.Thread(target=image_capture)
    t2=threading.Thread(target=sftp_loop_transfer)
    
    t1.start()
    t2.start()

