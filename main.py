import sys
import io

from smarty_counters import SmartyCounter, SmartyColourCalculator


def run(input_file):
    calc = SmartyColourCalculator(default_size=7, default_time=7)
    calc.group_size["red"] = 1
    calc.group_time["red"] = 13

    counter = SmartyCounter(calc)

    input_source = io.open(input_file, "r", encoding="utf-8")

    for raw_line in input_source:
        line = raw_line.strip()

        counter.add(line)

    counter.finish()

    print(counter.elapsed_seconds)


if __name__ == "__main__":
    run(sys.argv[1])
