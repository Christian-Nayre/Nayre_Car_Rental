car_library = {
    'Toyota': {
        'cars': {
            'Camry': {'model': '2020', 'cost': 2000, 'quantity': 5},
            'Corolla': {'model': '2020', 'cost': 1500, 'quantity': 3},
            'Rav4': {'model': '2020', 'cost': 1800, 'quantity': 4},
            'Yaris': {'model': '2020', 'cost': 1700, 'quantity': 2}
        }
    },
    'Hyundai': {
        'cars': {
            'Accent': {'model': '2020', 'cost': 1000, 'quantity': 3},
            'Elantra': {'model': '2020', 'cost': 1200, 'quantity': 2},
            'Santa Fe': {'model': '2020', 'cost': 1500, 'quantity': 4},
            'Tucson': {'model': '2020', 'cost': 1300, 'quantity': 3}
        }
    },
    'Mitsubishi': {
        'cars': {
            'Outlander': {'model': '2020', 'cost': 900, 'quantity': 4},
            'Mirage': {'model': '2020', 'cost': 800, 'quantity': 3},
            'Pajero': {'model': '2020', 'cost': 2200, 'quantity': 2},
            'Eclipse Cross': {'model': '2020', 'cost': 1000, 'quantity': 3}
        }
    },
    'Ford': {
        'cars': {
            'Fiesta': {'model': '2020', 'cost': 25000, 'quantity': 2},
            'Focus': {'model': '2020', 'cost': 23000, 'quantity': 3},
            'Escape': {'model': '2020', 'cost': 27000, 'quantity': 4},
            'Expedition': {'model': '2020', 'cost': 35000, 'quantity': 2}
        }
    },
    'Porsche': {
        'cars': {
            '911': {'model': '2020', 'cost': 3000, 'quantity': 3},
            'Panamera': {'model': '2020', 'cost': 3500, 'quantity': 2},
            'Cayenne': {'model': '2020', 'cost': 4000, 'quantity': 4},
            'Macan': {'model': '2020', 'cost': 3200, 'quantity': 3}
        }
    }
}

user_accounts = {}
user_rented_cars = {}
user_transactions = {}
admin_username = "admin"
admin_password = "1234"

def main():
    while True:
        try:
            print ("\n----------Welcome to Nayre Voyage Wheel's----------")
            print ("___________________________________________________\n")
            print ("1. Available Cars")
            print ("2. Register account")
            print ("3. Login as User")
            print ("4. Login as Administrator")
            print ("5. Exit")
            choice = int(input("Enter your choice:"))

            if choice == 1:
                while True:
                    available_cars()
                    car_choice = input("Browse another car(y/n)? ")
                    if car_choice == 'y':
                        available_cars()
                    else:
                        main()
            if choice == 2:
                sign_in()
            if choice == 3:
                log_in()
            if choice == 4:
                admin()
            if choice == 5:
                print ("Exiting...")
                quit()
            else: 
                print ("Plese input a valid number...")
        except ValueError as e:
            print (f"Error Occured; {e}.")
        

def sign_in():
    while True:
            try:
                wallet = 0
                print("\n----------SIGN IN----------")
                username = input("Enter your username (Leave blank to go back): ")

                if not username:
                    main()
                
                if username in user_accounts:
                    print ("User name is already taken, please enter a new username...")
                    sign_in()
                
                password = input("Enter your password (must be at least 8 characters): ")

                if len(password) < 8:
                    print ("Password must be at least 8 characters")
                else:
                    user_accounts[username] = {'username': username, 'password': password, 'wallet': wallet}
                    print ("Signed in successfully")
                    main()

                

            except ValueError as e:
                print (f"Error Occured: {e}")

def log_in():
    while True:
        print("\n----------LOG IN----------")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if not username:
            main()
        
        if username in user_accounts and password == user_accounts[username]['password']:
            print ("Login successful")
            user_menu(username)
        
        else:
                print("Invalid inputs. Account or password doesn't exist!")
                continue

def admin():
    print("----------ADMIN lOGIN----------")
    username = input("Enter username (leave blank to go back): ")
    if not username:
        main()
    if username == admin_username:
        password = input("Enter password: ")
        if password == admin_password:
            print("Log In Successful")
            admin_menu()
        else:
            print("Invalid Password or Username.")
            admin()
    else: 
        print("Try Again")
        admin()

