def main_menu():
    return {
        "reply_markup": {"inline_keyboard": [[{"text": "Army", "callback_data": "ArmyMenu"},
                                              {"text": "Info", "callback_data": "InfoMenu"}],
                                             [{"text": "Balance", "callback_data": "BalanceMenu"},
                                              {"text": "Admin", "callback_data": "AdminMenu"}]]}}


def army_menu():
    return {
        "reply_markup": {"inline_keyboard": [[{"text": "Balance", "callback_data": "BalanceMenu"},
                                              {"text": "BuyInfantry", "callback_data": "BuyInfantry"}],
                                             [{"text": "BuyTank", "callback_data": "BuyTank"},
                                              {"text": "BuyAirplane", "callback_data": "BuyAirplane"}],
                                             [{"text": "BuyFleet", "callback_data": "BuyFleet"},
                                              {"text": "Back", "callback_data": "BackMenu"}]]}}


def admin_menu():
    return {
        "reply_markup": {"inline_keyboard": [[{"text": "Back", "callback_data": "BackMenu"},
                                              {"text": "Info", "callback_data": "AdminInfo"}],
                                             [{"text": "ChangeBalance", "callback_data": "ChangeBalance"},
                                              {"text": "DeleteUser", "callback_data": "DeleteUser"}]]}}