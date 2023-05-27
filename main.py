import store
import products


def start(store_obj):
    while True:
        print("     Store Menu     ")
        print("     __________     ")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")
        print()

        if choice == "1":
            print("-------")
            all_products = store_obj.get_all_products()
            for i, product in enumerate(all_products, 1):
                print(f"{i}. {product.show()}")
            print("-------")
            print()

        elif choice == "2":
            print("-------")
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")
            print("-------")
            print()

        elif choice == "3":
            print("-------")
            all_products = store_obj.get_all_products()
            for i, product in enumerate(all_products, 1):
                print(f"{i}. {product.show()}")
            print("-------")
            print()

            shopping_list = []
            while True:
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break
                try:
                    product_number = int(product_number)
                    if product_number < 1 or product_number > len(all_products):
                        print("Invalid product number. Please try again.")
                        continue
                    product = all_products[product_number - 1]
                    quantity = int(input("Enter quantity: "))
                    shopping_list.append((product, quantity))
                    print("Items added to shopping list")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            try:
                total_price = store_obj.order(shopping_list)
                print("********")
                print(f"Order placed successfully! Total price: ${total_price}")
            except Exception as e:
                print(f"Failed to place order: {str(e)}")
            print()

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            print()


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
