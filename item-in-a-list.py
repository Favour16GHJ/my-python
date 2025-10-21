item = input("Enter an item: ")
list_items = ["tables", "chairs", "pens", "books"]

if item in list_items:
    print(f"{item} is found in the list.")
else:
    print(f"{item} is not found in the list.")
