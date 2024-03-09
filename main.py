import sys
import io

from smarty_counters import SmartyCounter, SmartyBoxCounter


def run(input_file):
    box_counter = SmartyBoxCounter(
        color_group_size={"red": 1}, color_seconds={"red": 13}
    )
    counter = SmartyCounter(box_counter)

    input_source = io.open(input_file, "r", encoding="utf-8")

    for raw_line in input_source:
        line = raw_line.strip()

        counter.add(line)

    counter.finish()

    print(counter.total_elapsed_seconds)


if __name__ == "__main__":
    run(sys.argv[1])
