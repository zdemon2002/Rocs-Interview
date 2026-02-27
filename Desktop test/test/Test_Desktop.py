from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# --------------------------------
# Driver Setup
# --------------------------------
def create_driver():
    capabilities = {
        "platformName": "Windows",
        "deviceName": "WindowsPC",
        "app": r"C:\\Windows\\System32\\notepad.exe"
    }

    return webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        desired_capabilities=capabilities
    )


# --------------------------------
# Wait Helpers
# --------------------------------
def wait_for_editor(driver, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.NAME, "Text editor"))
    )


def wait_for_window(driver, name, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.NAME, name))
    )


# --------------------------------
# Always Create Fresh Tab
# --------------------------------
def create_new_tab(driver):
    editor = wait_for_editor(driver)
    editor.click()
    editor.send_keys(Keys.CONTROL, "n")
    return wait_for_editor(driver)


# --------------------------------
# Your Working Save Logic
# --------------------------------
def save_file(driver):
    editor = wait_for_editor(driver)

    # Open Save dialog ONCE
    editor.send_keys(Keys.CONTROL, "s")

    # Click Save if button appears
    try:
        save_btn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.NAME, "Save"))
        )
        save_btn.click()
    except:
        pass

    # If overwrite appears → press Yes
    try:
        yes_btn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.NAME, "Yes"))
        )
        yes_btn.click()
    except:
        pass


# --------------------------------
# Reopen File via Search
# --------------------------------
# def reopen_file(driver, filename):
#     editor = create_new_tab(driver)

#     # Open dialog
#     editor.send_keys(Keys.CONTROL, "o")

#     # Small stabilization wait for dialog render
#     time.sleep(1)

#     # Directly type filename (focus is already in Search box)
#     editor.send_keys(filename)
#     editor.send_keys(Keys.ENTER)

#     # Wait for file to load
#     return wait_for_editor(driver)

# --------------------------------
# Main Flow
# --------------------------------
def automate():
    driver = create_driver()

    try:
        editor = create_new_tab(driver)

        expected_text = "Desktop automation test – completed"

        editor.send_keys("Desktop automation test")
        editor.send_keys(" – completed")

        filename = "Desktop automation test – completed.txt"  # default Notepad save name
        save_file(driver)

        # Give Windows a moment to commit file
        time.sleep(1)
        print("File saved:", filename)
        #Failed relics
        # reopen_file(driver, filename)

        # content = wait_for_editor(driver).text

        # if expected_text in content:
        #     print("Verification PASSED ✅")
        # else:
        #     print("Verification FAILED ❌")
        #     print("Actual content:", content)

    except Exception as e:
        print("Automation failed:", e)

    finally:
        time.sleep(1)
        driver.quit()


# --------------------------------
# Entry
# --------------------------------
if __name__ == "__main__":
    automate()