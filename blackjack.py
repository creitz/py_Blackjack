from decimal import Decimal

from player import Player
from utils import get_integer_input

class BlackJack():

    # The starting amount of money for each player, in dollars
    DEFAULT_START_DOLLARS = Decimal(1000)

    def play(self):
        """
        The entrypoint for the Blackjack class. Play the game!
        """

        # Get the number of players we want to play with
        num_players = self.ask_num_players()
        if num_players == 0:
            # No players :) Game is over!
            print('Cool, you decided to go touch grass instead. Game over!')
            return

        players = [Player(player_number=i+1, start_dollars=self.DEFAULT_START_DOLLARS)
                   for i in range(num_players)]
        self.get_bet(player=players[0])

    def get_bet(self, player: Player):
        """
        Prompts the user to enter a bet amount as an integer for the given player, and returns
        the amount once an integer is input.

        Args:
            player (Player): The player for which to get the bet

        Returns:
            int: The number of dollars input
        """
        blurb = ('Place bet for player {}. Input must be an integer. ${} remaining'
                 .format(player.player_number, player.dollars_remaining))
        prompt = '$: '
        input_amt = get_integer_input(blurb=blurb, prompt=prompt)

        # Make sure the user entered an amount <= the $ the player has left,
        # or keep prompting until they do.
        while input_amt > player.dollars_remaining:
            blurb = ('Insufficent balance. Enter an amount < ${} for player {}'
                     .format(player.dollars_remaining, player.player_number))
            input_amt = get_integer_input(blurb=blurb, prompt=prompt)

        return input_amt

    def ask_num_players(self) -> int:
        """
        Asks the user to input the number of players, and returns the result
        once an integer is input.

        Returns:
            int: The number of players
        """
        blurb = 'How many players do you want to play with? Input must be an integer.'
        prompt = '#: '
        return get_integer_input(blurb=blurb, prompt=prompt)

if __name__ == "__main__":
    game = BlackJack()
    game.play()