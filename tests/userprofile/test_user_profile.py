import pytest


@pytest.mark.django_db
def test_user_profile(user_profile_factory):
    user_profile = user_profile_factory.create()
    print(user_profile.first_name + " " + user_profile.last_name)
    assert user_profile == user_profile