import cv2
import os

# Playing video from file:
cap = cv2.VideoCapture('open.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = cap.read()
    if hasFrames:
        name = './data/frame' + str(sec) + '.jpg'
        cv2.imwrite(name, image)     # save frame as JPG file
        print('Creating...' + name)
    return hasFrames

sec = 0
frameRate = 0.2 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()