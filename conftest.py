from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()