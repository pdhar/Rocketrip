import oauth2
import requests

api_key             = "vW4u1UHOr7T9LloRXbGI9A"
api_secret          = "Wt1E87vMHENhe54EejfhYNKZwbnscz1iMMVQUdRQ"
access_token_key    = "1017369080-iAuxzsupRXi7SSbJqKqbT4LewpaKixxPgwt5j8o"
access_token_secret = "CpU6Vmazvz9lDmAr8cLobTr3zzU0c1upNmAhDBWXDSt9B"

oauth_token    = oauth2.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth2.Consumer(key=api_key, secret=api_secret)
signature_method_hmac_sha1 = oauth2.SignatureMethod_HMAC_SHA1()

def fetch_tweets(url, keyword, http_method, count=100):
  
  parameters = {"q" : keyword}

  req = oauth2.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
  
  return requests.get(req.to_url())

def process_and_return_random_tweet(url, keyword):
  response = fetch_tweets(endpoint, keyword, "GET")
  print(response.json())
	
if __name__ == "__main__":
  endpoint = "https://api.twitter.com/1.1/search/tweets.json"
  keyword  = "football" 
  process_and_return_random_tweet(endpoint, keyword)

