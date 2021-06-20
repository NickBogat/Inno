COLON = ":"
DOT = "."
AVAILABLE_PARTS_DAY = ["утра", "вечера", "дня", "ночи"]
AVAILABLE_PRETEXTS = ["в", "на", "около", "после"]
"""Это время утреннее"""
TRANSFER_TIME_MORNING = {
    "1": "01:00",
    "2": "02:00",
    "3": "03:00",
    "4": "04:00",
    "5": "05:00",
    "6": "06:00",
    "7": "07:00",
    "8": "08:00",
    "9": "09:00",
    "10": "10:00",
    "11": "11:00",
    "12": "12:00",
}
"""Это время вечерне"""
TRANSFER_TIME_EVENING = {
    "1": "13:00",
    "2": "14:00",
    "3": "15:00",
    "4": "16:00",
    "5": "17:00",
    "6": "18:00",
    "7": "19:00",
    "8": "20:00",
    "9": "21:00",
    "10": "22:00",
    "11": "23:00",
    "12": "0:00",
}
"""Это имена месацев с количеством дней и порядеовым номером"""
AVAILABLE_MONTH = {
    "января": [1, 31],
    "февраля": [2, 28],
    "марта": [3, 31],
    "апреля": [4, 30],
    "мая": [5, 31],
    "июня": [6, 30],
    "июля": [7, 31],
    "августа": [8, 31],
    "сентября": [9, 30],
    "октября": [10, 31],
    "ноября": [11, 30],
    "декабря": [12, 31],
}
"""Это соотношение количества дней в месяцах"""
MONTHS = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}


class FindTime:
    """
    Этот класс ищет xx.xx такой шаблон времени и xx --я
    и такой шаблон, и сохраняет в MASSIVE_STRINGS = [], MASSIVE_RESULTS = []
    """

    def __init__(self):
        self.MASSIVE_STRINGS = []
        self.MASSIVE_RESULTS = []

    def search_time(self, sentence):
        string = sentence.split()
        self.MASSIVE_STRINGS.append(string)
        temp_answer_time = []
        temp_answer_day = []
        for word in string:
            if DOT in word and not (word.isalpha()):
                temp_time = word.split(DOT)
                if temp_time[1].isdigit():
                    if 1 <= int(temp_time[1]) <= 12:
                        if 1 <= int(temp_time[0]) <= MONTHS[
                            temp_time[1]] and 1 <= \
                                int(temp_time[1]) <= 12:
                            temp_answer_day.append(word)
            elif COLON in word:
                temp_time = word.split(COLON)
                if 0 <= int(temp_time[0]) <= 24 and 0 <= int(
                        temp_time[1]) <= 60:
                    self.MASSIVE_RESULTS.append(word)
                    temp_answer_time.append(word)
            elif word in AVAILABLE_PARTS_DAY:
                temp_index = string.index(word)
                if temp_index >= 1:
                    temp_time = string[temp_index - 1]
                    if 1 <= int(temp_time) < 12:
                        if word == "вечера" or word == "дня":
                            result = TRANSFER_TIME_EVENING[temp_time]
                            self.MASSIVE_RESULTS.append(result)
                            temp_answer_time.append(result)
                        else:
                            result = TRANSFER_TIME_MORNING[temp_time]
                            self.MASSIVE_RESULTS.append(result)
                            temp_answer_time.append(result)
                    elif int(temp_time) == 12:
                        if word == "вечера" or word == "ночи":
                            result = "0:00"
                            self.MASSIVE_RESULTS.append(result)
                            temp_answer_time.append(result)
                        elif word == "дня":
                            result = "12:00"
                            self.MASSIVE_RESULTS.append(result)
                            temp_answer_time.append(result)
            elif word in AVAILABLE_MONTH.keys():
                temp_index = string.index(word)
                if temp_index >= 1:
                    temp_day = string[temp_index - 1]
                    if 1 <= int(temp_day) <= AVAILABLE_MONTH[word][1]:
                        temp_answer_day.append(
                            f"{temp_day}.{AVAILABLE_MONTH[word][0]}")
        if len(temp_answer_time) == 0 and len(temp_answer_day) == 0:
            print("-")
        else:
            print(
                f"{sentence} | {' '.join(temp_answer_time)}"
                f"{' '.join(temp_answer_day)}")


example = FindTime()
example.search_time("13.13 - это что?")
