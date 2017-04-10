capital = {"Россия": "Москва", "Китай": "Пекин", "Япония": "Токио", "Корея": "Сеул"}

for n in range(5):
    state = input("Введите страну: ")
    if state in capital:
        print("Знаю! Столица -", capital[state])
    else:
        new_capital = input("Не знаю... Скажите, какая столица: ")
        capital[state] = new_capital

for state in capital:
    answer = input("Введите столицу государства " + state + ": ")
    if answer == capital[state]:
        print("Вы угадали!")
    else:
        print("О-ла-ла! К сожалению, нет! Столица", state, "—", capital[state])
