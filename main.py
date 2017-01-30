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
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

import webapp2

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
    """

    def get(self):

        edit_header = "<h2>Signup</h2>"

        # a form for adding new movies
        signup_page = """
        <form action="/signup" method="post">
            <label>
                Username
                <input type="text" name="username"/>
            </label>
            <label>
                Password
                <input type="text" name="password"/>
            </label>
            <label>
                Verify password
                <input type="text" name="verify_password"/>
            </label>
            <label>
                Email (optional)
                <input type="text" name="email"/>
            <input type="submit" value="Submit"/>
        </form>
        """
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        main_content = edit_header + signup_page + error_element
        content = page_header + main_content + page_footer
        self.response.write(content)


        def post(self):
            have_error = False
            username = self.request.get('username')
            password = self.request.get('password')
            verify_password = self.request.get('verify_password')
            email = self.request.get('email')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
