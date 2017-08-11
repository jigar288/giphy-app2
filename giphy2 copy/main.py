#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

import jinja2
import os
import webapp2
import json
import urllib2
import urllib


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/giphy.html")
        # render_data = {
        # 'image_url': 'http://i3.kym-cdn.com/photos/images/facebook/000/234/739/fa5.jpg'
        # }
        query = self.request.get("search") or "puppies"
        index = int(self.request.get("index") or "1")

        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': query, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        request_url = base_url + urllib.urlencode(url_params)
        giphy_response = urllib2.urlopen(request_url)
            # "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_json = giphy_response.read()
        giphy_data = json.loads(giphy_json)
        giphy_url = giphy_data['data'][index]['images']['original']['url']
        render_data = {}
        render_data['image_url'] = giphy_url
        self.response.write(template.render(render_data))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
