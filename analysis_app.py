import openai
import os
import json
import argparse
from transformers import pipeline

### For this script the following packages should be installed: openai, os, json, argparse, transformers

# Retrieve the OpenAI API key from the windows environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text(text):
    # Specify the OpenAI GPT-3.5 engine and provide the text input
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=200,
        temperature=0.5,
        n=1,
    )

    return response.choices[0].text.strip()

def extract_entities(result):
    # Add logic to extract entities based on the analysis result
    # This can be done using Named Entity Recognition (NER) techniques
    # For simplicity, let's assume entities are words starting with a capital letter
    entities = [word for word in result.split() if word.istitle()]
    return entities

def extract_themes(result):
    # Add logic to extract themes based on the analysis result
    # This can be done using keyword extraction or topic modeling techniques
    # For simplicity, let's assume themes are unique words in the result
    themes = list(set(result.split()))
    return themes

def extract_sentiment(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(text)
    return result[0]['label']



def generate_report(original_text, analysis_result):
    entities = extract_entities(analysis_result)
    themes = extract_themes(analysis_result)
    sentiment = extract_sentiment(analysis_result)

    report = {
        "Original Text": original_text,
        "Entities": entities,
        "Themes": themes,
        "Sentiment": sentiment,
        "Analysis Result": analysis_result
    }

    return json.dumps(report, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Perform text analysis using the OpenAI API.")
    parser.add_argument("-t", "--text", help="Text to analyze", required=True)
    args = parser.parse_args()

    input_text = args.input_text

    # Perform text analysis
    analysis_result = analyze_text(input_text)

    # Generate and display the report
    report = generate_report(input_text, analysis_result)
    print(report)

if __name__ == "__main__":
    main()