def admin_menu():
    while True:
        print("\n----------Admin Menu----------")
        print("1. View All Transactions")
        print("2. Add Car")
        print("3. Edit Car Price")
        print("4. Remove Car")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_transactions()
        elif choice == '2':
            add_car()
        elif choice == '3':
            edit_car_price()
        elif choice == '4':
            remove_car()
        elif choice == '5':
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")


def view_all_transactions():
    print("\nAll Transactions:")
    for user, transactions in user_transactions.items():
        print(f"\nUser: {user}")
        for transaction in transactions:
            print(f"Transaction: {transaction}")


def add_car():
    brand = input("Enter the brand of the car: ")
    car_name = input("Enter the name of the car: ")
    model = input("Enter the model year of the car: ")
    cost = float(input("Enter the cost of the car: "))
    quantity = int(input("Enter the quantity of the car: "))

    if brand in car_library:
        car_library[brand]['cars'][car_name] = {'model': model, 'cost': cost, 'quantity': quantity}
    else:
        car_library[brand] = {'cars': {car_name: {'model': model, 'cost': cost, 'quantity': quantity}}}
    print("Car added successfully.")


def edit_car_price():
    available_cars()
    brand = input("Enter the brand of the car you want to edit: ")
    car_name = input("Enter the name of the car you want to edit: ")
    new_price = float(input("Enter the new price of the car: "))

    if brand in car_library and car_name in car_library[brand]['cars']:
        car_library[brand]['cars'][car_name]['cost'] = new_price
        print("Car price updated successfully.")
    else:
        print("Car not found.")
    if not brand:
        admin_menu()


def remove_car():
    print("Select the brand from which you want to remove a car:")
    print_available_brands()
    brand_choice = input("Enter the number of the brand: ")
    
    if brand_choice.strip() == '':
        print("Returning to the admin menu...")
        admin_menu()
    
    brand_index = int(brand_choice)
    if brand_index in available_brand_indices:
        selected_brand = available_brand_indices[brand_index]
        available_cars_for_brand = car_library[selected_brand]['cars']
        if len(available_cars_for_brand) > 0:
            print(f"\nAvailable cars for {selected_brand}:")
            print_available_cars_for_brand(selected_brand)
            car_name_choice = input("Enter the number of the car you want to remove: ")
            if car_name_choice.strip() == '':
                print("Returning to the admin menu...")
                admin_menu()
            car_name_index = int(car_name_choice)
            car_names = list(available_cars_for_brand.keys())
            if 1 <= car_name_index <= len(car_names):
                car_name = car_names[car_name_index - 1]
                del car_library[selected_brand]['cars'][car_name]
                print("Car removed successfully.")
                if not car_library[selected_brand]['cars']:
                    del car_library[selected_brand]
                    print(f"No cars left for {selected_brand}. Removed from the car library.")
            else:
                print("Invalid car number.")
        else:
            print(f"No cars available for {selected_brand}.")
    else:
        print("Invalid brand number. Please try again.")

def print_available_brands():
    print("Available Brands:")
    global available_brand_indices
    available_brand_indices = {}
    brand_index = 1
    for brand in car_library.keys():
        print(f"{brand_index}. {brand}")
        available_brand_indices[brand_index] = brand
        brand_index += 1

def print_available_cars_for_brand(brand):
    available_cars_for_brand = car_library[brand]['cars']
    index = 1
    for car_name in available_cars_for_brand.keys():
        print(f"{index}. {car_name}")
        index += 1

