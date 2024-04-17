# Image and PDF to Excel Converter

This Python application converts tables found in both image and PDF files into Excel format. It utilizes Flask as a web framework for handling file uploads and providing a user interface. The conversion of image files is achieved using the `img2table` library, while PDF files are processed using the `img2table` library in conjunction with Tesseract OCR.

## Features

- Accepts both image (JPEG, PNG, GIF) and PDF files for table extraction.
- Converts tables found in input files into Excel format (.xlsx).
- Provides a user-friendly web interface for file upload and conversion.
- Supports Tesseract OCR for PDF processing.

## Usage

### Prerequisites

- Python 3.x
- Tesseract OCR installed on your system (`tesseract-ocr` package).
- Necessary Python dependencies installed (see `requirements.txt`).
- Docker installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mycal-A/image_pdf2Excel.git
    ```

2. Navigate into the project directory:

    ```bash
    cd image_pdf2Excel
    ```

### Running with Docker

1. Build the Docker image:

    ```bash
    docker build -t image-pdf-to-excel .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 image-pdf-to-excel
    ```
