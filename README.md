# rms-utils

<span style="color:#ccc">
楽天RMSに自動ログインするためのPythonモジュールです（Seleniumベース）。
</span>

## 特徴

<span style="color:#ccc">
- Seleniumによる楽天RMSのログイン自動化  
- 中間認証（「遵守してRMSを利用します」など）にも対応  
- pip経由でGitHubからインストール可能
</span>

## インストール

<span style="color:#ccc">以下のコマンドでインストールできます（パブリックリポジトリの場合）:</span>

```bash
pip install git+https://github.com/egkoichinft/rms-utils.git


## 使い方

以下のように `rms_login_selenium` を呼び出します：

```python
from rms_login import rms_login_selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 認証情報
LOGIN_ID = 'your_login_id'
LOGIN_PASS = 'your_login_password'
USER_ID = 'your_user_id'
USER_PASS = 'your_user_pass'

# ログイン実行
rms_login_selenium(driver, LOGIN_ID, LOGIN_PASS, USER_ID, USER_PASS)
