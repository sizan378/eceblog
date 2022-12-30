from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):

    def test_create_user(self):
        User = get_user_model
        user = User.objects.create_user(email='sizan@mail.com', password='1234')
        self.assertEqual(user.email,'sizan@mail.com')
        self.assertEqual(user.is_active,True)
        self.assertEqual(user.is_staff,False)
        self.assertFalse(user.is_superuser)

        try:
            # in case of AbstractUser option username is None
            # in case of AbstractBaseUser option username is dose not exist
            self.assertIsNone(user.username)
        except:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="1234")

        
    def test_create_superuser(self):
        User = get_user_model
        admin_user = User.objects.create_superuser(email='super@mail.com', password='1234')
        self.assertEqual(admin_user.email,'super@mail.com')
        self.assertEqual(admin_user.is_active,True)
        self.assertEqual(admin_user.is_staff,True)
        self.assertEqual(admin_user.is_superuser,True)
        
        try:
            self.assertIsNone(admin_user.username)
        except:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@mail.com',
                password='1234',
                is_superuser=False
            )
        
