# %%
from twikit import Client
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.


def get_tweets(name):
    client = Client('en-US')
    client.login(
        auth_info_1=os.environ['T_USER'] ,
        auth_info_2=os.environ['T_EMAIL'],
        password=os.environ['T_PASSWORD']
    )

    user = client.get_user_by_screen_name(name)
    tweets = client.get_user_tweets(user.id, 'Tweets')
    
    client.logout()
    
    return tweets


if __name__ == "__main__":
    tweets = get_tweets('time')
    for tweet in tweets[:5]:
        print(tweet.created_at_datetime,'\t', tweet.text)