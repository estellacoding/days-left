# app.py
import streamlit as st
from how_many_days import calculate_total_days, calculate_awake_days, calculate_daily_countdown
import time

# 網頁標題
st.markdown(
    "<h1 style='font-size: 28px; text-align: left;'>How Many Days Left?</h1>",
    unsafe_allow_html=True
)

# 使用者輸入區域：年齡與睡眠時間
total_age = st.number_input("Please enter the typical human lifespan:", min_value=0, max_value=150, value=80, step=1)
current_age = st.number_input("Please enter your current age:", min_value=0, max_value=150, value=30, step=1)
sleep_hours = st.number_input("Please enter your average sleep hours per day:", min_value=0, max_value=24, value=8, step=1)

# 輸入有警告情況則不執行計算結果
has_warning = False

# 輸入預期壽命為 0
if total_age == 0:
    st.warning("Warning: The typical human lifespan cannot be zero. 80 is a good guess.")
    has_warning = True
# 當前年齡大於預期壽命
elif current_age > total_age:
    st.warning("Warning: Your current age is greater than the typical human lifespan!")
    has_warning = True

# 根據睡眠時間顯示不同的提示訊息
if sleep_hours == 0:
    st.info("Note: Seriously?! Are you secretly a superhero running on caffeine alone?")
if sleep_hours == 24:
    st.info("Note: Seriously?! Did you mean to join the world of hibernating bears?")
if 0 < sleep_hours < 5:
    st.info("Note: You have entered less than 5 hours of sleep. Make sure this reflects your actual sleeping habits. Remember, even vampires need a good nap to keep their fangs sharp!")
if 12 < sleep_hours < 24:
    st.info("Note: You have entered more than 12 hours of sleep. Make sure this reflects your actual sleeping habits. But sleeping beauty, is that you? That's a lot of beauty rest!")

# 當使用者點擊按鈕時執行計算
if st.button("Start Calculation"):
    if has_warning:
        # 如果有警告情況，顯示錯誤訊息就不執行計算
        st.error("Cannot proceed with calculation due to Warnings.")
    else:
        # 計算總天數與清醒天數
        total_days = calculate_total_days(total_age, current_age)
        awake_days = calculate_awake_days(total_age, current_age, sleep_hours)

        # 網頁標題
        st.markdown(
            "<h1 style='font-size: 26px; text-align: left;'>Days Countdown:</h1>",
            unsafe_allow_html=True
        )

        # 顯示清醒天數
        st.markdown(
            f"<div style='font-size: 50px; font-weight: bold; color: red; text-align: center;'>"
            f"{awake_days} days"
            f"</div>",
            unsafe_allow_html=True
        )

        # 當清醒天數大於 0 時，才顯示倒數計時器
        if awake_days > 0:
            # 創建一個空的佔位符，用於顯示倒數計時
            countdown_placeholder = st.empty()

            # 使用 Streamlit 的自動重新整理功能來實現倒數計時
            for _ in range(awake_days * 24 * 3600):  # 每秒更新一次
                # 取得當天剩餘的時、分、秒
                hours, minutes, seconds = calculate_daily_countdown()

                # 顯示倒數計時
                countdown_placeholder.markdown(
                    f"<div style='font-size: 24px; font-weight: light; color: red; text-align: center;'>"
                    f"Time left today: {hours} hours: {minutes} minutes: {seconds} seconds"
                    f"</div>",
                    unsafe_allow_html=True
                )

                # 如果剩餘時間為0，則結束迴圈
                if hours == 0 and minutes == 0 and seconds == 0:
                    break

                # 每秒更新一次
                time.sleep(1)
