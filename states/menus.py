from aiogram.dispatcher.filters.state import StatesGroup, State


class Menus(StatesGroup):
    main_menu = State()
    settings_submenu = State()
    represent_submenu = State()
    calendar = State()
    are_u_sure = State()
    reset_complete = State()
    representation_months = State()
    representation_year = State()
