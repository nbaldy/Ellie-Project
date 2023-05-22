import cv2
from threading import Thread

# From https://stackoverflow.com/a/40285604
class VideoStream:
    def __init__(self, windowName):
        self.text = ""
        self.frame = None
        self.name = windowName
        
    def openVideoThread(self, filename):
        return Thread(target=self.__openVideo, args=[filename])

    def showText(self, text):        
        self.text = text
            
    def __putText(self):
        font_face = cv2.FONT_HERSHEY_SIMPLEX = 0
        scale = 10
        color = (0, 0, 0)
        position = (200, 200)
        # Line thickness of 2 px
        thickness = 2
        cv2.putText(self.frame, self.text, position, font_face, scale, color, thickness, cv2.LINE_AA)
        print(self.text)

    def __openVideo(self, filename):
        cap = cv2.VideoCapture(filename)
        ret, frame = cap.read()
        while(True):
           ret, self.frame = cap.read()
           if not ret:
               # Video done
               break
           if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
               break
           self.__putText()
           cv2.imshow(self.name,self.frame)
        cap.release()
