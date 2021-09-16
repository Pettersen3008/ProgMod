import cv2
import sys

imgPath = sys.argv[1]
cascPath = 'haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(cascPath)

img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print('Found {0} faces!'.format(len(faces)))

for (x, y, w, h) in faces:

cv2.imshow("Faces Found", img)
cv2.waitKey(0)