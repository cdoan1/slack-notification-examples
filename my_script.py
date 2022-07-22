import requests
import json

def post_message_to_slack(text, blocks = None):
    return requests.post('https://example_endpoint.com', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'icon_emoji': slack_icon_emoji,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()

slack_info = 'There are *{}* double images detected for *{}* products. Please check the <https://{}.s3-eu-west-1.amazonaws.com/{}|Double Images Monitor>.'.format(
  123, 123, "foobar", "barfoo")

post_message_to_slack(slack_info)
