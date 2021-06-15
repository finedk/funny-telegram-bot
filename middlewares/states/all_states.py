from aiogram.dispatcher.filters.state import StatesGroup, State

class gender_person_in_photo_state(StatesGroup):
    step1 = State()
    step2 = State()

class ping_state(StatesGroup):
    step1 = State()
    step2 = State()
