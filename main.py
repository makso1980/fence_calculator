# Калькулятор расчёта ограждения (забора) для частного дома (v.0)

# ------------Импорт необходимых библиотек-----------------
import math

# -------------Переменные для хранения данных ----------------
segments = {}
fence_height = 0
l_sheet = 0
l_useful = 0

# -------------Блоки функций----------------------------------
def quantity_sheet_for_segment(segment_length):
    quantity_sheet = 0
    sheet_quantity = segment_length / l_useful
    quantity_sheet += sheet_quantity
    return quantity_sheet

def profile_sheet_calc(number_of_segments_calc):
    full_quantity_sheet_calc = 0
    for num in range(1, number_of_segments_calc + 1):
        user_length_segment = input('   Введите длину ' + str(num) + '-го отрезка в метрах: ')
        length_segment = user_length_segment.replace(',', '.')
        segments[('side_' + str(num))] = math.ceil(float(length_segment))
        full_quantity_sheet_calc += math.ceil(quantity_sheet_for_segment(segments[('side_' + str(num))]))
    return full_quantity_sheet_calc

# ------------Основной блок программы-----------------
print('Для подсчёта необходимых материалов при расчётах\
\nсооружения забора из профлиста, ответьте на следующие вопросы:')

# Данный параметр пока бесполезен и будет задействован в программе в дальнейшем, при вводе функции подсчёта металла
# для стоек и продольных балок.
type_of_perimetr = input('\n1. Ваш забор будет иметь замкнутый периметр? \n\
    "Да" - если периметр будет замкнутый. \n\
    "Нет" - если периметр будет с разрывом. \n\
    Введите ответ: ')

print('\n2. Выберите марку профнастила для ограждения из списка представленного ниже:\n\
    1 - Лист марки "С8"\n\
    2 - Лист марки "C20"\n\
    3 - Лист марки "C21"\n\
    4 - Лист марки "C44"\n\
    5 - Лист марки "HC35"')
sheet_type = int(input('    Введите номер марки профлиста: '))
if sheet_type == 1:
    l_sheet = 1.2
    l_useful = 1.15
elif sheet_type == 2:
    l_sheet = 1.15
    l_useful = 1.1
elif sheet_type == 3:
    l_sheet = 1.051
    l_useful = 1
elif sheet_type == 4:
    l_sheet = 1.047
    l_useful = 1
elif sheet_type == 5:
    l_sheet = 1.06
    l_useful = 1.11

h_user_input = input('\n3. Введите желаемую высоту ограждения в метрах: ')
h_sheet = float(h_user_input.replace(',', '.'))

number_of_segments = int(input('\n4. Введите количество отрезков ограждения: '))

full_quantity_sheet = profile_sheet_calc(number_of_segments)

sheet_cost_user_input = input('\n5. Введите стоимость одного профлиста в рублях: ')
sheet_cost = float(sheet_cost_user_input.replace(',', '.'))
cost = '{:,.0f}'.format(sheet_cost * full_quantity_sheet).replace(',', '`')

# --------------Блок вывода информации---------------------------
print()
print('Необходимое количество целых листов:', full_quantity_sheet, 'шт.')
print('Площадь профлиста, всего:', round((full_quantity_sheet * h_sheet * l_sheet), 2), 'м2')
print('Стоимость профлиста для строительства ограждения', cost, 'руб.')
