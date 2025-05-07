
from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='', parse_mode='html')
faker = Faker()

card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)

card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)

card_type_keybaord.row(
    types.KeyboardButton(text='JCB'),
    types.KeyboardButton(text='American Express'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='👋 Hi there! I can help you generate a test credit card number. Just pick a card type and I\'ll show you the number! 💳\nChoose a card type:', 
        reply_markup=card_type_keybaord,
    )

@bot.message_handler()
def message_handler(message: types.Message):

    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'JCB':
        card_type = 'jcb'
    elif message.text == 'American Express':
        card_type = 'amex'   
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Sorry! I did't anything",
        )
        return

    card_number = faker.credit_card_number(card_type)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Card {card_type}:\n<code>{card_number}</code>'
    )


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
