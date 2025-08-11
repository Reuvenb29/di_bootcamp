# test_item_ops.py
from menu_item import MenuItem

def main():
    burger = MenuItem("Burger", 35)
    print("save:", burger.save())        # True on first insert, False if duplicate

    print("update to Veggie Burger 37:", burger.update("Veggie Burger", 37))
    # Now self.name is "Veggie Burger"
    print("delete:", burger.delete())

if __name__ == "__main__":
    main()
