from researcher import search_news
from topic_selector import select_topics
from writer import write_post
from fact_checker import check_post
from x_publisher import publish_to_x
from output_manager import save_daily_result

queries = [
    "India technology stocks",
    "India AI companies",
    "India data center",
    "India cloud computing",
    "India cybersecurity"
]

def main():

    all_articles = []

    for query in queries:
        articles = search_news(query)

        all_articles.extend(articles)

    selected_article = select_topics(all_articles[:2])

    post = write_post(selected_article)

    fact_check = check_post(post, selected_article)
    
    if "VERDICT: PASS" in fact_check.upper():
        #publish_to_x(post) 
        save_daily_result(
            selected_article,
            post,
            fact_check,
            published=False
        )
    else:
        print("\nFACT CHECK FAILED ❌")
        save_daily_result(
            selected_article,
            post,
            fact_check,
            published=False
        )

if __name__ == "__main__":
    main()