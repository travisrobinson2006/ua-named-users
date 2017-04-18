#This script is just to be able to use a browswer to ensure server running;

import webapp2

class default(webapp2.RequestHandler):
	def get(self):
		self.response.write("Congrats: The server is running")