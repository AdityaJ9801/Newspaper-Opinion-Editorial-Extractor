# Newspaper Opinion & Editorial Extractor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project automatically identifies and extracts opinion/editorial pages from a collection of English-language newspapers in PDF format. It uses a combination of Optical Character Recognition (OCR) and a sophisticated Natural Language Processing (NLP) model to understand the content's meaning, consolidating all relevant pages into a single, final PDF.

## ✨ Features

-   **Intelligent Page Identification:** Moves beyond simple keyword matching by using a Hugging Face NLP model to analyze the semantic content and style of the text.
-   **Robust Text Extraction:** Handles both digitally native and scanned (image-based) PDFs by seamlessly falling back to an OCR engine (`Tesseract`).
-   **Automated Consolidation:** Merges all identified opinion/editorial pages from multiple newspaper files into one convenient PDF document.
-   **Environment-Agnostic:** Encapsulated in a Docker environment, ensuring it runs identically on any machine without complex setup.

## ⚙️ How It Works (Architecture Overview)

The system operates as a multi-stage filtration pipeline to ensure both accuracy and efficiency:

1.  **PDF Parsing & Text Extraction:** Each PDF page is processed. The system first attempts a fast, direct text extraction. If that fails or yields minimal text (indicating a scanned page), it automatically converts the page to an image and uses OCR to extract the text.

2.  **Heuristic Filtering:** A quick scan is performed on the extracted text for common opinion/editorial keywords (e.g., "opinion," "letters," "views"). This creates a list of potential candidates, efficiently filtering out obviously irrelevant pages like sports or advertisements.

3.  **ML-Powered Semantic Analysis:** Each candidate page is then analyzed by a pre-trained Natural Language Processing model. This model reads the text and determines if its content and tone align with "opinion and commentary" or "factual news reporting." This is the core step that ensures high accuracy.

4.  **Consolidation:** Pages that are successfully confirmed by the ML model are collected. Once all newspapers have been processed, these pages are merged in order into a single output PDF.

## 🚀 Getting Started

Follow these steps to set up and run the project. The only prerequisite is a working installation of Docker.

### Prerequisites

-   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your system.

### Installation & Execution

**1. Clone the Repository**

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

**2. Prepare Your Input Files**

Place all the newspaper PDF files you want to process inside the `newspapers` directory. The project structure should look like this:

```
.
├── newspapers/
│   ├── newspaper_A.pdf
│   ├── newspaper_B.pdf
│   └── ...
├── Dockerfile
├── main_orchestrator.py
└── ... (other python scripts)
```

**3. Build the Application Environment**

This command uses the `Dockerfile` to build a self-contained environment with all the necessary dependencies and tools. This may take several minutes on the first run as it downloads the required components.

```bash
docker build -t newspaper-processor .
```

**4. Run the Extraction Process**

Execute the following command to start the application. This will process all PDFs in the `newspapers` folder and generate the output file in your project directory.

*   **For macOS and Linux:**
    ```bash
    docker run --rm -v "$(pwd)":/app newspaper-processor
    ```

*   **For Windows (PowerShell):**
    ```bash
    docker run --rm -v "${PWD}:/app" newspaper-processor
    ```
*   **For Windows (Command Prompt):**
    ```bash
    docker run --rm -v "%cd%":/app newspaper-processor
    ```
This command links your current directory to the application's working directory inside the container, allowing it to read your input files and write the output back to your machine.

### Output

After the script finishes, a new file named `consolidated_opinion_editorial.pdf` will appear in the root of your project directory.

## 🛠️ Configuration

The behavior of the ML model can be fine-tuned by modifying the parameters in `ml_classifier.py`:

-   **`model_name`**: You can experiment with other zero-shot classification models from the Hugging Face Hub.
-   **`threshold`**: Adjust the confidence threshold (from `0.0` to `1.0`) to make the classifier more or less strict.

After making changes, remember to rebuild the Docker image using the `docker build` command.

## 💻 Technology Stack

-   **Backend:** Python
-   **PDF Handling:** PyPDF2, Poppler, pdf2image
-   **OCR:** Tesseract OCR Engine
-   **NLP/ML:** Hugging Face Transformers (PyTorch backend)
-   **Containerization:** Docker

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details."# Newspaper-Opinion-Editorial-Extractor" 
