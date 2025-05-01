# 🧾 Sales Summary Project

A simple Python project to generate a basic sales summary (total quantity & revenue) from a small SQLite database and display the results using a professional, exportable bar chart.

---

## 📌 Features

- Uses **SQLite** to store sample sales data.
- Extracts **total quantity sold** and **total revenue** per product using SQL.
- Displays results using **pandas** and **Plotly**.
- Saves an interactive-style **PNG chart** for reporting or presentation.
- Lightweight and beginner-friendly project structure.

---

## 📁 Project Structure

```bash
sales_summary_project/
├── create_db.py           # Script to create and populate the SQLite database
├── requirements.txt       # Python dependencies list
├── sales_chart.png        # Exported chart image (auto-generated)
├── sales_data.db          # SQLite database file with one table
├── sales_summary.py       # Main script to query, summarize, and plot sales
└── README.md              # Project documentation (you are here)
```

---

## ⚙️ Setup Instructions

### 1. Clone or create the folder

```bash
mkdir sales_summary_project
cd sales_summary_project
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Instructions

### Step 1: Create the SQLite database

Run the script to generate the `sales_data.db`:

```bash
python create_db.py
```

### Step 2: Generate the sales summary and save chart

Run the main script to generate the summary and export the chart as a PNG:

```bash
python sales_summary.py
```

After running, you'll see:
- Printed sales summary in the terminal.
- A chart saved as `sales_chart.png`.

---

## 📊 Output Example

- Terminal output:

```
Sales Summary:

   product  total_qty  revenue
0   Apples         15     22.5
1  Bananas         30     15.0
2  Oranges         25     25.0
```

- Chart saved to:
  ```
sales_chart.png
```

---

## 🧩 Dependencies

- Python 3.7+
- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)
- [kaleido](https://github.com/plotly/Kaleido) (for PNG export)

---



