import cv2
import time
import os
import hand as htm

pTime = 0
cap = cv2.VideoCapture(0)
FolderPath = "Fingers"
lst = os.listdir(FolderPath)
lst2 = []
# print(lst)
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    print(f"{FolderPath}/{i}")
    lst2.append(image)
print(lst2[0].shape)
detector = htm.handDetector(detectionCon=1)
fingerid = [4, 8, 12, 16, 20, 24, 28, 32]
while True:
    ret, frame = cap.read()
    # h, w, c = lst2[0].shape
    # frame[0:h, 0:w] = lst2[0]
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame, draw= False)
    # print(lmlist)

    if len(lmlist) != 0:
        fingers = []
        #viết cho ngón cái
        if lmlist[fingerid[0]][2] < lmlist[fingerid[0]-1][2]:
            fingers.append(1)
        else:
            fingers.append(0)

        # viết cho ngón dài
        for id in range (1,5):
            if lmlist[fingerid[id]][2] < lmlist[fingerid[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)
        songontay = fingers.count(1)
        # h, w, c = lst2[songontay - 1].shape
        # frame[0:h, 0:w] = lst2[songontay - 1]
        # hiện số ngón tay
        cv2.rectangle(frame, (0, 250), (100, 300), (0, 255, 0), -1)
        cv2.putText(frame, str(songontay), (30, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)
    #viết ra FPS
    cTime = time.time() 
    fps = 1/(cTime - pTime)
    pTime = cTime
    #show FPS lên màn
    cv2.putText(frame, f"FPS: {int(fps)}", (60,50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("Quan Ngo", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()