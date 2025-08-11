# menu_item.py
from db import get_connection

class MenuItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = int(price)

    def save(self) -> bool:
        """
        INSERT this item into the table.
        True on success, False on error (e.g., duplicate name).
        """
        sql = """
            INSERT INTO Menu_Items (item_name, item_price)
            VALUES (%s, %s)
            RETURNING item_id;
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (self.name, self.price))
                    _ = cur.fetchone()  # proves row inserted
            return True
        except Exception as e:
            print(f"[save] Error:", e)
            return False

    def delete(self) -> bool:
        """
        DELETE this item by its current name.
        True if a row was deleted, False if not found or error.
        """
        sql = """
            DELETE FROM Menu_Items
            WHERE item_name = %s
            RETURNING item_id;
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (self.name,))
                    row = cur.fetchone()
                    return row is not None
        except Exception as e:
            print(f"[delete] Error:", e)
            return False

    def update(self, new_name: str, new_price: int) -> bool:
        """
        UPDATE matched by current self.name.
        On success, update this object's fields too.
        """
        sql = """
            UPDATE Menu_Items
            SET item_name = %s, item_price = %s
            WHERE item_name = %s
            RETURNING item_id;
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (new_name, int(new_price), self.name))
                    row = cur.fetchone()
                    if row:
                        self.name = new_name
                        self.price = int(new_price)
                        return True
                    return False
        except Exception as e:
            print(f"[update] Error:", e)
            return False

    def __repr__(self) -> str:
        return f"MenuItem(name='{self.name}', price={self.price})"
