class Kacca:
    cash = int(0)

    def top_up(self, n):
        self.cash += n

    def count_1000(self):
        print(self.cash // 1000)

    def take_away(self, a: int):
        assert a <= self.cash, 'Not enogh cash'
        self.cash -= a
