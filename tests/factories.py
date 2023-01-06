import factory
from apps.post.models import ArticleModel, CategoryModel
from django.db.models.signals import post_save
from faker import Factory as FakeFactory
# from faker import factory
# import factory

faker = FakeFactory.create()


@factory.django.mute_signals(post_save)
class CategoryModelFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())

    class Meta:
        model = CategoryModel


@factory.django.mute_signals(post_save)
class ArticleModelFactory(factory.django.DjangoModelFactory):
    author_name = factory.LazyAttribute(lambda x: faker.name)
    title = factory.LazyAttribute(lambda x: faker.sentence())
    body = factory.LazyAttribute(lambda x: faker.sentence())
    image = factory.LazyAttribute(
        lambda x: faker.file_extension(category='image'))
    category = factory.SubFactory(CategoryModelFactory)
    status = True
    created_at = factory.LazyAttribute(
        lambda x: faker.date_time_this_century())
    updated_at = factory.LazyAttribute(
        lambda x: faker.date_time_this_century())

    class Meta:
        model = ArticleModel
