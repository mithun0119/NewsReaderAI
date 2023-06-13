from NewsReaderAI import NewsReaderAI

COUNTRIES = ['nl', 'gb']
CATEGORIES = ['sports', 'global']

for country in COUNTRIES:
    for category in CATEGORIES:
        app = NewsReaderAI(country, category)
        app.fetch_news()
