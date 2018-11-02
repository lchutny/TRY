# Strategy Game

def is_hot(n):
    move1 = float(n-1)
    move2 = float(n/2)
    if n <2:
        return False
    elif n = 2:
        return True
    else:
        if is_hot(move1) != is_hot(move2):
            return True
        else:
            return False


# Check input > 0,
if
# Get the state of the game:
