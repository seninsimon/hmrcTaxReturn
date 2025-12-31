
import os
from core.pdf_utils import merge_multiple_pages
from .mappings import (
    SA110_TC1,
    SA110_TC2
)


def generate_sa110(data_dict, output_path="sa110_completed.pdf", templates_dir="forms/sa110/templates"):


    # Configuration for all SA110 pages
    batch_config = [
        (os.path.join(templates_dir, "sa110_TC1.pdf"),
         SA110_TC1, data_dict.get('tc1', {})),
        (os.path.join(templates_dir, "sa110_TC2.pdf"),
         SA110_TC2, data_dict.get('tc2', {})),
        ]

    # Generate the merged PDF
    result_path = merge_multiple_pages(batch_config, output_path)

    return result_path
