#This script contains the API classes for all Named User API calls.
#See https://docs.urbanairship.com/api/ua/#api-named-user-association for details

import webapp2
import verify_request
import json
import response_writer
import data_retriever
import logging

class associate(webapp2.RequestHandler):#associate API; when fully implemented will associate a channel to a particular named user
	def post(self):
		response = {}
		response['ok'] = True

		if verify_request.verify_app_credential(self) != True:#verify valid user
			response = response_writer.generate_response(401)
			self.response.set_status(response['error_code'])

		elif 'application/vnd.urbanairship+json' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif 'version=3' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif 'application/json' not in self.request.headers['Content-type']:#include clause to check response[ok] because we don't want to override previous error messages:
			response = response_writer.generate_response(415)
			self.response.set_status(response['error_code'])
		else:
			try:
				request_data = json.loads(self.request.body)
				#write data handler functions here
			except ValueError:
				response = response_writer.generate_response(400)

		#attach proper response headers
		self.response.headers.add('Content-type','application/json')
		self.response.write(json.dumps(response))

class disassociate(webapp2.RequestHandler):#disasocciate API; when fully implemented will disassocate a channel from a particular user
	def post(self):
		response = {}
		response['ok'] = True

		if verify_request.verify_app_credential(self) != True:#verify valid user
			response = response_writer.generate_response(401)
			self.response.set_status(response['error_code'])

		elif 'application/vnd.urbanairship+json' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif 'version=3' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif 'application/json' not in self.request.headers['Content-type']:#include clause to check response[ok] because we don't want to override previous error messages:
			response = response_writer.generate_response(415)
			self.response.set_status(response['error_code'])
		else:
			try:
				request_data = json.loads(self.request.body)
				#write data handler functions here
			except ValueError:
				response = response_writer.generate_response(400)

		#attach proper response headers
		self.response.headers.add('Content-type','application/json')
		self.response.write(json.dumps(response))

class lookup(webapp2.RequestHandler):#lookup API, allows looking up of a particular named user-currently only one user available, hardcode
	def get(self, **kwargs):
		response = {}
		response['ok'] = True

		if verify_request.verify_app_credential(self) != True:#verify valid user
			response = response_writer.generate_response(401)
			self.response.set_status(response['error_code'])

		elif 'application/vnd.urbanairship+json' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif 'version=3' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif verify_request.verify_named_user(self) != True:#verify named user provided and is valid
			response = response_writer.generate_response(404)
			self.response.set_status(response['error_code'])
		else:#no issues, dump named user into json and attach to response
			named_user = json.loads(data_retriever.named_user_retriever(self))
			response['named_user'] = named_user

		#attach proper response headers
		self.response.headers.add('Content-type','application/json')
		self.response.headers.add('Data-Attribute','named_users')
		self.response.headers.add('Link','To the Past')

		self.response.write(json.dumps(response))

class listing(webapp2.RequestHandler):#listing API, lists all named users, currently only one and is hardcoded
	def get(self):
		response = {}#will be dumped as JSON object
		response['ok'] = True

		if verify_request.verify_app_credential(self) != True:#verify valid user
			response = response_writer.generate_response(401)
			self.response.set_status(response['error_code'])

		elif 'application/vnd.urbanairship+json' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		elif 'version=3' not in self.request.headers['accept']:#include clause to check response[ok] because we don't want to override previous error messages
			response = response_writer.generate_response(406)
			self.response.set_status(response['error_code'])

		listing = json.loads(data_retriever.listing_retriever(self))#gather listing as JSON list, dump into response
		response['listing'] = listing

		#attach proper response headers
		self.response.headers.add('Content-type','application/json')
		self.response.headers.add('Data-Attribute','named_users')
		self.response.headers.add('Link','The Adventure Of')

		self.response.write(json.dumps(response))

