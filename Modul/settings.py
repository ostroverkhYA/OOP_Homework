class Model:
    user_ball = 0
    user_health = 5
    rand_health = 5
    rand_level = 1
    level_up = rand_health

    def play(self):
        import random
        while True:
            user = input("Зараз атакуємо оберіть чарівник, рицар або злодій (Натисніть ч, р або з): ")
            list_play = ['ч', 'р', 'з']
            if user == 'с':
                print('Кількість балів - ', self.user_ball, ". Кількість здоров'я - ", self.user_health,
                      'Рівень ворога -',self.rand_level, ". Кількість здоров'я ворога - ", self.rand_health, ".")
            if user in list_play:
                rand = random.choice(list_play)
                if rand == 'ч' and user == 'з':
                    self.user_ball += 1
                    self.rand_health -= 1
                    print('ВАША АТАКА БУЛА УСПІШНОЮ!')
                if rand == 'р' and user == 'ч':
                    self.user_ball += 1
                    self.rand_health -= 1
                    print('ВАША АТАКА БУЛА УСПІШНОЮ!')
                if rand == 'з' and user == 'р':
                    self.user_ball += 1
                    self.rand_health -= 1
                    print('ВАША АТАКА БУЛА УСПІШНОЮ!')
                if rand == 'ч' and user == 'р':
                    print('ВАША АТАКА БУЛА ПРОВАЛЬНОЮ!')
                if rand == 'з' and user == 'ч':
                    print('ВАША АТАКА БУЛА ПРОВАЛЬНОЮ!')
                if rand == 'р' and user == 'з':
                    print('ВАША АТАКА БУЛА ПРОВАЛЬНОЮ!')
                if rand == 'р' and user == 'р':
                    print('НІЧИЯ!')
                if rand == 'з' and user == 'з':
                    print('НІЧИЯ!')
                if rand == 'ч' and user == 'ч':
                    print('НІЧИЯ!')
                user = input("Зараз захищяємось оберіть чарівник, рицар або злодій (Натисніть ч, р або з): ")
                list_play = ['ч', 'р', 'з']
                if user in list_play:
                    rand = random.choice(list_play)
                    if rand == 'ч' and user == 'з':
                        print('ВАШ ЗАХИСТ ПРОЙШОВ УСПІШНО!')
                    if rand == 'р' and user == 'ч':
                        print('ВАШ ЗАХИСТ ПРОЙШОВ УСПІШНО!')
                    if rand == 'з' and user == 'р':
                        print('ВАШ ЗАХИСТ ПРОЙШОВ УСПІШНО!')
                    if rand == 'ч' and user == 'р':
                        self.user_health -= 1
                        print('ВАШ ЗАХИСТ ПРОВАЛЕНО!')
                    if rand == 'з' and user == 'ч':
                        self.user_health -= 1
                        print('ВАШ ЗАХИСТ ПРОВАЛЕНО!')
                    if rand == 'р' and user == 'з':
                        self.user_health -= 1
                        print('ВАШ ЗАХИСТ ПРОВАЛЕНО!')
                    if rand == 'р' and user == 'р':
                        print('НІЧИЯ!')
                    if rand == 'з' and user == 'з':
                        print('НІЧИЯ!')
                    if rand == 'ч' and user == 'ч':
                        print('НІЧИЯ!')
                if self.rand_level == 2 and self.rand_health == 0:
                    raise GameOver
                if self.rand_health == 0:
                    self.user_ball += 5
                    print('you win''Кількість балів - ', self.user_ball, ". Кількість здоров'я - ", self.user_health,
                          'Рівень переможеного ворога', self.rand_level, ".")
                    self.rand_level += 1
                    self.level_up *= self.rand_level
                    self.rand_health += self.level_up
                    continue
                elif user == 'с':
                    print('Кількість балів - ', self.user_ball, ". Кількість здоров'я - ", self.user_health, 'Рівень ворога -',
                                   self.rand_level, ". Кількість здоров'я ворога - ", self.rand_health, ".")
                if self.user_health == 0:
                    raise GameLose


class GameOver(Exception):
    ...


class GameLose(Exception):
    ...
