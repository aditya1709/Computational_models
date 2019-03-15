import chess
import chess.engine

def next_move(board_state):
	engine = chess.engine.SimpleEngine.popen_uci("/home/aditya1709/Documents/Michigan_courses/EECS598_HCI/Final_project/UCI_interface/chessengines/stockfish_1/Linux/stockfish_1")
	board = chess.Board(board_state)
	result = engine.play(board, chess.engine.Limit(time=0.100))
	board.push(result.move)
	engine.quit()
	return board.fen(), str(result.move)

# if __name__ == '__main__': 
# 	main()