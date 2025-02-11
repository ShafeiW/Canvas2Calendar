# README.md

# 📅 Canvas2Calendar
Automatically sync your **Canvas** assignment due dates with **Google Calendar**! 🚀

## ✨ Features
- Fetches assignments from Canvas API 📚
- Adds due dates to Google Calendar 📆
- Prevents duplicate events ✅
- Runs automatically every **2 days** 🔄
- Supports **Pacific Time (PST/PDT)** 🌍

## 🛠 Installation
### **1. Clone this repository**
```bash
git clone https://github.com/ShafeiW/Canvas2Calendar.git
cd Canvas2Calendar
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set up Google Calendar API**
1. **Enable Google Calendar API** at [Google Cloud Console](https://console.cloud.google.com/)
2. **Create a Service Account & Download `credentials.json`**
3. **Share your Google Calendar with the Service Account** (Give **Make changes and manage sharing** permission)
4. **Copy your Calendar ID** and update `add_to_calendar.py`:
   ```python
   CALENDAR_ID = "your-calendar-id@group.calendar.google.com"
   ```

### **4. Set up Canvas API**
1. **Go to Canvas** ([your Canvas instance](https://canvas.sfu.ca/))
2. **Generate an API Token**:
   - Click **Account > Settings > Approved Integrations**
   - Click **+ New Access Token** → Generate it
   - Copy the token and paste it in `config.py`

### **5. Running the script manually**
To sync assignments immediately:
```bash
python main.py
```

## 🔄 Automating the Script
### **Windows: Run in Background**
```powershell
Start-Process python -ArgumentList "main.py" -WindowStyle Hidden
```

### **Mac/Linux: Use `nohup` or `screen`**
```bash
nohup python main.py &
```

## 📅 Checking If Events Are Added
1. **Open Google Calendar** ([calendar.google.com](https://calendar.google.com/))
2. Ensure your **calendar is checked** in the sidebar
3. Click **⚙️ Settings > Refresh**

## 🛑 .gitignore
```
credentials.json
config.py
venv/
.env
__pycache__/
*.pyc
*.pyo
```

## 📜 License
MIT License © 2025


## Acknowledgements
This project was born out of a fiery burst of determination, fueled by my deep-seated loathing for fruitcake.
