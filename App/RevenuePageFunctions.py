from selenium.webdriver import Keys
from CommonUtilities.DriverFunctionUtilities import DriverUtilitiesMethod
from Locators import RevenuePageLocator as Rpl


class RevenuePageFunction(DriverUtilitiesMethod):
    """
    This class contains functions to interact with and automate actions on the revenue page,
    such as moving the slider, filling slider input, selecting CPT checkboxes, and checking the total recurring amount.
    It inherits from DriverUtilitiesMethod to leverage common driver functionalities.
    """

    def move_and_check_slider_by_value(self, value: int):
        """
        Moves the slider to a specific value and checks if the value matches the expected one.

        Args:
            value (int): The target value for the slider.
        """
        # Get the current value of the slider
        current_value = int(self.get_attribute_value_of_element(
            element_locator=Rpl.slider_btn_input,
            attribute_name='value'
        ))

        # Move the slider in increments until the target value is reached
        while abs(current_value - value) >= 5:
            if current_value < value:
                self.move_slider(element_locator=Rpl.slider_btn, x_value=10, y_value=0)
            else:
                self.move_slider(element_locator=Rpl.slider_btn, x_value=-1, y_value=0)
            # Update current slider value
            current_value = int(self.get_attribute_value_of_element(
                element_locator=Rpl.slider_value_input,
                attribute_name='value'
            ))

        # Check if the final slider value matches the expected value
        if current_value != value:
            print(f"Expected: {value}, but got: {current_value}")
        else:
            print(f"Expected: {value}, matched with current value: {current_value}")

    def fill_and_check_value_in_slider_input(self, value):
        """
        Fills the slider input field with a given value and checks if the displayed slider value matches the input.

        Args:
            value (str): The value to fill in the slider input field.
        """
        # Clear any existing value in the slider input field
        self.fill_text_using_action_chain(element_locator=Rpl.slider_value_input, text='')

        # Use BACKSPACE to clear the field if needed (for Windows/Linux compatibility)
        for i in range(5):
            self.press_keyboard_key(Keys.BACKSPACE)

        # Fill the input field with the new value
        self.fill_text_using_action_chain(element_locator=Rpl.slider_value_input, text=value)

        # Get the current value from the slider button input and verify
        current_value = self.get_attribute_value_of_element(
            element_locator=Rpl.slider_btn_input,
            attribute_name='value'
        )

        # Compare expected value with actual value
        if current_value != value:
            print(f"Expected: {value}, but got: {current_value}")
        else:
            print(f"Expected: {value}, matched with current value: {current_value}")

    def select_cpt_checkbox(self, cpt):
        """
        Selects a CPT checkbox on the revenue page.

        Args:
            cpt (str): The CPT value to select the corresponding checkbox.
        """
        # Scroll to the element before clicking (ensure visibility)
        self.scroll_to_element(element_locator=Rpl.cpt_box_dynamic.format(cpt_to_select=cpt))

        # Click the corresponding CPT checkbox
        self.click_element(element_locator=Rpl.cpt_check_box_dynamic.format(cpt_to_select=cpt))

    def check_total_recurring_amount(self):
        """
        Checks the total recurring amount displayed on the revenue page and compares it with the expected value.

        The expected total is hardcoded as '$110700'.
        """
        # Get the total recurring amount from the page
        current_value = self.get_text(element_locator=Rpl.total_recurring_amount)

        # Compare the actual total with the expected value
        if current_value != '$110700':
            print(f"Expected: {'$110700'}, but got: {current_value}")
        else:
            print(f"Expected: {'$110700'}, matched with current value: {current_value}")
