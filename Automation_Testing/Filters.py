# # to do app add task automation script
import time

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
time.sleep(2)

category_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@role='combobox']")))
category_input.clear()
category_input.send_keys("Personal")

#status filter
Status_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[contains(@class,'w-full') and contains(@class,'p-2')])[1]")))
Status_dropdown.click()

incomplete_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='Incomplete']")))
incomplete_option.click()

# sort by filter
sort_by = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[contains(@class,'w-full') and contains(@class,'p-2')])[2]")))
sort_by.click()

priority= wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='Priority']")))
priority.click()

# order filter
order = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[contains(@class,'w-full') and contains(@class,'p-2')])[3]")))
order.click()

descending= wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='Descending']")))
descending.click()



