add = []
pedido = []
pedidos = True

def pedidoss():
  return pedidos == True

def salgados():
  tipes_sabor = int(input("digite o sabor que deseja: \n(1)Calabresa \n(2)Portuguesa \n(3)Mussarela  \n(4)Pepperoni\n"))
  adicionais_true_false = int(input("adicionais: (1)Sim (2)Não\n"))
  if adicionais_true_false == 1:
    adicionais()
    repetir()
  else:
    repetir()

def doces():
  tipes_sabor = int(input("digite o sabor que deseja: \n(1)Prestígio \n(2)Chocolate \n(3)Doce de Leite\n"))
  print(tipes_sabor)
  repetir()

def bebidas():
  tipes_sabor = int(input("digite a bebida que deseja: \n(1)Calabresa \n(2)Portuguesa \n(3)Mussarela  \n(4)Pepperoni\n"))
  print(tipes_sabor)
  repetir()

def select(selected):
  if selected == 1:
    return "Bacon"
  elif selected == 2:
    return "Requeijão"
  elif selected == 3:
    return "Milho"
  elif selected == 4:
    return "Azeitona"

def adicionais():

  print("adicionais: Bacon, Requeijão, Milho e Azeitona")
  qtd = int(input("Informe a quantidade de adições: "))
  selected = int(input("(1)Bacon\n(2)Requeijão\n(3)Milho\n(4)Azeitona\n"))
  select(selected)
  add.append(select(selected))

  for i in range(qtd - 1):
    selected = int(input())
    select(selected)
    add.append(select(selected))

def repetir():
    sugar_drink_finished_salgado = int(input("Quer pedir mais ou finalizar? (1)Pizzas Doces (2)Bebidas (3)Finalizar\n"))
    outras(sugar_drink_finished_salgado)

def true_false():
    a = int(input("finallizar o pedido? (1)Sim (2)Não\n"))
    if a == 1:
      return pedidoss == False
    else:
      return pedidoss == True

def outras(sugar_drink_finished_salgado):
  if sugar_drink_finished_salgado == 1:
    doces()
  elif sugar_drink_finished_salgado == 2:
    bebidas()
  elif sugar_drink_finished_salgado == 3:
    true_false()
  elif sugar_drink_finished_salgado == 4:
    salgados()

