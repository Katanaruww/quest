from aiogram import Dispatcher, Bot
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3

storage = MemoryStorage()


class FSM(StatesGroup):
    fio = State()
    rank = State()
    one_station = State()
    two_station = State()
    three_station = State()
    four_station_1 = State()
    four_station_2 = State()
    five_station_1 = State()
    five_station_2 = State()
    six_station_1 = State()
    six_station_2 = State()
    seven_station = State()


bot = Bot("5606690486:AAGTtIzwK9837iNdA0PTQ17SzMWhSc2Ak1E")
katana = Dispatcher(bot, storage=storage)

conn = sqlite3.connect('dat.db', check_same_thread=False)
cur = conn.cursor()
one_station = ["1", "2", "3", "1", "4", "3", "4", "1", "3", "2", "1", "1", "2", "4", "3", ]
two_station = ["стояние на реке угре", "куликовская битва", "1793", "736", "556"]
three_station = ["Петр I",
                 "Иван Грозный",
                 "Дмитрий Донской",
                 "Александр Невский",
                 "Георгий Константинович Жуков",
                 "Никита Сергеевич Хрущев",
                 "Екатерина II",
                 "Александр Васильевич Суворов",
                 "Андрей Ануфриевич Дубенский"]
four_station = [
    ["Сословия", "Неподатные", "Податные", "Дворянство", "Духовенство", "Крестьянство", "Мещанство", "Казачество",
     "Черносошные", "Владельческие"],
    ["Мануфактура", "Сословие", "Барщина", "Вече", "Реформа"]]
five_station = [["Д", "Б", "Ж", "В", "А", "Г", "Е"],
                ["А", "Е", "Д", "Б", "Д", "Г", "Е", "В"]]
six_station = [["куликовская битва", "между монахом Сергием Радонежским и князем Дмитрием Ивановичем",
                "Сказание о Мамаевом побоище"],
               ["Минину и Пожарскому", "К 200-летию освобождения Москвы от поляков в 1613", "Мартос"]]
seven_station = ["1886", "Дом Ветеринара", "Вощиный завод. Дудко", "Спасо-Преображенская",
                 "В честь жены владельца цементного завода - Евгении", "штаб генерала Молчанова"]


@katana.message_handler(commands=["start"], state=None)
async def start(message):
    first_name = message.chat.first_name
    username = message.chat.username
    msg_id = message.chat.id
    cur.execute("INSERT INTO data (tg_id, tg_tag, tg_name) VALUES (?, ?, ?)", (msg_id, username, first_name))
    conn.commit()
    row = cur.execute("SELECT * FROM data WHERE tg_id = ?", (msg_id,)).fetchone()
    if row[4] is None:
        await bot.send_message(message.chat.id, "<b>Введите ФИО⤵</b>", parse_mode="HTML")
        await FSM.fio.set()
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        start_quest = KeyboardButton("Начать🔓")
        markup.add(start_quest)
        await bot.send_message(msg_id, "<b>Вы уже прошли регистрацию! Нажмите кнопку ниже⤵</b>", parse_mode="HTML",
                               reply_markup=markup)


@katana.message_handler(commands=["two_station"], state=None)
async def two(message):
    row = cur.execute("SELECT twostat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
    print(row)
    if row[0] is None or row[0] == 0:
        await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №2. 'ЗАГАДОЧНАЯ'</b>\n"
                                                "<b>Введите ответ в формате:\nфраза/число\nфраза/число\n</b>\n "
                                                "P.S. / - или", parse_mode="HTML")
        await FSM.two_station.set()
    else:
        await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>", parse_mode="HTML")


@katana.message_handler(commands=["three_station"], state=None)
async def two(message):
    row = cur.execute("SELECT threestat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
    print(row)
    if row[0] is None or row[0] == 0:
        await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №3. 'ПОРТРЕТНАЯ ГАЛЛЕРЕЯ'</b>\n"
                                                "<b>Введите ответ в формате:\nфраза\nфраза\nфраза</b>\n ",
                               parse_mode="HTML")
        await FSM.three_station.set()
    else:
        await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>", parse_mode="HTML")


@katana.message_handler(commands=["four_station"], state=None)
async def two(message):
    row = cur.execute("SELECT fourstat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
    print(row)
    if row[0] is None or row[0] == 0:
        await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №4</b>\n"
                                                "<b>ЗАДАНИЕ №1</b>\n"
                                                "<b>Введите ответ в формате:\nслово\nслово\nслово</b>\n "
                                                "P.S. ответы только за первой задание!", parse_mode="HTML")
        await FSM.four_station_1.set()
    else:
        await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>", parse_mode="HTML")


