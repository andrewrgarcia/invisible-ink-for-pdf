# Invisible Ink for PDF

Invisible Ink for PDF is a Python project which adds a witchy layer of security to your PDF documents. Add invisible watermarks to your PDFs that are only seen when selecting the document area.

## Installation

To install the project, follow these steps:

1. **Clone the repository**:
    - `git clone https://github.com/yourusername/invisible_ink_for_pdf.git`
    - `cd invisible_ink_for_pdf`

2. **Create and activate a virtual environment**:
    - `python -m venv venv`
    - `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

3. **Install the required dependencies**:
    - `pip install -r requirements.txt`

4. **You're ready to work in the repository**.

## Usage

### Example 0: Add Invisible Watermark to a Specific File

This script adds an invisible watermark to a specified PDF file. Simply provide the input PDF, output PDF, and the watermark content.

```python
from invisible_ink import InvisiblePen

input_pdf = "./templates/Smiley.pdf"
output_pdf = "./watermarked_Smiley.pdf"
watermark_content = "(c) 2024 Andrew R. Garcia. All rights reserved." 

InvisiblePen().add_watermark(input_pdf, output_pdf, watermark_content)
```

### Example 1: Add Invisible Watermarks to All Files in a Folder

This script adds an invisible watermark to all PDF files in the current directory. Drag your PDF files to this folder and run the script.

```python
from invisible_ink import InvisiblePen

directory = "."
watermark_content = "(c) 2024 Andrew R. Garcia. All rights reserved." 

InvisiblePen().process_pdfs_in_path(directory, watermark_content)
```

### Example 2: Custom Watermark Pen

This script customizes the watermark pen with a specific location, font size, visibility, and color. It then adds the customized invisible watermark to all PDF files in the current directory. Drag your PDF files to this folder and run the script.

```python
from invisible_ink import InvisiblePen

directory = "."
watermark_content = "(c) 2024 Andrew R. Garcia. All rights reserved." 

pen = InvisiblePen(location=(100, 100), font_size=40, visibility=0.2, color=(255, 255, 255))
pen.process_pdfs_in_path(directory, watermark_content)
```

These examples may be run in the command line as `python example0.py` .

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
