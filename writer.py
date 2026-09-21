import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def write_post(selected_article):
    topic = selected_article["title"]
    prompt = f"""
You are an expert technology and stock-market content writer
focused on India.

Create ONE high-quality X post based on the topic below.

Topic:
{topic}

Requirements:

- Maximum 280 characters
- Clear and easy to understand
- Useful for technology and market followers
- Do not exaggerate
- Do not make unsupported claims
- Do not give direct buy/sell investment advice
- Avoid unnecessary hashtags
- Use at most 2 relevant hashtags
- Make the post engaging but professional

Return ONLY the final X post.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text.strip()


if __name__ == "__main__":

    test_topic = """
Indian semiconductor industry is attracting new investments,
with companies expanding manufacturing and chip-related
capabilities in the country.
"""

    post = write_post(test_topic)

    print("\nGENERATED X POST:")
    print("----------------------")
    print(post)
    print("----------------------")
    print("Characters:", len(post))