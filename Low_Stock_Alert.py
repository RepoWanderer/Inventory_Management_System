import sqlite3
def check_low_stock(threshold=5):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, quantity FROM products WHERE quantity < ?", (threshold,))
    low_stock_items = cursor.fetchall()

    conn.close()

    if low_stock_items:
        print("Low Stock Alert:")
        for item in low_stock_items:
            print(f"{item[0]} - {item[1]} left")
    else:
        print("All stock levels are sufficient.")

# Example usage
# check_low_stock()
