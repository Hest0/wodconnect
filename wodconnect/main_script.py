import wod_connect_bot

bot_token = 'your telegram bot_token here'
chat_id = 'your telegram chat_id here'
message = 'message here'

username = 'your_username'
password = 'your_password'
class_date = '13 June, 2023'
class_time = '17:00'

driver = wod_connect_bot.initialize_driver()
wod_connect_bot.login(driver, username, password)
wod_connect_bot.select_calendar_date(driver, class_date)
wod_connect_bot.book_class(driver, class_time)
wod_connect_bot.send_telegram_message(bot_token, chat_id, message)
