"""
from proj07 import drop_disc, board_display
from copy import deepcopy
w = 'w'
b = 'b'
board = [[0,0,w,0,0,0,0],
         [0,0,w,0,0,0,0],
         [0,0,w,b,0,0,0],
         [0,0,b,w,b,0,0],
         [0,b,b,w,b,0,0],
         [0,w,w,b,w,0,0],
        ]
student_board = deepcopy(board)
student_return = drop_disc(student_board, 3, 'black')
print('instructor board:',board)
print('instructor return: full;student_return:',student_return)
print('student_board:',student_board)
assert student_return == 'full' and student_board == board

student_return = drop_disc(student_board, 8, 'black')
print('instructor board:',board)
print('instructor return: None;student_return:',student_return)
print('student_board:',student_board)
assert student_return == None and student_board == board

student_return = drop_disc(student_board, 7, 'black')
print("asdasdasdasd 7:",student_return)
board = [[0, 0, 'w', 0, 0, 0, 0], [0, 0, 'w', 0, 0, 0, 0], [0, 0, 'w', 'b', 0, 0, 0], [0, 0, 'b', 'w', 'b', 0, 0], [0, 'b', 'b', 'w', 'b', 0, 0], [0, 'w', 'w', 'b', 'w', 0, 'b']]
print('instructor board:',board)
print('instructor return: 6; student_return:',student_return)
board_display(student_board)
print('student_board:',student_board)

assert student_return == 6 and student_board == board

student_return = drop_disc(student_board, 2, 'black')
print("asdasdasdasd 2:",student_return)
board_display(student_board)
board = [[0, 0, 'w', 0, 0, 0, 0], [0, 0, 'w', 0, 0, 0, 0], [0, 0, 'w', 'b', 0, 0, 0], [0, 'b', 'b', 'w', 'b', 0, 0], [0, 'b', 'b', 'w', 'b', 0, 0], [0, 'w', 'w', 'b', 'w', 0, 'b']]
print('instructor board:',board)
board_display(board)
print('instructor return: 4;student_return:',student_return)
print('student_board:',student_board)
board_display(student_board)
assert student_return == 4 and student_board == board
"""
"""
from proj07 import check_disc, board_display

w = 'w'
b = 'b'
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,b,0],
         [b,w,0,w,b,b,0],
         [b,0,w,w,w,b,0],
         [b,w,b,w,w,w,w],
         [b,w,w,w,w,b,b],
        ]
print("check_disc(3,5) instructor: False; student:",check_disc(board,3,5) )
assert check_disc(board,3,5) == False
print("check_disc(6,2) instructor: True ; student:",check_disc(board,6,2) )
assert check_disc(board,6,2) == True
print("check_disc(5,6) instructor: True ; student:",check_disc(board,5,6) )
assert check_disc(board,5,6) == True
print("check_disc(2,1) instructor: False; student:",check_disc(board,2,1) )
board_display(board)
assert check_disc(board,2,1) == False
print("check_disc(1,1) instructor: False; student:",check_disc(board,1,1) )
assert check_disc(board,1,1) == False
print("check_disc(0,1) instructor: None ; student:",check_disc(board,0,1) )
print()
print(check_disc(board,0,1))
print()
assert check_disc(board,0,1) == None
print("check_disc(4,1) instructor: True; student:",check_disc(board,4,1) )
board_display(board)
assert check_disc(board,4,1) == True
"""
"""
from proj07 import check_disc, board_display

w = 'w'
b = 'b'
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,b,0],
         [b,b,b,w,b,w,0],
         [0,w,w,b,w,b,0],
         [0,b,w,w,b,w,0],
         [b,b,w,b,w,b,w],
        ]
print("check_disc(3,4) instructor: True; student:",check_disc(board,3,4) )
assert check_disc(board,3,4) == True
print("check_disc(5,5) instructor: True ; student:",check_disc(board,5,5) )
assert check_disc(board,5,5) == True
print("check_disc(5,4) instructor: True ; student:",check_disc(board,5,4) )
assert check_disc(board,5,4) == True
print("check_disc(3,2) instructor: False; student:",check_disc(board,3,2) )
assert check_disc(board,3,2) == False
print("check_disc(1,1) instructor: False; student:",check_disc(board,1,1) )
assert check_disc(board,1,1) == False
print("check_disc(6,2) instructor: False ; student:",check_disc(board,6,2) )
assert check_disc(board,6,2) == False
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,b,0],
         [b,w,0,w,w,w,0],
         [0,b,w,b,w,b,0],
         [0,w,b,w,w,b,0],
         [b,w,w,b,b,b,w],
        ]
board_display(board)
print("check_disc(3,1) instructor: True ; student:",check_disc(board,3,1) )
assert check_disc(board,3,1) == True
print("check_disc(6,6) instructor: False; student:",check_disc(board,6,6) )
assert check_disc(board,6,6) == False
board = [[0,b,0,0,0,0,0],
         [0,0,b,0,0,b,0],
         [b,w,0,b,w,w,0],
         [0,b,w,b,b,b,0],
         [0,w,b,w,w,b,0],
         [b,w,w,b,b,b,w],
        ]
print("check_disc(1,2) instructor: True; student:",check_disc(board,1,2) )
assert check_disc(board,1,2) == True
"""
from proj07 import is_game_over

board = [['b', 'b', 'b', 'w', 'b', 'b', 'b'],
         ['w', 'w', 'w', 'b', 'w', 'w', 'w'],
         ['b', 'b', 'b', 'w', 'b', 'b', 'b'],
         ['w', 'w', 'w', 'b', 'w', 'w', 'w'],
         ['b', 'b', 'b', 'w', 'b', 'b', 'b'],
         ['w', 'w', 'w', 'b', 'w', 'w', 'w']]

print("is_game_over: Instructor: draw; student:",is_game_over(board))
assert is_game_over(board) == 'draw'

w = 'w'
b = 'b'
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,b,0],
         [0,0,0,w,b,b,0],
         [0,0,w,w,w,b,0],
         [0,w,b,w,w,w,0],
         [b,b,w,b,w,b,w]]
print("12345676543")
print(is_game_over(board))
print("is_game_over: Instructor: white; student:",is_game_over(board))
assert is_game_over(board) == 'white'





