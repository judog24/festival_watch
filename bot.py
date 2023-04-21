from mastodon import Mastodon
from datetime import datetime

mastodon = Mastodon(access_token="festival_usercred.secret")

#mastodon.status_post(status='Test', scheduled_at=datetime.fromtimestamp(1682088621.0))