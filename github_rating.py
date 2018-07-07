import requests

from datetime import datetime, timedelta


def get_week_ago_date():
    raw_week_ago_datetime = (
        datetime.now()
        - timedelta(weeks=1)
    )
    return raw_week_ago_datetime.strftime('%Y-%m-%d')


def fetch_popular_projects(week_ago_date, top_repos_amount):
    search_repo_url = 'https://api.github.com/search/repositories'
    qualifiers = {
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_repos_amount,
        'q': 'created:>{}'.format(week_ago_date),
        'language': 'python'
    }
    try:
        raw_response = requests.get(search_repo_url, params=qualifiers)
        most_popular_projects_data = raw_response.json().get('items')
    except requests.exceptions.RequestException:
        most_popular_projects_data = []
    return most_popular_projects_data


def fetch_open_issues_amount(project_data):
    repo_full_name = project_data['full_name']
    search_issues_url = (
        'https://api.github.com/repos/{}/issues'.format(repo_full_name)
    )
    try:
        raw_response = requests.get(search_issues_url)
        open_issues_amount = len(raw_response.json())
    except requests.exceptions.RequestException:
        open_issues_amount = 0
    return open_issues_amount


def print_popular_project_info(project_data, issues_amount, counter):
    print("""
{}. Repo name: {}
    Stars: {}
    Description: {}
    Issues amount: {}
    Link: {}""".format(
        counter,
        project_data['name'],
        project_data['stargazers_count'],
        project_data['description'],
        issues_amount,
        project_data['html_url']))


def main():
    top_repos_amount = 20
    week_ago_date = get_week_ago_date()
    most_popular_projects_data = fetch_popular_projects(
        week_ago_date,
        top_repos_amount
    )
    if most_popular_projects_data:
        counter = 1
        for project_data in most_popular_projects_data:
            project_issues_amount = fetch_open_issues_amount(project_data)
            print_popular_project_info(
                project_data,
                project_issues_amount,
                counter
           )
            counter += 1
    else:
        print('Request to GitHub API failed.')


if __name__ == '__main__':
    main()
