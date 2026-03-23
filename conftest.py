import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language: ru, en, es, fr etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    user_language = request.config.getoption("language")

    driver = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = ChromeOptions()
        options.add_experimental_option(
            'prefs',
            {'intl.accept_languages': user_language}
        )

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield driver

    print("\nquit browser..")
    driver.quit()