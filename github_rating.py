import requests

from datetime import datetime, timedelta


def get_week_ago_date():
    raw_week_ago_datetime = (
        datetime.now()
        - timedelta(weeks=1)
    )
    return raw_week_ago_datetime.strftime("%d/%m")


def find_popular_projects():
    pass

def main():
    get_week_ago_date()

if __name__ == '__main__':
    main()

