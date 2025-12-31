# HMRC Tax Return PDF Generator

Django-ready modular backend for generating HMRC tax return PDFs (SA100, SA102, etc.).

## 📁 Project Structure

```
hmrcTaxReturn/
├── core/                           # Shared utilities
│   ├── __init__.py
│   └── pdf_utils.py               # PDF overlay & merge functions
│
├── forms/                          # Form modules
│   ├── __init__.py
│   ├── sa100/                     # SA100 Self Assessment
│   │   ├── __init__.py
│   │   ├── mappings.py           # Field coordinates
│   │   ├── generator.py          # generate_sa100()
│   │   ├── test_data.py          # Sample data
│   │   └── templates/            # PDF templates (sa100_tr1.pdf, etc.)
│   │
│   └── sa102/                     # SA102 Employment Income
│       ├── __init__.py
│       ├── mappings.py           # Field coordinates (TODO)
│       ├── generator.py          # generate_sa102()
│       ├── test_data.py          # Sample data (TODO)
│       └── templates/            # PDF templates (sa102.pdf)
│
├── test_generators.py             # Test script
└── requirements.txt
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Test Generation

```bash
python test_generators.py
```

This will generate:

- `output/sa100_completed.pdf` - Combined SA100 (all 8 pages)
- `output/sa102_completed.pdf` - SA102 form (once configured)

## 📝 Usage

### Generate SA100

```python
from forms.sa100.generator import generate_sa100

data = {
    'tr1': {
        'utr_number': '1234567890',
        'nino': 'AB123456C',
        # ... more fields
    },
    'tr2': { ... },
    'tr3': { ... },
    # ... up to tr8
}

pdf_path = generate_sa100(data, output_path="sa100_completed.pdf")
```

### Generate SA102

```python
from forms.sa102.generator import generate_sa102

data = {
    'p1': {
        'employerName': 'ABC Company Ltd',
        'payeReference': '123/A456',
        'payFromEmployment': '50000.00',
        # ... more fields
    }
}

pdf_path = generate_sa102(data, output_path="sa102_completed.pdf")
```

## 🔧 Setting Up SA102

1. **Add Template**: Place `sa102.pdf` in `forms/sa102/templates/`

2. **Find Coordinates**: Use a PDF coordinate tool to identify field positions

3. **Update `forms/sa102/mappings.py`**:

```python
SA102_P1 = {
    'employerName': {'x': 100, 'y': 700, 'type': 'text'},
    'payeReference': {'x': 100, 'y': 680, 'type': 'text'},
    # ... add more fields
}
```

4. **Update `forms/sa102/test_data.py`**:

```python
DATA_SA102_P1 = {
    'employerName': 'ABC Company Ltd',
    'payeReference': '123/A456',
    # ... add test values
}
```

## 🌐 Django Integration

### Copy to Django Project

```bash
# Copy this entire folder into your Django project
cp -r hmrcTaxReturn /path/to/your/django/project/apps/
```

### Create Django Views

**`views.py`**:

```python
from django.http import FileResponse
from django.views.decorators.http import require_http_methods
import json
from forms.sa100.generator import generate_sa100
from forms.sa102.generator import generate_sa102

@require_http_methods(["POST"])
def generate_sa100_view(request):
    """Generate SA100 PDF endpoint"""
    data = json.loads(request.body)
    pdf_path = generate_sa100(data, output_path=f"media/sa100_{request.user.id}.pdf")
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

@require_http_methods(["POST"])
def generate_sa102_view(request):
    """Generate SA102 PDF endpoint"""
    data = json.loads(request.body)
    pdf_path = generate_sa102(data, output_path=f"media/sa102_{request.user.id}.pdf")
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
```

**`urls.py`**:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/generate/sa100/', views.generate_sa100_view, name='generate_sa100'),
    path('api/generate/sa102/', views.generate_sa102_view, name='generate_sa102'),
]
```

### Frontend Integration

**React/JavaScript Example**:

```javascript
async function downloadSA100(userData) {
  const response = await fetch("/api/generate/sa100/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "sa100_completed.pdf";
  a.click();
}

async function downloadSA102(employmentData) {
  const response = await fetch("/api/generate/sa102/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(employmentData),
  });

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "sa102_completed.pdf";
  a.click();
}
```

## 📦 Adding New Forms (e.g., SA103)

1. Create `forms/sa103/` directory
2. Add `__init__.py`, `mappings.py`, `generator.py`, `test_data.py`
3. Add templates to `forms/sa103/templates/`
4. Create Django view and endpoint

## 🛠️ Field Types

- **`text`**: Single-line text field

```python
{'x': 100, 'y': 200, 'type': 'text'}
```

- **`boxed`**: Individual character boxes

```python
{'x': 100, 'y': 200, 'type': 'boxed', 'box_width': 12, 'spacing': 1}
```

## 📄 License

Add your license here.
