#!/usr/bin/python

from __future__ import print_function
import sys

tried_so_far = 0
n_rows = 8
n_cols = 8
start_at = 0

class Board:
  def __init__(self, n_rows, n_cols):
    self.n_rows = n_rows
    self.n_cols = n_cols
    self.board = [-1]*(n_rows*n_cols)

  def __repr__(self):
    result = ""
    ind = 0
    for i in range(n_rows):
      for j in range(n_cols):
        if self.board[ind] == -1:
          result += '--'
        else:
          result += '%02d'%self.board[ind]
        ind += 1
        result += '  '
      result += '\n'
    return result

def build_next_moves(n_rows,n_cols):
  next_moves = []
  for i in range(n_rows*n_cols):
    #number,                     left, up, down, right
    possible_moves =\
      [   (-1-(2*n_cols),        1,  2, 0, 0),\
          ( 1-(2*n_cols),        0,  2, 0, 1),\
          (-2-n_cols,            2,  1, 0, 0),\
          ( 2-n_cols,            0,  1, 0, 2),\
          (-2+n_cols,            2,  0, 1, 0),\
          ( 2+n_cols,            0,  0, 1, 2),\
          (-1+(2*n_cols),        1,  0, 2, 0),\
          ( 1+(2*n_cols),        0,  0, 2, 1) ]
    next_moves.append([a[0]+i for a in possible_moves if (((i%n_cols)-a[1] >= 0) and \
                                               ((i%n_cols)+a[4] < n_cols) and \
                                               ((i/n_cols)-a[2] >= 0) and \
                                               ((i/n_cols)+a[3] < n_rows)) ])
  return next_moves

def next_steps(board_right_now,square,next_moves):
  return (a for a in next_moves[square] if board_right_now[a] == -1)

def track(board, next_moves, current_square, covered):
  global tried_so_far
  if covered == board.n_rows*board.n_cols:
    return 1
  for i in next_steps(board.board, current_square, next_moves):
    board.board[i] = covered+1
    tried_so_far += 1
    if track(board, next_moves, i, covered + 1) == 1:
      return 1
    board.board[i] = -1
  return 0

if __name__ == '__main__':
  if len(sys.argv) >= 4:
    start_at = int(sys.argv[3])
  if len(sys.argv) >= 3:
    n_cols = int(sys.argv[2])
  if len(sys.argv) >= 2:
    n_rows = int(sys.argv[1])
  b = Board(n_rows,n_cols)
  next_moves = build_next_moves(n_rows,n_cols)
  for i in range(n_rows*n_cols):
    print("next moves for %02d is %s"%(i,next_moves[i]))
  b.board[start_at] = 1
  result = track(b, next_moves, start_at, 1)
  if result == 1:
    print(b)
  else:
    print("No result!")





