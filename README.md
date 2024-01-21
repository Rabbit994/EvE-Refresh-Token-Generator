# EvE-Refresh-Token-Generator

This is easy flask app to create Refresh Tokens for Preston.

Setup Python with venv
Go to: https://developers.eveonline.com/applications and login to your EvE Account. 
Create a new application or use existing application. Make sure callback url is http://localhost:5000 unless you modify flask path.
Copy .env-example to .env and fill in the values.
Run the Flask Application and go to http://localhost:5000, it will redirect you to EvE Online Site to go through application flow.
It will take access token and generate a refresh token and display it for you. You can then use it in your app.