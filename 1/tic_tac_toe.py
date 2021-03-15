class TicTacToe:
    def __init__(self):
        self._current_player = 'x'

        self._board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    class Error(Exception):
        def __init__(self, message):
            self.txt = message

    def _show_board(self):
        print('*' * 13)
        print('  0 1 2')
        for number, line in enumerate(self._board):
            print(number, ' '.join(line))

    def _switch_player(self):
        if self._current_player == 'x':
            self._current_player = 'o'
        else:
            self._current_player = 'x'

    def _input_move(self):
        print(f'Ход игрока {self._current_player}:')

        x = input('x = ')
        y = input('y = ')

        return x, y

    def _validate_input(self, x, y):
        try:
            x = int(x)
            y = int(y)

            if self._board[y][x] != ' ':
                raise self.Error('Текущая позиция уже занята')

        except ValueError:
            raise self.Error("Введены некорректные координаты")
        except IndexError:
            raise self.Error('Координаты выходят за допустимый диапазон')

        return x, y

    def _make_move(self, x, y):
        x, y = self._validate_input(x, y)

        self._board[y][x] = self._current_player

    def _is_victory(self):
        win_line = [self._current_player] * 3

        for line in self._board:
            if line == win_line:
                return True

        for i in range(3):
            if [
                self._board[0][i],
                self._board[1][i],
                self._board[2][i]
            ] == win_line:
                return True

        if [
            self._board[0][0],
            self._board[1][1],
            self._board[2][2]
        ] == win_line:
            return True

        if [
            self._board[0][2],
            self._board[1][1],
            self._board[2][0]
        ] == win_line:
            return True

        return False

    def _board_is_filled(self):
        for line in self._board:
            for token in line:
                if token == ' ':
                    return False

        return True

    def start_game(self):
        while True:
            self._show_board()

            x, y = self._input_move()

            try:
                self._make_move(x, y)
            except self.Error as error:
                print(error)
                continue

            if self._is_victory():
                print(f'Игрок "{self._current_player}" выиграл!')
                break
            elif self._board_is_filled():
                print('Ничья!')
                break

            self._switch_player()


if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
