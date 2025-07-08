import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting trading bot...")
logging.info("Connecting to Binance API...")
logging.info("Successfully connected to Binance API.")
logging.info("Placed BUY order: BTCUSDT, Market, Qty: 0.001")
logging.info("Order executed successfully.")
logging.error("Failed to fetch market data: TimeoutError")
logging.info("Retrying fetch market data...")
logging.info("Stopping trading bot.")
