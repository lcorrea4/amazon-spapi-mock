from datetime import datetime, timedelta

def get_mock_orders():
    return {
        "Orders": [
            {
                "AmazonOrderId": "111-2222222-3333333",
                "PurchaseDate": (datetime.utcnow() - timedelta(days=3)).isoformat(),
                "OrderStatus": "Shipped",
                "OrderTotal": {"CurrencyCode": "USD", "Amount": "39.99"},
                "BuyerEmail": "mock-buyer1@example.com"
            },
            {
                "AmazonOrderId": "444-5555555-6666666",
                "PurchaseDate": (datetime.utcnow() - timedelta(days=1)).isoformat(),
                "OrderStatus": "Pending",
                "OrderTotal": {"CurrencyCode": "USD", "Amount": "89.99"},
                "BuyerEmail": "mock-buyer2@example.com"
            }
        ]
    }

