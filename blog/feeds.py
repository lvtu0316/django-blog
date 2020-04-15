from django.contrib.syndication.views import Feed

from blog.models import Post


class PostsRssFeed(Feed):
    title = '我的blog'
    link = '/'
    description = '个人博客'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return "[%s] %s" % (item.category, item.title)

    def item_description(self, item):
        return item.body_html
