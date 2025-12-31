
import os
from core.pdf_utils import merge_multiple_pages
from .mappings import (
    SA103s_SES1,
    SA103s_SES2
)


def generate_sa103s(data_dict, output_path="sa103s_completed.pdf", templates_dir="forms/sa103s/templates"):


    # Configuration for all SA103s pages
    batch_config = [
        (os.path.join(templates_dir, "sa103s_SES1.pdf"),
         SA103s_SES1, data_dict.get('ses1', {})),
        (os.path.join(templates_dir, "sa103s_SES2.pdf"),
         SA103s_SES2, data_dict.get('ses2', {})),
        ]

    # Generate the merged PDF
    result_path = merge_multiple_pages(batch_config, output_path)

    return result_path
