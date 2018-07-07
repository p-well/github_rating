import requests

from datetime import datetime, timedelta


def get_week_ago_date():
    raw_week_ago_datetime = (
        datetime.now()
        - timedelta(weeks=1)
    )
    return raw_week_ago_datetime.strftime('%Y-%m-%d')


def fetch_popular_projects(week_ago_date, top_size):
    search_repo_url = 'https://api.github.com/search/repositories'
    qualifiers = {
        'sort': 'stars',
        'order': 'desc',
        'q':'created: > week_ago_date',
        'language': 'python',
        'per_page': top_size
    }
    try:
        raw_response = requests.get(search_repo_url, params=qualifiers)
        most_popular_projects_data = raw_response.json().get('items')
    except requests.exceptions.RequestException:
        most_popular_projects_data = []
    return most_popular_projects_data


def fetch_open_issues_amount(most_popular_projects_data):
    repo_full_name = most_popular_projects_data['full_name']
    search_issues_url = (
        'https://api.github.com/repos/{}/issues'.format(repo_full_name)
    )
    try:
        issue_response = requests.get(search_issues_url)
        return len(issue_response.json())
    except requests.exceptions.RequestException:
        return None


def main():
    top_size = 2
    week_ago_date = get_week_ago_date()
    print(week_ago_date)
    find_popular_projects(week_ago_date, top_size)


if __name__ == '__main__':
    main()

# https://api.github.com/search/repositories?q=created:%3E2018-07-05+language:python&sort=stars&order=desc&per_page=20