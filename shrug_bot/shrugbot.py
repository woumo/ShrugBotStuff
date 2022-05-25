import tweepy

auth = tweepy.OAuth2AppHandler("QN7ZaI5mVqDdZodqYxB32ze7f", "GHSJ2sC0dOs3WRVuIi88cewTSCPKbpTdciTHa2bl5X77YGLblc")

api = tweepy.API(auth)

api.update_status("Hello y'all! My name's Shrug!")