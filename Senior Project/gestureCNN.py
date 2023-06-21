#Used to split a video into as many still images as possible to help with image gathering for CNN
#Not all of this is my code, I found it on the internet and modified it for our use-case.

import cv2
 # Path to video file
vidObj = cv2.VideoCapture("C:\\Users\\Richard Sinclair\\Downloads\\erase3.mp4")

# Used as counter variable
count = 3807

# checks whether frames were extracted
success = 1

while success:
    if count == 4000:
        print("Complete!")
        break
    # vidObj object calls read
    # function extract frames
    success, image = vidObj.read()

    # Saves the frames with frame-count
    print("Saving image %d..." % count)
    cv2.imwrite("C:\\Users\\Richard Sinclair\\Desktop\\CNN\\erase\\erase%d.jpg" % count, cv2.flip(image, -1))

    count += 1