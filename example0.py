"""
0th Example: Add Invisible Watermark to a Specific File

This script adds an invisible watermark to a specified PDF file.
Simply provide the input PDF, output PDF, and the watermark content.
"""

from invisible_ink import InvisiblePen

input_pdf = "./templates/Smiley.pdf"
output_pdf = "./watermarked_Smiley.pdf"
watermark_content = "(c) 2024 Andrew R. Garcia. All rights reserved." 

InvisiblePen().add_watermark(input_pdf, output_pdf, watermark_content)
