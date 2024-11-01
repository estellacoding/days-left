# how_many_days.py
import datetime
import pytz

def get_local_timezone(selected_timezone):
    # 根據使用者選擇的時區返回時區
    return pytz.timezone(selected_timezone)

def calculate_total_days(total_age, current_age):
    # 計算總年數天數
    return (total_age - current_age) * 365

def calculate_awake_days(total_age, current_age, sleep_hours):
    # 計算清醒天數
    total_days = calculate_total_days(total_age, current_age)
    awake_hours_ratio = (24 - sleep_hours) / 24  # 計算每天清醒時間比例
    awake_days = int(total_days * awake_hours_ratio)
    return awake_days

def calculate_daily_countdown(selected_timezone):
    # 取得使用者選擇時區
    local_tz = get_local_timezone(selected_timezone)
    # 取得使用者選擇時區的當地時間
    now = datetime.datetime.now(local_tz) 
    
    # 設定當天結束時間為 23:59:59.999999
    end_of_day = datetime.datetime.combine(
        now.date(), datetime.time(23, 59, 59, 999999, tzinfo=local_tz)
    )
    
    # 計算當前時間與當天結束時間之間的剩餘時間
    remaining_time = end_of_day - now
    
    # 取得當天剩餘時間的總秒數
    total_seconds = int(remaining_time.total_seconds())
    # 使用 divmod 函數將剩餘的秒數轉換為小時和剩餘秒數
    hours, remaining_seconds = divmod(total_seconds, 3600)
    # 使用 divmod 函數將剩餘秒數轉換為分鐘和秒
    minutes, seconds = divmod(remaining_seconds, 60)
    
    # 返回當天剩餘小時、分鐘和秒數
    return hours, minutes, seconds
