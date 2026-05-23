# ScrapSmart - Recycling Yard Assistant

ScrapSmart is a simple terminal-based Python program for managing basic recycling yard records. I built this project around a small recycling business scenario, where users may need to record different recyclable materials, check the estimated income, and keep a simple summary of daily recycling activity.

The program is not designed to be a large business system. Instead, it focuses on a clear and practical use case: helping users record materials, weights, prices, and income in an organised way.

## Main Features

- Add a new recycling record
- Automatically create a record ID
- Record the date and time for each transaction
- Calculate estimated income based on material weight and price per kg
- Display safety notes for different material types
- View all recycling records in a table format
- Search records by material type
- Generate a recycling summary
- Show a simple text-based bar chart for material weights
- Save and load records using a JSON file

## Materials Included

The current version includes several common recyclable materials:

- Cardboard
- Plastic
- Aluminium
- Copper
- Steel
- E-waste

Each material has a preset price per kilogram. When the user chooses a material and enters the weight, the program calculates the estimated income automatically.

## How to Run the Program

Make sure all project files are in the same folder:

```text
ScrapSmart-Recycling-Yard-Assistant/
├── main.py
├── recycling_record.py
├── records.json
└── README.md
```

Then run the program with:

```bash
python3 main.py
```

If you are using Windows, you may also run:

```bash
python main.py
```

## How the Program Works

The program starts with a menu. Users can choose an option by entering a number.

The main menu includes:

```text
1. Add new recycling record
2. View all records
3. Search records by material type
4. View summary
5. Save records
6. Load records
7. Exit
```

When a new record is added, the program creates a record ID, stores the material information, calculates the income, and records the current date and time.

Records can also be saved into `records.json`, so the data can be loaded again after the program is closed.

## Python Concepts Used

This project uses several Python concepts covered in the course:

- Functions
- Loops
- Lists
- Dictionaries
- Object-oriented programming
- JSON file handling
- Exception handling
- String formatting
- Basic input validation

## Advanced Concepts Used

### Object-Oriented Programming

I used a `RecyclingRecord` class to represent each recycling transaction. Each record stores information such as the record ID, material type, weight, price per kg, income, and record time.

This makes the code easier to organise because each recycling record is treated as one object instead of several separate variables.

### JSON File Handling

The program uses a JSON file to save and load recycling records. Before saving, each `RecyclingRecord` object is converted into a dictionary. When loading the file, the dictionary data is converted back into a `RecyclingRecord` object.

The price and income values are saved as numbers in the JSON file. The dollar sign is only added when the program displays the values to the user.

### Exception Handling

The program uses `try` and `except` to handle invalid user input. For example, if the user enters letters instead of a number for the material weight, the program will show an error message instead of crashing.

It also handles possible file errors, such as trying to load records before a saved file exists.

## Project Purpose

The purpose of this project is to connect Python programming with a realistic small business situation. Recycling yards often need to track materials, weights, prices, and income. This program provides a simple version of that process using Python.

The project is kept lightweight and easy to run, so it does not require any external libraries or special software.
