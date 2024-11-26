from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DriverUtilitiesMethod:

    def __init__(self, driver, explicit_timeout):
        """
        Initializes the DriverUtilitiesMethod with the given WebDriver instance and explicit wait timeout.

        :param driver: WebDriver instance for interacting with the browser.
        :param explicit_timeout: Time in seconds for explicit waits.
        """
        self.driver = driver
        self.explicit_timeout = explicit_timeout

    def navigate_to_url(self, url):
        """
        Navigates the browser to the given URL.

        :param url: URL to navigate to.
        """
        self.driver.get(url)

    def set_browser_window_size(self, width=0, height=0):
        """
        Sets the size of the browser window. If no size is given, it maximizes the window.

        :param width: Width of the window.
        :param height: Height of the window.
        """
        if not width or not height:
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(width=width, height=height)

    def explicitly_wait_till_presence_of_element_located(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):
        """
        Waits until the element is present in the DOM.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        locator_method = By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR
        WebDriverWait(self.driver, self.explicit_timeout * explicit_wait_multiplier).until(
            EC.presence_of_element_located((locator_method, element_locator))
        )

    def explicitly_wait_till_visibility_of_element_located(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):
        """
        Waits until the element is visible on the page.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        locator_method = By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR
        WebDriverWait(self.driver, self.explicit_timeout * explicit_wait_multiplier).until(
            EC.visibility_of_element_located((locator_method, element_locator))
        )

    def explicitly_wait_till_invisibility_of_element_located(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):
        """
        Waits until the element is no longer visible.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        locator_method = By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR
        WebDriverWait(self.driver, self.explicit_timeout * explicit_wait_multiplier).until(
            EC.invisibility_of_element_located((locator_method, element_locator))
        )

    def explicitly_wait_till_element_is_clickable(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):
        """
        Waits until the element is clickable.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        locator_method = By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR
        WebDriverWait(self.driver, self.explicit_timeout * explicit_wait_multiplier).until(
            EC.element_to_be_clickable((locator_method, element_locator))
        )

    def scroll_to_element(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):
        """
        Scrolls the page until the specified element is in view.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        self.explicitly_wait_till_presence_of_element_located(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1):
        """
        Clicks the element after waiting for it to be clickable.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        self.explicitly_wait_till_element_is_clickable(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        element.click()

    def input_text_in_field(self, element_locator: str, text: str, find_by="xpath", clear=False, explicit_wait_multiplier=1):
        """
        Enters text into an input field.

        :param element_locator: Locator for the input field (XPath or CSS).
        :param text: Text to enter into the field.
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param clear: If True, clears the field before entering the text.
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        self.explicitly_wait_till_presence_of_element_located(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, element_locator: str, find_by="xpath", explicit_wait_multiplier=1) -> str:
        """
        Retrieves the text of the element.

        :param element_locator: Locator for the element (XPath or CSS).
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        :return: Text content of the element.
        """
        self.explicitly_wait_till_visibility_of_element_located(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        return element.text

    def move_slider(self, element_locator: str, x_value=1, y_value=1, find_by="xpath", explicit_wait_multiplier=1):
        """
        Moves the slider element by a given offset.

        :param element_locator: Locator for the slider element (XPath or CSS).
        :param x_value: Horizontal movement of the slider.
        :param y_value: Vertical movement of the slider.
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        """
        self.explicitly_wait_till_visibility_of_element_located(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_value, y_value).perform()

    def get_attribute_value_of_element(self, element_locator: str, attribute_name, find_by="xpath", explicit_wait_multiplier=1):
        """
        Retrieves the value of an attribute of an element.

        :param element_locator: Locator for the element (XPath or CSS).
        :param attribute_name: Name of the attribute to retrieve.
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        :return: Value of the specified attribute.
        """
        self.explicitly_wait_till_visibility_of_element_located(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        return element.get_attribute(attribute_name)

    def fill_text_using_action_chain(self, element_locator: str, text: str, find_by="xpath", explicit_wait_multiplier=1, clear=False):
        """
        Fills text in an input field using ActionChains (ideal for complex interactions).

        :param element_locator: Locator for the input field (XPath or CSS).
        :param text: Text to enter into the field.
        :param find_by: Method to locate the element ('xpath' or 'css').
        :param explicit_wait_multiplier: Multiplier for explicit wait timeout.
        :param clear: If True, clears the field before entering the text.
        """
        self.explicitly_wait_till_presence_of_element_located(element_locator, find_by, explicit_wait_multiplier)
        element = self.driver.find_element(by=By.XPATH if find_by.lower() == "xpath" else By.CSS_SELECTOR, value=element_locator)
        actions = ActionChains(self.driver)
        if clear:
            element.clear()
        actions.send_keys_to_element(element, text).perform()

    def press_keyboard_key(self, key):
        """
        Simulates pressing a keyboard key.

        :param key: Key to press.
        """
        actions = ActionChains(self.driver)
        actions.send_keys(key).perform()
