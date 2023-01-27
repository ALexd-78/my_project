def go_upper_str():
    """ принимает на вход строку и возвращает её со всеми заглавными буквами """
    user_input = input("Введите строку")
    upper_str = user_input.upper()
    return upper_str


def go_title_str():
    """делает заглавными первые буквы каждого слова в строке, поступившей на вход """
    user_input = input("Введите строку")
    title_str = user_input.title()
    return title_str
