import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import sys


class DriverBase:
    """
    This class is responsible for initiating and managing web driver instances
    for different browsers (Chrome, Firefox, and Edge). It uses the
    `webdriver_manager` package to automatically download the appropriate
    driver executables.
    """

    def __init__(self, browser):
        """
        Initializes the browser for automation.

        Args:
            browser (str): The browser name (chrome, firefox, or edge) that
                           specifies which browser to use for automation.
        """
        # Set the selected browser in the environment variable 'driver_to'
        os.environ['driver_to'] = browser
        self.driver_run = os.environ['driver_to']  # Store the browser type for future reference

    def initiate_driver(self, option=None):
        """
        Initializes the web driver based on the selected browser.

        The function attempts to launch the selected browser with the given options.
        If no driver is found, it will attempt to download the appropriate driver
        using the `webdriver_manager` package.

        Args:
            option: Additional options for the web driver (e.g., headless mode, custom preferences).

        Returns:
            webdriver instance: A Selenium WebDriver object for the selected browser.

        Raises:
            SystemExit: If the selected browser is unsupported, the program will exit.
        """
        try:
            # If Chrome is selected
            if self.driver_run.lower() == 'chrome':
                # Try to initialize with service (recommended for newer versions)
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

            # If Firefox is selected
            elif self.driver_run.lower() == 'firefox':
                # Try to initialize with service (recommended for newer versions)
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=option)

            # If Edge is selected
            elif self.driver_run.lower() == 'edge':
                # Try to initialize with service (recommended for newer versions)
                driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=option)

            else:
                # If the browser is not supported, print a message and exit
                print(f"Currently {self.driver_run} driver is not supported")
                sys.exit(2)

            return driver  # Return the initialized driver

        except Exception as e:
            # Handle any exceptions that occur during the driver initialization
            print(f"An error occurred while initializing the {self.driver_run} driver: {e}")
            sys.exit(1)  # Exit the program with an error code
