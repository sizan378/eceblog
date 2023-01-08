import factory
from apps.post.models import ArticleModel, CategoryModel
from apps.notice.models import NoticeModel
from apps.userprofile.models import UserProfileModel
from django.db.models.signals import post_save
from faker import Factory as FakeFactory

faker = FakeFactory.create()


@factory.django.mute_signals(post_save)
class CategoryModelFactory(factory.django.DjangoModelFactory):
    title = faker.sentence()

    class Meta:
        model = CategoryModel


@factory.django.mute_signals(post_save)
class ArticleModelFactory(factory.django.DjangoModelFactory):
    author_name = faker.name()
    title = faker.sentence()
    body = faker.sentence()
    image = faker.file_extension(category='image')
    category = factory.SubFactory(CategoryModelFactory)
    status = True
    created_at = faker.date_time_this_century()
    updated_at = faker.date_time_this_century()

    class Meta:
        model = ArticleModel


class NoticeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NoticeModel

    title = faker.name()
    notice = faker.sentence()
    created_at = faker.date_time_this_century()
    updated_at = faker.date_time_this_century()


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfileModel

    first_name = faker.name()
    last_name = faker.name()
    email = faker.email()
    phone_number = '01234567894'
    address = faker.address()
    university = faker.word()
    department = faker.word()
    date_of_birth = faker.date_of_birth()
    country = faker.country()
    religion = 'islam'
