import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def select_topics(articles):

    articles_text = ""

    for index, article in enumerate(articles, start=1):
        articles_text += f"""
Article {index}
Title: {article['title']}
Published: {article['published']}
-------------------------
"""

    prompt = f"""
You are a technology and Indian stock-market research assistant.

Analyze the following news articles.

Select ONE interesting topic for an X post.

Prefer:
- Indian technology
- AI
- semiconductor
- IT companies
- fintech
- data centers
- cybersecurity
- cloud
- technology stocks
- Indian business/markets

Do NOT give investment advice.

News articles:

Return ONLY the number of the article you selected.

Example:
12

{articles_text}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    result = response.output_text.strip()

    try:
        selected_index = int(result)
    except ValueError:
        raise ValueError(
            f"AI returned an invalid article number: {result}"
        )

    if selected_index < 1 or selected_index > len(articles):
        raise ValueError(
            f"AI selected article {selected_index}, "
            f"but only {len(articles)} articles exist."
        )

    return articles[selected_index - 1]


if __name__ == "__main__":

    test_articles = [
        {
            "title": "India semiconductor industry expands",
            "published": "2026-09-17",
            "link": "https://example.com"
        }
    ]

    result = select_topics(test_articles)

    print(result)