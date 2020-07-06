import pytest
from flask import url_for


# @pytest.mark.skip
class TestArticleViews:

    def test_post_articles(self, client):
        json_data = {
            "title": "test title",
            "description": "test decription",
            "body": "test body",
        }
        resp = client.post(url_for('article.post_articles'), json=json_data)
        article_data = resp.get_json()['data']['article']
        assert article_data['articleId'] == 1

    def test_get_articles(self, client):
        resp = client.get(url_for('article.get_articles'))
        articles_data = resp.get_json()['data']['articles']
        assert len(articles_data) == 1
