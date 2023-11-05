pedido = []


def sabores_salgados(tipes_sabor):
    if tipes_sabor == 1:
        pedido.append('Calabresa')
    elif tipes_sabor == 2:
        pedido.append('Portuguesa')
    elif tipes_sabor == 3:
        pedido.append('Mussarela')
    elif tipes_sabor == 4:
        pedido.append('Pepperoni')
    print(pedido)

def sabores_doces(tipes_doce):
    if tipes_doce == 1:
        pedido.append('Prestígio')
    elif tipes_doce == 2:
        pedido.append('Chocolate')
    elif tipes_doce == 3:
        pedido.append('Doce de Leite')
    print(pedido)

def sabores_drinks(tipes_sabor):
    if tipes_sabor == 1:
        pedido.append('Coca')
    elif tipes_sabor == 2:
        pedido.append('Pepsi')
    elif tipes_sabor == 3:
        pedido.append('Guaraná')
    elif tipes_sabor == 4:
        pedido.append('Fanta')
    print(pedido)
