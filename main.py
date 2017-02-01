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
import cgi
import re


class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
    """

    def get(self):

#        edit_header = "<h2>Signup</h2>"

        signup_page = """
        <form action="/signup" method="post">
            <table>
                <tr>
                    <td class="label">
                        Username
                    </td>
                    <td>
                        <input type="text" name="username"/>
                    <td>
                </tr>
            </table>
            <table>
                <tr>
                    <td class="label">
                        Password
                    </td>
                    <td>
                        <input type="text" name="password"/>
                    </td>
                <tr>
            </table>
            <table>
                <tr>
                    <td class="label">
                        Verify password
                    </td>
                    <td>
                        <input type="text" name="verify_password"/>
                    </td>
                </tr>
            </table>
            <table>
                <tr>
                    <td class="label">
                        Email (optional)
                    </td>
                    <td>
                        <input type="text" name="email"/>
                    </td>
                <tr>
            </table>
            <input type="submit" value="Submit"/>
        </form>
        """
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        main_content = signup_page + error_element
        content = page_header + main_content + page_footer
        self.response.write(content)

class Welcome(webapp2.RequestHandler):
    """ Handles requests coming in to welcome screen
    """
    def post(self):

#        def valid_username(username):
 #       ("^[a-zA-Z0-9_-]{3,20}$")
#            error_escaped = cgi.escape(error, quote=True)
#            self.redirect("/?error=" + error_escaped)
        valid_username = re.match("^[a-zA-Z0-9_-]{3,20}$", username)
        if not valid_username:
            error = "That's not a valid username".format(new_movie)
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)

        valid_password = re.match("^.{3,20}$", password)
        if not valid_password:
            error = "That wasn't a valid password".format(new_movie)
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)

        valid_email = re.match("^[\S]+@[\S]+.[\S]+$", email)
        if not valid_email:
            error = "That's not a valid email".format(new_movie)
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)


#        def valid_password(password):
#            ("^.{3,20}$"), password)
#            error_escaped = cgi.escape(error, quote=True)
#            self.redirect("/?error=" + error_escaped)

#        def verify_password(password):
            #is this the same as password
#            error_escaped = cgi.escape(error, quote=True)
#            self.redirect("/?error=" + error_escaped)

#        def valid_email(email):
#            ( "^[\S]+@[\S]+.[\S]+$")
#            error_escaped = cgi.escape(error, quote=True)
#            self.redirect("/?error=" + error_escaped)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
