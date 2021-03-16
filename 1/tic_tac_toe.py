class TicTacToe:
    def __init__(self):
        self.__current_player = 'x'

        self.__board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    class Error(Exception):
        def __init__(self, message):
            self.txt = message

    def show_board(self):
        print('*' * 13)
        print('  0 1 2')
        for number, line in enumerate(self.__board):
            print(number, ' '.join(line))

    def switch_player(self):
        if self.__current_player == 'x':
            self.__current_player = 'o'
        else:
            self.__current_player = 'x'

    def input_move(self):
        print(f'Ход игрока {self.__current_player}:')

        x = input('x = ')
        y = input('y = ')

        return x, y

    def validate_input(self, x, y):
        try:
            x = int(x)
            y = int(y)

            if self.__board[y][x] != ' ':
                raise self.Error('Текущая позиция уже занята')

        except ValueError:
            raise self.Error("Введены некорректные координаты")
        except IndexError:
            raise self.Error('Координаты выходят за допустимый диапазон')

        return x, y

    def make_move(self, x, y):
        x, y = self.validate_input(x, y)

        self.__board[y][x] = self.__current_player

    def is_victory(self):
        win_line = [self.__current_player] * 3

        for line in self.__board:
            if line == win_line:
                return True

        for i in range(3):
            if [
                self.__board[0][i],
                self.__board[1][i],
                self.__board[2][i]
            ] == win_line:
                return True

        if [
            self.__board[0][0],
            self.__board[1][1],
            self.__board[2][2]
        ] == win_line:
            return True

        if [
            self.__board[0][2],
            self.__board[1][1],
            self.__board[2][0]
        ] == win_line:
            return True

        return False

    def board_is_filled(self):
        for line in self.__board:
            for token in line:
                if token == ' ':
                    return False

        return True

    def start_game(self):
        while True:
            self.show_board()

            x, y = self.input_move()

            try:
                self.make_move(x, y)
            except self.Error as error:
                print(error)
                continue

            if self.is_victory():
                print(f'Игрок "{self.__current_player}" выиграл!')
                break
            elif self.board_is_filled():
                print('Ничья!')
                break

            self.switch_player()


if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
