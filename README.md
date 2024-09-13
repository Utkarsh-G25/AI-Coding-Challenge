# Document Question Answering System

This project is a Flask-based web application that processes a PDF document and a JSON file containing questions, extracts text from the PDF, and uses OpenAI's GPT-4 model to answer the questions based on the document's content.

## Features

- Upload a PDF document and a JSON file with questions.
- Extract text from the PDF document.
- Use OpenAI's GPT-4o-mini model to answer questions based on the document's content.

## Requirements

- Python 3.7+
- Flask
- OpenAI Python library
- PyPDF2 (for PDF text extraction)
- dotenv (for environment variable management)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository url>
    cd document-question-answering
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Use `curl` or a tool like Postman to send a POST request to the `/answer-questions` endpoint with the PDF document and JSON file containing questions:
    ```sh
    curl -X POST http://127.0.0.1:5000/answer-questions -F 'questions=@questions.json' -F 'document=@document.pdf'
    ```

3. The application will process the files, extract text from the PDF, use OpenAI's GPT-4o-mini model to answer the questions.

## Project Structure

```
.
├── app.py                  # Main Flask application
├── extract.py              # PDF text extraction logic
├── openai_api.py           # OpenAI API interaction logic
├── requirements.txt        # Python package dependencies
├── .env                    # Environment variables
└── README.md               # Project documentation
```