# Deans List Comparison

A python script that compares Carleton University's deans list recipients with your current list of facebook friends.

### Technology
- Python 3
- Requests
- BeautifulSoup4

>Version 1.0

### Schedule Sender Setup(Windows)
- Download or clone the repository
- Make sure `pip` and Python 3 are installed
- Install the required modules using pip
```
$ pip install facebook-sdk
$ pip install requests
$ pip install BeautifulSoup4
```
- Create a config.py file in the same directiory as friends.py
- Create a facebook developer account and an app
- In the App Review header, submit a review for Taggable Friends
- Go to https://developers.facebook.com/tools/accesstoken/ and set a variable named ACCESS_TOKEN to the given string in your config.py file
