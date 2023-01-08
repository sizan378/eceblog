import pytest

@pytest.mark.django_db
def test_category(category_model_factory):
    # print(category_model_factory.title)
    title = category_model_factory.create()
    assert title == title


def test_article(db,article_model_factory):
    # print(article_model_factory.body)
    article = article_model_factory.create()
    assert article == article