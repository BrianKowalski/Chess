import pygame as p
from Chess import ChessEngine

width = 512
height = 512
cell = 8
sq_size = height // cell
images = {}
max_fps = 15


def loadImages():
    pieces = ['wp', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN',
              'wR']
    for img in pieces:
        images[img] = p.transform.scale(p.image.load('Chess/images/' + img + '.png'), (sq_size, sq_size))


def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(max_fps)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(cell):
        for c in range(cell):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def drawPieces(screen, board):
    for r in range(cell):
        for c in range(cell):
            piece = board[r][c]
            if piece != '--':
                screen.blit(images[piece], p.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


if __name__ == '__main__':
    main()
