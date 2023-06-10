import os
import requests
from googletrans import Translator
from bs4 import BeautifulSoup
import re
import logging


class NewsReaderAI:
    def __init__(self, refresh_articles=False) -> None:
        # Basic Config
        self.refresh_articles = refresh_articles
        self.logger = self.setup_logger()

        ## News API parameters
        self.API_KEY = "0ab72b36362d4380b8b374aeb8c38d48"
        self.API_KEY = "131353e264a04aeea5ac4a1c45b969f9"
        self.NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"

        ## Model Specific Settings
        self.SAVE_DIRECTORY = "privateGPT/source_documents"

        # Init
        os.makedirs(self.SAVE_DIRECTORY, exist_ok=True)

    def setup_logger(self):
        # Create a logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Create a formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Create a file handler and add it to the logger
        file_handler = logging.FileHandler("NewsReaderAI.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

    def html_to_text(self, html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        text = soup.get_text()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\n+", "\n", text)
        return text

    def get_web_article(self, url, start_text, length) -> str:
        response = requests.get(url)
        if response.status_code == 200:
            content = self.html_to_text(html_text=response.content)
            if start_text:
                try:
                    start_idx = content.index(start_text)
                    self.logger.debug(f"Found content in {start_idx}:{length}")
                    return content[start_idx : start_idx + length]
                except ValueError:
                    self.logger.warn(
                        f"short description was not found in website content for url:{url} "
                    )
                    self.logger.debug(start_text)
                    self.logger.debug(f"{content}\n")

            # If start_text is None This means we did not get content from the API
            # We will return what we can from the url
            return content

    def process_article(self, article) -> str:
        # Get the article details
        title = article.get("title", "")
        description = article.get("description", "")
        published_at = article.get("publishedAt", "")
        content = article.get("content", "")
        full_context = content
        url = article.get("url", None)
        url_img = article.get("urlToImage", None)

        if content:
            # check if content has more than 200 chars
            is_more_content = content[-1] == "]"
            if is_more_content and url:
                try:
                    content_intro = content[0 : content.index("…")]
                    # if content > 200 chars the last few words
                    # denote the actual lenth of the content
                    content_length = int(content[content.index("…") + 4 : -7])
                    full_context = self.get_web_article(
                        url=url, start_text=content_intro, length=content_length
                    )

                except Exception as e:
                    self.logger.exception(
                        f"Some problem with content. content:{content} error:", e
                    )
        else:
            # content is empty, try getting from website
            full_context = self.get_web_article(url=url, start_text=None, length=None)

        # Return English translation
        return (
            published_at,
            self.translate_text(
                text="\n\n".join(
                    [
                        f"{key}: {value}"
                        for key, value in {
                            "title": title,
                            "url": url,
                            "url_img": url_img,
                            "description": description,
                            "article": full_context,
                            "published": published_at,
                        }.items()
                    ]
                )
            ),
        )

    # Function to translate text using the Google Translate API
    def translate_text(self, text, src="nl", dest="en"):
        translator = Translator()

        try:
            translation = translator.translate(text, src=src, dest=dest)
            return translation.text
        except Exception as e:
            self.logger.exception(
                f"Translation failed for text: {text}. Error: {str(e)}"
            )
            return text

    def persist_article(self, article_text, filename):
        file_path = os.path.join(self.SAVE_DIRECTORY, filename)

        # Create and write the article content to the file
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"{article_text}\n")

            self.logger.info(f"Saved article: {file_path}")
        except Exception as e:
            self.logger.exception(
                f"Failed to save article: {filename}. Error: {str(e)}"
            )

    def fetch_news(self):
        # Request news data from the API

        response = requests.get(
            self.NEWS_API_ENDPOINT,
            params={
                "apiKey": self.API_KEY,
                "category": "sports",
                "country": "nl",
                "pageSize": 100,
            },
        )

        # Check if the request was successful
        if response.status_code == 200:
            # Get the news articles from the API response
            articles = response.json().get("articles", [])

            # Process each article and create a text file
            for article in articles:
                published, article_text = self.process_article(article=article)
                self.persist_article(article_text, filename=f"{published}.txt")
