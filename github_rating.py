import requests

from datetime import datetime, timedelta


def get_week_ago_date():
    raw_week_ago_datetime = (
        datetime.now()
        - timedelta(weeks=1)
    )
    return raw_week_ago_datetime.strftime('%Y-%m-%d')


def find_popular_projects():
    pass

def main():
    print(get_week_ago_date())

if __name__ == '__main__':
    main()

