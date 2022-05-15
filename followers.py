import tweepy
import os
import time
from datetime import datetime


def get_user_id(username: str):
    # Get a user
    # TODO validate that the user name does not have @, if does, remove it
    bearer_token = os.environ.get("twitter_bearer")
    client = tweepy.Client(bearer_token)
    response = client.get_user(username=username)
    return response.data.id


def retrieve_followers(twitter_user: str, pagination: str):
    # getting the followers and add them into a file to use them later
    followers_list = []
    bearer_token = os.environ.get("twitter_bearer")
    client = tweepy.Client(bearer_token)
    the_user = get_user_id(twitter_user)

    try:
        if pagination == "":
            the_mode = "w"
        else:
            the_mode = "a"

        with open("followers.txt", mode=the_mode) as file:
            while pagination != "End":
                if pagination == "":
                    response = client.get_users_followers(the_user, max_results=1000,user_fields=["profile_image_url", "id"])
                else:
                    response = client.get_users_followers(the_user, max_results=1000,pagination_token=pagination,user_fields=["profile_image_url", "id"])
                print(response.meta)

                lista = list(response.meta.keys())
                if lista.count('next_token')>0:
                    pagination = response.meta["next_token"]
                else:
                    pagination="End"

                for follower in response.data:
                    followers_list.append(follower)
                    file.write("id=" + str(follower.id) + ", username=" + str(follower.username) + "\n")
    except (NameError, TypeError) as error:
        print(f"General error..: {error}")
    except tweepy.errors.TooManyRequests as error_message:
        print(f"tweepy error: {error_message} ")
    except file.errors as error_message:
        print(f"file error: {error_message} closing followers file")
    else:
        print(f"the followers file was created successfully")
    finally:
        file.close()
        return pagination
        # print(len(followers_list))
        # print(followers_list)


def retrieve_followed(twitter_user: str, retrieve_status: bool):
    # getting the followers and add them into a file to use them later
    followed_list = []
    bearer_token = os.environ.get("twitter_bearer")
    client = tweepy.Client(bearer_token)

    with open("follows.txt", mode="w") as file:
        for response in tweepy.Paginator(client.get_users_following, get_user_id(twitter_user),
                                         user_fields=["profile_image_url", "id"]):
            for follows in response.data:
                followed_list.append(follows)
                file.write("id=" + str(follows.id) + ", username=" + str(follows.username) + "\n")
    file.close()
    #print(len(followed_list))
    #print(followed_list)


if __name__ == '__main__':
    print("retrieve users...")
    more_users = retrieve_followers("CarlosRangelM78","")

    while more_users != "End":
        now=datetime.now()
        print(f'Pause to wait for twitter license {now.strftime("%H:%M:%S")}')
        time.sleep(60)
        now = datetime.now()
        print(f'Continuing retrieving  {now.strftime("%H:%M:%S")}')
        more_users = retrieve_followers("CarlosRangelM78", more_users)

