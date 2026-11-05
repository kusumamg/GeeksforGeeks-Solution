class Solution:
    def calculateDiscount(self, products):
        products = products.copy()
        condition = (products["product_id"] % 2 == 0) & products["category"].str.startswith("A")
        products["discount"] = products["price"].where(condition, 0)

        return products[["product_id", "discount"]].sort_values("product_id")
