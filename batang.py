import math

if __name__ == "__main__":
    # Get user input
    days_since = int(input("How many days has it been since your last carton? : "))
    packs_remaining = int(input("How many packs do you have left? : "))
    cigarettes_remaining = int(input("How many cigarrettes are in your open pack? : ")) + (packs_remaining * 20)

    # Find average
    average = math.ceil(batang / days_since)

    # Show result to user
    print("\n\nYour average cigarettes per day is {}.".format(average))
