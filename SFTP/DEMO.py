import pysftp
import time
import threading

def sftp_connection():
    while True:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        try:
            with pysftp.Connection('sb-emea.avl.com', username='abhishek.hingwasia@avl.com', password='AvlAvl2931!!',
                                               cnopts=cnopts) as sftp:
                print('connection has been established')
                remotepath = '/Cummins_CTCI_NB/sftp_image_test/'

                while True:
                    remotepath = '/Cummins_CTCI_NB/sftp_image_test/'
                    try:

                       if sftp.exists(remotepath):


                        print('hi')
                        time.sleep(5)
                        print('hello')
                        time.sleep(5)
                    except:
                        print('connection/ssherror exception')
                        break
        except:
            print('connection has been breaked')
            time.sleep(5)

if __name__ == "__main__":
    t1 = threading.Thread(target=sftp_connection)
t1.start()