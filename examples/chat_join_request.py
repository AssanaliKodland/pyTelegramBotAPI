import telebot


bot = telebot.TeleBot('TOKEN')

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=telebot.util.update_types)

def is_api_group(chat_id):
    return chat_id == GROUP_CHAT_ID


@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return
