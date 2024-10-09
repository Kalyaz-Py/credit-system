import random
import json
import os

newNumb = ' '

def CreateCardNumber(cardNumb):
    global newNumb
    if cardNumb == cardNumb:
        cardNumb = []

        # Генерация номера карты состоящий из 1 цифр
        for i in range(1):
            cardNumb.append(str(random.randint(0,9)))
        newNumb = ''.join(cardNumb)

        card_data = loadCardData()

        if newNumb not in card_data:
            card_data[newNumb] = {"balance": 0} # Начальный баланс
            saveCardData(card_data)
    else: 
        newNumb == cardNumb
        
    return newNumb

def loadCardData():
    """Загрузка данных карт из файла JSON"""
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as f:
            return json.load(f)
    return {}

def saveCardData(card_data):
    """Сохранение данных карт в файл JSON"""
    with open("cards.json", "w") as f:
        json.dump(card_data, f, indent=4)

def updateBalance(cardNumber, amount):
    """Обновление баланса карты"""
    card_data = loadCardData()
    
    if cardNumber in card_data:
        card_data[cardNumber]["balance"] += amount
        saveCardData(card_data)
        print(f'Баланс карты {cardNumber} обновлен на {amount}. Новый баланс: {card_data[cardNumber]["balance"]}')
    else:
        print(f'Карта {cardNumber} не найдена.')

# Пример использования
# CreateCardNumber([0])

print(f'Новый номер карты: {newNumb}')
updateBalance(0, 50000)  # Уменьшаем баланс на 10