@katana.message_handler(commands=["five_station"], state=None)
async def two(message):
    row = cur.execute("SELECT fivestat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
    print(row)
    if row[0] is None or row[0] == 0:
        await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №5</b>\n"
                                                "<b>ЗАДАНИЕ №1</b>\n"
                                                "<b>Введите ответ в формате: буква-буква-буква</b>\n "
                                                "P.S. ответы только за первой задание!", parse_mode="HTML")
        await FSM.five_station_1.set()
    else:
        await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>", parse_mode="HTML")


@katana.message_handler(commands=["six_station"], state=None)
async def two(message):
    row = cur.execute("SELECT sixstat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
    print(row)
    if row[0] is None or row[0] == 0:
        await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №6</b>\n"
                                                "<b>ЗАДАНИЕ №1</b>\n"
                                                "<b>Введите ответ в формате:\nфраза\nфраза\nфраза</b>\n "
                                                "P.S. ответы только за первой задание!", parse_mode="HTML")
        await FSM.six_station_1.set()
    else:
        await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>", parse_mode="HTML")


@katana.message_handler(commands=["seven_station"], state=None)
async def two(message):
    row = cur.execute("SELECT sevenstat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
    print(row)
    if row[0] is None or row[0] == 0:
        await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №7</b>\n"
                                                "<b>Введите ответ в формате:\nфраза/число\nфраза/число\n</b>\n "
                                                "P.S. / - или", parse_mode="HTML")
        await FSM.seven_station.set()
    else:
        await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>", parse_mode="HTML")
@katana.message_handler(commands=["drop_data"], state=None)
async def drop(message):
    row = cur.execute("SELECT * FROM data").fetchall()
    for i in range(len(row)):
        await bot.send_message(message.chat.id, row[i])


@katana.message_handler(content_types=["text"], state=None)
async def text(message):
    if message.text == "Начать🔓":
        row = cur.execute("SELECT onestat FROM data WHERE tg_id = ?", (message.chat.id,)).fetchone()
        print(row)
        if row[0] is None or row[0] == 0:
            await bot.send_message(message.chat.id, "<b>СТАНЦИЯ №1. 'УГАДАЙКА-КА'</b>\n"
                                                    "<b>Введите ответ в формате - 1:2:3:4:5</b>\n "
                                                    "P.S. Только числа", parse_mode="HTML")
            await FSM.one_station.set()
        else:
            await bot.send_message(message.chat.id, "<b>Упсс...кажется ты уже прошел эту станцию)🚶🏼</b>",
                                   parse_mode="HTML")


@katana.message_handler(state=FSM.one_station)
async def start_data(message, state: FSMContext):
    one_stationn = message.text
    await state.update_data(one_station=one_stationn)
    data = await state.get_data()
    one_station_data = data.get('one_station')
    one_station_answer = one_station_data.split(":")
    print(one_station)
    print(one_station_answer)
    one_station_answer_zip = zip(one_station, one_station_answer)
    one_station_answer_list = list(one_station_answer_zip)
    for i in range(len(one_station_answer_list)):
        if one_station_answer_list[i][0] == one_station_answer_list[i][1]:
            cur.execute("UPDATE data SET onestat = onestat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nЧтобы приступить к следующему заданию напишите боту /two_station",
                           parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.two_station)
async def start_data(message, state: FSMContext):
    two_stationn = message.text
    await state.update_data(two_station=two_stationn)
    data = await state.get_data()
    two_station_data = data.get('two_station')
    two_station_answer = two_station_data.split("\n")
    print(two_station)
    print(two_station_answer)
    two_station_answer_zip = zip(two_station, two_station_answer)
    two_station_answer_list = list(two_station_answer_zip)
    for i in range(len(two_station_answer_list)):
        if two_station_answer_list[i][1] in two_station_answer_list[i][0]:
            cur.execute("UPDATE data SET twostat = twostat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nЧтобы приступить к следующему заданию напишите боту /three_station",
                           parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.three_station)
async def start_data(message, state: FSMContext):
    three_stationn = message.text
    await state.update_data(three_station=three_stationn)
    data = await state.get_data()
    three_station_data = data.get('three_station')
    three_station_answer = three_station_data.split("\n")
    print(three_station)
    print(three_station_answer)
    three_station_answer_zip = zip(three_station, three_station_answer)
    three_station_answer_list = list(three_station_answer_zip)
    for i in range(len(three_station_answer_list)):
        if three_station_answer_list[i][1] in three_station_answer_list[i][0]:
            cur.execute("UPDATE data SET threestat = threestat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nЧтобы приступить к следующему заданию напишите боту /four_station",
                           parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.four_station_1)
