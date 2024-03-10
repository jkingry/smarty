"""Smarty counters module"""

from collections import defaultdict
from typing import Dict


class SmartyColourCalculator:
    """
    A class that calculates the finish time for a set of Smarty colours.

    Attributes:
        BOX_LINE (str): A constant representing the line that indicates the end of a box.

    Methods:
        __init__(self, group_size=None, group_time=None, default_size=7, default_time=7):
            Initializes a new instance of the SmartyColourCalculator class.
        finish_box(self):
            Calculates and returns the finish time for the current box.
        reset(self):
            Resets the group counts to zero.
        add_smarty(self, color):
            Adds a Smarty of the specified color to the group counts and returns the time 
            it takes to complete a group.
        add(self, line):
            Adds a line to the SmartyColourCalculator instance and returns the finish time 
            if it's the end of a box, otherwise returns the time it takes to complete a group.
    """

    BOX_LINE: str = "box"

    def __init__(
        self,
        group_size: Dict[str, int] = None,
        group_time: Dict[str, int] = None,
        default_size: int = 7,
        default_time: int = 7,
    ):
        self.group_size: Dict[str, int] = defaultdict(lambda: default_size, **group_size or {})
        self.group_time: Dict[str, int]  = defaultdict(lambda: default_time, **group_time or {})
        self.group_counts = defaultdict(int)

    def finish_box(self) -> int:
        """
        Calculates the total finish time for all groups in the box.

        Returns:
            The total remaining time for all partial groups
        """
        finish_time = 0
        for color in self.group_counts:
            finish_time += self.group_time[color] * self.group_counts[color]
        self.group_counts.clear()

        return finish_time

    def reset(self) -> None:
        """
        Resets the group counts to zero.
        """
        self.group_counts.clear()

    def add_smarty(self, color: str) -> int:
        """
        Adds a Smarty of the specified color to the group counts and
        returns the time it takes to complete a group .
        """
        self.group_counts[color] += 1

        if self.group_counts[color] == self.group_size[color]:
            self.group_counts[color] = 0
            return self.group_time[color]

        return 0

    def add(self, line: str) -> int:
        """
        Adds a line to the SmartyColourCalculator instance and returns the finish time
        if it's the end of a box, otherwise returns the time it takes to complete a group.
        """
        if line == SmartyColourCalculator.BOX_LINE:
            return self.finish_box()
        else:
            return self.add_smarty(line)


class SmartyCounter:
    """
    A class representing a Smarty Counter.

    Attributes:
        calculator (SmartyColourCalculator): The calculator used for calculating elapsed time.
        elapsed_seconds (int): The total elapsed seconds.

    Methods:
        finish(): Finishes the current box and adds the elapsed time to the total.
        add(line: str): Adds the elapsed time for a line to the total.
        reset(): Resets the elapsed time and the calculator.
    """

    def __init__(self, calculator: SmartyColourCalculator):
        self.calculator = calculator
        self.elapsed_seconds = 0

    def finish(self) -> None:
        """
        Finishes the current box and adds the elapsed time to the total.
        """
        self.elapsed_seconds += self.calculator.finish_box()

    def add(self, line: str) -> None:
        """
        Adds the elapsed time for a line to the total.

        Args:
            line (str): The line to calculate the elapsed time for.
        """
        self.elapsed_seconds += self.calculator.add(line)

    def reset(self) -> None:
        """
        Resets the elapsed time and the calculator.
        """
        self.elapsed_seconds = 0
        self.calculator.reset()
