import twitter
import random
import os

auth = twitter.OAuth(consumer_key=os.environ['CONSUMER_KEY'],
consumer_secret=os.environ['CONSUMER_SECRET'],
token=os.environ['CONSUMER_TOKEN'],
token_secret=os.environ['CONSUMER_TOKEN_SECRET'])

t = twitter.Twitter(auth=auth)

words = ['さ','こ','ま','い','そ','じ']
out = ''

for i in range(7):
    rnd = random.randint(0,5)
    out = out + words[rnd]

# print(out)

#ツイートのみ
status=out #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

# #画像付きツイート
# pic=""　#画像を投稿するなら画像のパス
# with open(pic,"rb") as image_file:
#  image_data=image_file.read()
# pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
# id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
# t.statuses.update(status=status,media_ids=",".join([id=img1]))
