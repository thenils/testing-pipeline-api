from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test cearing new user with email successfully"""
        email = "test@gmail.com"
        password = "7990nilesh"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """testing for nirmalizing email for new user"""

        email = "testlondon@Myapp.com"

        user = get_user_model().objects.create_user(email, '7990nuilesh')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """raise error when user try to create account without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '7990nuilesh')

    def test_create_new_staffuser(self):
        """test creating new user with super user permisssions"""

        user = get_user_model().objects.create_staffuser(
            'test@suoperuser.com', '7990nilesh'
        )

        self.assertTrue(user.is_staff)

    def test_create_new_superuser(self):
        """test creating new user with super user permisssions"""

        user = get_user_model().objects.create_superuser(
            'test@suoperuser.com', '7990nilesh'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
