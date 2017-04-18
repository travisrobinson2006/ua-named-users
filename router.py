# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import default


app = webapp2.WSGIApplication([], debug=True)

app.router.add(webapp2.Route(r'/api/named_users/associate',handler='named_users.associate',name='associate'))
app.router.add(webapp2.Route(r'/api/named_users/disassociate',handler='named_users.disassociate',name='disassociate'))
app.router.add(webapp2.Route(r'/api/named_users/',handler='named_users.lookup',name='lookup'))
app.router.add(webapp2.Route(r'/api/named_users',handler='named_users.listing',name='listing'))
app.router.add(webapp2.Route(r'/',handler='default.default',name='default'))





