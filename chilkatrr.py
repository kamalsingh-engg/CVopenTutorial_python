import sys
import chilkat

#  This example requires the Chilkat SFTP API to have been previously unlocked.
#  See Unlock Chilkat SFTP for sample code.
glob = chilkat.CkGlobal()
success = glob.UnlockBundle("Anything for 30-day trial")
sftp = chilkat.CkSFtp()

success = sftp.Connect("sb-emea.avl.com",22)
if (success == True):
    success = sftp.AuthenticatePw("abhishek.hingwasia@avl.com","AvlAvl2931!!")

if (success == True):
    success = sftp.InitializeSftp()

if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

#  Synchronize (by uploading) the local directory tree rooted at "qa_data/sftpUploadTree"
#  with the remote directory tree rooted at "syncUploadTest"
#  Both directories are relative paths.  The remote directory
#  is relative to the HOME directory of the SSH user account.
#  The local directory is relative to the current working directory of the process.
#  It is also possible to use absolute paths.

remoteDir = "/Cummins_CTCI_NB/sftp_image_test/"
localDir = "D:/python_iot1"

#  Possible modes that can be passed to the SyncTreeUpload method are:
#  mode=0: Upload all files
#  mode=1: Upload all files that do not exist on the server.
#  mode=2: Upload newer or non-existant files.
#  mode=3: Upload only newer files. If a file does not already exist on the server, it is not uploaded.
#  mode=4: transfer missing files or files with size differences.
#  mode=5: same as mode 4, but also newer files.

#  This example will use mode 5 to upload missing, newer, or files with size differences.
mode = 5
#  This example turns on recursion to synchronize the entire tree.
#  Recursion can be turned off to synchronize the files of a single directory.
recursive = True
success = sftp.SyncTreeUpload(localDir,remoteDir,mode,recursive)
if (success != True):
    print(sftp.lastErrorText())
    sys.exit()

print("Success.")