async def start_data(message, state: FSMContext):
    four_station_1n = message.text
    await state.update_data(four_station_1=four_station_1n)
    data = await state.get_data()
    four_station_1_data = data.get('four_station_1')
    four_station_1_answer = four_station_1_data.split("\n")
    print(four_station[0])
    print(four_station_1_answer)
    four_station_1_answer_zip = zip(four_station[0], four_station_1_answer)
    four_station_1_answer_list = list(four_station_1_answer_zip)
    for i in range(len(four_station_1_answer_list)):
        if four_station_1_answer_list[i][1] == four_station_1_answer_list[i][0]:
            cur.execute("UPDATE data SET fourstat = fourstat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id, "<b>ЗАДАНИЕ №2</b>\n"
                                            "<b>Введите ответ в формате:\nслово\nслово\nслово</b>\n "
                                            "P.S. ответы только за второе задание!", parse_mode="HTML")
    await FSM.four_station_2.set()


@katana.message_handler(state=FSM.four_station_2)
async def start_data(message, state: FSMContext):
    four_station_2n = message.text
    await state.update_data(four_station_2=four_station_2n)
    data = await state.get_data()
    four_station_2_data = data.get('four_station_2')
    four_station_2_answer = four_station_2_data.split("\n")
    print(four_station[1])
    print(four_station_2_answer)
    four_station_2_answer_zip = zip(four_station[1], four_station_2_answer)
    four_station_2_answer_list = list(four_station_2_answer_zip)
    for i in range(len(four_station_2_answer_list)):
        if four_station_2_answer_list[i][1] == four_station_2_answer_list[i][0]:
            cur.execute("UPDATE data SET fourstat = fourstat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nЧтобы приступить к следующему заданию напишите боту /five_station",
                           parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.five_station_1)
async def start_data(message, state: FSMContext):
    five_station_1n = message.text
    await state.update_data(five_station_1=five_station_1n)
    data = await state.get_data()
    five_station_1_data = data.get('five_station_1')
    five_station_1_answer = five_station_1_data.split("-")
    print(five_station[0])
    print(five_station_1_answer)
    five_station_1_answer_zip = zip(five_station[0], five_station_1_answer)
    five_station_1_answer_list = list(five_station_1_answer_zip)
    for i in range(len(five_station_1_answer_list)):
        if five_station_1_answer_list[i][1] == five_station_1_answer_list[i][0]:
            cur.execute("UPDATE data SET fivestat = fivestat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id, "<b>ЗАДАНИЕ №2</b>\n"
                                            "<b>Введите ответ в формате: Буква-Буква-Буква</b>\n "
                                            "P.S. ответы только за второе задание!", parse_mode="HTML")
    await FSM.five_station_2.set()


@katana.message_handler(state=FSM.five_station_2)
async def start_data(message, state: FSMContext):
    five_station_2n = message.text
    await state.update_data(five_station_2=five_station_2n)
    data = await state.get_data()
    five_station_2_data = data.get('five_station_2')
    five_station_2_answer = five_station_2_data.split("-")
    print(five_station[1])
    print(five_station_2_answer)
    five_station_2_answer_zip = zip(five_station[1], five_station_2_answer)
    five_station_2_answer_list = list(five_station_2_answer_zip)
    for i in range(len(five_station_2_answer_list)):
        if five_station_2_answer_list[i][1] == five_station_2_answer_list[i][0]:
            cur.execute("UPDATE data SET fivestat = fourstat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nЧтобы приступить к следующему заданию напишите боту /six_station",
                           parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.six_station_1)
async def start_data(message, state: FSMContext):
    six_station_1n = message.text
    await state.update_data(six_station_1=six_station_1n)
    data = await state.get_data()
    six_station_1_data = data.get('six_station_1')
    six_station_1_answer = six_station_1_data.split("\n")
    print(six_station[0])
    print(six_station_1_answer)
    six_station_1_answer_zip = zip(six_station[0], six_station_1_answer)
    six_station_1_answer_list = list(six_station_1_answer_zip)
    for i in range(len(six_station_1_answer_list)):
        if six_station_1_answer_list[i][1] == six_station_1_answer_list[i][0]:
            cur.execute("UPDATE data SET sixstat = sixstat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id, "<b>ЗАДАНИЕ №2</b>\n"
                                            "<b>Введите ответ в формате:\nфраза\nфраза\nфраза</b>\n "
                                            "P.S. ответы только за второе задание!", parse_mode="HTML")
    await FSM.six_station_2.set()


