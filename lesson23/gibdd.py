def calculate_inspectors_salary():
    """
    Считывая с потока ввода номера автомобилей и их скорости,
    вычисляет итоговую выручку инспектора (сумму всех штрафов).
    :return: тип int, неотрицательное число - суммарная выручка
    """
    salary = 0
    reg_number, velocity = read_auto_data()
    while is_not_chief_reg_number(reg_number):
        if speed_violation(velocity):
            salary += tax_by_reg_number(reg_number)
        reg_number, velocity = read_auto_data()
    return salary


def read_auto_data():
    """
    Считывет с потока ввода два слова, разделённые пробелом, из одной строки.
        Первое слово - номер автомобиля (предполагается 6 символов).
        Второе слово - скорость.
    :return: кортеж (reg_number, velocity), при этом:
        reg_number - тип str, длина 6 символов - номер автомобиля
        velocity - тип float, неотрицательное число - скорость автомобиля
    """
    reg_number, velocity = input().split()
    velocity = float(velocity)
    assert len(reg_number) == 6, "Плохой регистрационный номер " + reg_number
    return reg_number, velocity


def is_not_chief_reg_number(reg_number):
    """
    Проверяет, является ли данный номер номером начальника или нет.
    :param reg_number: тип str, номер автомобиля (предполагается 6 символов).
    :return: тип bool - True, если данный номер не является номером начальника
    """
    return False  #FIXME


def speed_violation(velocity):
    """
    Проверяет, было ли нарушение скоростного режима на дороге.
    :param velocity: тип float, скорость в километрах час
    :return: bool - True, если нарушение ПДД установлено
    """
    pass  #FIXME


def tax_by_reg_number(reg_number):
    """
    Рассчёт штрафа по "крутости" автомобильного номера.
    Три совпадают - 5000 рублей, две совпадают - 1000 рублей, все разные - 500 рублей.
    :param reg_number: тип str, номер автомобиля
                (предполагается 6 символов, цифры в индексах с 1-го по 3-й включ.).
    :return:
    """
    pass  #fIXME


answer = calculate_inspectors_salary()
print(answer)
