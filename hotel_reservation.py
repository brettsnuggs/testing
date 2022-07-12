# Brett Snuggs, CIS261, Hotel Reservation
import datetime
from datetime import date
import locale


def get_start_date():
    running = True
    while running:
        data_entry = input("Enter arrival date (YYYY-MM-DD): ")
        try:
            year, month, day = map(int, data_entry.split('-'))
            start_date = datetime.date(year, month, day)
        except ValueError:
            print("Invalid date format. Try again.\n")
            continue
        if start_date < today:
            print("Arrival date must be today or later. Try again.")
            continue
        else:
            running = False

    return start_date


def get_end_date():
    running = True
    while running:
        end_date_entry = input("Enter departure date(YYY-MM-DD): ")
        try:
            year, month, day = map(int, end_date_entry.split('-'))
            end_date = datetime.date(year, month, day)
        except ValueError:
            print("Invalid date format. Try again.\n")
            continue
        if end_date <= today:
            print("Departure date must be after arrival date. Try again.")
            continue
        else:
            running = False

    return end_date


def nightly_rate(arrival, depart):

    if arrival.month == 8 or depart.month == 8:
        rate = 105.00
    else:
        rate = 85.00

    return rate


# main function
print("The Hotel Reservation Program\n")

today = date.today()

again = True
while again:
    arrival = get_start_date()
    depart = get_end_date()

    delta = depart - arrival
    nights = delta.days

    room_rate = nightly_rate(arrival, depart)
    price = nights * room_rate

    rate_message = ""
    if arrival.month == 8:
        rate_message = "(High Season)"

    date_format = "%B %d, %Y"

    locale.setlocale(locale.LC_ALL, "en_US")

    print()
    print(f"Arrival Date:   {arrival:{date_format}}")
    print(f"Departure Date: {depart:{date_format}}")
    print(f"Nightly Rate:   {locale.currency(room_rate)} {rate_message}")
    print(f"Total Nights:   {nights}")
    print(f"Total Price:    {locale.currency(price)}")

    new_res = input("\nContinue? (y/n): ")
    print()

    if new_res.lower() == 'y':
        continue
    else:
        print("Bye!")
        again = False
