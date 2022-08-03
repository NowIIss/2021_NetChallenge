import tweepy
import pymysql


def get_keys():
    twitter_auth_keys = {
        "consumer_key": "consumer_key",
        "consumer_secret": "consumer_secret",
        "access_token": "access_token",
        "access_token_secret": "access_token_secret"
    }

    auth_keys = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth_keys.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )

    return auth_keys


def get_msg():
    connect = pymysql.connect(host='host', user='user', password='password', \
                              db='db', charset='charset')
    cur = connect.cursor()

    query = "SELECT * FROM table_name"
    cur.execute(query)
    connect.commit()

    datas = cur.fetchall()

    return datas


def main():
    auth = get_keys()
    api = tweepy.API(auth)

    tweets = get_msg()
    for tweet in tweets:
        status = api.update_status(status=tweet)


if __name__ == "__main__":
    main()