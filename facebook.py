import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# 配置账号和密码
EMAIL = ""  # 替换为你的Facebook邮箱
PASSWORD = ""  # 替换为你的Facebook密码

# 启动Edge浏览器
driver = webdriver.Edge()

# 访问Facebook登录页面
driver.get("https://www.facebook.com")
time.sleep(2)

# 自动填充账号和密码
try:
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(EMAIL)
    time.sleep(1)

    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys(PASSWORD)
    time.sleep(1)

    # 点击登录按钮
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    time.sleep(5)  # 等待登录完成
except Exception as e:
    print(f"登录过程中出现错误: {e}")
    # 不退出程序，继续执行后续操作

# 访问目标网页
url = "https://www.facebook.com/groups/407387266101827/members"
driver.get(url)

# 等待直到指定的提取内容出现（群组成员列表）
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/user/")]'))
    )
    print("群组成员列表已加载！")
except Exception as e:
    print("等待超时，未能加载群组成员列表。")
    # 不退出程序，继续执行后续操作

# 提取群组ID
group_id = re.search(r"/groups/(\d+)/", url).group(1)

# 数据存储
data = []
extracted_user_ids = set()

# 滚动加载成员数据
scroll_count = 0
while len(data) < 98:
    member_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/groups/{}/user/")]'.format(group_id))
    new_data = []

    for link in member_links:
        try:
            href = link.get_attribute("href")
            user_id_match = re.search(r"/user/(\d+)/", href)
            if user_id_match:
                user_id = user_id_match.group(1)
                username = link.text.strip()

                # 增加对 username 的判断：如果 username 不为空，才进行后续操作
                if username and user_id not in extracted_user_ids:
                    extracted_user_ids.add(user_id)
                    new_data.append({"username": username, "user_id": user_id})
                    print(f"Extracted: {username}, {user_id}")

            if len(new_data) >= 7:
                break
        except Exception as e:
            print(f"Error extracting data: {e}")

    data.extend(new_data)

    if len(data) >= 98:
        break

    scroll_count += 1
    driver.execute_script("window.scrollBy(0, 600);")
    print(f"Scrolled {scroll_count} times...")
    time.sleep(2)

# 关闭浏览器
driver.quit()

# 保存数据到CSV文件
output_file = f"{group_id}.csv"
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")