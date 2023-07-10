from selenium.webdriver.common.by import By

def get_locator(locator_name):
    elements = root.findall(f".//locator[@name='{locator_name}']")
    try:
        if not elements:
            raise Exception(f"Locator {locator_name} not found in {path}")
        element = elements[0]
        locator_type = element.get("locator_type").lower()
        locator_value = element.get("locator_value")

        locator_value = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME
        }

        if locator_type not in locator_value:
            raise Exception(f"Unknown locator type {locator_type} in {path}")

        return locator_value[locator_type], locator_value

    except Exception as e:
        print(e)
        raise e