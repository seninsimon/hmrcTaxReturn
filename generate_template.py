from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def draw_boxes(c, x, y, box_width, box_height, num_boxes, spacing=0):
    """Draws a row of boxes starting at (x, y)."""
    current_x = x
    for _ in range(num_boxes):
        c.rect(current_x, y, box_width, box_height)
        current_x += box_width + spacing

def create_template(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "HMRC Tax Return - Dummy Template")

    c.setFont("Helvetica", 12)

    # Field 1: Name (Standard line)
    c.drawString(100, 700, "Full Name:")
    c.line(200, 700, 500, 700) # Underline

    # Field 2: UTR Number (Boxed)
    c.drawString(100, 650, "UTR Number:")
    # 10 boxes, 20x25, no extra spacing between them usually, but user asked for "different spaces"
    # Let's do standard tight boxes for UTR
    draw_boxes(c, 200, 635, 20, 25, 10, spacing=5)

    # Field 3: Postcode (Boxed with wider spacing)
    c.drawString(100, 600, "Postcode:")
    draw_boxes(c, 200, 585, 25, 25, 8, spacing=10)
    
    # Field 4: Income
    c.drawString(100, 550, "Total Income:")
    c.rect(200, 545, 150, 25) # Single large box

    c.save()
    print(f"Created template: {filename}")

if __name__ == "__main__":
    create_template("tax_return_template.pdf")
