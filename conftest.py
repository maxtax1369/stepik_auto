import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument(f"--lang={user_language}")

    print(f"\nstart {user_language} browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser

    print("\nquit browser..")
    browser.quit()