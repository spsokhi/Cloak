import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not access the camera. Try using index 1 or 2.")
    exit()

time.sleep(2)

print("📸 Capturing background... please stay still")
for _ in range(60):
    ret, bg = cap.read()
    if ret:
        bg = cv2.flip(bg, 1)
print("✅ Background captured")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1) 

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
    mask_inv = cv2.bitwise_not(mask)

    cloak_area = cv2.bitwise_and(bg, bg, mask=mask)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow("🪄 Invisibility Cloak", final)
    cv2.imshow("🎭 Cloak Mask (debug)", mask)

    key = cv2.waitKey(1) & 0xFF
    if key == 27: 
        break
    elif key == ord('b'):
        print("♻️ Re-capturing background...")
        for _ in range(60):
            ret, bg = cap.read()
            if ret:
                bg = cv2.flip(bg, 1)
        print("✅ Background updated")

cap.release()
cv2.destroyAllWindows()
