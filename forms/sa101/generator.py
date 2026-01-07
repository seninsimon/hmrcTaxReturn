"""
SA101 Form Generator
Generates filled SA101 Additional Information PDFs
"""

import os
from core.pdf_utils import merge_multiple_pages
from .mappings import (
    SA101_Ai1, SA101_Ai2, SA101_Ai3, SA101_Ai4
)


def generate_sa101(data_dict, output_path="sa101_completed.pdf", templates_dir="forms/sa101/templates"):
    """
    Generate a filled SA101 PDF from user data.

    Arguments:
        data_dict: Dictionary containing data for all SA101 pages
                   Keys: 'Ai1', 'Ai2', 'Ai3', 'Ai4'
        output_path: Path where the final PDF will be saved
        templates_dir: Directory containing the SA101 template PDFs

    Returns:
        Path to the generated PDF file
    """

    # Configuration for all SA101 pages
    # Note: Templates should be named sa101_Ai1.pdf, sa101_Ai2.pdf, etc.
    batch_config = [
        (os.path.join(templates_dir, "sa101_Ai1.pdf"),
         SA101_Ai1, data_dict.get('Ai1', {})),
        (os.path.join(templates_dir, "sa101_Ai2.pdf"),
         SA101_Ai2, data_dict.get('Ai2', {})),
        (os.path.join(templates_dir, "sa101_Ai3.pdf"),
         SA101_Ai3, data_dict.get('Ai3', {})),
        (os.path.join(templates_dir, "sa101_Ai4.pdf"),
         SA101_Ai4, data_dict.get('Ai4', {})),
    ]

    # Generate the merged PDF
    result_path = merge_multiple_pages(batch_config, output_path)

    return result_path
