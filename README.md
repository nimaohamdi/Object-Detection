# 🖼️ Object Detection with YOLOv8

![Object Detection Banner](images/sample_banner.jpg)

---

## 🔹 Project Overview
This project is an **Object Detection system** using the **YOLOv8** model.  
It can detect multiple objects in **images, videos, and live webcam feeds**, drawing bounding boxes with confidence scores.

> ⚠️ **Note:** Users are encouraged to replace the sample images and videos with their own data for testing.

---

## 🔹 Features
- Detect multiple objects simultaneously  
- Works on images, video files, and real-time webcam feeds  
- Displays confidence scores for each detected object  
- Easy to run and extend  

---

## 🔹 Tools & Libraries
- Python  
- [YOLOv8](https://ultralytics.com/) (`ultralytics`)  
- OpenCV  
- Matplotlib  

---

## 🔹 Installation
Install the required Python packages:

```bash
pip install ultralytics opencv-python matplotlib

🔹 How to Run
Image Detection

python src/detect.py

🔹 Video or Webcam Detection

python src/detect_video.py


Press q to exit the video or webcam feed.

🔹 Example Outputs

⚠️ Sample images are included, but users should use their own images or videos.



🔹 Notes

You can switch YOLOv8 models for better accuracy: yolov8n.pt (nano), yolov8s.pt (small), or yolov8m.pt (medium).

Adjust the file paths to your own images/videos.
