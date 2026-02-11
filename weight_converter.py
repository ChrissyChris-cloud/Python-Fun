def convert_weight():
    print("Weight converter (lb ↔ kg)\n")

    while True:
        unit = input("Lbs or Kg? ").strip().lower()

        if unit in ["lbs", "lb", "pounds", "pound"]:
            from_unit = "lb"
            to_unit = "kg"
            factor = 0.45359237
            break

        elif unit in ["kg", "kgs", "kilograms", "kilogram"]:
            from_unit = "kg"
            to_unit = "lb"
            factor = 2.20462262
            break

        elif unit in ["quit", "q", "exit"]:
            print("Bye!")
            return

        else:
            print("Please type 'lbs' or 'kg' (or 'quit' to exit)")
            continue

    while True:
        weight_str = input(f"Please enter weight in {from_unit}: ").strip()

        try:
            weight = float(weight_str)
            if weight < 0:
                print("Weight can't be negative.")
                continue
            break
        except ValueError:
            print("Please enter a number.")

    # Do the conversion
    result = weight * factor

    print(f"\n{weight:g} {from_unit} = {result:.2f} {to_unit}\n")

    # Ask if they want to do another conversion
    again = input("Another conversion? (y/n): ").strip().lower()
    if again.startswith("y"):
        print("-" * 40)
        convert_weight()
    else:
        print("Done. Good Bye!")


# Start the program
convert_weight()