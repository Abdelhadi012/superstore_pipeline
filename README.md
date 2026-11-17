# Superstore Pipeline

A Python project for extracting the Superstore CSV dataset. The implemented
pipeline stage reads `data/raw/Superstore.csv` into a Pandas DataFrame.
Validation, transformation, and database loading are not implemented yet.

## Setup

From the project root, install the pinned dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run extraction

```powershell
python main.py
```

The CSV path is resolved relative to `main.py`, not the current directory.

## Run tests

```powershell
python -m unittest discover -s tests
```

See [superstore_guide.md](superstore_guide.md) for the project tree,
Extract-layer details, and guide-only examples for implementing Validation
and Transform. Keep local secrets in `.env`; it is excluded from Git.