import time
from selenium.webdriver.common.by import By

def rms_login_selenium(driver, login_id, passwd, user_id, user_passwd):
    driver.get('https://glogin.rms.rakuten.co.jp/?sp_id=1')
    time.sleep(2)

    driver.find_element(By.NAME, 'login_id').send_keys(login_id)
    driver.find_element(By.NAME, 'passwd').send_keys(passwd)
    driver.find_element(By.NAME, 'submit').click()
    time.sleep(3)

    driver.find_element(By.NAME, 'user_id').send_keys(user_id)
    driver.find_element(By.NAME, 'user_passwd').send_keys(user_passwd)
    driver.find_element(By.NAME, 'submit').click()
    time.sleep(5)

    while True:
        current_url = driver.current_url
        print(f"▶ 現在URL: {current_url}")
        if current_url.strip().lower() == "https://mainmenu.rms.rakuten.co.jp/":
            print("✅ ログイン成功！メインメニュー到達")
            break
        try:
            submit_button = driver.find_element(By.NAME, 'submit')
            submit_button.click()
            print("▶ 中間認証 submitボタン押下")
            time.sleep(3)
        except:
            try:
                confirm_button = driver.find_element(By.CSS_SELECTOR, 'form#confirm button[type="submit"]')
                confirm_button.click()
                print("▶ 中間認証2 '遵守してRMSを利用します'ボタン押下")
                time.sleep(3)
            except Exception as e:
                print(f"⚠️ 中間認証ボタン見つからず: {e}")
                break
