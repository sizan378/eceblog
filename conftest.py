from pytest_factoryboy import register
from tests.factories import CategoryModelFactory, ArticleModelFactory, NoticeFactory, UserProfileFactory

register(ArticleModelFactory)
register(CategoryModelFactory)
register(NoticeFactory)
register(UserProfileFactory)
