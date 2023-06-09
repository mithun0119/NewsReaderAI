#API_KEY = '0ab72b36362d4380b8b374aeb8c38d48'

import requests
import os
from datetime import datetime
from googletrans import Translator

# News API parameters
API_KEY = '0ab72b36362d4380b8b374aeb8c38d48'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

# Countries and categories to fetch news data from
COUNTRIES = ['nl']  # Example countries: US, UK, Netherlands
CATEGORIES = ['sports']  # Example categories: sports, technology

# Directory to save the files
SAVE_DIRECTORY = 'privateGPT/source_documents'
# SAVE_DIRECTORY = 'newsfiles'

# Create the save directory if it doesn't exist
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

# Function to translate text using the Google Translate API
def translate_text(text, target_language):
    translator = Translator()

    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        print(f'Translation failed for text: {text}. Error: {str(e)}')
        return text

# Iterate over the countries and categories
for country in COUNTRIES:
    for category in CATEGORIES:
        # Request news data from the API
        response = requests.get(NEWS_API_ENDPOINT, params={'apiKey': API_KEY, 'category': category, 'country': country})

        # Check if the request was successful
        if response.status_code == 200:
            # Get the news articles from the API response
            articles = response.json().get('articles', [])

            # Process each article and create a text file
            for article in articles:
                # Get the article details
                title = article.get('title')
                description = article.get('description')
                published_at = article.get('publishedAt')

                if title and description and published_at:
                    published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d_%H-%M-%S')

                    # Translate the article to English
                    title_english = translate_text(title, 'en')
                    description_english = translate_text(description, 'en')

                    # Create the file path
                    file_name = f'{published_at}_{title_english}.txt'
                    file_path = os.path.join(SAVE_DIRECTORY, file_name)

                    # Create and write the article content to the file
                    try:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(f'Title: {title_english}\n')
                            file.write(f'Description: {description_english}\n')

                        print(f'Saved article: {file_path}')
                    except Exception as e:
                        print(f'Failed to save article: {file_name}. Error: {str(e)}')
                else:
                    print('Missing required article details.')
        else:
            print(f'Failed to retrieve news data for {country} and {category} from the API.')
