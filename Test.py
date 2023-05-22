from Visuals.Helpers import VideoStream
from time import sleep

vs = VideoStream("test")
vs.openVideoThread("Visuals/Dance_old.mp4").start()
for a in range(7):
    vs.showText(str(a))
    sleep(1)