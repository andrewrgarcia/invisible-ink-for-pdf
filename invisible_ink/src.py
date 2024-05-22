import os
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

class InvisiblePen:
    def __init__(self, location=(100, 40), font_size=20, visibility=0, color=(255,255,255)):
        """
        Adds invisible watermarks to PDF documents.

        Parameters:
        ---------------
        location (tuple): Coordinates for the watermark text on the page.
        font_size (int): Font size of the watermark text.
        visibility (float): Transparency of the watermark text (0 for invisible). Kind of defeats the purpose of invisible ink but okay.
        color (tuple): RGB color value for the watermark text in (255, 255, 255) format. Kind of defeats the purpose of invisible ink but okay.
        """
        self.location = location
        self.font_size = font_size
        self.visibility = visibility
        self.color = color

    def add_watermark(self, input_pdf, output_pdf, watermark_content):
        watermark_packet = self._create_watermark(watermark_content)
        self._slap_in_all_pages(input_pdf, output_pdf, watermark_packet)

    def process_pdfs_in_path(self, directory, watermark_content):
        pdf_found = False
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                pdf_found = True
                input_pdf = os.path.join(directory, filename)
                output_pdf = os.path.join(directory, f"watermarked_{filename}")
                self.add_watermark(input_pdf, output_pdf, watermark_content)
                print(f"Watermark added to {filename}")
        if not pdf_found:
            print("No PDF files found in the directory.")

    def _create_watermark(self, content):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Helvetica", self.font_size)
        self.color = [color%256/255 for color in self.color]
        print(self.color)
        can.setFillColorRGB(*self.color, alpha=self.visibility)  # Invisible text (alpha=0)
        can.drawString(*self.location, content)
        can.save()

        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        return packet

    def _read_pages(self, document, watermark):
        doc_pages = fitz.open(document)
        watermark_page = fitz.open("pdf", watermark.read())
        return doc_pages, watermark_page

    def _slap_watermark_in_page(self, watermark_page, num, doc_pages):
        page = doc_pages.load_page(num)
        page.show_pdf_page(page.rect, watermark_page, 0)

    def _slap_in_all_pages(self, input_pdf, output_pdf, watermark_packet):
        doc_pages, watermark_page = self._read_pages(input_pdf, watermark_packet)
        assert len(watermark_page) == 1
        for page_num in range(len(doc_pages)):
            self._slap_watermark_in_page(watermark_page, page_num, doc_pages)
        doc_pages.save(output_pdf)



