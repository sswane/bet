from termcolor import cprint

buy_in = round(float(input("Cost of buy in? ")), 2)
players = input("Names of players separated by space: ")
players_list = players.split()

pot = buy_in * len(players_list)

bets = dict()
for player in players_list:
    bets[player] = buy_in

cprint(f"Players & bets: {bets}", 'cyan')
cprint(f"Pot size: ${pot}", 'cyan')

winners = dict()
losers = dict()
evens = []
total_passed_in = 0
def end(name, amount_left):
    global total_passed_in 
    total_passed_in += amount_left
    total = amount_left - buy_in
    bets.update({name: total})
    if total > 0:
        winners[name] = total
        cprint(f"{name} won ${total}", 'green')
    elif total < 0:
        losers[name] = total
        total = abs(total)
        cprint(f"{name} lost ${total}", 'red')
    else:
        evens.append(name)
        cprint(f"{name} broke even", 'yellow')

for player in bets:
    amount_left = round(float(input("How much does " + player + " have left? ")), 2)
    end(player, amount_left)

if total_passed_in != pot:
    cprint("*** Please verify that your total buy in matches your total player input. ***", 'red')
    raise Exception("Those numbers don't add up...")
print(f"Totals after betting: {bets}")

# If a loser owes the same amount a winner won, then the loser should directly pay that winner.
for loser in list(losers.keys()):
    lost_amount = abs(losers.get(loser))
    for winner in list(winners.keys()):
        if winners.get(winner) == lost_amount:
            cprint(f"{loser} owes {winner} {winners.get(winner)}", 'red')
            del losers[loser]
            del winners[winner]

# All other losers should pay banker
if losers:
    for loser in losers:
        cprint(f"{loser} owes the bank ${lost_amount}", 'red')
# Banker should pay winners
if winners:
    for winner in winners:
        cprint(f"Banker owes {winner} ${winners.get(winner)}", 'red')

if evens:
    cprint(f"Remember that {evens} broke even, so they keep their money", 'yellow')