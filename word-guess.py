import random


def stringgenerate():
    a1 = "hello"
    a2 = "world"
    a3 = "well"
    a4 = "cool"
    a5 = "ok"
    a6 = "bruh"
    a7 = "lessgo"
    a8 = "github"
    a9 = "hehe"
    a10 = "dababy"
    a11 = "lav"
    a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]
    x = random.choice(a)
    game(x)


def game(a):
    acopy = a
    b = "*" * len(a)
    attempts = len(a)
    c = attempts
    w = " " * len(a)
    print(f"[>] {b}")
    success = 0
    while 1:
        print(f"[>] You have {attempts} attempts left")
        print(f"[>] Enter a letter without quotes\n")
        ch = input("[>] ")
        x = a.find(ch)
        m = w.find(ch)
        if m != -1:
            print(f"[>] You guessed it already! its wrong")
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
        print(f"[>] Congrats! word is ")
        print(f"[>] {acopy}")
    else:
        print(f"[>] Better luck next time")
    playagain()


def main():
    stringgenerate()


def playagain():
    ch = input(
        f"[>] If you want to play again,\n[>] Press (Y/N)\n[>] ").lower()
    #ch=input("")
    if ch == 'y':
        main()
    else:
        print(f"[>] Thanks for playing the game!\n")


main()
