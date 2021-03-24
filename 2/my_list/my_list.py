from itertools import zip_longest


class MyList(list):
    def __add__(self, other):
        return MyList(
            x + y for x, y
            in zip_longest(self, other,
                           fillvalue=0)
        )

    __radd__ = __add__

    def __sub__(self, other):
        return MyList(
            x - y for x, y
            in zip_longest(self, other,
                           fillvalue=0)
        )

    def __neg__(self):
        return MyList(
            -x for x in self
        )

    def __rsub__(self, other):
        return -(self - other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)
