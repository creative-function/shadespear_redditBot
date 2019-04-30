import praw
import pdb
import re
import os
import random

# Shakespearean Insults
#Shadespeare Bot

bot_username = 'Shadespear_bot'

shakes_a = \
[
    "artless,",
    "bawdy,",
    "beslubbering,",
    "bootless,",
    "churllish,"
]

shakes_b = \
[
    "basecourt,",
    "bat-fowling,",
    "beef-witted,",
    "beetle-headed,", 
    "boil-brained,"
]

shakes_c = \
[
    "apple-john",
    "baggage",
    "barnacle",
    "bladder",
    "pig-tongue"
]



# Create the Reddit instance and log in
reddit = praw.Reddit('bot1')

#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Create a list of posts replied to

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# Or load the list of posts we have replied to
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


# Pull the hottest 10 entries from a subreddit of your choosing
subreddit = reddit.subreddit('testingground4bots')

for submission in subreddit.hot(limit=10):
    # Make sure you didn't already reply to this post
    if submission.id not in posts_replied_to:

        # search for "keyword", in the submission title, Not case sensitive
        if re.search("shakesbot.6", submission.selftext, re.IGNORECASE):
            # tell me the title of the post
            print("Title: ", submission.selftext)
            # Reply
            submission.reply("test 20: I feel attacked. Shadespeare-bot.8 or roboChris, please help!")
            print("sentry Bot replying to : ", submission.selftext)
            print("---------------------------------\n")

            # Store id in list
            posts_replied_to.append(submission.id)







for comment in subreddit.stream.comments():

    # Make sure you didn't already reply to this comment
    if comment.id not in posts_replied_to:

        # Not case sensitive
        if re.search("Shadespeare-bot.8", comment.body, re.IGNORECASE):
            shakes_reply = "test 23-reply: William Shadespeare says: how dare you hurt my friend, you " + " ".join([random.choice(shakes_a),random.choice(shakes_b),random.choice(shakes_c),]) + "!"
            comment.reply(shakes_reply)
            print ('-------attack bot replying to call for help:')
            print("comment: ", comment.body)
            print(shakes_reply)
            print("---------------------------------\n")

            # Store id in list
            posts_replied_to.append(comment.id)


# Write updated list to file
with open("posts_replied_to.txt", "w") as f:
    print ('write posts_replied_to file to hard drive')
    for id in posts_replied_to:
        print ('found an ID to write!')
        print (id)
        f.write(id + "\n")



       

