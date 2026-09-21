# Python Daily Tech Agent

A lightweight automation project that gathers Indian technology news, selects a relevant story, drafts an X post, checks the content against the source, and saves the output for review or publishing.

## Overview

This project automates a simple publishing workflow:

1. Searches Google News RSS for Indian technology and market topics.
2. Uses OpenAI to identify the most relevant article.
3. Drafts a short, X-friendly post based on the selected topic.
4. Runs a fact-check step to assess whether the post is supported by the source.
5. Saves the result in the output folder.
6. Can optionally publish to X when API credentials are configured.

The system is designed for daily content creation around India’s technology ecosystem, AI, startups, infrastructure, and market-related news.

## Features

- Google News RSS search for trending tech stories
- AI-assisted topic selection
- X post generation with a short-form writing constraint
- AI-powered fact checking before publishing
- Daily JSON output and historical archive storage
- Optional X publishing integration

## Project structure

- main.py — orchestrates the complete pipeline
- researcher.py — fetches news articles from Google News RSS
- topic_selector.py — selects the best topic from collected articles
- writer.py — generates the final X post
- fact_checker.py — validates the post against the chosen source
- output_manager.py — stores results in the output folder
- x_publisher.py — publishes to X when enabled
- database.py — placeholder for future persistence work
- requirements.txt — project dependencies
- output/ — generated daily and historical output files

## Requirements

- Python 3.10+
- OpenAI API key
- Optional: X API credentials for publishing

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key

# Optional: only needed for X publishing
X_CONSUMER_KEY=your_x_consumer_key
X_CONSUMER_SECRET=your_x_consumer_secret
X_ACCESS_TOKEN=your_x_access_token
X_ACCESS_TOKEN_SECRET=your_x_access_token_secret
```

## Run the app

```bash
python main.py
```

The script will:

- query several technology-related search terms
- collect recent articles
- pick one topic
- generate a post
- fact-check the output
- save the result in the output folder

## Output format

Each run produces a JSON file in the output directory, such as:

- output/2026-09-20.json
- output/posts.json

The saved result includes:

- date
- source topic/title
- article link and published date
- generated post
- fact-check result
- publication status

## X publishing

The publishing logic exists in x_publisher.py. In the current main flow, the actual publish call is intentionally commented out:

```python
# publish_to_x(post)
```

To enable live posting:

1. add your X API credentials to .env
2. uncomment the publish line in main.py
3. run the script again

## Notes

- This project relies on OpenAI for article selection, writing, and fact-checking.
- The fact-check step is a validation aid, not a guarantee of perfect accuracy.
- The workflow is intentionally simple and intended for experimentation, learning, or lightweight automation.
- Google News RSS results may vary depending on query timing and feed availability.

## License

This project does not currently include a license file. If you plan to publish it publicly, add an appropriate open-source license.
