import config
import facebook
from bs4 import BeautifulSoup
import requests

def get_fb():
	ACCESS_TOKEN = config.ACCESS_TOKEN
	graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='2.7')
	profile = graph.get_object("me")
	friends = graph.get_connections("me", "taggable_friends", limit="10000")

	friend_list = [friend['name'] for friend in friends['data']]
	return friend_list
def get_deans():
	response = requests.get(("https://carleton.ca/awards/2016-2017-deans-honour-list/")) #Recieve the response from the webpage
	soup = BeautifulSoup(response.text, 'lxml')	#Parse into lxml
	soup=soup.find_all('td')	#Find all 'td tags'
	friends=get_fb()
	for link in soup:
		if(link.contents[0] in friends):
			print(link.contents[0])
get_deans()