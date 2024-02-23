from datetime import datetime, timedelta

today = datetime.now()
result = today - timedelta(days=5)
print(result)

# Print the date part only
print(result.strftime("%Y-%m-%d"))
