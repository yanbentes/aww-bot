import os
import discord
import requests
from keep_alive import keep_alive

client = discord.Client()
discord_token = os.environ['token']

reddit_api_id = os.environ['client_id']
api_secret_key = os.environ['secret_key']

reddit_password = os.environ['password']
reddit_username = 'moonlight-boy-238'

auth = requests.auth.HTTPBasicAuth(reddit_api_id, api_secret_key)

data = {'grant_type': 'password',
        'username': reddit_username,
        'password': reddit_password}

headers = {'User-Agent' : 'awwAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

reddit_token = res.json()['access_token']
headers['Authorization'] = f'bearer {reddit_token}'

@client.event
async def on_ready():
	print("{0.user}".format(client))

@client.event
async def on_message(message):
	if message.content.startswith("aww"):
		res = requests.get('https://oauth.reddit.com/r/aww/random', headers=headers)
		image_url = res.json()[0]['data']['children'][0]['data']['url']
		await message.channel.send(image_url)

keep_alive()
client.run(discord_token)