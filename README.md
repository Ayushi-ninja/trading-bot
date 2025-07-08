# Binance Trading Bot (Simulation Assignment)

This project is a simulated Binance trading bot built using Python. It is intended for educational purposes and mimics the basic functionality of connecting to the Binance API, placing simulated orders, logging events, and handling exceptions.

## 📌 Features

- Simulates connecting to the Binance API
- Simulated BUY/SELL order placement
- Basic error handling
- Logging to `bot.log`
- Modular code structure for easy understanding

## 📁 Project Structure

TRADING-BOT/
│
├── logs/ # Contains log files (bot.log)
│ └── bot.log
│
├── venv/ # Python virtual environment
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ └── pyvenv.cfg
├── .env # Environment variables (add   your Gmail credentials here)
├── bot.py # Core bot logic
├── create_log.py # Log creation and setup
├── gui.py # Optional GUI script (if applicable)
├── main.py # Entry point to run the bot
├── trading_bot.log # Sample log for assignment
├── utils.py # Utility functions (email, etc.)
├── README.md # You are here 📄

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7 or above installed.

🛠️ How to Run

1.Clone the repository:

.git clone https://github.com/Ayushi-ninja/trading-bot
.cd trading-bot

🐍 Create Virtual Environment

.python -m venv venv .venv\Scripts\activate # On Windows

2.Install dependencies (use a virtual environment if needed):

.pip install -r requirements.txt
(If you don’t have a requirements.txt, just install manually:)

.pip install python binance python-dotenv 
.pip install colorama


3.Run the bot:

.python main.py
.python gui.py 
Follow the prompts in the terminal to place test orders.


📝 Sample Usage

Enter trading symbol (e.g., BTCUSDT): BTCUSDT
Enter side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): LIMIT
Enter quantity: 0.001
Enter limit price: 58000
Confirm order (Y/N)? Y


📒 Logs
.All logs are saved under the logs/ directory (bot.log file).
.Automatically created when the script runs.
.Includes errors, warnings, and success messages.


👩‍💻 Author
Made with 💻 by Ayushi Rajput


🧪 Disclaimer
This bot runs only on the Binance Futures Testnet — it does not execute real trades. For learning and simulation purposes only.
