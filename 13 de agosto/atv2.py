def get_email_info(email):
    endereco = email.split('@')
    dominio = endereco[1].split('.')[0]
    return endereco[0], dominio
        

def main():
    from os import system
    system('cls')

    while True:
        email = input('Digite o seu endereco de email :')
        if '@' not in email:
            system('cls')
            print('Email invalido')
        else:
            break
    endereco, dominio = get_email_info(email)
    print(f'Ola o seu endereco é {endereco} e o dominio é {dominio}')

if __name__ == '__main__':
    main()