import justpy as jp
from game import TicTacToe

game = TicTacToe()

def cell_click(self, msg):
    row, col = self.row, self.col
    result = game.makeMove(row, col)
    game.gameOver = result["status"] in ["win", "draw"]
    update_board(msg.page)
    msg.page.message.text = result["message"]

    if game.gameOver:
        for row_cells in msg.page.cells:
            for cell in row_cells:
                cell.disabled = True

def reset_click(self, msg):
    game.resetGame()
    update_board(msg.page)
    msg.page.message.text = "Game reset! Player X's turn."

    for row_cells in msg.page.cells:
        for cell in row_cells:
            cell.disabled = False

def update_board(page):
    for i in range(3):
        for j in range(3):
            cell = page.cells[i][j]
            cell.text = game.board[i][j] if game.board[i][j] != '_' else ''
            if cell.text == 'X':
                cell.style = "background-color: rgb(177, 123, 23); color: white;"
            elif cell.text == 'O':
                cell.style = "background-color: rgb(26, 105, 26); color: white;"
            else:
                cell.style = "background-color: rgb(83,83,83);" if game.gameOver else "background-color: black;"

def tic_tac_toe():
    game.resetGame()
    wp = jp.WebPage()
    wp.title = "Tic Tac Toe"
    wp.body_style = "background-color: rgb(50, 50, 50); color: rgb(190, 190, 190);"

    container = jp.Div(
        style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 30rem; height: 35rem; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: rgb(32,32,32); border: 0px; border-radius: 8px;",
        a=wp
    )

    # Title
    jp.Div(
        text="Tic Tac Toe",
        style="font-size: 2rem; font-weight: bold; text-align: center; margin-top: 1rem; margin-bottom: 1rem;",
        a=container
    )

    # Message
    wp.message = jp.P(text="Player X's turn", style="font-size: 1.25rem; text-align: center; margin: 1rem;", a=container)

    grid_container = jp.Div(style="display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);", a=container)
    grid = jp.Div(style="display: grid; grid-template-columns: repeat(3, 1fr); width: 16rem; margin: auto; background-color: black; border-collapse: collapse; border: 0;", a=grid_container)

    wp.cells = []
    for i in range(3):
        row_cells = []
        for j in range(3):
            border_classes = "border-gray-400 h-20 text-3xl "
            if i < 2:
                border_classes += "border-b-2 "
            if j < 2:
                border_classes += "border-r-2 "
            cell = jp.Button(text='', classes=border_classes, a=grid)
            cell.row, cell.col = i, j
            cell.on('click', cell_click)
            row_cells.append(cell)
        wp.cells.append(row_cells)

    # Reset Button
    def hover_in(self, msg):
        self.style = (
            "margin-top: 1rem; padding: 0.75rem 1.5rem; background-color: rgb(22, 22, 22); "
            "color: white; border-radius: 0.375rem; font-size: 1rem; font-weight: bold; "
            "border: none; cursor: pointer; transform: scale(1.05); transition: transform 0.2s ease;"
        )

    def hover_out(self, msg):
        self.style = (
            "margin-top: 1rem; padding: 0.75rem 1.5rem; background-color: white; "
            "color: rgb(33, 33, 33); border-radius: 0.375rem; font-size: 1rem; font-weight: bold; "
            "border: none; cursor: pointer; transition: background-color 0.3s ease, transform 0.2s ease;"
        )

    resetBtn = jp.Button(
        text='New Game',
        style=(
            "margin-top: 1rem; padding: 0.75rem 1.5rem; background-color: white; "
            "color: rgb(33, 33, 33); border-radius: 0.375rem; font-size: 1rem; font-weight: bold; "
            "border: none; cursor: pointer; transition: background-color 0.3s ease, transform 0.2s ease;"
        ),
        click=reset_click,
        a=container
    )

    resetBtn.on('mouseenter', hover_in)
    resetBtn.on('mouseleave', hover_out)

    return wp

jp.justpy(tic_tac_toe)