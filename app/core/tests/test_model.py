from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@email.com"
        password = "testpassword123321"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that new users email is normalized"""
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(
             email=email,
             password="test34234234"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Tests creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test1234")

    def test_create_new_superuser(self):
        """Tests creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email="test@email.com",
            password="test2342343"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)