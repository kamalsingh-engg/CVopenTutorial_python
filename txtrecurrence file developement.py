import pysftp
import os
import cv2 as cv
import shutil
import time
from time import asctime
from time import sleep
from datetime import datetime,timedelta
from time import asctime
from time import sleep
import threading



def directory():
    print('samosa')

    while True:
        now = datetime.now()

        path_1 = 'D:/python_iot/{}/{}/{}/{}/{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        if os.path.exists(path_1):
            #print("already path created ")
            #sleep(2)
            pass

        else:
            os.makedirs(path_1)
            print("path created")

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



def sftp_loop_transfer():
    while True:
        now = datetime.now()
        t1 = datetime.today() - timedelta(minutes=1)
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection('sb-emea.avl.com', username='abhishek.hingwasia@avl.com', password='AvlAvl2931!!',
                               cnopts=cnopts) as sftp:
            print('connection has been established')
            # file1 = 'image{}_{}_{}'.format(now.date(), now.hour, now.minute) + '.jpg'
            localFilePath = 'D:/python_iot/{}/{}/{}/{}/{}/avlguriot{}'.format(now.year, now.month, now.day, now.hour,
                                                                              t1.minute,now.second)+'.txt'
            print(localFilePath)
            if os.path.exists(localFilePath):
                remoteFilePath = '/Cummins_CTCI_NB/sftp_image_test/avlguriot{}_{}_{}_{}_{}_{}'.format(now.second,
                                                                                                      now.month,now.day
                                                                                                      ,now.hour,
                                                                                                      t1.minute,
                                                                                                      now.second)+'.txt'

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
        t2 = datetime.today() - timedelta(minutes=3)
        localFilePath = 'D:/python_iot/{}/{}/{}/{}/{}/'.format(now.year, now.month, now.day, now.hour,
                                                                          t2.minute)
        if os.path.exists(localFilePath):
            shutil.rmtree(localFilePath)
            print("path removed")
            sleep(1)
        else:
            print("path already removed")
            sleep(40)




if __name__ == "__main__":
    t1 = threading.Thread(target=directory)
    t2 = threading.Thread(target=text_write)
    t3 = threading.Thread(target=sftp_loop_transfer)
    t4 = threading.Thread(target=delete_folder)

    t1.start()
    t2.start()
    t3.start()
    t4.start()