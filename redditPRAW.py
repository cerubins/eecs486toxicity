from IPython import display
import praw

def main():
    reddit = praw.Reddit(client_id='tFCJsxRKCFRRvUXspS8_yw',
                         client_secret='iuPB4OxQHXSxpH5U6wRCqi6XeAvJOA',
                         user_agent='TheNameIsAtlas')
    headlines = set()

    for post in reddit.subreddit('sports').new(limit=None):
        headlines.add(post.title)
        display.clear_output()
        print(headlines)

if __name__ == "__main__":
    main()