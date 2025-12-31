"""
Core PDF Utilities for HMRC Tax Return Forms
Shared functions for creating and merging PDF overlays
"""

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter


def helper_fill_boxed_text(c, text, x, y, box_width, spacing=0):
    """
    Helper function to fill text into boxes.

    Arguments:
        c: The canvas object
        text: The string to print
        x: Starting X coordinate
        y: Starting Y coordinate (bottom-left of text)
        box_width: Width of each box (to center text) or step size
        spacing: Gap between boxes (optional)
    """
    current_x = x

    for char in str(text):
        # Calculate center of the box
        center_x = current_x + (box_width / 2)

        # Draw the character centered
        # +5 for vertical padding/centering approx
        c.drawCentredString(center_x, y + 5, char)

        current_x += box_width + spacing


def create_overlay(data, mapping):
    """
    Creates a transparent PDF overlay with the data filled in.

    Arguments:
        data: Dictionary of field names and values
        mapping: Dictionary of field configurations (x, y, type, etc.)

    Returns:
        BytesIO packet containing the overlay PDF
    """
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.setFont("Helvetica", 12)

    for field_key, value in data.items():
        if field_key not in mapping:
            continue

        config = mapping[field_key]
        x = config['x']
        y = config['y']
        field_type = config.get('type', 'text')

        if field_type == 'text':
            c.drawString(x, y, str(value))

        elif field_type == 'boxed':
            box_width = config.get('box_width', 20)
            spacing = config.get('spacing', 0)
            helper_fill_boxed_text(c, value, x, y, box_width, spacing)

    c.save()
    packet.seek(0)
    return packet


def merge_pdfs(template_path, overlay_packet, output_path):
    """
    Merges the overlay packet onto the template PDF.

    Arguments:
        template_path: Path to the template PDF file
        overlay_packet: BytesIO packet containing the overlay
        output_path: Path where the merged PDF will be saved
    """
    # Read the existing PDF
    existing_pdf = PdfReader(open(template_path, "rb"))
    output = PdfWriter()

    # Read the created overlay
    new_pdf = PdfReader(overlay_packet)

    # Merge on the first page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    with open(output_path, "wb") as outputStream:
        output.write(outputStream)


def merge_multiple_pages(pages_config, output_path):
    """
    Merge multiple filled PDF pages into a single document.

    Arguments:
        pages_config: List of tuples (template_path, mapping, data)
        output_path: Path for the final merged PDF

    Returns:
        Path to the generated PDF
    """
    final_writer = PdfWriter()
    temp_files = []

    for index, (template, mapping, data) in enumerate(pages_config):
        import os
        if not os.path.exists(template):
            print(f"Skipping {template} (not found)")
            continue

        temp_output = f"temp_page_{index+1}.pdf"

        # Create overlay
        overlay = create_overlay(data, mapping)

        # Merge overlay with template
        merge_pdfs(template, overlay, temp_output)

        # Add the page(s) to final writer
        reader = PdfReader(temp_output)
        for page in reader.pages:
            final_writer.add_page(page)

        temp_files.append(temp_output)

    # Write final output
    with open(output_path, "wb") as f_out:
        final_writer.write(f_out)

    # Cleanup temp files
    import os
    for f in temp_files:
        if os.path.exists(f):
            os.remove(f)

    return output_path
