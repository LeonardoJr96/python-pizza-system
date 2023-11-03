from assets import module

pedidos = module.pedidoss()

while module.pedidoss() == True:
  tipes = int(input("Selecione um número que deseja começar: (1)Pizzas salgadas (2)Pizzas doces (3)Bebidas: "))
  if tipes == 1:
    module.salgados()
  elif tipes == 2:
    module.doces()
  elif tipes == 3:
    module.bebidas()
print(f'build finished')