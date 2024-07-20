from requests_oauthlib import OAuth2Session

client_id = 'lOP4bqI9d5OOTWYIoeDjLFv6xKBu9vU7ppPCMtOs'
client_secret = 'pbkdf2_sha256$720000$LPjqLaK18loBjoDDTzk1EX$Q+/Kl592Yb/li9ja2nJGl9BZW9Hef0s/+rn1rIpcc1w='
authorization_base_url = 'http://localhost:8000/o/authorize/'
token_url = 'http://localhost:8000/o/token/'

# Create an OAuth2Session instance
oauth = OAuth2Session(client_id)

# Step 1: Redirect user to the OAuth provider to get the authorization code
authorization_url, state = oauth.authorization_url(authorization_base_url)
print('Please go to {} and authorize access.'.format(authorization_url))

# Step 2: Get the authorization verifier code from the callback URL
redirect_response = input('Paste the full redirect URL here: ')

# Step 3: Fetch the access token
token = oauth.fetch_token(
    token_url,
    authorization_response=redirect_response,
    client_secret=client_secret
)

# Step 4: Access a protected resource
response = oauth.get('http://localhost:8000/myapp/api/protected/')
print(response.json())
