from jinja2 import TemplateRuntimeError
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser")
        return driver
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching firefox browser")
        return driver
    else:
        driver=webdriver.Ie()
        return driver

def pytest_addoption(parser):  #This will get the value from CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption("--browser")


########################## PyTest HTML Reports ###################

#it is hook for adding environment info to HTML Report
def pytest_configure(config):
    metadata = getattr(config,'_metadata',None)
    if metadata is not None:
        metadata['Project Name'] = 'nop Commerce'
        metadata['Module Name'] = 'Customers'
        metadata['Tester'] = 'Sindhu'
    # config.metadata['Project Name'] = 'nop Commerce'
    # config.metadata['Module Name'] = 'Customers'
    # config.metadata['Tester'] =  'Sindhu'

#it is hook for delete/modify Environment info to HTML Report
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
