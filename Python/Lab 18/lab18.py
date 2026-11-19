def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("==================================================")
print("            MATHEMATICS LEARNING TOOL             ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("[ERROR] Please enter a non-negative integer.")
        else:
            ans = factorial(n)
            print("[RESULT] Factorial of " + str(n) + " (" + str(n) + "!) = " + str(ans))

    elif choice == "2":
        terms = int(input("Enter number of terms to generate: "))
        if terms <= 0:
            print("[ERROR] Number of terms must be positive.")
        else:
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print("[RESULT] Fibonacci series (" + str(terms) + " terms):", series)

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 3.")