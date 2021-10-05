import random

class Thrower:
    """
    A code template that facilitates the throwing of dice as directed
    by the director.

    Attributes:
    num_throws (int): determines how many times the player has rolled the dice.
    dice (list): sets a list of dice to be used in important game functions.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Thrower): an instance of Thrower.
        """
        self.num_throws = 0
        self.dice = []

    def can_throw(self):
        """Checks to see if the user can throw again

        Args:
            self (Thrower): an instance of Thrower.
        """

        if 5 in self.dice or 1 in self.dice or self.num_throws < 0:
            return True
        else:
            return False

    def get_points(self):
        """Checks to see how many points the user scored this round.

        Args:
            self (Thrower): an instance of Thrower.
        """
        total_points = 0
        for i in self.dice:
            if i == 5:
                total_points += 50
            elif i == 1:
                total_points += 100
        return total_points

    def throw_dice(self):
        """Randomly generates an integer for 5 separate dice in the range of 1-6

        Args:
            self (Thrower): an instance of Thrower.
        """
        self.dice = [random.randint(1 , 6) for _ in range(5)]
        self.num_throws += 1

