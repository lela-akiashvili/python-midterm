def calculator():
    
    print("შეიყვანეთ ორი რიცხვი")
    while True:
        try:
            raw1 = input("შეიყვანეთ პირველი რიცხვი: ").strip()
            raw2 = input("შეიყვანეთ მეორე რიცხვი: ").strip()

            # ანაცვლებს ,-ს . ით, რადგან სწორად აღიქვას რიცხვი
            
            raw1 = raw1.replace(",", ".")
            raw2 = raw2.replace(",", ".")

            num1 = eval(raw1)
            num2 = eval(raw2)

            operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ").strip()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("ნულზე გაყოფა არ შეიძლება!")
                    continue
                result = num1 / num2
            else:
                print("არასწორი ოპერაცია — გამოიყენეთ მხოლოდ +, -, * ან /.")
                continue

            print(f"შედეგი: {result}")

            again = input("გაგრძელება? (y/n): ").strip().lower()
            if again != "y":
                print("კალკულატორი დასრულდა.")
                break
            

        except ValueError:

            print("რიცხვი არასწორია — დარწმუნდით, რომ შეიყვანეთ სწორი ციფრები")

            break


if __name__ == "__main__":

    calculator()

if __name__ == "__main__":
    calculator()
