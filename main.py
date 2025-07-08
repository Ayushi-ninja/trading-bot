"""
Binance Futures Testnet Trading Bot
Created by: Ayushi Rajput
Date: July 8, 2025
Description:
This script allows a user to place simulated trades on Binance Futures Testnet via CLI.
Supports both Market and Limit orders with basic input validation and logging.
"""

from bot import BasicBot
import logging
import os
from colorama import init, Fore, Style

init(autoreset=True)

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Setup logging
log_file = os.path.join("logs", "bot.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    bot = BasicBot()
    print(Fore.GREEN +"Welcome to the Binance Testnet Trading Bot")
    
    while True:
        try:
            symbol = input(Fore.CYAN +"Enter trading symbol (e.g., BTCUSDT): ").upper()
            side = input(Fore.CYAN +"Enter side (BUY/SELL): ").upper()
            order_type = input(Fore.CYAN +"Enter order type (MARKET/LIMIT): ").upper()
            quantity = float(input(Fore.CYAN +"Enter quantity: "))
            price = None
            stop_price = None

            if order_type == 'LIMIT':
                price = input(Fore.CYAN + "Enter limit price: ")
            elif order_type == 'STOP_MARKET':
                stop_price = input(Fore.CYAN + "Enter stop price: ") 
            elif order_type == 'STOP_LIMIT':
                stop_price = input(Fore.CYAN + "Enter stop price: ")
                price = input(Fore.CYAN + "Enter limit price: ")
            
            summary = f"Symbol: {symbol}, Side: {side}, Type: {order_type}, Qty: {quantity}"
            if price:
                summary += f", Price: {price}"
            if stop_price:
                summary += f", Stop Price: {stop_price}"

            print(Fore.YELLOW + summary)
            confirm = input(Fore.GREEN + "Confirm order (Y/N)? ").strip().upper()
            if confirm != 'Y':
                print(Fore.RED + "Order cancelled.\n")
                continue    
   
            order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)

            if order:
                print(Fore.GREEN + "Order Placed Successfully:")
                print(Fore.GREEN + str(order))   
            else:
                print( Fore.RED +"Order Failed")
                
        except KeyboardInterrupt:
            print(Fore.RED + "\nExiting...")
            break
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            print(Fore.RED + f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
