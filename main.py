from recycling_record import RecyclingRecord
import json

records = []

APP_TITLE = "ScrapSmart - Recycling Yard Assistant"
FILE_NAME = "records.json"

MATERIAL_PRICES = {
    "cardboard": 0.20,
    "plastic": 0.35,
    "aluminium": 1.50,
    "copper": 8.00,
    "steel": 0.50,
    "e-waste": 2.00
}

SAFTEY_NOTES = {
    "cardboard": "Keep cardboard dry before recycling.",
    "plastic": "Clean plastic bottles before collection.",
    "aluminium": "Aluminium cans should be separated from general waste.",
    "copper": "Copper has a high value and should be stored securely.",
    "steel": "Steel may be heavy. Use proper lifting methods.",
    "e-waste": "E-waste should be handled carefully and stored separately."
}

def show_menu():
    print("\n" + "=" * 45)
    print(f"{APP_TITLE:^45}")
    print("=" * 45)
    print("1. Add new recycling record")
    print("2. View all records")
    print("3. Serach records by material type")
    print("4. View summary")
    print("5. Save records")
    print("6. Load records")
    print("7. Exit")
    print("8. Clear all records")

def pause():
    input("\nPress Enter to return to the menu...")

def format_money(amount):
    return f'${amount:.2f}'

def generate_record_id():
    highest_number = 0

    for record in records:
        if record.record_id.startswith("R") and record.record_id[1:].isdigit():
            number = int(record.record_id[1:])

            if number > highest_number:
                highest_number = number

    next_number = highest_number + 1
    return f'R{next_number:03d}'



def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_material():
    print("\nAvaliable materials:")
    
    material_list = list(MATERIAL_PRICES.keys())

    for index, material in enumerate(material_list, start = 1):
        price = MATERIAL_PRICES[material]
        print(f'{index}. {material.title()} - {format_money(price)}/kg')

    while True:
        choice = input("Choose a material number: ")
        
        try:
            choice = int(choice)
            
            if 1 <= choice <= len(material_list):
                return material_list[choice - 1]
            else:
                print("Invalid choice. Please choose a number from the list.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def add_record():
    print("\n--- Add New Recycling Record ---")

    record_id = generate_record_id()
    material = choose_material()
    weight = get_positive_float("Enter weight in kg: ")
    price_per_kg = MATERIAL_PRICES[material]

    new_record = RecyclingRecord(record_id, material, weight, price_per_kg)
    records.append(new_record)

    print("\nRecord added successfully.")
    print(f"Record ID: {new_record.record_id}")
    print(f"Date/Time: {new_record.record_time}")
    print(f"Material: {new_record.material.title()}")
    print(f"Weight: {new_record.weight:.2f} kg")
    print(f'Estimated income: ${new_record.income:.2f}')
    print(f'Safety note: {SAFTEY_NOTES[material]}')

def print_records_table(record_list):
    print("-" * 90)
    print(
        f"{'ID':<7}"
        f"{'Date/Time':<18}"
        f"{'Material':<15}"
        f"{'Weight(kg)':>12}"
        f"{'Price/kg':>12}"
        f"{'Income':>12}"
    )
    print("-" * 90)

    for record in record_list:
        price_text = format_money(record.price_per_kg)
        income_text = format_money(record.income)

        print(
            f"{record.record_id:<7}"
            f"{record.record_time:<18}"
            f"{record.material.title():<15}"
            f"{record.weight:>12.2f}"
            f"{price_text:>12}"
            f"{income_text:>12}"
        )

    print("-" * 90)

def view_records():
    print("\n--- All Recycling Records ---")

    if len(records) == 0:
        print("No records found.")
    else:
        print_records_table(records)

def search_records():
    print("\n--- Search Records ---")
    search_material = input("Enter material type to search: ").lower().strip()

    found_records = []

    for record in records:
        if record.material.lower() == search_material:
            found_records.append(record)
    
    if len(found_records) == 0:
        print("No matching records found.")
    else:
        print(f'\nRecords for {search_material.title()}:')
        print_records_table(found_records)

def view_summary():
    print("\n--- recycling Summary ---")

    if len(records) == 0:
        print("No records avaliable for summary.")
        return

    total_weight = 0
    total_income = 0
    material_weights = {}
    material_income = {}

    for record in records:
        total_weight += record.weight
        total_income += record.income

        if record.material not in material_weights:
            material_weights[record.material] = 0
            material_income[record.material] = 0

        material_weights[record.material] += record.weight
        material_income[record.material] += record.income

    most_collected_material = max(material_weights, key = material_weights.get)
    highest_income_material = max(material_income, key=material_income.get)
    average_income = total_income / len(records)

    print(f'Total records: {len(records)}')
    print(f"Total weight: {total_weight:.2f} kg")
    print(f"Total estimated income: {format_money(total_income)}")
    print(f"Average income per record: {format_money(average_income)}")
    print(f"Most collected material: {most_collected_material.title()}")
    print(f"Highest income material: {highest_income_material.title()}")

    print("\nWeight by material:")
    print("-" * 60)

    max_weight = max(material_weights.values())

    for material, weight in sorted(material_weights.items()):
        bar_length = int((weight / max_weight) * 30)
        bar = "#" * bar_length
        print(f"{material.title():<12} | {bar:<30} {weight:.2f} kg")

    print("-" * 60)


def save_records():
    data = []

    for record in records:
        data.append(record.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent = 4)

    print(f'Records saved successfully to {FILE_NAME}.')

def load_records():
    global records

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        loaded_records = []

        for item in data:
            record = RecyclingRecord.from_dict(item)
            loaded_records.append(record)

        records = loaded_records

        print(f'Records loaded successfully from {FILE_NAME}.')

    except FileNotFoundError:
        print(f"NO saved file found. Please save records first.")

    except json.JSONDecodeError:
        print("The saved file is empty or damaged.")

    except KeyError:
        print("The saved file has missing information.")

    except ValueError:
        print("The saved file contains invalid number data.")

def clear_records():
    global records

    confirm = input("Are you sure you want to clear all records? Type YES to confirm: ")

    if confirm == "YES":
        records = []

        try:
            with open(FILE_NAME, "w") as file:
                json.dump(records, file, indent=4)

            print("All records have been cleared.")

        except OSError:
            print("There was a problem clearing the saved file.")
    else:
        print("Clear operation cancelled.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_record()
            pause()
        elif choice == "2":
            view_records()
            pause()
        elif choice == "3":
            search_records()
            pause()
        elif choice == "4":
            view_summary()
            pause()
        elif choice == "5":
            save_records()
            pause()
        elif choice == "6":
            load_records()
            pause()
        elif choice == "7":
            print("Thank you for using ScrapSmart.")
            break
        elif choice == "8":
            clear_records()
            pause()
        else:
            print("Invalid choice. Please entr a number from 1 to 8.")
            pause()

if __name__ == "__main__":
    main()


    

    
