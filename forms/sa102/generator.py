"""
SA102 Form Generator
Generates filled SA102 Employment Income PDFs
"""

import os
from core.pdf_utils import create_overlay, merge_pdfs
from .mappings import SA102_P1, SA102_P2


def generate_sa102(data_dict, output_path="sa102_completed.pdf", templates_dir="forms/sa102/templates"):
    """
    Generate a filled SA102 PDF from user data.

    Arguments:
        data_dict: Dictionary containing data for SA102 pages
                   Keys: 'p1', 'p2' (if multiple pages)
        output_path: Path where the final PDF will be saved
        templates_dir: Directory containing the SA102 template PDFs

    Returns:
        Path to the generated PDF file

    Example:
        data = {
            'p1': {
                'employerName': 'ABC Company Ltd',
                'payeReference': '123/A456',
                'payFromEmployment': '50000.00',
                # ... more fields
            }
        }
        pdf_path = generate_sa102(data)
    """

    # Get the data for page 1
    page_data = data_dict.get('p1', {})

    # Template path
    template_path = os.path.join(templates_dir, "sa102.pdf")

    # Check if template exists
    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"SA102 template not found at: {template_path}")

    # Create overlay with the data
    overlay = create_overlay(page_data, SA102_P1)

    # Merge overlay with template
    merge_pdfs(template_path, overlay, output_path)

    return output_path
