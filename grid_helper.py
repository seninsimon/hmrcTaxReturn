import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter
import sys
import os

def create_grid_overlay(width, height, step=50):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))
    c.setFont("Helvetica", 8)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)  # Light grey lines

    # Draw vertical lines & X labels
    for x in range(0, int(width), step):
        c.line(x, 0, x, height)
        for y in range(0, int(height), step):
            c.drawString(x + 2, y + 2, f"{x},{y}")

    # Draw horizontal lines
    for y in range(0, int(height), step):
        c.line(0, y, width, y)

    c.save()
    packet.seek(0)
    return packet

def add_grid_to_pdf(input_pdf_path, output_pdf_path):
    if not os.path.exists(input_pdf_path):
        print(f"Error: File '{input_pdf_path}' not found.")
        return

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Get page size from first page (assuming all same)
    page_width = float(reader.pages[0].mediabox.width)
    page_height = float(reader.pages[0].mediabox.height)
    
    print(f"Page size: {page_width} x {page_height}")

    # Create one overlay for all pages
    grid_packet = create_grid_overlay(page_width, page_height)
    grid_pdf = PdfReader(grid_packet)

    for page in reader.pages:
        # Create a fresh copy of the grid for each page (merging modifies the page object in place)
        # Note: In pypdf merging, we merge ONTO the content page.
        # But we want the grid ON TOP.
        # So we merge the grid page ONTO the original page.
        page.merge_page(grid_pdf.pages[0])
        writer.add_page(page)

    with open(output_pdf_path, "wb") as f:
        writer.write(f)
    print(f"Grid created: {output_pdf_path}")

if __name__ == "__main__":
    # Default to 'tax_return_template.pdf' if no argument given, mainly for testing
    filename = "tax_return_template.pdf"
    
    # If user provides a filename directly in code or args, we could use that.
    # Let's prompt or check for the file
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    output = f"grid_{filename}"
    add_grid_to_pdf(filename, output)
