def calculate_future_value(principal, interest_rate, time_period):
    future_value = principal * (1 + interest_rate) ** time_period
    return future_value

while True:
    try:
        # Get user inputs
        principal = float(input("Enter the principal amount: "))
        interest_rate = float(input("Enter the interest rate (in decimal form): "))
        time_period = int(input("Enter the time period (in years): "))

        # Calculate and display the future value
        result = calculate_future_value(principal, interest_rate, time_period)
        print("The future value of your investment is:", result)

        # Ask if the user wants to perform another calculation
        another_calculation = input("Perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
            break  # Exit the loop if the user doesn't want to continue

    except ValueError:
        print("Invalid input! Please enter numeric values.")
