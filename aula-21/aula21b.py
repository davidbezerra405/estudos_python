def somar(a=0, b=0, c=0):
    """
    Parametros opcionais
    :param a: se não informado vale 0
    :param b: se não informado vale 0
    :param c: se não informado vale 0
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(8)
somar()
