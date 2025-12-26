"""
SA100 Form Generator
Generates filled SA100 Self Assessment Tax Return PDFs
"""

import os
from core.pdf_utils import merge_multiple_pages
from .mappings import (
    SA100_TR1, SA100_TR2, SA100_TR3, SA100_TR4,
    SA100_TR5, SA100_TR6, SA100_TR7, SA100_TR8
)


def generate_sa100(data_dict, output_path="sa100_completed.pdf", templates_dir="forms/sa100/templates"):
    """
    Generate a filled SA100 PDF from user data.

    Arguments:
        data_dict: Dictionary containing data for all SA100 pages
                   Keys: 'tr1', 'tr2', 'tr3', 'tr4', 'tr5', 'tr6', 'tr7', 'tr8'
        output_path: Path where the final PDF will be saved
        templates_dir: Directory containing the SA100 template PDFs

    Returns:
        Path to the generated PDF file

    Example:
        data = {
            'tr1': {'utr_number': '1234567890', 'nino': 'AB123CD', ...},
            'tr2': {'employmentYes': 'X', ...},
            'tr3': {...},
            # ... etc
        }
        pdf_path = generate_sa100(data)
    """

    # Configuration for all SA100 pages
    batch_config = [
        (os.path.join(templates_dir, "sa100_tr1.pdf"),
         SA100_TR1, data_dict.get('tr1', {})),
        (os.path.join(templates_dir, "sa100_tr2.pdf"),
         SA100_TR2, data_dict.get('tr2', {})),
        (os.path.join(templates_dir, "sa100_tr3.pdf"),
         SA100_TR3, data_dict.get('tr3', {})),
        (os.path.join(templates_dir, "sa100_tr4.pdf"),
         SA100_TR4, data_dict.get('tr4', {})),
        (os.path.join(templates_dir, "sa100_tr5.pdf"),
         SA100_TR5, data_dict.get('tr5', {})),
        (os.path.join(templates_dir, "sa100_tr6.pdf"),
         SA100_TR6, data_dict.get('tr6', {})),
        (os.path.join(templates_dir, "sa100_tr7.pdf"),
         SA100_TR7, data_dict.get('tr7', {})),
        (os.path.join(templates_dir, "sa100_tr8.pdf"),
         SA100_TR8, data_dict.get('tr8', {})),
    ]

    # Generate the merged PDF
    result_path = merge_multiple_pages(batch_config, output_path)

    return result_path
