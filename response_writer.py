#Writes response messages; currently only used to write messages in event of error code

import json
import logging

error_message_400 = 'Please provide a valid request'
error_message_401 = 'Invalid application key or application secret'
error_message_404 = 'Please us a valid Named User ID'
error_message_406 = 'Can only return response of form application/vnd.urbanairship+json with API version=3;'
error_message_415 = 'Please Send Content as JSON'

def generate_response(error_code):
	response = {}
	if error_code < 400:
		response['operation_id'] = 1#placeholder

	else:
		response['error_code'] = error_code
		response['ok'] = False
		response['operation_id'] = 1#placeholder; in production would retrieve actual op ID
		response['details'] = {}#will contain information according to Error Object docs-see https://docs.urbanairship.com/api/ua/#error-object
		response['details']['path'] = 'this is a path' #hardcoded path
		response['details']['location'] = {}
		response['details']['location']['line'] = 11
		response['details']['location']['column'] = 11

		if error_code == 400:
			response['error'] = error_message_400
			response['details']['error'] = error_message_400
		elif error_code == 401:
			response['error'] = error_message_401
			response['details']['error'] = error_message_401
		elif error_code == 404:
			response['error'] = error_message_404
			response['details']['error'] = error_message_404
		elif error_code == 406:
			response['error'] = error_message_406
			response['details']['error'] = error_message_406
		elif error_code == 415:
			response['error'] = error_message_415
			response['details']['error'] = error_message_415

	return response

