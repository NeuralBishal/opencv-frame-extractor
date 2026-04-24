import cv2

def frameCapture(path):
    vidobj = cv2.VideoCapture(path)
    
    # Check if video opened successfully
    if not vidobj.isOpened():
        print(f"Error: Could not open video file at {path}")
        return
    
    count = 0
    success = 1
    
    while success:
        success, image = vidobj.read()
        
        if success:  # Only save if frame was read successfully
            cv2.imwrite(f'frame{count}.jpg', image)
            print(f"Saved frame{count}.jpg")
            count += 1
        else:
            print("End of video reached")
    
    vidobj.release()
    print(f"Total frames saved: {count}")

if __name__ == '__main__':
    frameCapture('Black and White Grunge Criminal Investigation Bumper Video.mp4')