from candlesticks.binance_api import export_candlestick_data

pairs = ["ADAUSDT", "BTCUSDT", "ETHUSDT", "DOGEUSDT"]

start_date = "1 Jan 2019"
end_date = "30 Jul 2021"

for pair in pairs:
	print(f"[INFO]Working on pair {pair}")
	fname = f"./data/{pair}.csv"
	export_candlestick_data(pair, start_date, end_date, fname)
	print("[INFO] Moving to the next pair..")

print("[INFO] Export finished.")