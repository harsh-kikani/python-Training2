menu = {
    'pizza':100,
    'pasta':70,
    'burger':60,
    'frenkie':80,
    'salad':40,
    'coffee':50,
    
}
print("Welcome to Restaurant")
print("Pizza: Rs100\nPasta: Rs70\nBurger: Rs60\nfrenkie: Rs80\nSalad: Rs40\nCoffee: Rs50")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
 
else:
    print(f"ordered item {item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (yes/no) ")

if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
       order_total += menu[item_2]
       print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available !")
        
print(f"the total amount of items to pay is Rs{order_total}")           