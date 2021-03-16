from itertools import zip_longest


class MyList(list):
    def __add__(self, other):
        return MyList(
            x + y for x, y
            in zip_longest(self, other,
                           fillvalue=0)
        )

    def __sub__(self, other):
        return MyList(
            x - y for x, y
            in zip_longest(self, other,
                           fillvalue=0)
        )

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)
