from test_data import DATA_SA100_TR1, DATA_SA100_TR2, DATA_SA100_TR3, DATA_SA100_TR4, DATA_SA100_TR5, DATA_SA100_TR6, DATA_SA100_TR7, DATA_SA100_TR8
from form_mappings import SA100_TR1, SA100_TR2, SA100_TR3, SA100_TR4, SA100_TR5, SA100_TR6, SA100_TR7, SA100_TR8
import os
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


BATCH_CONFIG = [
    ("sa100_tr1.pdf", SA100_TR1, DATA_SA100_TR1),
    ("sa100_tr2.pdf", SA100_TR2, DATA_SA100_TR2),
    ("sa100_tr3.pdf", SA100_TR3, DATA_SA100_TR3),
    ("sa100_tr4.pdf", SA100_TR4, DATA_SA100_TR4),
    ("sa100_tr5.pdf", SA100_TR5, DATA_SA100_TR5),
    ("sa100_tr6.pdf", SA100_TR6, DATA_SA100_TR6),
    ("sa100_tr7.pdf", SA100_TR7, DATA_SA100_TR7),
    ("sa100_tr8.pdf", SA100_TR8, DATA_SA100_TR8),
]

OUTPUT_FILENAME = "final_completed_return.pdf"

if __name__ == "__main__":
    # PdfMerger is deprecated/removed in some versions, use PdfWriter
    from pypdf import PdfWriter

    print(f"Starting batch process...")
    # This writer will hold the final combined document
    final_writer = PdfWriter()
    temp_files = []

    for index, (template, mapping, data) in enumerate(BATCH_CONFIG):
        if not os.path.exists(template):
            print(f"Skipping {template} (not found)")
            continue

        temp_output = f"temp_page_{index+1}.pdf"

        # Create overlay
        overlay = create_overlay(data, mapping, "overlay.pdf")

        # Merge overlay with template to create a single page/doc
        # We reuse the existing logic but save to temp file
        merge_pdfs(template, overlay, temp_output)

        # Add the page(s) from this temp file to our final writer
        reader = PdfReader(temp_output)
        for page in reader.pages:
            final_writer.add_page(page)

        temp_files.append(temp_output)

    # Write final output
    with open(OUTPUT_FILENAME, "wb") as f_out:
        final_writer.write(f_out)

    # Cleanup temp files
    for f in temp_files:
        os.remove(f)

    print(f"\nTotal Success! Verification: {OUTPUT_FILENAME}")
