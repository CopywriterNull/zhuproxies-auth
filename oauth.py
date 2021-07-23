class Oauth(object):
  client_id = "868000731511283742"
  client_secret = "Gsp0OY1TIUoyEjRFLpPK4Doe5dWswl4w"
  scope = "identify%20email%20webhook.incoming"
  redirect_uri = "https://zhu-discord-oauth.herokuapp.com/"
  discord_login_url = "https://discord.com/api/oauth2/authorize?client_id={}&redirect_uri=https%3A%2F%2Fzhu-discord-oauth.herokuapp.com%2F&response_type=code&scope={}".format(client_id,scope)
  
  
