import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.fixture(autouse=True)
def admin_user(client):
    admin_user = get_user_model().objects.create_superuser(
        email='admin@email.com',
        password='1234'
    )
    client.force_login(admin_user)


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        email='user@email.com',
        password='1234',
        name='Test user'
    )


@pytest.mark.django_db
class TestAdminUser:

    def test_user_listed(self, client, user):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = client.get(url)

        assert user.name in str(res.content)
        assert user.email in str(res.content)

    def test_user_change_page(self, user, client):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[user.id])
        res = client.get(url)

        assert res.status_code == 200

    def test_create_user_page(self, client):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = client.get(url)

        assert res.status_code == 200
