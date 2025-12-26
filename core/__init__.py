"""
Core module for HMRC Tax Return PDF generation
"""

from .pdf_utils import (
    create_overlay,
    merge_pdfs,
    merge_multiple_pages,
    helper_fill_boxed_text
)

__all__ = [
    'create_overlay',
    'merge_pdfs',
    'merge_multiple_pages',
    'helper_fill_boxed_text'
]
