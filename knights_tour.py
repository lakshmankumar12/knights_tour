#!/usr/bin/python

from __future__ import print_function
import sys

tried_so_far = 0
size = 8

class Board:
  def __init__(self, size):
    self.size = size
    self.board = [-1]*(size*size)

  def __repr__(self):
    result = ""
    ind = 0
    for i in range(size):
      for j in range(size):
        if self.board[ind] == -1:
          result += '--'
        else:
          result += '%02d'%self.board[ind]
        ind += 1
        result += '  '
      result += '\n'
    return result

def next_moves(i, size):
   #number, left, up, down, right
  possible_moves =\
    [   (-1-(2*size), 1,  2, 0, 0),\
        ( 1-(2*size), 0,  2, 0, 1),\
        (-2-size,     2,  1, 0, 0),\
        ( 2-size,     0,  1, 0, 2),\
        (-2+size,     2,  0, 1, 0),\
        ( 2+size,     0,  0, 1, 2),\
        (-1+(2*size), 1,  0, 2, 0),\
        ( 1+(2*size), 0,  0, 2, 1) ]
  return [a[0]+i for a in possible_moves if (((i%size)-a[1] >= 0) and \
                                             ((i%size)+a[4] < size) and \
                                             ((i/size)-a[2] >= 0) and \
                                             ((i/size)+a[3] < size)) ]

def next_steps(board_right_now,square):
  global size
  return (a for a in next_moves(square, size) if board_right_now[a] == -1)

def track(board, current_square, covered):
  global tried_so_far
  global size
  if covered == (size*size):
    return 1
  for i in next_steps(board.board, current_square):
    board.board[i] = covered+1
    tried_so_far += 1
    if track(board, i, covered + 1) == 1:
      return 1
    board.board[i] = -1
  return 0

if __name__ == '__main__':
  b = Board(size)
  for i in range(size*size):
    print("next moves for %02d is %s"%(i,next_moves(i,size)))
  b.board[0] = 1
  result = track(b, 0, 1)
  if result == 1:
    print(b)
  else:
    print("No result!")





