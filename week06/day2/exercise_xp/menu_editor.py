# menu_editor.py
from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n=== Restaurant Menu Manager ===")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")
        choice = input("Choose an option: ").strip().upper()

        if choice == "V":
            name = input("Enter item name to view: ").strip()
            item = MenuManager.get_by_name(name)
            print(f"Found: {item}" if item else "No item with that name.")

        elif choice == "A":
            add_item_to_menu()

        elif choice == "D":
            remove_item_from_menu()

        elif choice == "U":
            update_item_from_menu()

        elif choice == "S":
            show_restaurant_menu()

        elif choice == "E":
            print("\nExiting... Final restaurant menu:")
            show_restaurant_menu()
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

def add_item_to_menu():
    name = input("New item name: ").strip()
    price_str = input("New item price (integer): ").strip()
    if not price_str.isdigit():
        print("Price must be an integer.")
        return
    item = MenuItem(name, int(price_str))
    print("Item was added successfully." if item.save() else "Error adding item.")

def remove_item_from_menu():
    name = input("Enter item name to delete: ").strip()
    item = MenuItem(name, 0)
    print("Item was deleted successfully." if item.delete() else "Error: item not found or could not be deleted.")

def update_item_from_menu():
    current_name = input("Enter current item name: ").strip()
    new_name = input("Enter NEW item name: ").strip()
    new_price_str = input("Enter NEW item price (integer): ").strip()
    if not new_price_str.isdigit():
        print("New price must be an integer.")
        return
    item = MenuItem(current_name, 0)
    print("Item was updated successfully." if item.update(new_name, int(new_price_str)) else "Error updating item.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("(menu is empty)")
        return
    print("\n--- Restaurant Menu ---")
    for it in items:
        print(f"{it.name:20} ... {it.price}")

if __name__ == "__main__":
    show_user_menu()
