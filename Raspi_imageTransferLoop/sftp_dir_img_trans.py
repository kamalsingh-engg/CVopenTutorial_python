from picamera import PiCamera
import pysftp
import os
import cv2
import shutil
import time
from time import asctime
from time import sleep
from datetime import datetime,timedelta
from time import asctime
from time import sleep
import threading
camera = PiCamera()

# with pysftp.Connection('sb-emea.avl.com', username='abhishek.hingwasia@avl.com', password='AvlAvl2931!!',
# cnopts=cnopts) as sftp:
# print('connection has been established')

def directory():


    while True:
        now = datetime.now()

        path_1 = '/home/pi/SFTP_IMG/{}/{}/{}/{}/{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        if os.path.exists(path_1):
            #print("already path created ")
            #sleep(2)
            pass

        else:
            os.makedirs(path_1)

            print("path created")
def image_capture():
    while True:

        now = datetime.now()

        save_path = '/home/pi/SFTP_IMG/{}/{}/{}/{}/{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        filename = 'avlsecuritygateimg{}'.format(now.second)
        if os.path.exists(save_path) and ret :
            completeName = os.path.join(save_path, filename + '.jpg')
            camera.resolution = (500, 400)
            camera.capture(completeName)
            print(completeName+'has been captured')
            sleep(1)
        elif not os.path.exists(save_path):
            print('file save path not found')
            sleep(1)




'''

def text_write():
    while True:

        now = datetime.now()
        save_path = 'D:/python_iot/{}/{}/{}/{}/{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        filename =  'avlguriot{}'.format(now.second)
        if os.path.exists(save_path):
            completeName = os.path.join(save_path, filename + '.txt')
            file1 = open(completeName, 'w')
            file1.write('avliotgur{}'.format(now.second))
            sleep(1)
        else:
            print('file save path not found')
            sleep(2)

'''

def sftp_loop_transfer():
    while True:

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection('sb-emea.avl.com', username='abhishek.hingwasia@avl.com', password='AvlAvl2931!!',
                               cnopts=cnopts) as sftp:
            print('connection has been established')
            while True:
                now = datetime.now()
                t1 = datetime.today() - timedelta(seconds=1)
                # file1 = 'image{}_{}_{}'.format(now.date(), now.hour, now.minute) + '.jpg'
                localFilePath = '/home/pi/SFTP_IMG/{}/{}/{}/{}/{}/avlsecuritygateimg{}'.format(now.year, now.month, now.day,
                                                                                      now.hour,
                                                                                  now.minute,t1.second)+'.jpg'
                print(localFilePath)
                if os.path.exists(localFilePath):
                    remoteFilePath = '/Cummins_CTCI_NB/sftp_image_test/avlsecuritygateimg{}_{}_{}_{}_{}_{}'.format(now.date(),
                                                                                                    now.hour,
                                                                                                          now.minute,
                                                                                                          t1.second)+\
                                     '.jpg'

                    sftp.put(localFilePath, remoteFilePath)
                    print('file has been transferred')

                    #shutil.rmtree(localFilePath)
                    #print("path removed")
                else:
                    print('wait for the file')
                    sleep(1)

       # except:
            #print('it is continuously run the file')

def delete_folder():
    while True:
        now = datetime.now()
        t2 = datetime.today() - timedelta(days=2)
        localFilePath = 'D:/python_iot/{}/{}/{}/{}/{}/'.format(now.year, now.month, t2.day)
        if os.path.exists(localFilePath):
            shutil.rmtree(localFilePath)
            print("path removed")
            sleep(1)
        else:
            print("path already removed")
            sleep(40)




if __name__ == "__main__":
    t1 = threading.Thread(target=directory)
    t2 = threading.Thread(target=image_capture)
    t3 = threading.Thread(target=sftp_loop_transfer)
    t4 = threading.Thread(target=delete_folder)

    t1.start()
    t2.start()
    t3.start()
    t4.start()