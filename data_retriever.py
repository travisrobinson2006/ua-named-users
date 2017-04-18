#This script is here to retrieve named user and listing data
#Currently all values are hard coded and will only return those values

import json

named_user_1234 = {}
named_user_1234['named_user_id'] = 'named_user_1234'
named_user_1234['tags'] = {}
named_user_1234['tags']['crm'] = ['tag1','tag2']
named_user_1234['channels'] = []
named_user_1234['channels'].append({'channel_id':'ABCD','device_type':'ios','installed':True,'opt_in':True,'push_address':'FFFF','created':'2013-08-08T20:41:06','last_registration':'2014-05-01T18:00:27','alias':'xxxx'})

def named_user_retriever(self):#will only receive valid named users
	named_user_id = self.request.GET['id']

	if named_user_id == 'named_user_1234':#hardcode named user data
		named_user = named_user_1234	

		return json.dumps(named_user)

def listing_retriever(self):#retrieves listing of named users//currently only the hardcoded one
	listing = {}
	listing['next_page'] = 'https://go.urbanairship.com/api/named_users?start=user-1234'
	listing['named_users'] = []
	listing['named_users'].append(named_user_1234)

	return json.dumps(listing)