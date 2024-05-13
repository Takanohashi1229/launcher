from selenium import webdriver
import time

def auto_like(username, password, like_interval, like_count):
    # ブラウザのドライバーをロード
    driver = webdriver.Chrome()  # Chromeの場合。他のブラウザを使用する場合はそれに応じたドライバーを使用してください。

    # Noteにログイン
    driver.get("https://note.com/login")
    time.sleep(2)  # ページの読み込みを待つ

    # ユーザー名とパスワードを入力してログイン
    driver.find_element_by_name("LoginForm[mail]").send_keys(username)
    driver.find_element_by_name("LoginForm[password]").send_keys(password)
    driver.find_element_by_css_selector(".button").click()
    time.sleep(2)  # ログイン処理を待つ

    # 指定されたいいね回数だけ投稿にいいねをする
    for _ in range(like_count):
        driver.get("https://note.com/")  # いいねをするページに移動
        time.sleep(2)  # ページの読み込みを待つ

        # いいねをする
        like_buttons = driver.find_elements_by_css_selector(".cardActions__item--like button")
        for button in like_buttons:
            button.click()
            time.sleep(1)  # いいねの処理を待つ
        
        # 次のいいねまで待つ
        time.sleep(like_interval)

    # ブラウザを閉じる
    driver.quit()

# ユーザー名とパスワードを入力
username = "YourUsername"
password = "YourPassword"

# いいねする間隔（秒）といいねする回数を指定
like_interval = 60  # 60秒ごとにいいね
like_count = 10     # 10回いいねする

# 自動いいねを開始
auto_like(username, password, like_interval, like_count)
