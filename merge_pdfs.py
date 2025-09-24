import os
import logging
from PyPDF2 import PdfWriter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def merge_pdfs(pages_to_merge, output_filename="consolidated_opinion_editorial.pdf"):
    """
    Merges a list of PyPDF2 page objects into a single PDF file.

    Args:
        pages_to_merge (list): A list of PyPDF2 PageObject instances.
        output_filename (str): The name of the output consolidated PDF file.
    """
    if not pages_to_merge:
        logging.warning("No pages provided to merge. Output PDF will not be created.")
        return

    writer = PdfWriter()
    for i, page_obj in enumerate(pages_to_merge):
        try:
            writer.add_page(page_obj)
            logging.debug(f"Added page {i+1} to consolidated PDF.")
        except Exception as e:
            logging.error(f"Error adding page {i+1} to writer: {e}")

    try:
        with open(output_filename, "wb") as output_pdf:
            writer.write(output_pdf)
        logging.info(f"Successfully created consolidated PDF: '{output_filename}' with {len(pages_to_merge)} pages.")
    except Exception as e:
        logging.error(f"Error writing consolidated PDF to '{output_filename}': {e}")

if __name__ == "__main__":
    # This script will be called by the main orchestrator, but for standalone test:
    # Create dummy pages (normally these would come from the PDF processing)
    # from PyPDF2 import PdfReader
    # dummy_reader = PdfReader("path/to/a/sample.pdf")
    # if len(dummy_reader.pages) >= 2:
    #     dummy_pages = [dummy_reader.pages[0], dummy_reader.pages[1]]
    #     merge_pdfs(dummy_pages, "test_merged_dummy.pdf")
    # else:
    #     logging.warning("Not enough pages in sample.pdf for dummy merge test.")
    pass