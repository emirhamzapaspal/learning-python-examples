print("rock,paper,scissors")
p1 = input('p1 choose:')
p2 = input('p2 choose:')
if p1 == "rock" and p2 == "scissors":
    print("p1 won")
elif p1 == "paper" and p2 == "rock":
    print("p1 won")
elif p1 == "scissors" and p2 == "paper":
    print("p1 won")
else:
    print("p2 won")