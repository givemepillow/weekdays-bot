from aiogram.dispatcher.filters.state import StatesGroup, State


class Menus(StatesGroup):
    main_menu = State()
    settings_submenu = State()
    represent_submenu = State()
