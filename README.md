# How Many Days Left?

How Many Days Left? 是一個互動式的 Streamlit 應用程式，讓使用者以視覺化的方式計算可用天數。

受到 [Andrew Ng - How to Build Your Career in AI](https://info.deeplearning.ai/how-to-build-a-career-in-ai-book) 啟發下，完成這個工具，想提醒自己人生最重要的事情是什麼？無論今天選擇什麼，它值得你有限的 1/30,000 壽命之一嗎？讓每一天都變得意義非凡吧！

如果不用本機執行，也可以直接進入 [How Many Days Left?](https://days-left.streamlit.app/) 這個網頁。

# 主要功能
- 計算可用天數：根據預期壽命、目前年齡與睡眠時數，計算從現在到預期壽命的可用天數。
- 即時倒數計時：取得本地時區時間，顯示當天剩餘的小時、分鐘與秒數。
- 即時提示訊息：當輸入的數值異常時，提供警告確保輸入的正確性。

# 前置步驟
## 複製專案
```
git clone https://github.com/estellacoding/days-left.git
cd days-left
```

# 安裝套件
```
pip install -r requirements.txt
```

# 專案結構
```
days-left
├── app.py                # 主應用程式
├── how_many_days.py      # 計算邏輯函數
├── README.md
└── requirements.txt
```

# 執行程式
## 啟動 Streamlit
```
streamlit run app.py
```
## 開啟瀏覽器
開啟瀏覽器，進入 localhost:8501，即可使用專案介面。

## 輸入資料
- 輸入預期壽命 (預設 80 歲)。
- 輸入您的目前年齡 (預設 30 歲)。
- 輸入您的平均每日睡眠時數 (預設 8 小時)。
- 點擊「Start Calculation」按鈕。
- 就會開始計算並顯示可用天數。