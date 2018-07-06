import requests

from datetime import datetime, timedelta


def get_week_ago_date():
    raw_week_ago_datetime = (
        datetime.now()
        - timedelta(weeks=1)
    )
    return raw_week_ago_datetime.strftime('%Y-%m-%d')


def find_popular_projects(week_ago_date, top_size):
    search_repo_url = 'https://api.github.com/search/repositories'
    query_params = {
        'language': 'python',
        'q': 'created: > week_ago_date',
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size
    }
    try:
        raw_response = requests.get(search_repo_url, params=query_params)
        #print(raw_response)
        print(type(raw_response))
        print(raw_response.json())
        print(raw_response.json()['items'])
        #return repo_response.json()['items']
    except requests.exceptions.RequestException:
        return None

def main():
    top_size = 2
    week_ago_date = get_week_ago_date()
    print(week_ago_date)
    find_popular_projects(week_ago_date, top_size)

if __name__ == '__main__':
    main()

