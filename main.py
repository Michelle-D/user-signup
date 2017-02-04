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
import logging

logger = logging.getLogger(__name__)

user_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    logger.warning(str(username and user_RE.match(username)))
    return username and user_RE.match(username)

password_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    logger.warning(str(password and password_RE.match(password)))
    return password and password_RE.match(password)

email_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    logger.warning(str(not email or email_RE.match(email)))
    return not email or email_RE.match(email)


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
                        <input type="password" name="password" value=""/>
                    </td>
                <tr>
            </table>
            <table>
                <tr>
                    <td class="label">
                        Verify password
                    </td>
                    <td>
                        <input type="password" name="verify_password" value=""/>
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

class Signup(webapp2.RequestHandler):
    def get(self):
        self.response.write(content)

    def post (self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify_password')
        email = self.request.get('email')

        if not valid_username(username):
            error = "That's not a valid username"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)

        if not valid_password(password):
            error = "That wasn't a valid password"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)
        elif password!=verify:
            error = "Your passwords didn't match"

        if not valid_email(email):
            logger.warning("email")
            error = "That's not a valid email"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)

class Welcome(webapp2.RequestHandler):
    """ Handles requests coming in to welcome screen
    """
    def get(self):
        username = self.request.get('username')
        if valid_username(self):
            sentence = "Welcome, " + username + "!"
            welcome_content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(welcome_content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
