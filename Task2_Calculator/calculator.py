class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b


def main():
    calc = Calculator()

    while True:
        print("\n====== SIMPLE CALCULATOR ======")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("👋 Exiting Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numeric values.")
                continue

            if choice == "1":
                result = calc.add(num1, num2)

            elif choice == "2":
                result = calc.subtract(num1, num2)

            elif choice == "3":
                result = calc.multiply(num1, num2)

            elif choice == "4":
                result = calc.divide(num1, num2)

            print(f"✅ Result: {result}")

        else:
            print("❌ Invalid choice! Please select between 1-5.")


if __name__ == "__main__":
    main()
