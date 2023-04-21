import os
from mastodon import Mastodon
from datetime import datetime

token = os.environ['FESTIVAL_WATCH_BOT']
secret_api_base_url = os.environ['API_BASE_URL']
secret_client_id = os.environ['CLIENT_ID']
secret_client_secret = os.environ['CLIENT_SECRET']
secret_access_token = os.environ['ACCESS_TOKEN']

mastodon = Mastodon(
    api_base_url = secret_api_base_url,
    client_id = secret_client_id,
    client_secret = secret_client_secret,
    access_token = secret_access_token)

mastodon.status_post(status='Test', scheduled_at=datetime.fromtimestamp(1682088621.0))
