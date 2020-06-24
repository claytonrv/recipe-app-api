import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestModels:
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = "test@ytotech.com"
        password = "pass123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        assert get_user_model().objects.all().count() == 1
        assert user.email == email
        assert user.check_password(password)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@YTOSYSTEMAS.COM"
        user = get_user_model().objects.create_user(
            email=email, password="1234"
        )

        assert user.email == email.lower()

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with pytest.raises(ValueError):
            get_user_model().objects.create_user(
                email=None, password="1234"
            )

    def test_create_super_user(self):
        """Test creating a new super user is successfull"""
        user = get_user_model().objects.create_superuser(
            email="clayton@email.com", password="1234"
        )
        assert user.is_superuser
        assert user.is_staff
