from binance.client import Client
from binance.exceptions import BinanceAPIException
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Get the existing logger
logger = logging.getLogger(__name__)

class BasicBot:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET")
        )
        # Set base URL for Binance Futures Testnet
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        self.client._request_options = {"timeout": 10}
        self.client.API_URL = 'https://testnet.binancefuture.com/fapi'  
        self.client.timestamp_offset = 0
        self.client.futures_ping()  
        

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Place an order of various types (MARKET, LIMIT, STOP_MARKET, STOP_LIMIT).
        """
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    quantity=quantity,
                    price=price,
                    timeInForce='GTC'
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP_MARKET',
                    stopPrice=stop_price,
                    quantity=quantity,
                    timeInForce='GTC'
                )
            elif order_type == 'STOP_LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP',
                    price=price,
                    stopPrice=stop_price,
                    quantity=quantity,
                    timeInForce='GTC'
                )
            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            logger.info(f"{order_type} order placed: {order}")
            return order

        except Exception as e:
            logger.error(f"{order_type} order failed: {e}")
            print(f"{order_type} order failed: {e}")
            return None

    def place_oco_order_spot(self, symbol, side, quantity, price, stop_price, stop_limit_price):
        """
        Place an OCO (One Cancels the Other) order on SPOT market only.
        """
        try:
            order = self.client.create_oco_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                stopLimitPrice=stop_limit_price,
                stopLimitTimeInForce='GTC'
            )
            logger.info(f"OCO order placed: {order}")
            return order

        except Exception as e:
            logger.error(f"OCO order failed: {e}")
            print(f"OCO order failed: {e}")
            return None

    def place_twap_order(self):
        logger.info("TWAP strategy not implemented")
        print("TWAP strategy logic not yet implemented.")

    def place_grid_strategy(self):
        logger.info("Grid strategy not implemented")
        print("Grid strategy logic not yet implemented.")