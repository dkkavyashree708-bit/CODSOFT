import random
import string


class PasswordGenerator:

    def generate_password(self, length, complexity):

        if complexity == 1:
            characters = string.ascii_letters

        elif complexity == 2:
            characters = string.ascii_letters + string.digits

        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation

        else:
            return "Invalid complexity choice!"

        password = ''.join(random.choice(characters) for _ in range(length))
        return password


def main():
    generator = PasswordGenerator()

    print("====== PASSWORD GENERATOR ======")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("❌ Length must be greater than 0.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    print("\nSelect Password Complexity:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Characters (Strong)")

    try:
        complexity = int(input("Enter choice (1-3): "))
    except ValueError:
        print("❌ Invalid input.")
        return

    password = generator.generate_password(length, complexity)

    print("\n✅ Generated Password:")
    print(password)


if __name__ == "__main__":
    main()
