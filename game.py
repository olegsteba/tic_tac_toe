import pygame
from gameparts import Board


pygame.init()

# Определение констант
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4
FILE_STATISTICS = 'results.txt'

# Настройка экрана
# Задать размер графического окна для игррового поля
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом
screen.fill(BG_COLOR)


# Функция отвечает за отрисовку горизонтальных и вертикальных линий
def draw_lines():
    # Горизонтальные линии
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Вертикальные линии
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# Функция отвечает за отрисовку фигур
# крестик или нолик на доске
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(file_name, msg):
    """Записывает в файл результаты игры."""
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{msg}\n')


# Функция описывающая логику игры
def main():
    # Создать игровое поле - объект класса Board
    game = Board()
    current_player = 'X'
    running = True
    # Отрисовать поле в терминале
    draw_lines()

    # В цикле обрабатываются таки события, как
    # нажание кнопки мыши и закрытие окна
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)

                    if game.check_win(current_player):
                        msg = f'Победители {current_player}'
                        print(msg)
                        save_result(FILE_STATISTICS, msg)
                        running = False
                    elif game.is_board_full():
                        msg = 'Ничья!'
                        print(msg)
                        save_result(FILE_STATISTICS, msg)
                        running = False

                    current_player = 'O' if current_player == 'X' else 'X'

                    draw_figures(game.board)

        # Обновить окно игры
        pygame.display.update()

    # Закрыть окно игры
    pygame.quit()


if __name__ == '__main__':
    main()
