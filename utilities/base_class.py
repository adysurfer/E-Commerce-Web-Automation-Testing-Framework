import pytest
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def perform_actions(self):
        # class used to perform various functions
        action = ActionChains(self.driver)
        return action

    def get_scroll_window(self):
        self.driver.execute_script("window.scrollTo(0, 250)")

    def get_dropdown_by_text(self, select_country, text):

        sel = Select(select_country)
        sel.select_by_visible_text(text)

    def get_logger(self):

        """
        Logging and generating HTML html_reports
        Logs Order:

        Debug
        Info
        Warning
        Error
        Critical

        """

        logger = logging.getLogger()

        # File location
        file_handler = logging.FileHandler('logfile.log')

        # In which format to print
        # format is log.warning("2019-07-07 12:40:14,788 : ERROR :<testfilename>:<testmethodname>: Error message")

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(message)s")
        file_handler.setFormatter(formatter)

        # File Handler Object (Which file to print)
        logger.addHandler(file_handler)

        # Define logs by this hierarchy otherwise if u take warning first  then only below warning logs are displayed
        # skipping debug and info
        # if u want to setup logs hierarchy use setlevel

        logger.setLevel(logging.INFO)

        return logger


