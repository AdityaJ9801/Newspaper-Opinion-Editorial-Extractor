# _2_pdf_processor.py

import os
import logging
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Configure Tesseract path if it's not in your system's PATH (especially for Windows)
# Example:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_pdf_page(page, page_num, pdf_path):
    """
    Extracts text from a single PDF page. Tries direct extraction first,
    then falls back to robust OCR if text is sparse or missing.
    """
    text = ""
    try:
        # First attempt: Direct text extraction from PyPDF2
        extracted_text = page.extract_text()
        if extracted_text and len(extracted_text.strip()) > 50:
            text = extracted_text
            logging.debug(f"Successfully extracted text directly from {os.path.basename(pdf_path)}, page {page_num+1}.")
    except Exception as e:
        logging.warning(f"Could not directly extract text from {os.path.basename(pdf_path)}, page {page_num+1}. Error: {e}")

    # If direct extraction fails or yields very little text, use OCR.
    if not text:
        logging.info(f"Direct text extraction failed or text is sparse. Falling back to OCR for {os.path.basename(pdf_path)}, page {page_num+1}.")
        try:
            page_image = convert_from_path(
                pdf_path,
                dpi=200,
                first_page=page_num + 1,
                last_page=page_num + 1
            )[0]
            ocr_text = pytesseract.image_to_string(page_image, lang='eng')
            if ocr_text and len(ocr_text.strip()) > 20:
                text = ocr_text
                logging.info(f"Successfully extracted text via OCR from {os.path.basename(pdf_path)}, page {page_num+1}.")
            else:
                 logging.warning(f"OCR produced no text for {os.path.basename(pdf_path)}, page {page_num+1}.")
        except Exception as e:
            logging.error(f"OCR process failed for {os.path.basename(pdf_path)}, page {page_num+1}. Check if poppler is installed and in PATH. Error: {e}")
            text = ""

    return text

def is_opinion_page(text):
    """
    Identifies if a page is an Opinion/Editorial section by primarily checking the header.
    This is a more direct and reliable method than general keyword searching.
    """
    if not text:
        return False
        
    # Isolate the header region (e.g., the first 500 characters of the page)
    # Page headers containing section titles are almost always at the very top.
    header_text = text[:500].lower()
    
    # Define keywords that strongly indicate an Opinion/Editorial section header.
    # These are less ambiguous than searching the entire article content.
    section_keywords = [
        "opinion", 
        "editorial", 
    ]

    # Check if any of the specific section keywords are present in the header text.
    if any(keyword in header_text for keyword in section_keywords):
        return True

    return False

def process_newspaper(pdf_path):
    """
    Processes a single newspaper PDF, extracts pages identified as Opinion/Editorial,
    and returns their page objects.
    """
    opinion_pages = []
    try:
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        logging.info(f"Processing '{os.path.basename(pdf_path)}' with {num_pages} pages.")

        for i, page in enumerate(reader.pages):
            page_text = extract_text_from_pdf_page(page, i, pdf_path)

            # Use the new, more direct identification function
            if is_opinion_page(page_text):
                logging.info(f"SUCCESS: Identified '{os.path.basename(pdf_path)}', page {i+1} as Opinion/Editorial.")
                opinion_pages.append(page)

    except Exception as e:
        logging.error(f"Error processing PDF '{pdf_path}': {e}")
    return opinion_pages