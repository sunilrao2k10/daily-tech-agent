import json
import os
from datetime import datetime


OUTPUT_DIR = "output"


def save_daily_result(
    selected_article,
    post,
    fact_check,
    published=False
):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    daily_file = os.path.join(
        OUTPUT_DIR,
        f"{today}.json"
    )

    result = {
        "date": today,
        "topic": selected_article["title"],
        "source": {
            "title": selected_article["title"],
            "link": selected_article["link"],
            "published": selected_article["published"]
        },
        "post": post,
        "fact_check": fact_check,
        "published": published
    }

    # Save today's result
    with open(
        daily_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    # Save to historical posts file
    posts_file = os.path.join(
        OUTPUT_DIR,
        "posts.json"
    )

    posts = []

    if os.path.exists(posts_file):

        with open(
            posts_file,
            "r",
            encoding="utf-8"
        ) as file:

            posts = json.load(file)

    posts.append(result)

    with open(
        posts_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            posts,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"\nDaily result saved: {daily_file}")
    print(f"Historical posts saved: {posts_file}")