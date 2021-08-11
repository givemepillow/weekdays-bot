from aiogram.types import ReplyKeyboardMarkup

from .buttons import (
    represent_btn, settings_btn, main_menu_btn,
    first_view_btn, second_view_btn,
    edit_holidays_btn, reset_holidays_btn,
    go_back_btn, holidays_btn, edit_holidays_cancel_btn,
    edit_holidays_save_btn, yes_btn, no_btn
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
).add(first_view_btn, second_view_btn, holidays_btn, go_back_btn)

# Settings submenu.
settings_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(edit_holidays_btn, reset_holidays_btn, go_back_btn)

# Go to main menu
go_back_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(go_back_btn)

# Edit calendar menu.
edit_calendar_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(edit_holidays_save_btn, edit_holidays_cancel_btn)


are_u_sure_submenu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
).add(yes_btn, no_btn)
