from random import randint

def main():
    a = randint(1, 100)
    
    while True:
        try :
            b = int(input('Devinez le numéro: '))
            if b == a:
                print('Correct!')
                break

        except ValueError:
            print('Veuillez entrer un nombre entier')
main()