#tip_calc

def calculate_tip(bill_amount, tip_percentage):
    # Calculate the tip based on the bill amount and tip percentage
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    return tip, total
def main():
    # Get user input for bill amount and tip percentage
    #“Try to run this code. If something goes wrong, don’t crash — handle it instead.”
    #Instead of crashing, it jumps to the except block and prints a helpful message
    try:
        bill_amount = float(input("Enter the bill amount: $"))
        tip_percentage = float(input("Enter the amount of tip you want to give (in %): "))
        tip, total = calculate_tip(bill_amount, tip_percentage)
    
        print(f"\nTip: ${tip:.2f}")
        print(f"Total with tip: ${total:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for bill amount and tip percentage.")

if __name__ == "__main__":
    main()