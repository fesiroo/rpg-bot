import telebot
from telebot import types
import random
token = "6026122444:AAFVfrtEYOTlf0_IS4olurDTtCcXp0pCXyE"
bot = telebot.TeleBot(token)
hp = damage = 0 
races = {"эльф": {"hp": 900, "damage": 700},
        "гном": {"hp": 1200, "damage": 800},
        "человек": {"hp": 1000, "damage": 1000},
        "хоббит": {"hp": 1500, "damage": 760},
        "русалка": {"hp": 890, "damage": 1200}}
jobs = {"хиллер": {"hp": 2500, "damage": 600},
        "лучник": {"hp": 1500, "damage": 1100},
        "маг": {"hp": 1300, "damage": 1200},
        "мечник": {"hp": 1700, "damage": 1300},
        "копейщик": {"hp": 1600, "damage": 1400}}
enemies = ["хиличурл", "маг бездны", "шамашурл", "пустынники", "плесенники"]
def create_monster():
    random_name = random.choice(enemies)
    random_hp = random.randrange(1000, 3000)
    random_damage = random.randrange(700, 1900)
    return [random_name, random_hp, random_damage]
def race_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    for race in races.keys():
        keyboard.add(types.KeyboardButton(text = race))
    return keyboard
def job_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    for job in jobs.keys():
        keyboard.add(types.KeyboardButton(text = job))
    return keyboard
def quest():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = "Путь"
    btn2 = "Вернуться в главное меню"
    keyboard.add(btn1, btn2)
    return keyboard
@bot.message_handler(commands = ['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("Об игре")
    btn2 = types.KeyboardButton("Начать игру")
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, "Готов ли ты играть?", reply_markup = keyboard)
@bot.message_handler(content_types=['text'])
def main(message):
    global hp, damage 
    victim = create_monster()
    if message.text == "Начать игру":
        bot.send_message(message.chat.id, "Выберите расу", reply_markup = race_menu())
    if message.text == "эльф":
        hp += races["эльф"]["hp"]
        damage += races["эльф"]["damage"]
        img = open("эльф.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Вы эльф, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Выберите профессию", reply_markup = job_menu())
    if message.text == "гном":
        hp += races["гном"]["hp"]
        damage += races["гном"]["damage"]
        img = open("гном.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Вы гном, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Выберите профессию", reply_markup = job_menu())
    if message.text == "человек":
        hp += races["человек"]["hp"]
        damage += races["человек"]["damage"]
        img = open("человек.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Вы человек, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Выберите профессию", reply_markup = job_menu())
    if message.text == "хоббит":
        hp += races["хоббит"]["hp"]
        damage += races["хобит"]["damage"]
        img = open("хобит.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Вы хобит, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Выберите профессию", reply_markup = job_menu())
    if message.text == "русалка":
        hp += races["русалка"]["hp"]
        damage += races["русалка"]["damage"]
        img = open("русалка.jpg", "rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Вы русалка, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Выберите профессию", reply_markup = job_menu())
    if message.text == "хиллер":
        hp += jobs["хиллер"]["hp"]
        damage += jobs["хиллер"]["damage"]
        bot.send_message(message.chat.id, f"Вы хиллер, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Готовы ли в к приключениям?", reply_markup = quest())
    if message.text == "лучник":
        hp += jobs["лучник"]["hp"]
        damage += jobs["лучник"]["damage"]
        bot.send_message(message.chat.id, f"Вы лучник, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Готовы ли в к приключениям?", reply_markup = quest())
    if message.text == "маг":
        hp += jobs["маг"]["hp"]
        damage += jobs["маг"]["damage"]
        bot.send_message(message.chat.id, f"Вы маг, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Готовы ли в к приключениям?", reply_markup = quest())
    if message.text == "мечник":
        hp += jobs["мечник"]["hp"]
        damage += jobs["мечник"]["damage"]
        bot.send_message(message.chat.id, f"Вы мечник, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Готовы ли в к приключениям?", reply_markup = quest())
    if message.text == "копейщик":
        hp += jobs["копейщик"]["hp"]
        damage += jobs["копейщик"]["damage"]
        bot.send_message(message.chat.id, f"Вы копейщик, ваш текущий hp: {hp}, ваш damage: {damage}")
        bot.send_message(message.chat.id, "Готовы ли в к приключениям?", reply_markup = quest())
    if message.text == "Путь":
        event = random.randint(1, 2)
        if event == 1:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = "Путь"
            btn2 = "Вернуться в главное меню"
            keyboard.add(btn1, btn2)
            bot.send_message(message.chat.id, "Вы никого не встретили", reply_markup = keyboard)
        if event == 2:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn3 = "Драться"
            btn4 = "Убежать"
            btn2 = "Вернуться в главное меню"
            keyboard.add(btn3, btn4, btn2)
            bot.send_message(message.chat.id, f"Вы встретили врага {victim[0]}, hp: {victim[1]}, damage: {victim[2]}", reply_markup = keyboard)
    if message.text == "Драться":
        victim[1] -= damage
        if victim[1] <= 0:
            hp += 500
            damage += 700
            bot.send_message(message.chat.id, f"Вы победили врага, ваш hp: {hp}, ваш damage: {damage}")
        elif victim[1] > 0:
            hp -= victim[2]
            bot.send_message(message.chat.id, "Вас атакуют")
            if hp <= 0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
                btn2 = "Вернуться в главное меню"
                keyboard.add(btn2)
            elif hp > 0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
                btn3 = "Драться"
                btn4 = "Убежать"
                btn2 = "Вернуться в главное меню"
                keyboard.add(btn3, btn4, btn2)
                bot.send_message(message.chat.id, f"Ваш hp: {hp}, ваш damage: {damage}, у врага hp {victim[1]}, damage: {victim[2]}", reply_markup = keyboard)
    if message.text == "Убежать":
        run = random.randint(1, 2)
        if run == 1:
            bot.send_message(message.chat.id, "Вы убежади от врага", reply_markup = quest())
        if run == 2:
            hp -= victim[2]
            bot.send_message(message.chat.id, "Вас нашел враг")
            if hp <= 0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
                btn2 = "Вернуться в главное меню"
                keyboard.add(btn2)
                bot.send_message(message.chat.id, "Вас победил враг")
            elif hp>0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
                btn3 = "Драться"
                btn4 = "Убежать"
                btn2 = "Вернуться в главное меню"
                keyboard.add(btn3, btn4, btn2)
                bot.send_message(message.chat.id, f"Ваш hp: {hp}, ваш damage: {damage}, у врага hp {victim[1]}, damage: {victim[2]}", reply_markup = keyboard)
    if message.text == "Вернуться в главное меню":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton("Об игре")
        btn2 = types.KeyboardButton("Начать игру")
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup = keyboard)
    if message.text == "Об игре":
        bot.send_message(message.chat.id, "Это rpg бот, вы здесь можете выбрать расу, профессию и драться с монстрами")

bot.polling(non_stop=True)

    
