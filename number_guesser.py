from enum import Enum
from random import randint


class GuessStatus(Enum):
    HIGH: str = "Too high"
    LOW: str = "Too low"
    CORRECT: str = "Correct"


class NumberGuesserGame:
    def __init__(self):
        print("WELCOME TO THE NUMBER GUESSING GAME!\n")

    @staticmethod
    def _get_bound(bound_type: str) -> int:
        while True:
            try:
                bound = int(input(f"Enter the {bound_type} bound:  "))
                break
            except ValueError:
                print(f"The {bound_type} bound must be an integer. Try again.\n")

        return bound

    @property
    def _invalid_bounds(self) -> bool:
        status: bool = False
        if self.lower_bound >= self.upper_bound:
            status = True

        return status

    def _set_bounds(self) -> None:
        self.lower_bound = self._get_bound("lower")
        self.upper_bound = self._get_bound("upper")

        while self._invalid_bounds:
            print(
                "The lower bound must be smaller than the upper bound. You entered"
                f" {self.lower_bound} for the lower bound and {self.upper_bound} for"
                " the upper bound. Try again.\n"
            )
            self._set_bounds()

    @property
    def _out_of_bounds(self) -> bool:
        status: bool = True
        if self.lower_bound <= self.guess <= self.upper_bound:
            status = False

        return status

    def _check_guess(self) -> GuessStatus:
        status: GuessStatus

        if self.guess < self.secret_number:
            status = GuessStatus.LOW
        elif self.guess > self.secret_number:
            status = GuessStatus.HIGH
        else:
            status = GuessStatus.CORRECT

        return status

    def _get_guess(self) -> None:
        try:
            self.guess: int = int(
                input(
                    f"Guess a number between {self.lower_bound} and"
                    f" {self.upper_bound}:  "
                )
            )
        except ValueError:
            print("The guess must be an integer. Try again.\n")
            self._get_guess()

        while self._out_of_bounds:
            print(
                f"The guess must be between the lower bound {self.lower_bound}"
                f" and upper bound {self.upper_bound}. Try again.\n"
            )
            self._get_guess()

    def play(self):
        self._set_bounds()
        self.secret_number: int = randint(self.lower_bound, self.upper_bound)

        status: GuessStatus = None
        tries: int = 0

        while status != GuessStatus.CORRECT:
            self._get_guess()
            status = self._check_guess()
            print(status.value, "\n")
            tries += 1

        print(f"Congratulations! You won the game in {tries} tries!")
        print("Exiting the game...")


if __name__ == "__main__":
    game = NumberGuesserGame()
    game.play()
