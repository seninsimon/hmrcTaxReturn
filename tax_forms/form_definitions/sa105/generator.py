
import os
from tax_forms.core.pdf_utils import merge_multiple_pages
from .mappings import (
    SA105_UKP1,
    SA105_UKP2
)


def generate_sa105(data_dict, output_path="sa105_completed.pdf", templates_dir="forms/sa105/templates"):

    # Configuration for all SA105 pages
    batch_config = [
        (os.path.join(templates_dir, "sa105_UKP1.pdf"),
         SA105_UKP1, data_dict.get('ukp1', {})),
        (os.path.join(templates_dir, "sa105_UKP2.pdf"),
         SA105_UKP2, data_dict.get('ukp2', {})),
    ]

    # Generate the merged PDF
    result_path = merge_multiple_pages(batch_config, output_path)

    return result_path
