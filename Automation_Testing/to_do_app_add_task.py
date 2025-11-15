# # to do app add task automation script
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("https://bug-test-swart.vercel.app/")
driver.maximize_window()
wait = WebDriverWait(driver, 5)

# Enter Task name
name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Task description']")))
name.send_keys("meeting")

#select category dropdown
category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'w-full') and contains(@class,'p-2')]")))
category_dropdown.click()

category_personal= wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='Personal']")))
category_personal.click()

# Select Priority "High"
priority_high = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='High']")))
priority_high.click()

# Enter Due Date
due_date = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='react-datepicker__input-container']/input")))
due_date.click()
due_date.clear()
due_date.send_keys("11/16/2025")

# Click add task button
add_task = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Task']")))
add_task.click()

