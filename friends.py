import config
import facebook

def get_fb():
	ACCESS_TOKEN = config.ACCESS_TOKEN
	graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='2.7')
	profile = graph.get_object("me")
	friends = graph.get_connections("me", "taggable_friends", limit="10000")

	friend_list = [friend['name'] for friend in friends['data']]
	return friend_list
def get_deans():
	print("Testing")
print(get_fb())