def user_menu(username):
    while True:
        try:
            print (f"\nWelcome to Nayre Voyage Wheel's {username}!\n")
            print ("1. Rent a Car")
            print ("2. Return a Car")
            print ("3. Top up Wallet")
            print ("4. Past Transactions")
            print ("5. Display Cars")
            print ("6. Check Balance & Rented Cars")
            print ("7. Logout")
            print ("8. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                rent_car(username)
            if choice == 2:
                return_car(username)
            if choice == 3:
                load_wallet(username)
            if choice == 4:
                view_past_transactions(username)
            if choice == 5:
                available_cars()
                enter  = input("Press enter to continue...")
                if not enter:
                    user_menu(username)
            if choice == 6:
                check_balance_and_rented_cars(username)
                choice = input("Press enter to continue...")

                if not choice:
                    user_menu(username)
            if choice == 7:
                choice = input("Do you wish to logout from your account (y/n)?:\n")
                
                if choice == 'y':
                    print ("Logging out from your account...")
                    main()
            if choice == 8:
                print ("Exiting...")
                quit()

        except ValueError as e:
            print (f"Error Occured; {e}.")
            
def rent_car(username):
    available_cars()
    number = int(input('\nEnter the number of the car you want to rent: '))
    if 1 <= number <= len(available_cars_list):
        selected_car = available_cars_list[number - 1]
        if selected_car['quantity'] > 0:
            delivery_place = input("Enter the delivery place: ")
            cost = selected_car['cost']
            if user_accounts[username]['wallet'] >= cost:
                car_library[selected_car['brand']]['cars'][selected_car['car_name']]['quantity'] -= 1
                
                receipt = {
                    'username': username,
                    'brand': selected_car['brand'],
                    'car_name': selected_car['car_name'],
                    'model': selected_car['model'],
                    'delivery_place': delivery_place,
                    'cost': cost
                }
                user_transactions.setdefault(username, []).append(receipt)
                user_rented_cars.setdefault(username, []).append(selected_car)
                user_accounts[username]['wallet'] -= cost
                print("\n------------Receipt------------")
                print_receipt(receipt)
            else:
                print("Sorry, you do not have enough balance in your wallet to rent this car.")
        else:
            print(f"Sorry {username}, but {selected_car['car_name']} is all occupied. Please select another car.")
    else:
        print("Invalid number, please try again")

def print_receipt(receipt):
    for key, value in receipt.items():
        print(f"{key}: {value}")

def available_cars():
    global available_cars_list
    available_cars_list = []
    print("\nAvailable brands:")
    brand_index = 1
    brand_indices = {}
    for brand in car_library.keys():
        print(f"{brand_index}. {brand}")
        brand_indices[brand_index] = brand
        brand_index += 1

    brand_choice = int(input('\nChoose a brand (Enter the number): '))
    selected_brand = brand_indices.get(brand_choice)
    if selected_brand:
        print(f"\nAvailable cars for {selected_brand}:")
        index = 1
        for car_name, car_info in car_library[selected_brand]['cars'].items():
            print(f"{index}. {car_name} - Model: {car_info['model']} - Cost: {car_info['cost']} - Quantity: {car_info['quantity']}")
            available_cars_list.append({'brand': selected_brand, 'car_name': car_name, 'model': car_info['model'], 'cost': car_info['cost'], 'quantity': car_info['quantity']})
            index += 1
    else:
        print("Invalid brand choice. Please try again.")
        available_cars()

def return_car(username):
    print("\nYour rented cars:")
    if username in user_rented_cars and user_rented_cars[username]:
        index = 1
        for car in user_rented_cars[username]:
            print(f"{index}. {car['brand']} - {car['car_name']} - {car['model']}")
            index += 1
        try:
            return_index = int(input('\nEnter the number of the car you want to return: '))
            if 1 <= return_index <= len(user_rented_cars[username]):
                returned_car = user_rented_cars[username].pop(return_index - 1)
                car_library[returned_car['brand']]['cars'][returned_car['car_name']]['quantity'] += 1
                print(f"\nYou have returned the {returned_car['car_name']}. Thank you!")
            else:
                print("Invalid number, please try again")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("You have not rented any cars.")

def view_past_transactions(username):
    if username in user_transactions:
        
        print(f"\nPast transactions for {username}:")
        for receipt in user_transactions[username]:
            print_receipt(receipt)
            print("--------------------------------\n")
    else:
        print("No past transactions found for this user.")

def load_wallet(username):
       while True:
        try:
            print("Top-up balance for wallet:")
            print("Available for purcahse:")
            print(f"Username: {username}, Current Wallet: {user_accounts[username]['wallet']}$")

            amt = float(input("Enter amount to top up: "))
            user_accounts[username]['wallet'] += amt
            print("Purchase Successful")
            print(f"Username: {username}, New Balance: {user_accounts[username]['wallet']}")
            user_menu(username)
        except ValueError as e:
            user_menu(username)

def check_balance_and_rented_cars(username):
    print(f"Current Wallet Balance: {user_accounts[username]['wallet']}$")
    if username in user_rented_cars:
        if user_rented_cars[username]:
            print("\nRented Cars:")
            for car_info in user_rented_cars[username]:
                print(f"{car_info['car_name']} - Model: {car_info['model']}")
        else:
            print("No cars have been rented.")
    else:
        print("No cars have been rented.")
main()             