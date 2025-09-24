# main_orchestrator.py

import os
import logging

from pdf_processor import process_newspaper
from merge_pdfs import merge_pdfs

# Configure logging for clear output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main orchestration function. It processes PDFs from a local directory,
    identifies opinion/editorial pages based on section headers, and merges them.
    """
    INPUT_DIR = "newspapers"
    OUTPUT_PDF_NAME = "consolidated_opinion_editorial.pdf"

    logging.info(f"Starting newspaper opinion/editorial extraction from local directory: '{INPUT_DIR}'")

    # --- Pre-computation Check ---
    if not os.path.isdir(INPUT_DIR):
        logging.error(f"Error: The directory '{INPUT_DIR}' was not found.")
        logging.error("Please create this directory, place your PDF newspaper files inside it, and run the script again.")
        return

    all_opinion_pages_objects = []

    # --- Process each newspaper PDF ---
    for root, _, files in os.walk(INPUT_DIR):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, filename)
                
                # The process_newspaper function now returns a list of confirmed page objects directly.
                confirmed_pages = process_newspaper(pdf_path)
                
                if confirmed_pages:
                    all_opinion_pages_objects.extend(confirmed_pages)
                else:
                    logging.info(f"No Opinion/Editorial pages found in '{os.path.basename(pdf_path)}'.")

    logging.info("-" * 50)
    logging.info(f"Total Opinion/Editorial pages identified across all files: {len(all_opinion_pages_objects)}")
    logging.info("-" * 50)

    # --- Merge all identified pages into a single PDF ---
    if all_opinion_pages_objects:
        merge_pdfs(all_opinion_pages_objects, OUTPUT_PDF_NAME)
    else:
        logging.warning("No Opinion/Editorial pages were identified across all newspapers. No output PDF will be created.")

    logging.info("Process completed.")


if __name__ == "__main__":
    main()