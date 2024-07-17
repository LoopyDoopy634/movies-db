from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from .views import fetch_commits

class LatestCommitsFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "Latest Commits"
    link = "/rss/"
    description = "Updates on the latest commits to the repository."

    def items(self):
        commits = fetch_commits()
        return commits[:10]  # Limit to latest 10 commits

    def item_title(self, item):
        return item['commit']['message']

    def item_description(self, item):
        return f"Commit by {item['commit']['author']['name']} on {item['commit']['author']['date']}"

    def item_link(self, item):
        return item['html_url']
