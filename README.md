# Rocketrip Assignment

* Python version: Tested on version 2.7.3, but should work on latest version.

* Instructions: python rocketrip_assignment.py "keyword"

* Dependencies:

	* oauth2 	 - https://github.com/joestump/python-oauth2
	* requests - https://pypi.python.org/pypi/requests

* Issues:
	If you get the following exceptions while using requests module run the following command:
	
	InsecurePlatformWarning or SNIMissingWarning

	```bash

		pip install pyopenssl ndg-httpsclient pyasn1

	```