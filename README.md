# 🛡️ SafeNet Kids – Child Online Safety Monitoring System

SafeNet Kids is a **Python-based desktop application** designed to protect children from harmful online content.
The system continuously monitors browser activity, typed text, and screen content in real time to detect dangerous or inappropriate behavior such as cyberbullying, explicit material, gambling sites, drug-related content, and self-harm discussions.

When a threat is detected, the application immediately alerts parents, terminates unsafe browser sessions, and logs the event for later review. The system acts as a **real-time digital guardian for children's online activity**.

---

# 🚀 Features

* 🔍 **Real-time browser monitoring**
* ⌨️ **Keyboard input analysis for harmful text**
* 🧠 **NLP-based cyberbullying detection using VADER sentiment analysis**
* 🖼️ **Computer vision-based explicit content detection**
* 🚫 **Automatic browser termination when threats are detected**
* 📊 **Parent dashboard with activity logs**
* 🔒 **Password-protected monitoring control**
* 📁 **Audit logging for parental review**

---

# 🧠 Detection Capabilities

SafeNet Kids detects multiple categories of online threats:

* Cyberbullying
* Self-harm or suicidal content
* Adult/explicit content
* Gambling websites
* Drug-related content

The system uses a **multi-layered detection approach** combining:

* Keyword filtering
* Natural Language Processing (NLP)
* Computer Vision (Image Analysis)

---

# 🏗️ System Architecture

The system consists of several modular components:

| Module          | Description                                           |
| --------------- | ----------------------------------------------------- |
| Monitor         | Central coordinator managing all monitoring processes |
| NLP Analyzer    | Detects harmful language using sentiment analysis     |
| Image Analyzer  | Detects explicit content from screen captures         |
| Key Logger      | Captures and analyzes typed text                      |
| Process Manager | Terminates unsafe browser sessions                    |
| Dashboard       | Parent interface to monitor activity                  |

---

# 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries & Frameworks**

* CustomTkinter (GUI)
* NLTK (VADER Sentiment Analysis)
* OpenCV (Computer Vision)
* TensorFlow (Image Classification)
* psutil (Process monitoring)
* PyGetWindow (Active window detection)
* Pillow (Screen capture)
* plyer (System notifications)

---

# 📂 Project Structure

```
SafeNet-Kids/
│
├── core/
│   ├── monitor.py
│   ├── nlp_analyzer.py
│   ├── image_analyzer.py
│   ├── key_logger.py
│   └── process_manager.py
│
├── gui/
│   ├── dashboard.py
│   └── auth_window.py
│
├── data/
│   ├── threat_database.json
│   └── safenet_audit.log
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/SafeNet-Kids.git
cd SafeNet-Kids
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Download NLP Data

```python
import nltk
nltk.download('vader_lexicon')
```

---

### 4️⃣ Run the Application

```bash
python main.py
```

---

# 📊 How It Works

1. The system continuously monitors the active browser window.
2. Keyboard input is analyzed for harmful or abusive language.
3. Screenshots are periodically captured and analyzed for explicit content.
4. When harmful content is detected:

   * A parent alert notification is triggered
   * Active browsers are terminated
   * The event is logged in the audit file.

---

# 🔮 Future Improvements

* Machine learning models for improved cyberbullying detection
* Cross-platform support (macOS & Linux)
* Email/SMS alerts for parents
* Web-based monitoring dashboard
* Advanced content filtering

---

# ⚠️ Disclaimer

SafeNet Kids is intended for **educational and parental supervision purposes only**.
Users must ensure ethical and responsible use of monitoring tools.

---

# 📄 License

This project is licensed under the **MIT License**.






