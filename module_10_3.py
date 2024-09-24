# Задача "Банковские операции"
import threading, random, time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.count = 0
        self.number_of_trans = 100
    def deposit(self):    # Будет совершать 100 транзакций пополнения средств.
        for i in range(self.number_of_trans):
            self.count += 1
            self.money = random.randrange(50, 500)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.balance <= 500 and self.lock.locked():
                self.lock.release()
                self.balance += self.money
                self.lock.acquire()
            else:
                self.balance += self.money
            print(f'Пополнение: {self.money}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):     # Будет совершать 100 транзакций снятия.
        for i in range(self.number_of_trans):
            self.money = random.randrange(50, 500)
            print(f'Запрос на: {self.money}')
            if self.money <= self.balance:
                self.balance = self.balance - self.money
                print(f'Снятие {self.money}. Баланс {self.balance}')
            elif self.count == self.number_of_trans:
                print('Запрос отклонён')
            elif self.money > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.01)

bk = Bank()
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')