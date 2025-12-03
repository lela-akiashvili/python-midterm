import os

BALANCE_FILE = "balance.txt" #ბალანსის ფაილი
PINCODE_FILE = "pincode.txt"          # პინ კოდის ფაილი


# პინის ჩატვირთვა ან შექმნა

def load_pin():
    if not os.path.exists(PINCODE_FILE):
        with open(PINCODE_FILE, "w") as file:
            file.write("10244")  # Default PIN 1234
        return "1024"
    
    with open(PINCODE_FILE, "r") as file:
        return file.read().strip()

# პინის შემოწმება

def check_pin():
    correct_pin = load_pin()
    attempts = 3

    while attempts > 0:
        pin = input("შეიყვანეთ თქვენი PIN კოდი: ")
        
        if pin == correct_pin:
            print(" PIN სწორია.\n")

            return True
        else:
            attempts -= 1
            print(f" არასწორი PIN! დარჩენილი მცდელობები: {attempts}")

    print("3 მცდარ მცდელობაში ბანკომატი დაიბლოკება.")

    return False

def load_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as file:
            file.write("0")
        return 0
    with open(BALANCE_FILE, "r") as file:
        return float(file.read())

def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))

def check_balance(balance):
    print(f"თქვენი ბალანსია: {balance} ლარი")

def deposit(balance):
    amount = float(input("შეიყვანეთ შესატანი თანხა: "))
    if amount <= 0:
        print(" თანხა უნდა იყოს 0-ზე მეტი!")
        return balance
    balance += amount
    print(f" ოპერატია შესრულდა წარმატებით. ანგარიშზე დამატებულია {amount} ლარი")
    return balance

def withdraw(balance):
    amount = float(input("შეიყვანეთ გასატანი თანხა: "))
    if amount <= 0:
        print(" თანხა უნდა იყოს 0-ზე მეტი!")
        return balance
    if amount > balance:
        print(" ბალანსზე არ არის საკმარისი თანხა!")
        return balance
    balance -= amount
    print(f" ოპერატია შესრულდა წარმატებით წარმატებით. ანგარიშიდან გატანილია {amount} ლარი")
    return balance

def atm():
    if not check_pin(): 
        return
    
    balance = load_balance()

    while True:
        print("\n--- ბანკომატი ---")
        print("1. ბალანსის ნახვა")
        print("2. თანხის შეტანა")
        print("3. თანხის გატანა")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპერაცია (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)
            save_balance(balance)

        elif choice == "3":
            balance = withdraw(balance)
            save_balance(balance)

        elif choice == "4":
            print("გმადლობთ ბანკომატის გამოყენებისთვის!")
            break

        else:
            print(" არასწორი ტრანზაქცია! სცადეთ თავიდან.")

atm()    


