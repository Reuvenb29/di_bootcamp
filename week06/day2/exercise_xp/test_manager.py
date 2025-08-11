# test_manager.py
from menu_item import MenuItem
from menu_manager import MenuManager

# seed a couple items
MenuItem("Soup", 18).save()
MenuItem("Steak", 85).save()

# lookups
print("get_by_name('Soup'):", MenuManager.get_by_name("Soup"))
print("all_items():", MenuManager.all_items())
