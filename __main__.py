from flask import Flash,request, render_template,redirect,session
from oauth import Oauth

app = Flash(__name__)
@app.route("/",methods = ["get"])
def index():
  return redirect(Oauth.discord_login_url)
  
  
@app.route("/login",methods = ["get"])
def login();
  return "logged in"

if(__name__ == "__main__"):
  app.run(debug=True)

