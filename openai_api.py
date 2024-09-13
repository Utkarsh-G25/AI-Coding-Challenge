import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_answers(document_text, questions):
    """Use OpenAI's API to answer questions based on the provided document."""
    answers = {}
    chunk_size = 100000
    overlap = 2000

    for question in questions:
        answer = "Data Not Available"
        for i in range(0, len(document_text), chunk_size - overlap):
            chunk = document_text[i : i + chunk_size]
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": f"Document: {chunk}... \nQuestion: {question}\nAnswer:",
                    },
                ],
                max_tokens=100,
                temperature=0.5,
            )
            chunk_answer = response.choices[0].message["content"].strip()
            finish_reason = response.choices[0].finish_reason
            if finish_reason == "stop":
                answer = chunk_answer
                break
        answers[question] = answer
    return answers
