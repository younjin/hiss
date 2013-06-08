# WINDOWS USERS REJOICE

# Jealous of your MacLovin friends and their sexy Terminal?
# Show them how cool you are by tweeting @them from cmd! Yeah!

# This Twitter app was built with the sample code provided at
# Python on Campus, an event hosted by WatPy on 8 June, 2013.
# Additional help was provided by tutors (@psobot, @amtinits,
# among others) hovering nearby. :)
# http://watpy.ca/learn/project/twitter/

# You will need to install tweepy (third party library):
# > pip install tweepy

import sys
import argparse
import tweepy

# Setting up argument parsing
parser = argparse.ArgumentParser(description='Twitter commandline.')
parser.add_argument('-t', '--tweet', help='post a new tweet')
parser.add_argument('-v', '--view', help='view timeline', action="store_true")
parser.add_argument('-s', '--search', help='search Twitter')

# Visit dev.twitter.com and log in with the intended account.
# Visit applications and create a new application.
# Under Settings > Application type > Access, select Read and Write.
# Under Details, Create my access token.

# Paste the four relevant codes below:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    # Checking if authentication was valid:
    if api.verify_credentials() == False:
        print("Warning: unable to authorise with provided tokens.")
        print("Are you a hacker? Y/N")
        print("Kidding, you don't actually get to answer. Bye!")
        sys.exit(-1)
    
    args = parser.parse_args()

    # Optional: you can print the results of the parsing:
    #print(args.tweet)

    # Function for printing timeline:
    def print_timeline():
        for status in api.home_timeline():
            print(status.author.screen_name.encode("utf-8") + " " + status.text.encode("utf-8"))
    
    # Function for posting a tweet:
    def tweet(status):
        if len(status) > 140:
            over = len(status)-140
            print("You are %d characters over the limit. BE CONCISE!" % over)
        else:
            api.update_status(status)
            print("New tweet: {0}" % status)
    
    # Function for searching Twitter:
    def search(query):
        results = api.search(query)
        for result in results:
            print(result.from_user.encode("utf-8") + " " + result.text.encode("utf-8"))

    if args.tweet:
        tweet(args.tweet)
    elif args.view:
        print_timeline()
    elif args.search:
        search(args.search)
    else:
        print("You might want to provide an argument! Try -h for options.")
