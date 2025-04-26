Tamil News Sentiment Analyzer
This project fetches live Tamil news headlines from Thanthi TV, translates them to English, and performs sentiment analysis using VADER.

Features
Scrapes latest headlines from Thanthi TV

Translates Tamil headlines to English

Analyzes the sentiment: Positive, Negative, or Neutral

Automatically updates every 15 minutes

Requirements
Python 3.x

requests

beautifulsoup4

googletrans

vaderSentiment

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YourUsername/RepoName.git
cd RepoName
Install the required packages:

bash
Copy
Edit
pip install requests beautifulsoup4 googletrans==4.0.0-rc1 vaderSentiment
How to Run
Simply execute the script:

bash
Copy
Edit
python your_script_name.py
It will fetch, translate, and analyze the latest headlines automatically.

The program will update every 15 minutes.

Press Ctrl+C to stop the program manually.

Folder Structure
bash
Copy
Edit
/project-folder
  ├── news_sentiment.py  # (your Python code)
  └── README.md
Output Example
vbnet
Copy
Edit
Fetching headlines...

Date & Time: 2025-04-26 15:30:20
Original Headline (Tamil): அரசியல் கூட்டணி பேச்சுவார்த்தை இன்று தொடரும்
Translated Headline (English): Political alliance talks continue today
Sentiment: Neutral

Waiting for 15 minutes before next update...
Notes
If translation fails, original Tamil headline will be used.

If you get too many translation errors, Google Translator API may rate limit you temporarily.

