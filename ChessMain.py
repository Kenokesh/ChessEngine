import pygame, sys, time
from random import randint
from os.path import abspath, join, splitext, basename
from os import listdir

WIDTH = HEIGHT =512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}

...

def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wP']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load ("images/" + piece +"png"), (SQ_SIZE , SQ_SIZE))
...

...
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)

    
...