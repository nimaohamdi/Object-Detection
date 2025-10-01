from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture("../videos/test_video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    frame = results[0].plot()  

    cv2.imshow("Object Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
