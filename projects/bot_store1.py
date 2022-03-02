import sqlite3, logging, string, json, os
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token='5185200513:AAG0Alrfmdz_lawgs-gveGrzHZTZ-YDc6Jw')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Hey)\nWelcome to thekhachik's store :3", reply_markup=kb_start)

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('/pics')
kb2 = KeyboardButton('/notes')
kb3 = KeyboardButton('/links')
kb_start.row(kb1, kb2, kb3)

x = [InlineKeyboardButton(text="🔵Telegram", url='https://t.me/thekhachik'),
     InlineKeyboardButton(text="🔴Instagram", url='https://www.instagram.com/thekhachik/?hl=ru')]
y = [InlineKeyboardButton(text="⚫Github️", url='https://github.com/thekhachik'), InlineKeyboardButton(text="🔵VK", url='https://vk.com/thekhachik')]
kb_links = InlineKeyboardMarkup(row_width=1)
kb_links.row(*y).row(*x).insert(InlineKeyboardButton(text="⚪Mirea️", url='https://online-edu.mirea.ru/user/profile.php?id=40935'))
@dp.message_handler(commands=["links"])
async def links(message: types.Message):
    await message.answer("Links", reply_markup=kb_links)

kb_pics = ReplyKeyboardMarkup(resize_keyboard=True)
kb11 = KeyboardButton('/show_pics')
kb12 = KeyboardButton('/add_pic')
kb13 = KeyboardButton('/delete_pic')
kb14 = KeyboardButton("/back")
kb_pics.row(kb11, kb12, kb13, kb14)
@dp.message_handler(commands=["pics"])
async def pics(message: types.Message):
    await message.answer("Choose command🖤",reply_markup=kb_pics)

    
class FSMAdmin(StatesGroup):
    photo= State()
    description = State()

def sql_start_pics():
    global base, cur
    base = sqlite3.connect("pics.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute('CREATE TABLE IF NOT EXISTS pics(img TEXT, description TEXT)')
    base.commit()

async def sql_add_pics(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO pics VALUES (?, ?)", tuple(data.values()))
        base.commit()
        
async def sql_show_pics(message):
    for ret in cur.execute('SELECT * FROM pics').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], ret[1])

async def sql_read():
    return cur.execute('SELECT * FROM pics').fetchall()

async def sql_delete_pic(data):
    cur.execute('DELETE FROM pics WHERE description == ?', (data,))
    base.commit()

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True) #, one_time_keyboard=True
kb = KeyboardButton('/cancel')
kb_cancel.add(kb)
@dp.message_handler(state="*", commands=['cancel'])
@dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Cancel😝", reply_markup=kb_pics)

@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as dictionary: #открываем словарь
        dictionary['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Write description", reply_markup=kb_cancel) 

@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as dictionary:
        dictionary['description'] = message.text
    #async with state.proxy() as dictionary:
     #   await message.reply(str(dictionary))
    await message.answer("Great💋", reply_markup=kb_pics)
    await sql_add_pics(state)
    await state.finish()

@dp.message_handler(commands=["show_pics"])
async def show_pics(message: types.Message):
    await sql_show_pics(message)
    await message.answer("Don't show it to anyone😂", reply_markup=kb_pics)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith("del "))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sql_delete_pic(callback_query.data.replace("del ", ""))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} was deleted', show_alert=True)

@dp.message_handler(commands=["delete_pic"])
async def delete_pic(message: types.Message):
    read = await sql_read()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0])
        await bot.send_message(message.from_user.id, f"{ret[1]}", reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton("Delete", callback_data=f'del {ret[1]}')))
        
@dp.message_handler(commands=['add_pic'], state=None)
async def add_pic(message: types.Message):
    await FSMAdmin.photo.set() #Переключение с обычного в машинное состояние 
    await message.answer("Upload photo", reply_markup=kb_cancel)

@dp.message_handler(commands=['back'])
async def back(message: types.Message):
    await message.answer("⬅️Back", reply_markup=kb_start)


kb_notes = ReplyKeyboardMarkup(resize_keyboard=True)
kb111 = KeyboardButton('/show_notes')
kb121 = KeyboardButton('/add_note')
kb131 = KeyboardButton('/delete_note')
kb141 = KeyboardButton("/back")
kb_notes.row(kb111, kb121, kb131, kb141)
@dp.message_handler(commands=["notes"])
async def notes(message: types.Message):
    await message.answer("Choose command🖤",reply_markup=kb_notes)

class FSMAdmin1(StatesGroup):
    description1 = State()

def sql_start_notes():
    global base1, cur1
    base1 = sqlite3.connect("notes.db")
    cur1 = base1.cursor()
    if base1:
        print("( 1 ) Data base connected OK!")
    base1.execute('CREATE TABLE IF NOT EXISTS notes(description1 VARCHAR(700))')
    base1.commit()

async def sql_add_note(state):
    async with state.proxy() as data:
        cur1.execute("INSERT INTO notes VALUES (?)", tuple(data.values()))
        base1.commit()
        
async def sql_show_notes(message):
    for ret in cur1.execute('SELECT * FROM notes').fetchall():
        await bot.send_message(message.from_user.id, ret[0]) #message.from_user.id,

async def sql_read1():
    return cur1.execute('SELECT * FROM notes').fetchall()

async def sql_delete_note(data):
    cur1.execute('DELETE FROM notes WHERE description1 == ?', (data,))
    base1.commit()

kb_cancel1 = ReplyKeyboardMarkup(resize_keyboard=True) #, one_time_keyboard=True
kb01 = KeyboardButton('/cancel.')
kb_cancel1.add(kb01)
@dp.message_handler(state="*", commands=['cancel.'])
@dp.message_handler(Text(equals="cancel.", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state1 = await state.get_state()
    if current_state1 is None:
        return
    await state.finish()
    await message.answer("Cancel😝", reply_markup=kb_notes)

@dp.message_handler(state=FSMAdmin1.description1)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as dictionary:
        dictionary['description'] = message.text
    #async with state.proxy() as dictionary:
     #   await message.reply(str(dictionary))
    await message.answer("Great💋", reply_markup=kb_notes)
    await sql_add_note(state)
    await state.finish()

@dp.message_handler(commands=["show_notes"])
async def show_notes(message: types.Message):
    await sql_show_notes(message)
    await message.answer("- Don't show it to anyone😂", reply_markup=kb_notes)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith("del "))
async def del_callback_run1(callback_query: types.CallbackQuery):
    await sql_delete_note(callback_query.data.replace("del ", ""))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} was deleted', show_alert=True)

@dp.message_handler(commands=["delete_note"])
async def delete_note(message: types.Message):
    read = await sql_read1()
    for ret in read:
        #await bot.send_photo(message.from_user.id, ret[0])
        await bot.send_message(message.from_user.id, f'''{ret[0]}''', reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton("Delete", callback_data=f'''del {ret[0]}''')))
        
@dp.message_handler(commands=['add_note'], state=None)
async def add_note(message: types.Message):
    await FSMAdmin1.description1.set() #Переключение с обычного в машинное состояние 
    await message.answer("Write New Note!", reply_markup=kb_cancel1)


async def on_startup(_):
    print("Bot is online")
    sql_start_pics()
    sql_start_notes()

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
