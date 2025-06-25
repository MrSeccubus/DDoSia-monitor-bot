# DDosia Monitor

## Setup

### Install requirements

```bash
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Get the telegram group invite link

[Google](https://www.google.com/search?q=inurl%3At.me+ddosia+informer) for `inurl:t.me ddosia informer`
Add the group invite link in config.yml

### Telegram API key

Make sure you have a telegram account
Go to https://my.telegram.org
Click API development tools and create a new application.
Note down the api_id and api_hash.
Put them in `config.yml`

###  Configure Slack access

[Read the fine manual](https://api.slack.com/messaging/webhooks).
Add the webhook to the config.