import cv2
import pytesseract

"""
# license_plate = cv2.imread('test.jpg', 0)
cv2.imshow('plate', license_plate)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite('ticket.jpg', license_plate)
"""
# if you want camera its 0 and if its a video you wirte the video name
enter = cv2.VideoCapture(0)

while enter.isOpened():
    # true or false will be saved to ret and the frame will saved to frame 
    ret, frame = enter.read()

    # argument source and what we want it to convert to 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.medianBlur(gray, 5)
    cv2.imshow('frame', blurred_frame)
    text = pytesseract.image_to_string(frame)
    print(text)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

enter.release()
cv2.destroyAllWindows()