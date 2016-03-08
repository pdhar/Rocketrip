# Rocketrip Assignment

* Python version: Tested on versions 2.7.3, 3.5

* Instructions: python rocketrip_assignment.py "keyword"

* Output 

	Example Usage:

	```bash

	python rocketrip_assignment.py "football"

	```
	Result:

	```
		@TheREAL_Monte : RT @espn: In 1998, they joined the NFL together as college legends.
		In 2016, they depart the NFL together as football legends. https://t.co… 
		media : 
		http://pbs.twimg.com/media/Cc4k-rLW4AApyIx.jpg
	```

* Dependencies:

	* oauth2 	 - https://github.com/joestump/python-oauth2
	* requests - https://pypi.python.org/pypi/requests

* Issues:
	If you get the following exceptions while using requests module run the following command:
	
	InsecurePlatformWarning or SNIMissingWarning

	```bash

		pip install pyopenssl ndg-httpsclient pyasn1

	```
