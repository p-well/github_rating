# Github Trends

This is CLI program used for searching for the most popular Python repositories on Github. <br/>

Script finds 20 most stargazers counted repositories created during the last week and prints out the following infomation: <br/>

- Projct name
- Stars amount
- Project description
- Opened issues amount
- Repo URL

Data is represented in descending order of repo stars.

The program is based on GitHub [REST API v3](https://developer.github.com/v3/)


Pavel Kadantsev, 2018. <br/>
p.a.kadantsev@gmail.com


# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using command ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment in order to keep your global scope clean.

# Usage

To execute the script use the following command in CLI: ```python github_rating.py```. <br />
Encoding changing may be required for correct script running on Windows platform: ```chcp 65001``` for UTF-8 encoding.

# Example of Script Launch

<pre>

<b> >python github_rating.py</b>

1.  Project: homelab
    Stars: 1383
    Description: Brad's homelab setup
    Issues amount: 2
    Link: https://github.com/bradfitz/homelab

2.  Project: hacker-job-trends
    Stars: 418
    Description: None
    Issues amount: 8
    Link: https://github.com/timqian/hacker-job-trends

3.  Project: laravel-self-diagnosis
    Stars: 361
    Description: Perform Self-Diagnosis Tests On Your Laravel Application
    Issues amount: 4
    Link: https://github.com/beyondcode/laravel-self-diagnosis

4.  Project: CssGitHubWindows
    Stars: 356
    Description: (UserStyle) GitHub Windows Edition [MIT]
    Issues amount: 5
    Link: https://github.com/Athari/CssGitHubWindows

5.  Project: Machine_Learning_Journey
    Stars: 311
    Description: This is the Curriculum for "Machine Learning Journey" By Siraj Raval on Youtube
    Issues amount: 0
    Link: https://github.com/llSourcell/Machine_Learning_Journey

</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
