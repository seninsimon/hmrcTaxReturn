import os
import sys
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
    # Optional: Center text within the box width
    # If box_width is just the step, we can print at current_x + margin
    # Let's assume we want to center the char in the box:
    # Char check:

    for char in str(text):
        # specific visual adjustment can be done here.
        # For now, let's print roughly in the middle of current_x and current_x + box_width

        # Calculate center of the box
        center_x = current_x + (box_width / 2)

        # Draw the character centered
        # +5 for vertical padding/centering approx
        c.drawCentredString(center_x, y + 5, char)

        current_x += box_width + spacing


def create_overlay(data, mapping, output_filename):
    """
    Creates a transparent PDF with the data filled in.
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
    """
    # Read the existing PDF
    existing_pdf = PdfReader(open(template_path, "rb"))
    output = PdfWriter()

    # Read the created overlay
    new_pdf = PdfReader(overlay_packet)

    # Merge on the first page (loop if multiple pages needed)
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    with open(output_path, "wb") as outputStream:
        output.write(outputStream)

    print(f"Successfully created: {output_path}")


FIELD_MAPPING = {
    'utr_number': {
        'x': 91,
        'y': 735,
        'type': 'text'
    },
    'nino': {
        'x': 91,
        'y': 722,
        'type': 'text'
    },
    'Employerreference': {
        'x': 148,
        'y': 710,
        'type': 'text'
    },
    'date': {
        'x': 148,
        'y': 688,
        'type': 'text'
    },
    'dateofbirthday': {
        'x': 68,
        'y': 134,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthmonth': {
        'x': 106,
        'y': 134,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthyear': {
        'x': 142,
        'y': 134,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'phonenumber': {
        'x': 323,
        'y': 146,
        'type': 'boxed',
        'box_width': 15 ,
        'spacing': 1
    },
     'dateofbirthday2': {
        'x': 70,
        'y': 47,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthmonth2': {
        'x': 106,
        'y': 47,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthyear2': {
        'x': 142,
        'y': 47,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'NationalInsuranceNumber1': {
        'x': 326,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'NationalInsuranceNumber2': {
        'x': 364,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'NationalInsuranceNumber3': {
        'x': 398,
        'y': 85,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'NationalInsuranceNumber4': {
        'x': 442,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'NationalInsuranceNumber5': {
        'x': 480,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
}

# 2. Define the data to populate
DUMMY_DATA = {
    'utr_number': "1234567890",
    'nino': "AB123CD",
    'Employerreference': "1234567890",
    'date': "12122022",
    'dateofbirthday': "12",
    'dateofbirthmonth': "12",
    'dateofbirthyear': "2022",
    'phonenumber': "1234567890000",
    'dateofbirthday2': "12",
    'dateofbirthmonth2': "12",
    'dateofbirthyear2': "2022",
    'NationalInsuranceNumber1': "00",
    'NationalInsuranceNumber2': "00",
    'NationalInsuranceNumber3': "00",
    'NationalInsuranceNumber4': "00",
    'NationalInsuranceNumber5': "0"
}


# ==========================================
# FILE CONFIGURATION
# ==========================================
# REPLACE THESE WITH YOUR FILENAMES
TEMPLATE_FILE = "tax_return_template.pdf"  # Default
OUTPUT_FILE = "filled_tax_return.pdf"      # Default

if __name__ == "__main__":
    # Support command line args: python fill_pdf.py [input_pdf] [output_pdf]
    template_path = TEMPLATE_FILE
    output_path = OUTPUT_FILE

    if len(sys.argv) > 1:
        template_path = sys.argv[1]
        # Construct output name based on input if not provided
        base_name = os.path.splitext(template_path)[0]
        output_path = f"filled_{base_name}.pdf"

    if len(sys.argv) > 2:
        output_path = sys.argv[2]

    print(f"Using template: {template_path}")
    print(f"Output file: {output_path}")

    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' not found.")
    else:
        overlay_pdf = create_overlay(DUMMY_DATA, FIELD_MAPPING, "overlay.pdf")
        merge_pdfs(template_path, overlay_pdf, output_path)
