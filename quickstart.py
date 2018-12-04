"""
This template is written by @the-unknown
 What does this quickstart script aim to do?
- This is my template which includes the new QS system.
  It includes a randomizer for my hashtags... with every run, it selects 10 random hashtags from the list.
 NOTES:
- I am using the bot headless on my vServer and proxy into a Raspberry PI I have at home, to always use my home IP to connect to Instagram.
  In my comments, I always ask for feedback, use more than 4 words and always have emojis.
  My comments work very well, as I get a lot of feedback to my posts and profile visits since I use this tactic.
   As I target mainly active accounts, I use two unfollow methods.
  The first will unfollow everyone who did not follow back within 12h.
  The second one will unfollow the followers within 24h.
"""
# !/usr/bin/python2.7
import random
from instapy import InstaPy
from instapy.util import smart_run
for i in range (10):
    print("session nubmber: " + str(i))
    # get a session!
    session = InstaPy(username='nirhemo',
                  password='Tal5304',
                  headless_browser=True)

    # let's go! :>
    with smart_run(session):
        hashtags = ['love', 'instagood', 'photooftheday', 'fashion', 'beautiful', 'happy','cute', 'tbt', 'like4like',
                    'followme', 'picoftheday','follow', 'me','selfie', 'summer','art','instadaily','friends',
                    'repost','nature']

        random.shuffle(hashtags)
        my_hashtags = hashtags[:10]
        # general settingsx`
        session.set_dont_like(['sad', 'rain', 'depression'])
        session.set_do_follow(enabled=True, percentage=40, times=1)
        session.set_do_comment(enabled=True, percentage=30)
        session.set_comments([u'What an amazing shot! :heart_eyes: What do you think of my recent shot?',
                              u'What an amazing shot! :heart_eyes: I think you might also like mine. :wink:',
                              u'Wonderful!! :heart_eyes: Would be awesome if you would checkout my photos as well!',
                              u'Wonderful!! :heart_eyes: I would be honored if you would checkout my images and tell me what you think. :wink:',
                              u'This is awesome!! :heart_eyes: Any feedback for my photos? :wink:',
                              u'This is awesome!! :heart_eyes:  maybe you like my photos, too? :wink:',
                              u'I really like the way you captured this. I bet you like my photos, too :wink:',
                              u'I really like the way you captured this. If you have time, check out my photos, too. I bet you will like them. :wink:',
                              u'Great capture!! :smiley: Any feedback for my recent shot? :wink:',
                              u'Great capture!! :smiley: :thumbsup: What do you think of my recent photo?',
                              u'Awesome shot !!!, Come see my pics, and follow me :wink:'],

                             media='Photo')
        session.set_do_like(True, percentage=70)
        session.set_delimit_liking(enabled=True, max=100, min=0)
        session.set_delimit_commenting(enabled=True, max=20, min=0)
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=3000,
                                        max_following=2000,
                                        min_followers=100,
                                        min_following=50)
        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "follows"], sleepyhead=True,
                                     stochastic_flow=True, notify_me=True,
                                     peak_likes=(100, 1000),
                                     peak_comments=(21, 250),
                                     peak_follows=(200, None))
        session.set_user_interact(amount=1, randomize=False, percentage=40)

        # activity



        session.like_by_tags(my_hashtags, amount=100, media=None)

        session.unfollow_users(amount=500, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=24 * 60 * 60,
                               sleep_delay=501)
        session.unfollow_users(amount=300, InstapyFollowed=(True, "nonfollowers"), style="FIFO",
                               unfollow_after=60 *60*12, sleep_delay=501)

