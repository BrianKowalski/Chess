class GameState:
    def __init__(self):
        #создание доски 8 на 8, b - черные, w - белые, 2 буква обозначение на английском, '--' - пустые клетки
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp' for _ in range(8)],
            ['--' for _ in range(8)],
            ['--' for _ in range(8)],
            ['--' for _ in range(8)],
            ['--' for _ in range(8)],
            ['wp' for _ in range(8)],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.whiteToMove = True
        self.moveLog = []