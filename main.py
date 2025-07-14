import logging
from spapi_mock import get_mock_orders

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_orders(orders):
    for order in orders.get("Orders", []):
        print("\n📦 Amazon Order")
        print(f"🆔 Order ID: {order['AmazonOrderId']}")
        print(f"📅 Purchase Date: {order['PurchaseDate']}")
        print(f"🚚 Status: {order['OrderStatus']}")
        print(f"💰 Total: {order['OrderTotal']['Amount']} {order['OrderTotal']['CurrencyCode']}")
        print(f"📧 Buyer Email: {order['BuyerEmail']}")

def main():
    logging.info("Fetching mock Amazon orders...")
    orders = get_mock_orders()
    display_orders(orders)
    logging.info("Done.")

if __name__ == "__main__":
    main()

