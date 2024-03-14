import unittest
from unittest.mock import patch
from analysis_app import analyze_text, extract_entities, extract_sentiment, extract_themes


class TestAnalysisApp(unittest.TestCase):

    @patch("analysis_app.openai.Completion.create")
    def test_analyze_text(self, mock_openai_completion_create):
        # Set up mock response for the OpenAI API
        mock_openai_completion_create.return_value.choices[0].text.strip.return_value = "Mock analysis result"

        # Test analyze_text function with a sample input
        input_text = input("Enter input text: ")
        result = analyze_text(input_text)

        # Assert that the OpenAI API was called with the correct parameters
        mock_openai_completion_create.assert_called_once_with(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=200,
            temperature=0.5,
            n=1,
        )

        # Assert that the result matches the expected value
        self.assertEqual(result, "Mock analysis result")

    def test_extract_entities(self):
        # Test extract_entities function with a sample input
        result = extract_entities("This is a Sample Text with Entities like John and Apple Inc.")

        # Assert that the entities are correctly extracted
        self.assertEqual(result, ["John", "Apple", "Inc."])

    def test_extract_themes(self):
        # Test extract_themes function with a sample input
        result = extract_themes("This text has themes like Python, OpenAI, and Natural Language Processing.")

        # Assert that the themes are correctly extracted
        self.assertEqual(result, ["Python", "OpenAI", "Natural", "Language", "Processing."])

    def test_extract_sentiment(self):
        # Test extract_sentiment function with a sample input
        result = extract_sentiment("This is a positive text.")

        # Assert that the sentiment is correctly extracted
        self.assertEqual(result, "POSITIVE")

if __name__ == "__main__":
    unittest.main()