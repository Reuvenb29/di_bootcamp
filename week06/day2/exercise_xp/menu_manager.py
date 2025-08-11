# menu_manager.py
from db import get_connection
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name: str) -> MenuItem | None:
        sql = """
            SELECT item_name, item_price
            FROM Menu_Items
            WHERE item_name = %s;
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (name,))
                    row = cur.fetchone()
                    if row:
                        item_name, item_price = row
                        return MenuItem(item_name, item_price)
                    return None
        except Exception as e:
            print("[get_by_name] Error:", e)
            return None

    @classmethod
    def all_items(cls) -> list[MenuItem]:
        sql = """
            SELECT item_name, item_price
            FROM Menu_Items
            ORDER BY item_name;
        """
        items: list[MenuItem] = []
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    for item_name, item_price in cur.fetchall():
                        items.append(MenuItem(item_name, item_price))
        except Exception as e:
            print("[all_items] Error:", e)
        return items





# test_manager.py
from menu_item import MenuItem
from menu_manager import MenuManager

# seed a couple items
MenuItem("Soup", 18).save()
MenuItem("Steak", 85).save()

# lookups
print("get_by_name('Soup'):", MenuManager.get_by_name("Soup"))
print("all_items():", MenuManager.all_items())
