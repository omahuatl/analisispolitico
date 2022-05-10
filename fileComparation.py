txt_file = open("followers.txt", "r")
followers_list = txt_file.readlines()
#print(followers_list)
txt_file.close()

txt_file = open("follows.txt", "r")
follows_list = txt_file.readlines()
#print(follows_list)
txt_file.close()




#los que si estan
match_list_YES= set(follows_list).intersection(followers_list)
#los que no estan
match_list_NO= set(follows_list).symmetric_difference(followers_list)
print("Los que SI te siguen: \n")
print(match_list_YES)
print("Los que NO te siguen: \n")
print(match_list_NO)


with open("traitors.txt",mode="w") as file:
    for nel in match_list_NO:
        file.write(nel)
file.close()