import random


def is_valid_edge(left, right):
    if left.isdigit() and right.isdigit():
        if int(left) > int(right) or int(left) == int(right):
            return False
        else:
            return True
    else:
        return False


def is_valid(text, left, right):
    if text.isdigit():
        text = int(text)
        left = int(left)
        right = int(right)
        if left <= text <= right:
            return True
        else:
            return False
    else:
        return False


again = 'так'
print("Ласкаво просимо в числову вгадайку")
while again.lower() == 'так':
    counter = 0
    left = input("Введіть початок проміжку:")
    right = input("Введіть кінець проміжку:")

    while not is_valid_edge(left, right):
        print("Ви ввели неправильні межі!")
        left = input("Введіть початок проміжку:")
        right = input("Введіть кінець проміжку:")
    else:
        left = int(left)
        right = int(right)
    number = random.randint(left, right)
    while True:
        your_choise = input("Введіть число від " + str(left) + " до " + str(right) + ":")
        if is_valid(your_choise, left, right):
            your_choise = int(your_choise)
            counter += 1
            if your_choise < number:
                print('Ваше число менше ніж задумане, спробуйте ще раз.')
            elif your_choise > number:
                print('Ваше число більше ніж задумане, спробуйте ще раз.')
            else:
                print('Ви вгадали, вітаємо!')
                print('Вам знадобилось стільки спроб:' + str(counter))
                break
        else:
            print("Ви ввели неправильне число! Введіть число від " + str(left) + " до " + str(right) + ".")
    again = input("Бажаєте зіграти ще раз? Так/Ні")
print('Дякуємо за гру! Ще побачимось...')
