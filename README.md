# bet
Bet with friends with least number of payouts. Not necessary to pay the pot upfront. 

`pip3 install termcolor` yeah, I wanted colored output :)

`python3 code.py`

Example:
```
Cost of buy in? 10
Names of players separated by space: Becca Rob Steph Sarah Arefeen Nehreen
Players & bets: {'Becca': 10.0, 'Rob': 10.0, 'Steph': 10.0, 'Sarah': 10.0, 'Arefeen': 10.0, 'Nehreen': 10.0}
Pot size: $60.0
How much does Becca have left? 11
Becca won $1.0
How much does Rob have left? 4.50
Rob lost $5.5
How much does Steph have left? 10
Steph broke even
How much does Sarah have left? 12
Sarah won $2.0
How much does Arefeen have left? 7
Arefeen lost $3.0
How much does Nehreen have left? 15.5
Nehreen won $5.5
Totals after betting: {'Becca': 1.0, 'Rob': -5.5, 'Steph': 0.0, 'Sarah': 2.0, 'Arefeen': -3.0, 'Nehreen': 5.5}
Rob owes Nehreen 5.5
Arefeen owe's the bank $3.0
Banker owes Becca $1.0
Banker owes Sarah $2.0
Remember that ['Steph'] broke even, so they keep their money
```

## Getting started
### Requirements
- Python3
- venv `pip3 install virtualenv` then `virtualenv --python=python3.9` (these will only need to be done once)

### Activate virtual environment & run program
```sh
source venv/bin/activate
pip install termcolor
python code.py
```

> It's also possible to skip the virtual env & just run the commands but could interfere with your other python projects if they use the same packages. 

### End venv
`deactivate`