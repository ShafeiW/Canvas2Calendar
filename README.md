# 📅 Canvas2Calendar
Automatically sync your **Canvas** assignment due dates with **Google Calendar**! 🚀

## ✨ Features
- Fetches assignments from Canvas API 📚
- Adds due dates to Google Calendar 📆
- Prevents duplicate events ✅
- Supports **Pacific Time (PST/PDT)** 🌍

## 🛠 Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/ShafeiW/Canvas2Calendar.git
   cd Canvas2Calendar
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Google API credentials:**
   - Create a **Google Cloud Project** and enable **Google Calendar API**
   - Download `credentials.json` and place it in the project folder
   - Share your Google Calendar with your service account

4. **Set up Canvas API:**
   - Go to Canvas **Account > Settings > Approved Integrations**
   - Generate a new **Access Token** and add it to `config.py`

## 🚀 Usage
Run the script to sync assignments:
```bash
python main.py
```

## 🔧 Configuration
Edit `config.py` with your **Canvas API URL**, **Access Token**, and **Google Calendar ID**.

## 🛑 .gitignore
**Make sure `credentials.json` and `config.py` are ignored in Git!**

## 🤝 Contributing
Pull requests are welcome! Feel free to fork and submit improvements.

## 📜 License
MIT License © 2025
