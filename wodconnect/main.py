import bot

bot_token = 'your telegram bot_token here'
chat_id = 'your telegram chat_id here'
message = 'message here'

username = 'your_username'
password = 'your_password'
class_date = '13 June, 2023'
class_time = '17:00'

driver = bot.initialize_driver()
bot.login(driver, username, password)
bot.select_calendar_date(driver, class_date)
bot.book_class(driver, class_time)
bot.send_telegram_message(bot_token, chat_id, message)
