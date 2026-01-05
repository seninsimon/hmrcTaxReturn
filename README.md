# HMRC Tax Return Generator (Django)

This project is a Django-based application designed to generate HMRC Self Assessment tax return PDFs (SA100, SA102, SA103S, SA105, SA110). It supports filling these forms with data provided via API requests (POST) or by fetching data from an external HMRC data source (GET).

## Features

- **Modular Design:** Each tax form is handled by a dedicated generator module within the `tax_forms` app.
- **Dynamic Data Fetching:** The SA100 and Unified generators can fetch live data from a specified external API.
- **Unified PDF Generation:** A single endpoint to generate and merge all applicable forms for a user into one PDF file.
- **Flexible Input:** Supports both JSON payloads (POST) and automatic data retrieval (GET).
- **PDF Merging:** Uses `pypdf` to combine multiple form pages and documents.

## Project Structure

```
hmrcTaxReturn/
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── tax_project/             # Main project configuration
│   ├── settings.py          # App registration, middleware, etc.
│   └── urls.py              # Main URL routing
├── tax_forms/               # Core application logic
│   ├── views.py             # API Views (Endpoint logic)
│   ├── urls.py              # App-specific URL routing
│   ├── core/                # Shared utilities (PDF merging, overlay)
│   └── form_definitions/    # Definitions for each form type
│       ├── sa100/           # SA100 Generator, Mappings, Templates
│       ├── sa102/           # SA102 Generator, Mappings, Templates
│       ├── sa103s/          # SA103S Generator, Mappings, Templates
│       ├── sa105/           # SA105 Generator, Mappings, Templates
│       └── sa110/           # SA110 Generator, Mappings, Templates
└── media/                   # Output directory for generated PDFs
```

## Prerequisites

- Python 3.8+
- pip

## Installation

1.  **Clone the repository** (if moving to a new machine).
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    _Dependencies include:_ `django`, `reportlab`, `pypdf`, `requests`, `pillow` (automatically handled by reportlab/django deps usually).

## Running the Server

1.  Start the development server:
    ```bash
    python manage.py runserver
    ```
2.  The API will be accessible at `http://localhost:8000/`.

## API Endpoints

### 1. Unified PDF Generation (Recommended)

Generates a complete tax return containing all forms populated with available data.

- **URL:** `/api/generate/unified/`
- **Method:** `GET`
- **Behavior:**
  - Fetches data from the configured external API.
  - Normalizes data keys (e.g., converts `PRO11_1_0` to `PRO11.1_0`).
  - Generates PDFs for all present forms (SA100, SA102, SA103S, SA105, SA110).
  - Merges them into a single file `hmrc_full_return.pdf`.

### 2. Individual Form Generation

Generate specific forms individually.

- **SA100 (Main Return):** `/api/generate/sa100/`
  - **GET:** Fetches dynamic data.
  - **POST:** Accepts JSON body with `tr1`, `tr2`, etc. keys.
- **Other Forms:**
  - `/api/generate/sa102/` (Employment)
  - `/api/generate/sa103s/` (Self-Employment Short)
  - `/api/generate/sa105/` (UK Property)
  - `/api/generate/sa110/` (Tax Calculation)
  - **GET:** Uses default test data located in `test_data.py`.
  - **POST:** Accepts JSON body.

## Configuration

- **External API URL:** Configured in `tax_forms/views.py` inside `fetch_unified_data()` function.
  - Current: `http://192.168.1.56:8000/api/hmrc/MTR/generate_Data_for_tax_return/`
- **Templates:** PDF templates are located in `tax_forms/form_definitions/<form>/templates/`. Ensure these files exist for generation to work correctly.

## Development Notes

- **Adding New Forms:**
  1.  Create a new folder in `tax_forms/form_definitions/`.
  2.  Add `generator.py`, `mappings.py`, and `templates/`.
  3.  Register the new generator in `tax_forms/views.py`.
  4.  Update `generate_unified_pdf_view` to include the new form logic.
