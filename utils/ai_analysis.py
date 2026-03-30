import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def generate_ai_analysis(formation, width, depth, compactness):
    if not api_key:
        return "Error: OPENAI_API_KEY was not found in the .env file."

    prompt = f"""
You are a professional soccer tactical analyst.

Analyze the following team shape:

Formation: {formation}
Width: {width}
Depth: {depth}
Compactness: {compactness}

Provide a short tactical analysis in 3 to 4 sentences.
Focus on structure, spacing, strengths, and possible weaknesses.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an elite soccer tactical analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI error: {str(e)}"