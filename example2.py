"""
Example 2: Custom Watermark Pen

This script customizes the watermark pen with specific location, font size, visibility, and color.
It then adds the customized invisible watermark to all PDF files in the current directory.
Drag your PDF files to this folder and run the script.
"""

from invisible_ink import InvisiblePen

directory = "."
watermark_content = "(c) 2024 Andrew R. Garcia. All rights reserved." 

pen = InvisiblePen(location=(100, 100), font_size=40, visibility=0.2, color=(255, 255, 255))
pen.process_pdfs_in_path(directory, watermark_content)
