
import facebook

ACCESS_TOKEN = "EAAKmexW29owBAAwxAIoeZBl6PVStngnCrdj0eqFF7byjG6O40LdBHt2ZAA86jizuGGT1OZBtQQOXh1mVuSQrSpCEin4wxeThd8v67QZCZAOAZCN0CAJ28obFg78MFp2cZAh5PXeaau61PgFUkkYVYryMEaAP4eslqS8KEo3b4M4856nirswiRLykI74NAZC1DtcZD"
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='2.7')
profile = graph.get_object("me")
friends = graph.get_connections("me", "taggable_friends", limit="500")

friend_list = [friend['name'] for friend in friends['data']]

print(friend_list)