buy_in = int(input("Cost of buy in? "))
players = input("Names of players separated by space: ")
players_list = players.split()

pot = buy_in * len(players_list)

bets = dict()
for player in players_list:
    bets[player] = buy_in

print(f"Players & bets: {bets}")
print(f"Pot size: ${pot}")

winners = dict()
losers = dict()
def end(name, amount_left):
    total = amount_left - buy_in
    bets.update({name: total})
    if total > 0:
        winners[name] = total
        print(f"{name} won ${total}")
    elif total < 0:
        losers[name] = total
        total = abs(total)
        print(f"{name} lost ${total}")
    else:
        print(f"{name} broke even")

for player in bets:
    amount_left = int(input("How much does " + player + " have left? "))
    end(player, amount_left)

print(f"Totals after betting: {bets}")

while losers:
    highest_winner = max(winners, key=bets.get)
    biggest_loser = min(losers, key=bets.get)

    diff = winners.get(highest_winner) + losers.get(biggest_loser)
    if diff >= 0:
        print(f"{biggest_loser} owes all their money")
        del losers[biggest_loser]
        winners.update({highest_winner: winners.get(highest_winner) - diff})
        if diff == 0:
            print(f"{biggest_loser} owes {highest_winner} ${winners.get(highest_winner)}")
        else:
            print(f"{biggest_loser} owes {highest_winner} ${diff}")
    else:
        amount = abs(diff)
        print(f"{biggest_loser} owes {highest_winner} ${winners.get(highest_winner)}")
        print(f"{highest_winner} has been paid off and {biggest_loser} has ${amount} left to pay out to other winners")
        del winners[highest_winner]
        losers.update({biggest_loser: diff})
print(f"{highest_winner} has been paid off. All winners have been paid off.")