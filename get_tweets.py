import sys
import csv
#http://www.tweepy.org/
import tweepy
#Twitter API credentials and enter them here
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#method to get a user's last tweets
def get_tweets(username):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	number_of_tweets = 1

	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
		print(tweet.text)
		tweets_for_csv.append([tweet.text])

	#write to a new csv file from the array of tweets
	outfile = username + "_tweets.csv"
	print ("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)
		print(tweets_for_csv)

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")

