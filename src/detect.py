from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt


model = YOLO("yolov8n.pt") 


image_path = "E:/jstnimo/coding/Object-Detection/images/test.jpg"

img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results = model(img_rgb)


result_img = results[0].plot()  


plt.imshow(result_img)
plt.axis('off')
plt.show()
