# common.py
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from gpt import translate_text
from keyboards.keyboards import language_keyboard

router = Router()


# Обрабатываем команду /start
@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    """Обрабатывает команду /start"""
    await state.clear()  # Очищаем прошлое состояние
    await message.answer("Выберите язык перевода:", reply_markup=language_keyboard)


# Обрабатываем выбор языка
@router.message(lambda message: message.text in ["Английский", "Немецкий"])
async def set_language(message: types.Message, state: FSMContext):
    """Запоминаем выбранный язык"""
    language_map = {"Английский": "английский", "Немецкий": "немецкий"}
    chosen_language = language_map.get(message.text)

    await state.update_data(language=chosen_language)  # Сохраняем язык в state
    await message.answer(f"Вы выбрали {chosen_language}. Введите текст для перевода.")


# Обрабатываем текст для перевода
@router.message()
async def handle_translation(message: types.Message, state: FSMContext):
    """Переводит текст с выбранным языком"""
    data = await state.get_data()
    target_language = data.get("language")

    if target_language:
        translated_text = await translate_text(message.text, target_language)
        await message.answer(f"Перевод ({target_language}):\n{translated_text}")
    else:
        await message.answer("Сначала выберите язык перевода командой /start")
