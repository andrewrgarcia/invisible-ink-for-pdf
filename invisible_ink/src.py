import os
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_watermark(content):
    packet = io.BytesIO()
    # Create new PDF
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 20)
    can.setFillColorRGB(1, 1, 1, alpha=0.00)  # Invisible text (alpha=0)
    can.drawString(100, 40, content)
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf.pages[0]

def add_watermark(input_pdf, output_pdf, watermark_content):
    watermark = create_watermark(watermark_content)
    existing_pdf = PdfReader(open(input_pdf, "rb"))
    output = PdfWriter()

    for page in existing_pdf.pages:
        page.merge_page(watermark)
        output.add_page(page)

    with open(output_pdf, "wb") as outputStream:
        output.write(outputStream)

def process_pdfs_in_path(directory, watermark_content):
    pdf_found = False
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_found = True
            input_pdf = os.path.join(directory, filename)
            output_pdf = os.path.join(directory, f"watermarked_{filename}")
            add_watermark(input_pdf, output_pdf, watermark_content)
            print(f"Watermark added to {filename}")
    if not pdf_found:
        print("No PDF files found in the directory.")
