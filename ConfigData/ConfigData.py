class ConfigData:
    """
    This class holds configuration data used throughout the automation process.
    It defines values such as the URL to navigate to, timeout settings, CPT values to select,
    and slider values to interact with.
    """

    def __init__(self):
        """
        Initializes configuration values for the automation tasks.
        """
        self.web_url = 'https://www.fitpeo.com/'  # The website URL to visit
        self.explicit_timeout = 10  # The timeout for explicit waits (in seconds)
        self.cpt_list_to_select = ['99091', '99453', '99454', '99474']  # List of CPT codes to select
        self.slider_value_to_move = 820  # The target value to move the slider to
        self.slider_value_to_fill = '560'  # The value to input into the slider field (as a string)
