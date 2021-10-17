from cv2 import cv2
import time
import random
import dropbox
start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    accessToken="3Lupbi4GSnUAAAAAAAAAAfYRiyOvgp8DQbEMkc_XOyAABM77LxkYMJMu5jhnL_by"
    file=img_name
    file_from=file
    file_to="/"+img_name
    dbx=dropbox.Dropbox(accessToken)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=10):
            name=take_snapshot()
            upload_file(name)
main()