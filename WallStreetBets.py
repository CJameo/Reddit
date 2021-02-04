import datetime as dt
from psaw import PushshiftAPI

api = PushshiftAPI()

start_time = int(dt.datetime(2021, 2, 3).timestamp())

submissions = list(api.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter=['url', 'author', 'title', 'subreddit']))

for s in submissions:
    #print(s.created_utc)
    #print(s.title)
    #print(s.url)           

    words = s.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        print(s.title)