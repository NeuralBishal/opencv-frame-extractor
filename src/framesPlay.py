
import cv2
import os

print(f'Playing frames from: {os.getcwd()}')
count = 0
while True:
    frame = cv2.imread(f'frame{count}.jpg')
    if frame is None:
        break
    cv2.imshow('Video Playback (Press Q to quit)', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    count += 1
    if count % 100 == 0:
        print(f'Played {count} frames...', end='\r')
cv2.destroyAllWindows()
print(f'\n✅ Successfully played {count} frames!')
