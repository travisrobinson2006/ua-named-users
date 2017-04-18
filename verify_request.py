import json
import response_writer
import base64
import logging

def verify_app_credential(self):#verify credentials provided and are valid; returns true if they are and false if they're not
	
	if self.request.authorization is None:
		return False
	else:
		username, password = base64.b64decode(self.request.authorization[1]).split(':')#source:https://gist.github.com/jeremydw/bc901de8b7e59cbeb190
			#converts basic auth string to readable username and password
	if username == 'application_key' and password == 'application_secret':#check if valid, use hardcoded values, would refenence DB to ensure
		return True
	else:
		return False

def verify_named_user(self):#verify user name provided and is valid; returns true if so and false if not
	try: #verify user name exists
		named_user_id = self.request.GET['id']
	except KeyError:
		return False
	else:
		if named_user_id != 'named_user_1234':#use hardcoded values here, would reference DB to ensure
			return False
		else:
			return True