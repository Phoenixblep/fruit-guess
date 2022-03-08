import random

def stringgenerate():
    option1 = [
        "apple", "an _____ a day, keeps the doctor away.", "Apples Are 25% Air."
    ]
    option2 = [
        "mango", "_____ is also known as the king of fruits.", "Mangoes first appeared in India over 5,000 years ago."
    ]
    option3 = [
        "grape", "A ______ come in green and black variants and is seedless.", "Table and Wine Grapes Are Different."
    ]
    option4 = [
        "orange", "______ juice contains Vitamin C, Vitamin A, Calcium.", "There are over 600 varieties of oranges."
    ]
    option5 = [
        "banana", "The _______ may have been the world's first cultivated fruit.", "A banana is a berry not a fruit."
    ]
    a = [option1, option2, option3, option4, option5]
    answer = random.choice(a)
    x = answer[0]
    stringgenerate.hint = answer[1]
    stringgenerate.fact = answer[2]
    game(x)

def game(a):
    acopy = a
    b = "*" * len(a)
    attempts = len(a)
    c = attempts
    w = " " * len(a)
    print(f"[>] {b}")
    success = 0
    print(f"Hint: {stringgenerate.hint}")
    while 1:
        print(f"\n[>] You have {attempts} attempts left.")
        print(f"[>] Enter a letter without quotes\n")
        ch = input("[>] ")
        x = a.find(ch)
        m = w.find(ch)
        if m != -1:
            print(f"\n[>] You guessed it already! its wrong")
            print(f"[>] Previous wrong guesses : ")
            print(f"[>] {w}")
            continue
        if x == -1:
            w = ch + ", " + w
            print(f"[>] Previous wrong guesses : {w}")
            print(f"[>] Wrong guess! try again")
            attempts = attempts - 1
            print(f"[>] {b}")
        else:
            print("[>] Correct Guess!\n")
            b = b[0:x] + a[x] + b[x + 1:c]
            a = a[0:x] + '*' + a[x + 1:c]
            success = success + 1
            print(f"[>] {b}")
        if attempts == 0:
            flag = 1
            break
        if success == c:
            flag = 0
            break
    if flag == 0:
        print(f"[>] Congrats! word is {acopy}")
        print(f"Fun Fact, {stringgenerate.fact}")
    else:
        print(f"[>] Better luck next time.")
    playagain()

def main():
    stringgenerate()

def playagain():
    ch = input(
        f"\n[>] If you want to play again,\n[>] Press (Y/N)\n[>] ").lower()
    if ch == 'y' or ch == 'yes':
        main()
    else:
        print(f"[>] Thanks for playing the game!\n")

main()
