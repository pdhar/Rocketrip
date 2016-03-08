# https://github.com/joestump/python-oauth2
import oauth2
# https://pypi.python.org/pypi/requests
import requests
# https://docs.python.org/3.5/library/
import sys
import random

"""

  Author : Pranav Dhar
  Date : 03/07/16
  Description : A Simple python program ( function ) that returns a random tweet based on 'keyword' search. 
  Usage : python rocketrip_assignment "keyword"

  Documentation for Search API: https://dev.twitter.com/rest/public/search

"""

api_key             = "vW4u1UHOr7T9LloRXbGI9A"
api_secret          = "Wt1E87vMHENhe54EejfhYNKZwbnscz1iMMVQUdRQ"
access_token_key    = "1017369080-iAuxzsupRXi7SSbJqKqbT4LewpaKixxPgwt5j8o"
access_token_secret = "CpU6Vmazvz9lDmAr8cLobTr3zzU0c1upNmAhDBWXDSt9B"

oauth_token    = oauth2.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth2.Consumer(key=api_key, secret=api_secret)
signature_method_hmac_sha1 = oauth2.SignatureMethod_HMAC_SHA1()

"""
  fetch_tweets

  params:
  url - twitter endpoint to get oauth token and make search query.
  keyword - search word
  count  - number of tweets to sample

"""
def fetch_tweets(url, keyword, count=15):
  
  parameters  = {"q" : keyword, "count" : count, "include_entities" : "true"}
  http_method = "GET"

  req = oauth2.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
  
  return requests.get(req.to_url())

"""
  process_and_return_random_tweet

  params:
  url - twitter endpoint to get oauth token and make search query.
  keyword - search word

"""
def process_and_return_random_tweet(url, keyword):
  response = fetch_tweets(endpoint, keyword, 50)
  
  # Basic check for valid response status
  if(response.status_code != 200):
    print("Please verify credentials.")
    return

  response_json = response.json()

  tweets = response_json["statuses"]
  
  if len(tweets) == 0:
    print("No tweets matching keyword: %s" % keyword)
    return

  random_tweet = random.sample(tweets, 1)[0]
  
  username   = random_tweet["user"]["screen_name"].encode('utf-8')
  tweet_text = random_tweet["text"].encode('utf-8') # To support non english characters.

  media_links = []
  if("media" in random_tweet["entities"].keys()):
    for media in random_tweet["entities"]["media"]:
      media_links.append(media["media_url"].encode('utf-8')) 
      
  display_tweet_formatted(username, tweet_text, media_links)

"""
  display_tweet_formatted

  params:
  username    - tweet user
  tweet_text  - tweet text 
  media_links - media links inside tweet

"""
def display_tweet_formatted(username, tweet_text, media_links):
  print("@%s : %s " % (username, tweet_text))
  if(len(media_links) > 0):
    print("media : ")
    for link in media_links:
      print(link)

if __name__ == "__main__":
  endpoint = "https://api.twitter.com/1.1/search/tweets.json"
  keyword  = "football"

  if len(sys.argv) == 2:
    keyword = sys.argv[1]
    process_and_return_random_tweet(endpoint, keyword)
  else:
    print("Usage : python rocketrip_assignment 'keyword' ")
