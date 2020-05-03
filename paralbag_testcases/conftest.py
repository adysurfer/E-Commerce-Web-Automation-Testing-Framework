import pytest
from selenium import webdriver

# global driver value in assigned here and this is assigned to screenshot
driver = None

# conftest file , the fixtures defined in this file can be used in any py test module of the package by passing
# the method as an argument

"""
Theory : Software test fixtures initialize test functions. They provide a fixed baseline so that tests execute reliably
and produce consistent, repeatable, results. Initialization may setup services, state, or other operating environments.
"""


# To give command line options, Pass different values to a test function, depending on command line options
# Source: https://docs.pytest.org/en/latest/example/simple.html


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action='store', default='chrome'
    )


# scope="class", fixture will just execute once before execution of functions in other file, and wont repeat for
# every function, and after yield part will be execute once after all functions will complete its execution
@pytest.fixture
def setup(request):
    global driver
    # config.getoption is associated with pytest_addoption function
    browser_name = request.config.getoption("browser_name")
    # Chrome
    if browser_name == "chrome":
        # Chrome Options
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("headless")
        # chrome_options.add_argument("ignore-certificate-errors")

        chrome_path = "C:\\Users\\Aditya\\PycharmProjects\\webdrivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

    # Firefox
    elif browser_name == "firefox":

        firefox_path = "C:\\Users\\Aditya\\PycharmProjects\\webdrivers\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefox_path)

    else:
        print("Wrong Browser Selected")

    driver.get("https://parallax-bag4.mybigcommerce.com/")

    # Assigning local driver here to the class driver, it will pass to class driver itself as a class variable
    request.cls.driver = driver

    # post tear down methods will be executed after yield, in the end
    yield
    driver.quit()

# Take Screenshots of the Errors and put them in HTML html_reports
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '\
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)




