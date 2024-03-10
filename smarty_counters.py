from collections import defaultdict


class SmartyColourCalculator:
    BOX_LINE = "box"

    def __init__(
        self,
        group_size=None,
        group_time=None,
        default_size=7,
        default_time=7
    ):
        self.group_size = defaultdict(lambda: default_size, **group_size or {})
        self.group_time = defaultdict(lambda: default_time, **group_time or {})
        self.group_counts = defaultdict(int)

    def finish_box(self):
        finish_time = 0
        for color in self.group_counts:
            finish_time += self.group_time[color] * self.group_counts[color]
        self.group_counts.clear()

        return finish_time

    def reset(self):
        self.group_counts.clear()

    def add_smarty(self, color):
        self.group_counts[color] += 1

        if self.group_counts[color] == self.group_size[color]:
            self.group_counts[color] = 0
            return self.group_time[color]

        return 0

    def add(self, line):
        if line == SmartyColourCalculator.BOX_LINE:
            return self.finish_box()
        else:
            return self.add_smarty(line)


class SmartyCounter:
    def __init__(self, calculator: SmartyColourCalculator):
        self.calculator = calculator
        self.elapsed_seconds = 0

    def finish(self):
        self.elapsed_seconds += self.calculator.finish_box()

    def add(self, line):
        self.elapsed_seconds += self.calculator.add(line)

    def reset(self):
        self.elapsed_seconds = 0
        self.calculator.reset()
