# Kamil Seternus 2020
# Gra kółko i krzyżyk
# Projekt v1.0

# ********** Zmienne Globalne **********

# Utworzenie tablicy która jest tablicą(ang. board) gry
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Utworzenie zmiennej definiującej czy gra ma dalej się toczyć, zmienna typu boolean
game_still_on = True

# Utworzenie zmiennej
winner = None

# Ustawienie aktualnego gracza na krzyżyk, jako, że krzyżyk zawsze rozpoczyna grę
current_player = 'X'

# *************** Funkcje ***************

# Utworzenie funkcji odpowiedzialnej za wyświetlanie tablicy z grą
def display_board():
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]}  ')
    print('-----------------')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]}  ')
    print('-----------------')
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]}  ')


# Funkcja odpowiadająca za przekazanie tury drugiemu graczowi
def handle_turn(player):
    # Funkcja input pytająca o wybór miejsca w którym chcemy postawić kółko/krzyżyk
    # i przypisująca ją do zmiennej position
    position = input(f"\n{player}'s Your turn! Choose place (1-9): \n")

    # pętla działająca na zmiennej boolean, jeśli zmienna valid jest nie jest prawdziwa to pętla while poniżej
    # sprawdza czy wpisana pozycja jest zgodna.
    valid = False
    while not valid:
        # pętla while sprawdzająca czy wpisana wartość znajduje się w zakresie 1-9, czyli obszarze gry
        # jeśli nie, wyświetl komunikat o błędzie i poproś ponownie o pozycję
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input(f"{player}'s Your turn! Please choose again. (1-9): \n")

        # przypisanie zmiennej input jako integer i pomniejszenie jej o 1 (Indeksowanie w tablicy liczone od 0, wpisanie
        # wartości 1 bez pomniejszenia jej skutkowało by ustawieniem kółka/krzyżyka w pozycji o 1)
        position = int(position) - 1

        # Jeśli pozycja na planszy jest wolna('-') to warunek valid jest prawdziwy
        if board[position] == '-':
            valid = True
        else:
            print('Place occupied! Choose another position.')

    board[position] = player

    display_board()

    return

# Funkcja sprawdzająca wiersze w poszukiwaniu X lub O jako wygranego
def check_rows():
    # Ustawienie zmiennej globalnej game_still_on
    global game_still_on
    # Zmienna row1 przypisana wartości z tablicy o indeksie 0 a ta pozycja tablicy jest taka sama jak pozycja 1 i 2
    # to mamy zwycięzce w rządzie pierwszym. Aby uniknąć wygranej z powodu placeholdera - musi być też różna od -
    row1 = board[0] == board[1] == board [2] != '-'
    row2 = board[3] == board[4] == board [5] != '-'
    row3 = board[6] == board[7] == board [8] != '-'

    # Jeśli w którymś rzędzie jest wygrany to ustaw globalną zmienną na False tym samym zakończ grę
    if row1 or row2 or row3:
        game_still_on = False

    # Zwróc (return) wygranego X lub O, sprawdzamy tylko pierwszą wartość z rzędu w tablicy
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    return


def check_collumns():
    # Ustawienie zmiennej globalnej game_still_on
    global game_still_on
    # Zmienna col1 przypisana wartości z tablicy o indeksie 0 a ta pozycja tablicy jest taka sama jak pozycja 3 i 6
    # to mamy zwycięzce w pierwszej kolumnie. Aby uniknąć wygranej z powodu placeholdera - musi być też różna od -
    col1 = board[0] == board[3] == board [6] != '-'
    col2 = board[1] == board[4] == board [7] != '-'
    col3 = board[2] == board[5] == board [8] != '-'

    # Jeśli w którymś rzędzie jest wygrany to ustaw globalną zmienną na False tym samym zakończ grę
    if col1 or col2 or col3:
        game_still_on = False

    # Zwróc (return) wygranego X lub O, sprawdzamy tylko pierwszą wartość z rzędu w tablicy
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]

    return


def check_diagonal():
    # Ustawienie zmiennej globalnej game_still_on
    global game_still_on
    # Zmienna diag1 przypisana wartości z tablicy o indeksie 0 a ta pozycja tablicy jest taka sama jak pozycja 4 i 8
    # to mamy zwycięzce po pierwszej przekątnej. Aby uniknąć wygranej z powodu placeholdera '-' musi być też różna od'-'
    diag1 = board[0] == board[4] == board [8] != '-'
    diag2 = board[2] == board[4] == board [6] != '-'

    # Jeśli w którymś rzędzie jest wygrany to ustaw globalną zmienną na False tym samym zakończ grę
    if diag1 or diag2:
        game_still_on = False

    # Zwróc (return) wygranego X lub O, sprawdzamy tylko pierwszą wartość z rzędu w tablicy
    if diag1:
        return board[0]
    elif diag2:
        return board[2]

    return


# Funkcja sprawdzająca czy ktoś wygrał, funkcja check_game_over odwołuje się do niej.
# Funkcja sprawdza najpierw czy w którymś wierszu jest zwycięzca, następnie kolumnie a końcu w przekątnych
def check_winner():
    # Ustawienie zmiennej globalnej winner
    global winner
    row_win = check_rows()
    collumn_win = check_collumns()
    diagonal_win = check_diagonal()

    if row_win:
        winner = row_win
    elif collumn_win:
        winner = collumn_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None

    return

# Funkcja sprawdzająca czy jest remis
def check_tie():
    # Ustawienie zmiennej globalnej game_still_on
    global game_still_on
    # Jeśli w tablicy (na planszy gry) nie ma już żadnego '-' oznacza to, że plansza zostałą wypełniona i jest remis
    if '-' not in board:
        game_still_on = False

    return


# Funkcja zmieniająca gracza z X na O i O na X
def change_player():
    # Ustawienie zmiennej globalnej current player
    global current_player

    # Jeśli graczem był krzyżyk (X) ustaw gracza na kółko (O) i odwrotnie
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

    return


# Funkcja sprawdzająca czy gra się zakończyła odwołująca sie do funkcji sprawdzającej wygranego lub remis
def check_game_over():
    check_winner()
    check_tie()

    return

# Główna funkcja gry, to ona jest odpowiedzialna za całą rozgrywkę
def game_on():

    # Wyświetlanie zainicjowanej tablicy z grą
    display_board()

    # Główna pętla while w której toczy się gra, przekazanie tury graczowi, sprawdzenie czy są zwycięzcy, zmiana
    # gracza.
    while game_still_on:

        # Przekazanie tury aktualnemu graczowi
        handle_turn(current_player)

        # Sprawdzenie czy ktoś wygrał bądźczy jest remis
        check_game_over()

        # Jeśli nie ma ramisu bądźwygranych zmiana gracza z X na O, z O na X.
        change_player()

    # Jeśli 'wyskoczymy' z pętli powyżej w punkcie check_if_game_over przejdziemy do polecenia if
    # sprawdzająca któy gracz wygrał lub czy jest remis
    if winner == 'X' or winner == 'O':
        print(f'\nPlayer {winner} has won!')
    elif winner == None:
        print('\nNo one won. Tie!')

    return

print('Tic Tac Toe game! 2k20\n')
game_on()
# Input który zatrzymuje program przed zamknięciem się po wykonaniu gry
input("Press enter to close program")