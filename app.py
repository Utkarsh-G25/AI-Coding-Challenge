from flask import Flask, request, jsonify
from extract import extract_text_from_pdf
from openai_api import get_answers
from dotenv import load_dotenv
import json
import logging


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"pdf", "json"}


@app.route("/answer-questions", methods=["POST"])
def answer_questions():
    try:
        if "questions" not in request.files or "document" not in request.files:
            return (
                jsonify(
                    {
                        "error": "Please upload both a questions file and a document file."
                    }
                ),
                400,
            )

        questions_file = request.files["questions"]
        document_file = request.files["document"]

        if not (
            allowed_file(questions_file.filename)
            and allowed_file(document_file.filename)
        ):
            return (
                jsonify(
                    {"error": "Invalid file type. Only PDF and JSON files are allowed."}
                ),
                400,
            )

        questions_data = json.load(questions_file)
        questions = questions_data.get("questions", [])

        document_text = extract_text_from_pdf(document_file)

        answers = get_answers(document_text, questions)

        return jsonify(answers)
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return (
            jsonify({"error": "An error occurred while processing your request."}),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True)
