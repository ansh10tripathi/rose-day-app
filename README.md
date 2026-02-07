# 🌹 Rose Day App

A romantic web application that allows users to create and share a personalized rose with a heartfelt message using a unique, shareable link.  
Built with FastAPI and designed with elegant UI animations to make the experience special and memorable.

---

## ✨ Features

- 🌹 Create a personalized rose with recipient name and message
- 🔗 Generate a unique, shareable link for each rose
- 💌 Click-to-reveal message with typewriter animation
- 🌗 Light / Dark mode with a pill-style toggle
- 🌫 Fade-on-idle toggle for a clean UI experience
- 💕 Floating hearts animation
- 📱 Fully responsive (works on mobile, tablet, desktop)
- 🗃️ Persistent storage using SQLite and SQLAlchemy

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Templating Engine:** Jinja2
- **Database:** SQLite
- **ORM:** SQLAlchemy

---

## 🚀 How It Works

1. The sender opens the **Send a Rose** page
2. Enters the recipient’s name and a custom message
3. The app generates a **unique URL**
4. The recipient opens the link and sees:
   - A rose-themed page
   - A hidden message revealed with animation

Each rose is stored in the database and can be viewed by anyone with the link.

---

## 🧑‍💻 Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ansh10tripathi/rose-day-app.git
cd rose-day-app


