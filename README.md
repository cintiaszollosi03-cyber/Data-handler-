# Data Generator + Exporter (CSV / JSON / XLSX / PDF / Oracle)

Small Python project that generates **synthetic data** for a simple **people–workplace–address** domain and exports it into multiple formats.

## Supported export formats

* CSV
* JSON
* Excel (XLSX)

---

## What the project generates

* **People**
  `(id, name, age, male, workplace, address)`

* **Workplaces**
  `(id, name, location, employees)`

* **Addresses**
  `(id, street, city, country, resident)`

Relationships between entities are stored using IDs or string references.

---

## Project structure

```
project_root/
│
├── data/
│   ├── handler/
│   │   ├── __init__.py
│   │   ├── csv_dict.py      # CSV export (Dict-based)
│   │   ├── json_handler.py  # JSON export
│   │   └── xlsx.py          # Excel (XLSX) export
│   
│
├── generator.py             # Synthetic data generation
├── model_dataclasses.py     # Domain models (dataclasses, used by the app)
├── model_classes.py         # Alternative OOP model implementation
└── __init__.py
```

---

## Models: `model_dataclasses.py` vs `model_classes.py`

This repository contains **two model implementations**:

* **`model_dataclasses.py`**
  Used by the application. Simple `@dataclass`-based models designed for data generation and export.

* **`model_classes.py`**
  Alternative OOP-style implementation demonstrating:

  * custom `__str__`
  * hashing
  * ordering (`@total_ordering`)

Both represent the **same domain**, but serve different **learning and demonstration purposes**.

---

## Requirements

* Python **3.12+**
* Packages listed in `requirements.txt`

---

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
```

### Activate virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (cmd):**

```cmd
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

Upgrade pip and install requirements:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

All generated files are written into the **`output/`** folder.

---

## Notes

* The project focuses on file-based exports (CSV, JSON, XLSX)
* No database or PDF generation is required
* Designed for educational and demonstration purposes

---
