from CommonUtilities.DriverFunctionUtilities import DriverUtilitiesMethod
from Locators import HomePageLocator as Hpl


class HomePageFunctions(DriverUtilitiesMethod):
    """
    This class contains functions to interact with the homepage elements,
    such as clicking the revenue calculator button.
    It inherits from DriverUtilitiesMethod to leverage common driver functionalities.
    """

    def click_revenue_calculator_btn(self):
        """
        Clicks on the revenue calculator button on the homepage.

        This function finds the revenue calculator button using its locator
        and simulates a click action.
        """
        # Click the revenue calculator button using the element locator defined in HomePageLocator
        self.click_element(element_locator=Hpl.revenue_calculator_btn)
