class ShopifyAgent:
    def __init__(self):
        pass

    def generate_shopify_ql(self, question: str):
        # MOCK ShopifyQL generation
        return """
        SELECT
          product_title,
          SUM(quantity) as total_sold
        FROM orders
        WHERE created_at >= date_sub('day', 30)
        GROUP BY product_title
        ORDER BY total_sold DESC
        LIMIT 5
        """

    def explain_data(self, raw_data):
        # MOCK business explanation
        return (
            "Based on the last 30 days of sales, Product X is selling consistently.\n\n "
            "You currently have 5 units left in stock, so it is recommended to reorder soon "
            "to avoid running out of inventory."
        )
