def test_project_is_configured(driver, base_url):
    """
    Sanity check of the project configuration.
    """
    assert driver.current_url.startswith(base_url)