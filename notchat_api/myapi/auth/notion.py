# Notion auth

import os
from flask_dance import OAuth2ConsumerBlueprint


client_id = os.environ.get("NOTION_CLIENT_ID")
client_secret = os.environ.get("NOTION_CLIENT_SECRET")

assert client_id is not None
assert client_secret is not None

notion_blueprint = OAuth2ConsumerBlueprint(
    "notion",
    __name__,
    client_id=client_id,
    client_secret=client_secret,
    base_url="https://api.notion.com/v1/",
    token_url="https://api.notion.com/v1/oauth/token",
    authorization_url="https://api.notion.com/v1/oauth/authorize",
    redirect_url="http://localhost:5000/auth/notion/callback",
)


