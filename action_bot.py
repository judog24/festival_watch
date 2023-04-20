import os
from mastodon import Mastodon
from datetime import datetime

token = os.environ['FESTIVAL_WATCH_BOT']
mastodon = Mastodon(access_token=token)

mastodon.status_post(status='Test', scheduled_at=datetime.fromtimestamp(1682088621.0))