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

def fetch_tweets(url, keyword, http_method, count=15):
  
  parameters = {"q" : keyword, "count" : count, "include_entities" : "true"}

  req = oauth2.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
  
  return requests.get(req.to_url())

def process_and_return_random_tweet(url, keyword):
  response = fetch_tweets(endpoint, keyword, "GET", 15)
  
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
  
  username   = random_tweet["user"]["screen_name"]
  tweet_text = random_tweet["text"].encode('utf-8') # To support non english characters.

  print(username)
  print(tweet_text)

  if("media" in random_tweet["entities"].keys()):
    for media in random_tweet["entities"]["media"]:
      print media["media_url"]
      


if __name__ == "__main__":
  endpoint = "https://api.twitter.com/1.1/search/tweets.json"
  keyword  = "football"

  if len(sys.argv) == 2:
    keyword = sys.argv[1]
  else:
    print("Usage : python rocketrip_assignment 'keyword' ")
    # return 

  process_and_return_random_tweet(endpoint, keyword)
