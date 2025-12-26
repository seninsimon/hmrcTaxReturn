"""
SA102 Form Generator
Generates filled SA102 Self Assessment Tax Return PDFs
"""

import os
from core.pdf_utils import merge_multiple_pages
from .mappings import (
    SA102_TR1
)


def generate_sa102(data_dict, output_path="sa102_completed.pdf", templates_dir="forms/sa102/templates"):

    # Configuration for all SA102 pages
    batch_config = [
        (os.path.join(templates_dir, "sa102_tr1.pdf"),
         SA102_TR1, data_dict.get('tr1', {})),
        # (os.path.join(templates_dir, "sa102_tr2.pdf"),
        #  SA102_TR2, data_dict.get('tr2', {})),
    ]

    # Generate the merged PDF
    result_path = merge_multiple_pages(batch_config, output_path)

    return result_path
