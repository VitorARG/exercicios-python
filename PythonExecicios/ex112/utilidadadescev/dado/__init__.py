#112: dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.
def leiadinhero(msg):
    while True:
        num = str(input(msg))
        num = num.replace(',', '.')
        if num.replace('.', '').isnumeric():
            num = float(num)
            return num
        else:
            num = num.strip()
            print(f'\033[31mErro {num} é um preço invalido\033[m ')