@katana.message_handler(state=FSM.six_station_2)
async def start_data(message, state: FSMContext):
    six_station_2n = message.text
    await state.update_data(six_station_2=six_station_2n)
    data = await state.get_data()
    six_station_2_data = data.get('six_station_2')
    six_station_2_answer = six_station_2_data.split("\n")
    print(six_station[1])
    print(six_station_2_answer)
    six_station_2_answer_zip = zip(six_station[1], six_station_2_answer)
    six_station_2_answer_list = list(six_station_2_answer_zip)
    for i in range(len(six_station_2_answer_list)):
        if six_station_2_answer_list[i][1] == six_station_2_answer_list[i][0]:
            cur.execute("UPDATE data SET sixstat = sixstat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nЧтобы приступить к следующему заданию напишите боту /seven_station",
                           parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.seven_station)
async def start_data(message, state: FSMContext):
    seven_stationn = message.text
    await state.update_data(seven_station=seven_stationn)
    data = await state.get_data()
    seven_station_data = data.get('seven_station')
    seven_station_answer = seven_station_data.split("\n")
    print(seven_station)
    print(seven_station_answer)
    seven_station_answer_zip = zip(seven_station, seven_station_answer)
    seven_station_answer_list = list(seven_station_answer_zip)
    for i in range(len(seven_station_answer_list)):
        if seven_station_answer_list[i][1] in seven_station_answer_list[i][0]:
            cur.execute("UPDATE data SET sevenstat = sevenstat + 1 WHERE tg_id = ?", (message.chat.id,))
            conn.commit()
        else:
            pass
    roww = cur.execute(
        "SELECT onestat, twostat, threestat, fourstat, fivestat, sixstat, sevenstat  FROM data WHERE tg_id = ?",
        (message.chat.id,)).fetchone()
    row_sum = 0
    for i in range(len(roww)):
        row_sum += roww[i]
    cur.execute("UPDATE data SET allstat = ? WHERE tg_id = ?", (row_sum, message.chat.id))
    conn.commit()
    row = cur.execute(
        "SELECT onestat, twostat, threestat, fourstat, fivestat, sixstat, sevenstat, allstat  FROM data WHERE tg_id = ?",
        (message.chat.id,)).fetchone()

    await bot.send_message(message.chat.id,
                           "<b>Отлично! Данные успешно отправлены</b>✅ \nВы успешно выполнили все задание💞\n"
                           "<b>Через мгновение вам будут отправлены ваши баллы</b>(место будет оглашено чуть позже)\n",
                           parse_mode="HTML")
    await bot.send_message(message.chat.id, f"<b>Станция №1: </b>{row[0]}\n"
                                            f"<b>Станция №2: </b>{row[1]}\n"
                                            f"<b>Станция №3: </b>{row[2]}\n"
                                            f"<b>Станция №4: </b>{row[3]}\n"
                                            f"<b>Станция №5: </b>{row[4]}\n"
                                            f"<b>Станция №6: </b>{row[5]}\n"
                                            f"<b>Станция №7: </b>{row[6]}\n"
                                            f"<b>Общая сумма баллов: </b>{row[7]}\n",
                           parse_mode="HTML")
    await bot.send_message(message.chat.id, "<code>По всем тех. вопросам обращаться ко мне</code> - @katana_tm", parse_mode="HTML")
    await state.finish()


@katana.message_handler(state=FSM.fio)
async def start_data(message, state: FSMContext):
    fio = message.text
    await state.update_data(fio=fio)
    await bot.send_message(message.chat.id, "<b>Отлично!</b> Теперь введи свой класс⤵", parse_mode="HTML")
    await FSM.rank.set()


@katana.message_handler(state=FSM.rank)
async def start_data(message, state: FSMContext):
    first_name = message.chat.first_name
    username = message.chat.username
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_quest = KeyboardButton("Начать🔓")
    markup.add(start_quest)
    msg_id = message.chat.id
    rank = message.text
    await state.update_data(rank=rank)
    data = await state.get_data()
    fio = data.get('fio')
    rank = data.get('rank')
    cur.execute("UPDATE data SET fio = ?, rank = ? WHERE tg_id = ?", (fio, rank, msg_id,))
    conn.commit()
    await bot.send_message(-1001817537217, f"<b>{first_name}(@{username}) - Прошел регистрацию✅</b>", parse_mode="HTML")
    await bot.send_message(message.chat.id, "Великолепно✅ \nВы можете начать квест нажав на кнопку ниже",
                           parse_mode="HTML", reply_markup=markup)
    await state.finish()


executor.start_polling(katana)
