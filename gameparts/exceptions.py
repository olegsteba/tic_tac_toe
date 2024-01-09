class FieldIndexError(IndexError):
    """Класс, обработки ошибок при вводе данных."""

    def __str__(self):
        return 'Введеное значение за границами игрового поля.'


class CellOccupiedError(Exception):
    """Класс, обработки ошибки на занятость ячейки"""

    def __str__(slef):
        return 'Попытка изменить занятую ячейку'
