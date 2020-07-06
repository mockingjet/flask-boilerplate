from .modules.articles.models import Article, Category, Tag


def create_articles():
    c1 = Category('f2e').save()
    c2 = Category('devops').save()

    t1 = Tag('js', c1).save()
    t2 = Tag('docker', c2).save()

    a1 = Article(title="advanced javascript",
                 description="the best way to improve your js skills",
                 body="...",
                 extended_tags=[t1]).save()

    a2 = Article(title="docker tutorial",
                 description="get to know how to containerized your app",
                 body="...",
                 extended_tags=[t2]).save()
