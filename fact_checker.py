import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def check_post(post, selected_article):

    prompt = f"""
You are a fact checker for an India technology and financial
news X account.

Check whether the following X post is supported by the provided
news articles.

X POST:
{post}

SOURCE ARTICLES:
{selected_article["title"]}

Check for:

1. Factual accuracy
2. Whether the claims are supported by the articles
3. Whether numbers, company names, dates or other details are correct
4. Any exaggerated or unsupported claims

Return the result in exactly this format:

VERDICT: PASS or FAIL

REASON:
Explain briefly why.

CORRECTIONS:
If something is wrong or unsupported, explain what should be changed.
If everything is correct, write "None".
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text.strip()


if __name__ == "__main__":

    test_post = """
India's semiconductor industry is attracting new investments,
strengthening the country's position in the global chip supply chain.
#IndiaTech #Semiconductor
"""

    test_articles = [
        {
            "title": "India semiconductor industry attracts new investment",
            "published": "Today"
        },
        {
            "title": "Companies expand semiconductor manufacturing in India",
            "published": "Today"
        }
    ]

    result = check_post(test_post, test_articles)

    print("\nFACT CHECK RESULT:")
    print("----------------------")
    print(result)
    print("----------------------")