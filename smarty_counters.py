from collections import defaultdict


class SmartyBoxCounter:
    def __init__(
        self,
        color_group_size=None,
        color_seconds=None,
        default_seconds=7,
        default_group_size=7,
    ):
        self.color_group_size = defaultdict(
            lambda: default_group_size, **color_group_size
        )
        self.color_seconds = defaultdict(lambda: default_seconds, **color_seconds)
        self.elapsed_seconds = 0
        self.group_counts = defaultdict(int)

    def finish_box(self):
        finish_time = 0
        for color in self.group_counts:
            finish_time += self.color_seconds[color] * self.group_counts[color]
        self.group_counts.clear()

        return finish_time

    def reset(self):
        self.elapsed_seconds = 0
        self.group_counts.clear()

    def add(self, color):
        self.group_counts[color] += 1

        if self.group_counts[color] == self.color_group_size[color]:
            self.group_counts[color] = 0
            self.elapsed_seconds += self.color_seconds[color]
            return self.color_seconds[color]

        return 0


class SmartyCounter:
    def __init__(self, counter: SmartyBoxCounter):
        self.counter = counter
        self.total_elapsed_seconds = 0

    def finish(self):
        return self.add("box")

    def reset(self):
        self.total_elapsed_seconds = 0
        self.counter.reset()

    def add(self, input_line):
        if input_line == "box":
            added_seconds = self.counter.finish_box()
        else:
            added_seconds = self.counter.add(input_line)
        self.total_elapsed_seconds += added_seconds

        return added_seconds
