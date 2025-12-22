# HMRC PDF Data Populator

This tool allows you to programmatically fill text into HMRC PDF forms (like SA100). It uses a coordinate-based system to overlay text and supports "boxed" characters (where each letter goes into a separate box).

## 1. Setup

**Prerequisites:** Python installed.

1.  Open your terminal/command prompt in this folder.
2.  Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## 2. Quick Start

To generate the filled PDF with the current configuration:

```bash
python fill_pdf.py
```

This will read the templates listed in `fill_pdf.py`, populate them with dummy data, and create **`final_completed_return.pdf`**.

## 3. How to Add a New PDF Page

If you want to add a new form page (e.g., `tr2.pdf`), follow this workflow:

### Step A: Get Coordinates

1.  Place your new PDF file (e.g. `tr2.pdf`) in this folder.
2.  Run the helper tool to generate a grid over it:
    ```bash
    python grid_helper.py tr2.pdf
    ```
3.  Open the newly created `grid_tr2.pdf`. You will see X,Y numbers printed all over the page.
4.  Note down the coordinates for the fields you want to fill.

### Step B: Configure Mapping

1.  Open **`form_mappings.py`**.
2.  Create a new dictionary for your form (e.g., `SA100_TR2`).
3.  Add your fields using the coordinates you found:
    ```python
    SA100_TR2 = {
        'my_field_name': {'x': 100, 'y': 200, 'type': 'text'},
        'my_boxed_field': {'x': 100, 'y': 300, 'type': 'boxed', 'box_width': 12, 'spacing': 1},
    }
    ```

### Step C: Add Data

1.  Open **`test_data.py`**.
2.  Add a data dictionary with values for your fields:
    ```python
    DATA_SA100_TR2 = {
        'my_field_name': "Hello World",
        'my_boxed_field': "123456",
    }
    ```

### Step D: Register in Batch Process

1.  Open **`fill_pdf.py`**.
2.  Find the `BATCH_CONFIG` list.
3.  Add your new file to the list:
    ```python
    BATCH_CONFIG = [
        ("sa100_removed.pdf", SA100_TR1, DATA_SA100_TR1),
        ("tr2.pdf",           SA100_TR2, DATA_SA100_TR2), # <--- Added here
    ]
    ```
4.  Run `python fill_pdf.py`. It will now fill both pages and combine them into one file.

## Files Guide

| File               | Purpose                                                                    |
| :----------------- | :------------------------------------------------------------------------- |
| `fill_pdf.py`      | The main script. Run this to generate your PDF.                            |
| `form_mappings.py` | Stores the X,Y coordinates for all your forms. Edit this to add new forms. |
| `test_data.py`     | Stores the dummy data to be printed. Edit this to change values.           |
| `grid_helper.py`   | Utility tool to help you find X,Y coordinates on a PDF.                    |
