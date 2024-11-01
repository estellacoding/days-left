# how_many_days.py
import datetime

def calculate_total_days(total_age, current_age):
    # 計算總年數天數
    return (total_age - current_age) * 365

def calculate_awake_days(total_age, current_age, sleep_hours):
    # 計算清醒天數
    total_days = calculate_total_days(total_age, current_age)
    awake_hours_ratio = (24 - sleep_hours) / 24  # 計算每天清醒時間比例
    awake_days = int(total_days * awake_hours_ratio)
    return awake_days

def calculate_daily_countdown():
    # 取得本地時間（無時區）
    now = datetime.datetime.now()
    
    # 設定當天結束時間為 23:59:59.999999
    end_of_day = datetime.datetime.combine(now.date(), datetime.time(23, 59, 59, 999999))
    
    # 計算當前時間與當天結束時間之間的剩餘時間
    remaining_time = end_of_day - now
    
    total_seconds = int(remaining_time.total_seconds())
    if total_seconds < 0:
        # 如果已經過了當天結束時間，設定剩餘時間為0
        return 0, 0, 0
    
    # 使用 divmod 函數將剩餘的秒數轉換為小時和剩餘秒數
    hours, remaining_seconds = divmod(total_seconds, 3600)
    # 使用 divmod 函數將剩餘秒數轉換為分鐘和秒
    minutes, seconds = divmod(remaining_seconds, 60)
    
    # 返回當天剩餘小時、分鐘和秒數
    return hours, minutes, seconds
