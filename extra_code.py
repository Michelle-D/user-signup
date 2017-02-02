USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile("^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)



    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify_password')
        email = self.request.get('email')

        params = dict(username = username,
                        email = email)

        if not valid_username:
            params['error_username'] = "That's not a valid username"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)
            have_error = True

        if not valid_password:
            params['error_password'] = "That wasn't a valid password"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)
            have_error = True
        elif password != verify_password:
            params['error_verify'] = "Your passwords didn't match"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)
            have_error = True

        if not valid_email:
            params['error_email'] = "That's not a valid email"
            error_escaped = cgi.escape(error, quote=True)
            self.redirect("/?error=" + error_escaped)
            have_error = True
