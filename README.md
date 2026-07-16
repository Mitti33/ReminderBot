# 🧠 Power Reminder Bot

A lightweight Python automation that delivers a **daily random notification** inspired by *The 48 Laws of Power* directly to your Android phone.

Unlike simple random quote generators, the bot remembers which reminders have already been sent, ensuring that every law is shown **once per cycle** before reshuffling.

The project is fully automated using **GitHub Actions**, so notifications are delivered every day even when your computer is turned off.

---

## ✨ Features

* 📱 Sends daily push notifications to your Android phone using **ntfy**
* 🎲 Randomized, non-repeating reminder order
* 🧠 Tracks progress using persistent state
* ☁️ Runs automatically on GitHub Actions
* 📂 Stores reminders in a clean JSON format
* 🔄 Automatically reshuffles after all reminders have been shown

---

## 📁 Project Structure

```text
power-reminder-bot/
│
├── .github/
│   └── workflows/
│       └── notify.yml
│
├── data/
│   ├── laws.json
│   └── state.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 How It Works

1. Loads all reminders from `data/laws.json`.
2. Maintains a shuffled order of reminders.
3. Sends the next reminder as a push notification using **ntfy**.
4. Updates `state.json` to remember progress.
5. GitHub Actions commits the updated state so the bot continues where it left off.

This guarantees that reminders are not repeated until every reminder has been delivered once.

---

## 🛠️ Technologies Used

* Python
* GitHub Actions
* JSON
* ntfy
* Requests

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/power-reminder-bot.git
cd power-reminder-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
python main.py
```

If your phone is subscribed to the configured **ntfy** topic, you'll instantly receive a notification.

---

## ⚙️ Automation

The repository includes a GitHub Actions workflow that runs automatically every day at the scheduled time.

You can also trigger it manually from the **Actions** tab in GitHub.

---

## 🔮 Future Improvements

* Multiple reminder variants for each law
* AI-generated original summaries
* Support for multiple books and knowledge collections
* Rich notification formatting
* Configurable notification schedule
* Web dashboard for managing reminder collections

