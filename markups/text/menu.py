from aiogram.types import ReplyKeyboardMarkup

from .buttons import (
    represent_btn, settings_btn, main_menu_btn,
    first_view_btn, second_view_btn,
    edit_holidays_btn, reset_holidays_btn,
    go_back_btn, info_btn
)

# Main menu.
main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(represent_btn, settings_btn)

# Represent submenu.
represent_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=3
).add(first_view_btn, second_view_btn, info_btn, go_back_btn)

# Settings submenu.
settings_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(edit_holidays_btn, reset_holidays_btn, go_back_btn)

# Go to main menu
default_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(main_menu_btn, go_back_btn)
