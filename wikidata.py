import requests
import csv


def get_category_members(category, cmcontinue=None):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:{category}",
            "cmlimit": 50,
            "format": "json",
            "cmcontinue": cmcontinue
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


def fetch_all_articles(category):
    articles = []
    cmcontinue = None
    while True:
        data = get_category_members(category, cmcontinue)
        articles.extend(data['query']['categorymembers'])
        if 'continue' in data:
            cmcontinue = data['continue']['cmcontinue']
        else:
            break
    return articles


def get_article_details(page_id):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
            "action": "query",
            "pageids": page_id,
            "prop": "info|extracts|revisions",
            "inprop": "url",
            "rvprop": "timestamp",
            "rvlimit": "max",
            "explaintext": True,
            "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


category = "Artificial_intelligence"
articles = fetch_all_articles(category)

with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'URL', 'Extract', 'Revisions']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for article in articles:
        print(article['title'])
        page_id = article['pageid']
        details = get_article_details(page_id)
        page = details['query']['pages'][str(page_id)]
        revisions = [rev['timestamp'] for rev in page.get('revisions', [])]
        writer.writerow({
                        'Title': page['title'],
                        'URL': page['fullurl'],
                        'Extract': page['extract'],
                        'Revisions': '; '.join(revisions)
        })
print(f"Details of {len(articles)} articles saved to 'wikipedia.csv'")
