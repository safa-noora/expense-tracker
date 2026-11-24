# Expense Tracker

A simple Python application that helps users manage and track their daily expenses.

## Features

- Add new expenses with category, amount and description.
- View all recorded expenses.
- Calculate total expenses.
- View category-wise expense summaries.
- Validate user inputs to prevent invalid entries.
- Automatically save expenses to a JSON file.
- Load previously saved expenses when the application starts.

## Technologies Used

- **Python** – Application logic and functionality.
- **JSON** – Persistent storage of expense records.

## Project Structure

```text
expense-tracker/
│
├── main.py
├── expenses.json
└── README.md
```

## How to Run

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd expense-tracker
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Data Storage

The application uses JSON to store expense records.

Expenses are saved in `expenses.json`, allowing users to retain their data even after closing the application. Previously saved expenses are loaded automatically when the program starts.

## Future Improvements

- Edit and delete expenses.
- Track expenses by date.
- Generate monthly expense summaries.
- Set monthly spending budgets.
- Build a web interface using Flask.