# 🎯 Focsy — AI Anti-Doomscrolling System

Focsy is an AI-powered computer vision project designed to help users reduce mobile phone distractions while working on a laptop. It uses the laptop camera, with user permission, to analyze posture and hand position and identify prolonged phone-focused behavior.

When the detected distraction continues beyond a predefined threshold, Focsy automatically triggers an alarm to bring the user's attention back to their task.

## ✨ Features

* 📷 Real-time laptop camera monitoring
* 🧠 Computer vision-based distraction detection
* 👤 Face and posture analysis
* 📱 Phone-usage behavior detection
* ⏱️ Customizable distraction threshold
* 🔔 Automatic alarm when the threshold is exceeded
* 🔒 Designed for local processing and user consent
* ⚡ Real-time detection

## 🛠️ Technologies Used

* **Python**
* **OpenCV** — camera access and real-time image processing
* **MediaPipe** — face and pose landmark detection
* **NumPy** — numerical processing
* **playsound** — alarm playback
* **Threading** — non-blocking alarm execution

## ⚙️ How It Works

```text
Laptop Startup / Manual Launch
          ↓
     Camera Permission
          ↓
     Camera Activated
          ↓
   Real-Time Frame Capture
          ↓
  Face + Pose Landmark Analysis
          ↓
 Phone-Focused Behavior Detected
          ↓
   Threshold Timer Starts
          ↓
 Threshold Exceeded?
      ↙          ↘
    No             Yes
    ↓               ↓
Continue        🔔 Alarm
Monitoring
```

## 📂 Project Structure

```text
Focsy/
│
├── doomscroll.py
├── alarm.mp3
├── README.md
└── venv/
```

### File Description

| File            | Purpose                              |
| --------------- | ------------------------------------ |
| `doomscroll.py` | Main Python application              |
| `alarm.mp3`     | Audio used for the distraction alert |
| `README.md`     | Project documentation                |
| `venv/`         | Python virtual environment           |

## 🚀 Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Focsy
```

### 2. Create a virtual environment

Python 3.10 is recommended for compatibility with the computer-vision dependencies.

```bash
py -3.10 -m venv venv
```

### 3. Activate the environment

Windows CMD:

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

### 4. Install dependencies

```cmd
pip install opencv-python mediapipe numpy playsound==1.2.2
```

## ▶️ Run the Project

Make sure the virtual environment is activated:

```cmd
venv\Scripts\activate
```

Then run:

```cmd
python doomscroll.py
```

The application will open the laptop camera and begin real-time monitoring.

Press **Q** to exit the application.

## ⏱️ Threshold Time

The project uses a configurable threshold to determine how long distraction must continue before the alarm is triggered.

For example:

```python
DOOMSCROLL_TIME = 20
```

This means the detected distraction must persist for approximately **20 seconds** before the alarm activates.

You can change it to:

```python
DOOMSCROLL_TIME = 30
```

or:

```python
DOOMSCROLL_TIME = 60
```

depending on your preferred threshold.

## 🔔 Alarm System

When the detected phone-focused behavior remains active beyond the threshold, the application plays:

```text
alarm.mp3
```

The alarm is executed separately so that audio playback does not unnecessarily block the video-processing loop.

## 🧠 AI / Computer Vision Concepts

### Computer Vision

Computer vision allows the system to process camera frames and extract information about the user's posture and movements.

### MediaPipe

MediaPipe provides facial and pose landmarks that can be used to analyze head orientation and body position.

### Real-Time Processing

Frames are continuously captured and analyzed while the camera is active.

### Behavioral Detection

The project uses visual indicators such as posture and hand position as signals of possible phone distraction.

### Threshold-Based Alert

A timer ensures that short or accidental movements do not immediately trigger the alarm.

## 🔐 Privacy

Focsy is designed as a local computer-vision prototype.

* Camera access requires user permission.
* Video is processed locally.
* No camera footage is intentionally uploaded to a server.
* No personal data is intentionally stored by the application.

> **Note:** The system detects behavioral indicators associated with phone distraction; it does not directly determine a person's mental state or definitively prove that they are doomscrolling.

## 🎯 Future Improvements

* 📱 More reliable phone-object detection using YOLO
* 🖥️ Graphical user interface
* 📊 Daily distraction statistics
* ⏰ Custom schedules and thresholds
* 🔔 Multiple alarm sounds
* 📈 Focus-time analytics
* 🤖 ML-based behavior classification
* 🚀 Automatic application startup
* 🔒 Additional privacy controls

## 💡 Use Cases

* Students studying with laptops
* Remote workers
* Programmers
* Online learners
* Digital productivity monitoring
* Personal focus management

## 👩‍💻 Author

**Vaishnavi Gandikota**

AI/ML Engineer | Computer Vision | Machine Learning

## ⭐ Project Goal

> **Less scrolling. More focusing.**

Focsy explores how AI and computer vision can be used to encourage healthier digital habits through real-time, user-controlled alerts.
