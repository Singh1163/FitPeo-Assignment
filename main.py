import inspect
import time
from CommonUtilities.DriverBaseUtilities import DriverBase
from CommonUtilities.DriverFunctionUtilities import DriverUtilitiesMethod
from App.HomePageFunctions import HomePageFunctions
from App.RevenuePageFunctions import RevenuePageFunction
from ConfigData.ConfigData import ConfigData


def browser_automation():
    """
    Initializes a browser session, navigates to the required webpage, interacts with the page elements,
    and performs automated actions to simulate user behavior on a web page.

    - Opens the browser.
    - Navigates to the URL specified in the configuration.
    - Interacts with the homepage and revenue page elements like buttons, sliders, and checkboxes.
    - Validates the slider's value and checks the total recurring amount.
    - Handles any exceptions that occur during the automation process and ensures the browser is closed at the end.

    Returns:
        bool: True if the automation was successful, False otherwise.
    """
    # Initialize the driver
    db = DriverBase('Chrome')  # Instantiate DriverBase with 'Chrome' browser
    driver = db.initiate_driver()  # Initiate the driver

    try:
        # Load configuration data (e.g., URL, slider value, timeout, etc.)
        cd = ConfigData()  # Load configuration data from the ConfigData module

        # Setup driver functions with the explicit timeout setting from the configuration
        driver_function = DriverUtilitiesMethod(driver=driver, explicit_timeout=cd.explicit_timeout)

        # Set the browser window size
        driver_function.set_browser_window_size(width='1920', height='1080')

        # Navigate to the specified URL
        driver_function.navigate_to_url(cd.web_url)

        # Instantiate page-specific functions for homepage and revenue page
        homepage = HomePageFunctions(driver=driver, explicit_timeout=cd.explicit_timeout)
        revenue_page = RevenuePageFunction(driver=driver, explicit_timeout=cd.explicit_timeout)

        # Click on the revenue calculator button on the homepage
        homepage.click_revenue_calculator_btn()

        # Move the slider to a specific value and verify its value
        revenue_page.move_and_check_slider_by_value(value=cd.slider_value_to_move)

        # Fill the slider input field and verify the value
        revenue_page.fill_and_check_value_in_slider_input(value=cd.slider_value_to_fill)

        # Loop through the list of CPTs to select the checkboxes and apply them
        for cpt in cd.cpt_list_to_select:
            time.sleep(0.2)  # Adding a short delay between each action to mimic human behavior
            revenue_page.select_cpt_checkbox(cpt=cpt)

        # Check and validate the total recurring amount displayed on the page
        revenue_page.check_total_recurring_amount()

        # Close the browser once the automation is complete
        driver.quit()

    except Exception as e:
        # Catch any exceptions and log the type of error with the function where it occurred
        print(f"Exception {type(e).__name__} occurs at: {inspect.stack()[1].function}")

        # Ensure the driver quits even when an exception occurs
        driver.quit()

        return False  # Return False to indicate failure

    return True  # Return True to indicate successful execution


def main():
    """
    Main function to execute the browser automation with retries.

    The browser automation function is retried up to 5 times in case of failure. If successful,
    it stops further retries.
    """
    for i in range(5):  # Retry up to 5 times if it fails
        if browser_automation():
            break  # Exit the loop if the automation is successful


if __name__ == '__main__':
    main()  # Execute the main function when the script is run
