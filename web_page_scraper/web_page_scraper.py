import requests
from bs4 import BeautifulSoup
import os
import string


def save_article(article_title, article_body):
    # Replace spaces in article title with underscores and remove punctuation
    translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    file_name = article_title.translate(translation_table).replace(' ', '_') + '.txt'

    # Remove all spaces from article title
    file_name = ''.join(article_title.split()) + '.txt'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(article_body)

    print(f"Article '{article_title}' saved as '{file_name}'.")


def process_page(url, page_number, article_type):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Create directory for current page
        directory = f'Page_{page_number}'
        os.makedirs(directory, exist_ok=True)

        articles = soup.find_all('article')
        for article in articles:
            article_type_span = article.find('span', {'data-test': 'article.type'})
            if article_type_span and article_type_span.text.strip() == article_type:
                article_title = article.find('h3', {'itemprop': 'headline'}).text.strip()
                article_body = article.find('div', {'class': 'c-article-body'}).text.strip()
                save_article(os.path.join(directory, article_title), article_body)

    else:
        print(f"The URL returned {response.status_code}!")


def main():
    page_count = int(input("Enter the number of pages: "))
    article_type = input("Enter the type of articles: ")

    base_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2022&page='

    for page_number in range(1, page_count + 1):
        url = f'{base_url}{page_number}'
        process_page(url, page_number, article_type)

    print("Saved all articles.")


if __name__ == "__main__":
    main()
