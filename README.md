# Newspaper Opinion & Editorial Extractor

## Overview

This project is a streamlined and efficient pipeline designed to automate the process of identifying, extracting, and consolidating Opinion/Editorial sections from a collection of English-language newspapers in PDF format.

It uses a direct and reliable **header analysis technique**, focusing on explicit section titles to ensure high accuracy. The system is built to handle both text-based and image-based (scanned) PDFs, making it a robust solution for diverse document sources.

---

## Features

-   **Targeted Header Analysis**: Focuses on identifying explicit section titles (e.g., "Opinion," "Editorial," "Views") typically found at the top of a page for highly accurate detection.
-   **High Accuracy & Reliability**: By targeting official section headers, the system avoids the ambiguity of analyzing full article text, leading to fewer false positives and more reliable results.
-   **Efficient & Lightweight**: The removal of large machine learning models results in significantly faster processing times and a smaller, simpler installation footprint.
-   **Robust PDF Processing (OCR)**: Natively handles both digitally created and scanned PDFs through an integrated Optical Character Recognition (OCR) engine.
-   **Consolidated Output**: Merges all identified opinion/editorial pages from multiple newspapers into a single, clean PDF file for easy reading and analysis.

---

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2.  **Tesseract OCR Engine**: This is a crucial dependency for processing scanned PDFs.
    -   **Windows**: Download and run the installer from the [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) page. **Important:** Make sure to add the Tesseract installation directory to your system's `PATH` environment variable.
    -   **macOS**: `brew install tesseract`
    -   **Linux (Debian/Ubuntu)**: `sudo apt-get update && sudo apt-get install tesseract-ocr`

3.  **Poppler**: This is a PDF rendering library required for converting PDF pages to images for OCR.
    -   **Windows**: Download the latest binary from [this link](https://github.com/oschwartz10612/poppler-windows/releases/), extract it, and add its `bin` folder to your system's `PATH`.
    -   **macOS**: `brew install poppler`
    -   **Linux (Debian/Ubuntu)**: `sudo apt-get install poppler-utils`

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/newspaper-extractor.git
    cd newspaper-extractor
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Create and Install Dependencies**:
    Create a `requirements.txt` file with the following content:
    ```txt
    # requirements.txt
    PyPDF2
    opencv-python-headless
    pytesseract
    Pillow
    pdf2image
    ```
    Then, install the packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

1.  **Place Your PDFs**: Create a directory named `newspapers` in the root of the project folder. Place all the newspaper PDF files you want to process inside this directory.

    ```
    newspaper-extractor/
    ├── newspapers/
    │   ├── newspaper_A.pdf
    │   ├── newspaper_B.pdf
    │   └── ...
    ├── ... (other project files)
    ```

2.  **Execute the Main Script**:
    Run the orchestrator script from the project's root directory:
    ```bash
    python main_orchestrator.py
    ```

3.  **Check the Output**:
    The script will process all the files, displaying its progress in the terminal. Once completed, a new file named `consolidated_opinion_editorial.pdf` will be generated in the project's root directory.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
