import pysftp
import os
from datetime import datetime,timedelta
from time import asctime
from time import sleep
import threading



def sftp_connection():
    while True:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        try:
            with pysftp.Connection('sb-emea.avl.com', username='abhishek.hingwasia@avl.com', password='AvlAvl2931!!',
                                   cnopts=cnopts) as sftp:
                while True:
                    sftp.get(2,1)
                    print('ramu shyamu')
                    sleep(3)
                    print('keshav madhav')
        except:
            print('connection loose ')
            sleep(5)




if __name__ == "__main__":
    t1 = threading.Thread(target=sftp_connection)
t1.start()