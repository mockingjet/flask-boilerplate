import pytest
from flask import url_for


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
        assert article_data['tags'] == []
        assert 'createdAt' in article_data

    def test_get_articles(self, client):
        resp = client.get(url_for('article.get_articles'))
        articles_data = resp.get_json()['data']['articles']

        assert len(articles_data) == 1

    def test_put_article(self, client):
        json_data = {
            "title": "updated test title",
            "description": "updated test decription",
            "body": "updated test body",
        }
        resp = client.put(
            url_for('article.put_article', _id=1), json=json_data)
        article_data = resp.get_json()['data']['article']

        assert article_data["articleId"] == 1
        assert 'updated' in article_data["title"]
        assert 'updated' in article_data["description"]
        assert 'updated' in article_data["body"]
