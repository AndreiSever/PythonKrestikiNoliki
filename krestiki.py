import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  

class Game:
    """
    Класс для игры в Крестики-Нолики
    """
    
    def __init__(self):
        """
        Инициалирует переменные. Рисует пустое игровое поле.

        Атрибуты
        --------
        X : string
            Используется для заполнения массива с ходами. (Значение "X")
        O : string
            Используется для заполнения массива с ходами. (Значение "O")
        EMPTY : string
            Используется для заполнения массива с ходами. (Значение " ")
        NUM_SQUARES : int
            Количество полей на игровой доске. (Значение 9)
        TIE : string
            Ничья. (Значение "ТИЕ")
        xCircle, yCircle : array_like
            Массивы с Х, Y координатами круга.
        radius : int
            Радиус круга. (Значение 0.4)
        fill : bool
            Заливка круга. (Значение False)
        xLine1, yLine1, xLine2, yLine2: array_like
            Массив с X,Y координатами линии. Рисует крестик.
        color : string
            Цвет фигур. (Значение "k")
        xLine3, yLine3 : array_like
            Массив с X,Y координатами линии.
        colorWin : string
            Цвет линии при по окончании игры. (Значение "r")
        fig
            Создание фигуры
        ax 
            Добавляет подокно.
        """
        self.X = "X"
        self.O = "O"
        self.EMPTY = " "
        self.NUM_SQUARES = 9
        self.TIE = "TIE"
        self.xCircle = [0.5,1.5,2.5,0.5,1.5,2.5,0.5,1.5,2.5]
        self.yCircle = [2.5,2.5,2.5,1.5,1.5,1.5,0.5,0.5,0.5]
        self.radius = 0.4
        self.fill =False
        self.xLine1 = [[0,1],[1,2],[2,3],[0,1],[1,2],[2,3],[0,1],[1,2],[2,3]]
        self.yLine1 = [[2,3],[2,3],[2,3],[1,2],[1,2],[1,2],[0,1],[0,1],[0,1]]
        self.xLine2 = [[0,1],[1,2],[2,3],[0,1],[1,2],[2,3],[0,1],[1,2],[2,3]]
        self.yLine2 = [[3,2],[3,2],[3,2],[2,1],[2,1],[2,1],[1,0],[1,0],[1,0]]
        self.color = 'k'
        self.xLine3 = [[0,3],[0,3],[0,3],[0.5,0.5],[1.5,1.5],[2.5,2.5],[0,3],[0,3]]
        self.yLine3 = [[2.5,2.5],[1.5,1.5],[0.5,0.5],[3,0],[3,0],[3,0],[3,0],[0,3]]
        self.colorWin = 'r'
        self.fig = plt.figure()    
        self.ax = self.fig.add_subplot(111,aspect='equal')
        self.color = 'k'
        self.ax.set_xticks([1,2,3])
        self.ax.set_yticks([1,2,3])
        self.ax.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
        self.ax.grid()
        plt.draw()
        plt.pause(0.1)             
    def ask_yes_no(self,question,error):
        """
        Выбирает сторону в игре.
        
        Параметры
        ---------
        question : string
            Задает вопрос.
        error : string
            Задает сообщение ошибки.
        
        Возврат
        -------
        response : string
            Возвращает строку.
        
        Ошибки
        ------
        y_or_n
            Возникает если не равен "y" или "n".
        """
        response = None
        while response not in ("y", "n"):
            response = str(input(question).lower())
            y_or_n=self.y_n(response)
            if y_or_n==True:
                print(error)
        return response
    def y_n(self,response):
        """
        Проверяет на равенство определенным значениям.
        
        Параметры
        ---------
        response : string
            Введенная строка.
        
        Возврат
        -------
        bool
            Возвращает True
        bool
            Возвращает False
        """
        if response not in ("y", "n"):
            return True
        return False
     
    def ask_number(self,question, low, high,error):
        """
        Просит ввести число из диапазона
        
        Параметры
        ---------
        question : string
            Задает вопрос.
        error : string
            Задает сообщение ошибки.
        high : int
            Максимальный порог значения.
        low : int
            Минимальный порог значения.
        
        Возврат
        -------
        response : string
            Возвращает строку.
            
        Ошибки
        ------
        l_h
            Возникает если не входит в диапазон значений.
        ValueError
            Возникает если введено не число.
        """
        response = None
        while response not in range(low, high):
            response = input(question)
            try:
               response = int(response)
               l_h=self.low_high(response,low, high)
               if l_h==True:
                   print(error)
            except ValueError:
               print(error)
        return response
    def low_high(self,response,low, high):
        """
        Проверяет на вхождение в диапазон значений.
        
        Параметры
        ---------
        response : string
            Введенная строка.
        high : int
            Максимальный порог значения.
        low : int
            Минимальный порог значения.
            
        Возврат
        -------
        bool
            Возвращает True
        bool
            Возвращает False
        """
        if response<low or response>high-1:
            return True
        return False
    def pieces(self):
        """
        Определяет принадлежность перового хода.
        
        Возврат
        -------
        computer : string
            Возвращает "Х" или "О"
        human : string
            Возвращает "Х" или "О"
        """
        go_first = self.ask_yes_no("Играть крестиками? (y, n): ","\nНекорректный ввод. Попробуйте еще раз!\n")
        if go_first == "y":
            print("\n Вы играете кректиками.")
            human = self.X
            computer = self.O
        else:
            print("\n Вы играете ноликами")
            computer = self.X
            human = self.O
        return computer, human
     
     
    def new_board(self):
        """
        Создаёт новую игровую доску.
        
        Возврат
        -------
        board : array
            Массив со строковыми значениями.
        """
        board = []
        for square in range(self.NUM_SQUARES):
            board.append(self.EMPTY)
        return board
     
     
    def display_board(self,board):
        """
        Рисует крестики и нолики.
        
        Параметры
        ---------
        board : array
            Массив со строковыми значениями.
        """
        for i in range(self.NUM_SQUARES):
            if (board[i]!=self.EMPTY):
                if (board[i]==self.X):
                    line1 = Line2D(self.xLine1[i], self.yLine1[i],color=self.color)
                    line2 = Line2D(self.xLine2[i], self.yLine2[i],color=self.color)
                    self.ax.add_line(line1)
                    self.ax.add_line(line2)
                    plt.draw()
                    plt.pause(0.1)
                if (board[i]==self.O):
                    self.ax.add_artist(plt.Circle((self.xCircle[i], self.yCircle[i]), self.radius, color=self.color, fill=self.fill))
                    plt.draw()
                    plt.pause(0.1)
    def linewin(self,combinationwin):
        """
        Рисует линию при победе.
        
        Параметры
        ---------
        combinationwin : int or None
            Индекс победной комбинации или None при ничье.
        """
        if combinationwin!=None:
            line = Line2D(self.xLine3[combinationwin], self.yLine3[combinationwin],color=self.colorWin)
            self.ax.add_line(line)
            plt.draw()
            plt.pause(0.1)
    def legal_moves(self,board):
        """
        Создаёт список доступных ходов.
        
        Параметры
        ---------
        board : array
            Массив со строковыми значениями.
            
        Возврат
        -------
        moves : array
            Массив со строковыми значениями. Доступные ходы.
        """
        moves = []
        for square in range(self.NUM_SQUARES):
            if board[square] == self.EMPTY:
                moves.append(square)
        return moves
     
     
    def winner(self,board):
        """
        Определяет победителя в игре.
        
        Параметры
        ---------
        board : array
            Массив со строковыми значениями.
        
        Возврат
        -------
        winner : array
            Массив с числами. Побеная комбинация.
        indexWin : int or None
            Возвращает индекс при победе или None при ничье.
        TIE : string
            Ничья.
        None
            Возвращает пока не заполнены все клетки или не победа.
        """
        WAYS_TO_WIN = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))
        indexWin = None
        for row in WAYS_TO_WIN:
            if board[row[0]] == board[row[1]] == board[row[2]] != self.EMPTY:
                winner = board[row[0]]
                indexWin = WAYS_TO_WIN.index(row)
                return winner,indexWin
        if self.EMPTY not in board:
            return self.TIE, indexWin
        return None
     
     
    def human_move(self,board):
        """
        Ходит человек.
        
        Параметры
        ---------
        board : array
            Массив со строковыми значениями.
        
        Возврат
        -------
        move : int
            Возврат введенного числа.
        
        Ошибки
        ------
        move_legal
            Возникает если нет числа в массиве.
        """
        legal = self.legal_moves(board)
        move = None
        while move not in legal:
            move = self.ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, self.NUM_SQUARES,"\nНекорректный ввод.Нужно ввести только число от 0 до 8!\n")
            move_legal=self.move_l(move,legal)
            if move_legal==True:
                print("\nЭто поле уже занято. Выбери другое.\n")
        return move
    def move_l (self,move,legal):
        """
        Проверяет на существовании числа в массиве.
        
        Параметры
        ---------
        move : int
            Введенное число.
        legal : array
            Массив числовых значений. Разрешенные ходы.
        
        Возврат
        -------
        bool
            Возвращает True
        bool
            Возвращает False
        """
        if move not in legal:
            return True
        return False 
    def computer_move(self,board, computer, human):
        """
        Ходит компьютер.
        
        Параметры
        ---------
        board : array
            Массив со строковыми значениями.
        computer : string
            Сторона за которую играет компьютер.
        human : string
            Сторона за которую играет человек.
        
        Возврат
        -------
        move : int
            Возвращает значение хода компьютера.
        """
        board = board[:]
        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
     
        print("Я выберу поле номер", end = " ")
        for move in self.legal_moves(board):
            board[move] = computer
            if self.winner(board) == computer:
                print(move)
                return move
            board[move] = self.EMPTY
     
        for moves in self.legal_moves(board):
            board[move] = human
            if self.winner(board) == human:
                print(move)
                return move
            board[move] = self.EMPTY

        for move in BEST_MOVES:
            if move in self.legal_moves(board):
                print(move)
                return move
          
    def next_turn(self,turn):
        """
        Осуществляет переход хода.
        
        Параметры
        ---------
        turn : string
            Значение предыдущего игрока, "Х" или "О".
        
        Возврат
        -------
        O : string
            Возвращает "О" если ходил "Х"
        Х : string
            Возвращает "Х" если ходил "О"
        """
        if turn == self.X:
            return self.O
        else:
            return self.X
     
     
    def congrat_winner(self,the_winner, computer, human):
        """
        Выводит итог игры.
        
        Параметры
        ---------
        the_winner : string
            Значение победителя равное или "Х", или "О"
        computer : string
            Сторона компьютера в игре.
        human : string
            Сторона человека в игре.
        """
        if the_winner == computer:
            print("Вы проиграли!")
        elif the_winner == human:
            print("Вы выиграли!")
        elif the_winner == self.TIE:
            print("Ничья!")
    
    def main(self):
        """
        Основная функция, которая вызывает все остальные.
        """        
        computer, human = self.pieces()
        turn = self.X
        board = self.new_board()
        while not self.winner(board):
            if turn == human:
                move = self.human_move(board)
                board[move] = human
            else:
                move = self.computer_move(board, computer, human)
                board[move] = computer
            self.display_board(board)
            turn = self.next_turn(turn)
        the_winner,combinationwin =self.winner(board)
        self.linewin(combinationwin)
        self.congrat_winner(the_winner, computer, human)
plt.ion()
# запуск программы
clas=Game()
clas.main()
input("Нажмите Enter, чтобы выйти.")
plt.close()
