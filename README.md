# Object Detection with YOLOv8

![Object Detection Banner](images/sample_banner.jpg)

---

## 📋 Overview
This project implements an **Object Detection system** using the **YOLOv8** model, developed by Ultralytics. YOLOv8 is a state-of-the-art real-time object detection framework capable of detecting multiple objects in **images**, **videos**, and **live webcam feeds** with high accuracy. The system draws bounding boxes around detected objects and provides confidence scores.

> ⚠️ **Note:** Users are encouraged to replace the sample images and videos with their own datasets for testing and fine-tuning.

---

## ✨ Features
- Multi-object detection in real-time
- Supports images, video files, and live webcam feeds
- Displays confidence scores for each detected object
- Highly extensible and customizable
- Optimized for various hardware configurations

---

## 🛠️ Tools & Libraries
- **Python** (3.8+)
- **[YOLOv8](https://ultralytics.com/)** (`ultralytics` package)
- **OpenCV** (for image and video processing)
- **Matplotlib** (for visualization)
- **imageio** (for video handling)

---

## 📊 Performance
The accuracy of YOLOv8 varies across its different model sizes (nano, small, medium, large, extra-large) based on the COCO dataset benchmark (mAP50-95). Below is a summary:

| Model       | mAP50 (%) | mAP50-95 (%) |
|-------------|-----------|--------------|
| YOLOv8n     | 52.4      | 37.3         |
| YOLOv8s     | 56.5      | 44.0         |
| YOLOv8m     | 63.3      | 50.2         |
| YOLOv8l     | 67.3      | 53.4         |
| YOLOv8x     | 68.5      | 54.7         |

For a visual comparison, see the [accuracy chart](#accuracy-chart).

### Accuracy Chart
```json
{
  "type": "bar",
  "data": {
    "labels": ["YOLOv8n", "YOLOv8s", "YOLOv8m", "YOLOv8l", "YOLOv8x"],
    "datasets": [{
      "label": "mAP50-95 (%)",
      "data": [37.3, 44.0, 50.2, 53.4, 54.7],
      "backgroundColor": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"],
      "borderColor": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"],
      "borderWidth": 1
    }]
  },
  "options": {
    "scales": {
      "y": {
        "beginAtZero": true,
        "max": 60,
        "title": {
          "display": true,
          "text": "mAP50-95 (%)"
        }
      },
      "x": {
        "title": {
          "display": true,
          "text": "YOLOv8 Models"
        }
      }
    },
    "plugins": {
      "legend": {
        "display": false
      },
      "title": {
        "display": true,
        "text": "Comparison of mAP50-95 Accuracy for YOLOv8 Models"
      }
    }
  }
}

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
