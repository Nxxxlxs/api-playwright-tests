import pytest
from playwright.sync_api import sync_playwright

from api.clients.users_client import UsersClient



@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com"
        )
        yield context
        context.dispose()


@pytest.fixture
def users(api_context):
    return UsersClient(api_context)
