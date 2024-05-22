"""
Example 1: Add Invisible Watermarks to All Files in This Folder

This script adds an invisible watermark to all PDF files in the current directory.
Drag your PDF files to this folder and run the script.
"""

from invisible_ink import InvisiblePen

directory = "."
watermark_content = "(c) 2024 Andrew R. Garcia. All rights reserved." 

InvisiblePen().process_pdfs_in_path(directory, watermark_content)
