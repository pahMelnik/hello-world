import random

number_of_players = 1  # Кол-во ботов
base_dice_number = 6  # кол-во кубиков у игрока изначально
how_mach_dices_bot = base_dice_number
how_mach_dices_player = base_dice_number
bot = {a: 0 for a in range(1, 7)}
player = {a: 0 for a in range(1, 7)}


def roll(who, how_mach):
    for k in [random.randrange(1, 7) for j in range(how_mach)]:
        who[k] += 1


def blind_bot(who):

    if who[blind[1]] > blind[0]:
        blind[0] += 1
        return blind
    else:
        return 'check'


roll(bot, how_mach_dices_bot)
roll(player, how_mach_dices_player)
print(bot, player)
print('roll result :', player)
blind = input('your blind? how mach, number: ').split()
for i in range(len(blind)):
    blind[i] = int(blind[i])
print(blind_bot(bot))
