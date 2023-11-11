# Telegram Quiz Scraper

This Python script is designed to scrape quiz questions from a Telegram chat history stored in a `result.json` file and save them into a CSV file.

Demo Video :- https://youtu.be/GMbvKSAbxkQ
## Requirements

- Python 3.x
- `pandas` library (for CSV handling)
- `json` library (for JSON parsing)

## Usage

1. **Download Telegram Chat History**

   - Obtain the `result.json` file containing your Telegram chat history.

2. **Install Dependencies**

   Make sure you have Python 3.x installed on your system. Install the required libraries using the following command:

   ```
   pip install pandas
   ```

3. **Run the Script**

   Execute the `telegram_quiz_scraper.py` file using a Python interpreter. The script will prompt you to provide the path to the `result.json` file.

   ```
   python telegram_quiz_scraper.py
   ```

4. **Output**

   The script will generate a `quiz_questions.csv` file containing the scraped quiz questions.

## How it Works

This script parses the `result.json` file, extracts quiz questions, and saves them into a CSV file using the following steps:

1. Load the JSON data from `result.json`.

2. Parse the messages in the chat history.

3. Identify and extract quiz questions from the messages.

4. Save the extracted questions into a CSV file (`quiz_questions.csv`).

## Disclaimer

This script assumes that the quiz questions in the Telegram chat history have a specific format that can be reliably identified. If the format changes, or if there are variations in how questions are presented, the script may need to be adjusted accordingly.

## Troubleshooting

- If you encounter any issues while running the script, please make sure that you have provided the correct path to the `result.json` file and that it contains the expected data.
- If the format of the quiz questions in your chat history is different from what the script expects, you may need to modify the parsing logic in the script to accommodate the specific format used in your chat.

This project is licensed under the [MIT License](LICENSE).
