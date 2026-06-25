def get_fare_details(distance, cab_type, travel_time):
    fare_chart = {
        "Mini": 12,
        "Sedan": 18,
        "SUV": 25
    }

    if cab_type not in fare_chart:
        return None

    rate_per_km = fare_chart[cab_type]
    travel_cost = distance * rate_per_km

    booking_fee = 30

    # Night surcharge (10 PM - 5 AM)
    night_charge = 0
    if travel_time >= 22 or travel_time <= 5:
        night_charge = travel_cost * 0.20

    # Discount for long trips
    discount = 0
    if distance > 30:
        discount = travel_cost * 0.10

    total_amount = travel_cost + booking_fee + night_charge - discount

    return {
        "base_fare": travel_cost,
        "booking_fee": booking_fee,
        "night_charge": night_charge,
        "discount": discount,
        "total": total_amount
    }


try:
    distance = float(input("Enter travel distance (km): "))
    cab_type = input("Choose Cab Type (Mini/Sedan/SUV): ").title()
    travel_time = int(input("Enter travel hour (0-23): "))

    if not (0 <= travel_time <= 23):
        print("Invalid hour entered.")
    else:
        bill = get_fare_details(distance, cab_type, travel_time)

        if bill is None:
            print("Selected cab type is unavailable.")
        else:
            print("\n========== CAB BOOKING RECEIPT ==========")
            print(f"Distance Travelled : {distance} km")
            print(f"Cab Type           : {cab_type}")
            print(f"Travel Time        : {travel_time}:00")
            print("-----------------------------------------")
            print(f"Base Fare          : ₹{bill['base_fare']:.2f}")
            print(f"Booking Fee        : ₹{bill['booking_fee']:.2f}")
            print(f"Night Charge       : ₹{bill['night_charge']:.2f}")
            print(f"Discount           : ₹{bill['discount']:.2f}")
            print("-----------------------------------------")
            print(f"Total Amount       : ₹{bill['total']:.2f}")
            print("=========================================")

except ValueError:
    print("Please enter valid numeric values.")