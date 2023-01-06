import pytest
from pytest_factoryboy import register
from tests.factories import CategoryModelFactory, ArticleModelFactory


register(ArticleModelFactory)
register(CategoryModelFactory)
