class Board(object):
    """Класс, который описывает игровое поле"""

    field_size = 3

    # Инициализировать игровое поле - список списков с проблами.
    # Пробелы это пустые клетки
    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    # Метод отображения ходов игрока
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод отрисовки игрового поля
    # def display(self):
    #     for row in self.board:
    #         print('|'.join(row))
    #         print('-' * 5)

    # Метод для определения ничьи.
    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    # Метод определяющий победу.
    def check_win(self, player):
        # Проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True

        # Проверка по диагоналям
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False

    # Переопределить метот __str__
    def __str__(self):
        return (
            'Объект игрового поля размером'
            f'{self.field_size}x{self.field_size}'
        )
