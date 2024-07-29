from django.test import TestCase
from django.urls import reverse
import pytest
from users.models import User

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"



def test_integration():
    user=User(
        first_name = "Test Passed",
        last_name = "pass",
        email = "pass"
    )
    assert user.first_name == "Test Passed"