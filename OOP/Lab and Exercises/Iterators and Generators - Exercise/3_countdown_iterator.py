
# Create a class called countdown_iterator. Upon initialization it should receive a count.
# Implement the iterator, so it returns each number of the countdown (from count to 0 inclusive).

class countdown_iterator:

    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> int:
        if self.count >= 0:
            self.count -= 1
            return self.count + 1
        raise StopIteration()


if __name__ == '__main__':
    iterator = countdown_iterator(10)
    for item in iterator:
        print(item, end=" ")
