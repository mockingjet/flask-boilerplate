import pytest
from flask import url_for


@pytest.fixture(autouse=True)
def seed_article(client):
    json_data = {
        "title": "title",
        "description": "decription",
        "body": "body",
    }
    client.post(url_for('article.post_articles'), json=json_data)


class TestArticleViews:

    def test_get_articles_by_id(self, client):
        resp = client.get(url_for('article.get_article', _id=1))
        article_data = resp.get_json()['data']['article']

        assert article_data['articleId'] == 1

    def test_post_articles(self, client):
        json_data = {
            "title": "test title",
            "description": "test decription",
            "body": "test body",
        }
        resp = client.post(url_for('article.post_articles'), json=json_data)
        article_data = resp.get_json()['data']['article']

        assert article_data['articleId'] == 2
        assert article_data['tags'] == []
        assert 'createdAt' in article_data

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
