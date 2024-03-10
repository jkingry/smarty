"""Smart Calculator - Count smarty eating time for an input file.

Usage:
    python main.py <input_file>

Example:
    python main.py input.txt
"""

import sys
import io

from smarty_counters import SmartyCounter, SmartyColourCalculator


def run(input_file: str):
    """
    Run the smart calculator with the input file.
    """
    calc = SmartyColourCalculator(default_size=7, default_time=7)
    calc.group_size["red"] = 1
    calc.group_time["red"] = 13

    counter = SmartyCounter(calc)

    with io.open(input_file, "r", encoding="utf-8") as input_source:
        for raw_line in input_source:
            line = raw_line.strip()
            counter.add(line)
        counter.finish()
        print(counter.elapsed_seconds)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    run(sys.argv[1])
