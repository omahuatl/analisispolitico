import tweepy
import os

bearer_token= os.environ.get("twitter_bearer")
client = tweepy.Client(bearer_token)



#Get a user
the_user="CarlosRangelM78"
response=client.get_user(username=the_user)
user_id=response.data.id

#print(response.meta)
#print(response.data)

#getting the followers and add them into a file to use them later
followers_list=[]
with open("followers.txt",mode="w") as file:
    for response in tweepy.Paginator(client.get_users_followers,user_id, user_fields=["profile_image_url","id"]):
        for follower in response.data:
            followers_list.append(follower)
            file.write("id="+str(follower.id)+", username="+str(follower.username)+"\n")
file.close()
print(len(followers_list))
print(followers_list)


#getting the followers and add them into a file to use them later
follows_list=[]
with open("follows.txt",mode="w") as file:
    for response in tweepy.Paginator(client.get_users_following,user_id, user_fields=["profile_image_url","id"]):
        for follows in response.data:
            follows_list.append(follows)
            file.write("id="+str(follows.id)+", username="+str(follows.username)+"\n")
file.close()
print(len(follows_list))
print(follows_list)
