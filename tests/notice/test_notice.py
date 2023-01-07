import pytest
import factory
from faker import Faker
from apps.notice.models import NoticeModel

fake = Faker()


class NoticeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NoticeModel

    title = fake.name()
    notice = fake.sentence()
    created_at = fake.date_time_this_century()
    updated_at = fake.date_time_this_century()



def test_function_fixture(module_fixture):
  assert module_fixture == 2