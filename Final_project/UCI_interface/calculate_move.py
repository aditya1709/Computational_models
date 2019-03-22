import chess
import chess.uci

def next_move(board_state, engine_name):
	engine = chess.uci.popen_engine("/home/aditya1709/Documents/Michigan_courses/EECS598_HCI/Final_project/UCI_interface/chessengines/"+engine_name+"/Linux/"+engine_name)
	engine.uci()
	board = chess.Board(board_state)
	engine.position(board)
	result = engine.go(movetime=2000)
	board.push(chess.Move.from_uci(str(result.bestmove.uci())[:4]))
	engine.quit()
	result = result.bestmove.uci()
	return board.fen(), str(result)[:4]

# if __name__ == '__main__': 
# 	main()