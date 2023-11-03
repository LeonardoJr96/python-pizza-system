# Python-Pizza-System

Este documento descreve um sistema de pedidos em Python, abordando os requisitos, funcionalidades e instruções de uso! fornecendo informações sobre o Sistema de Pedido de Pizza, que permite aos clientes fazerem pedidos de pizzas salgadas, pizzas doces e bebidas. O sistema é composto por dois arquivos: `app_python.py` (script principal) e `module.py` (módulo contendo funções relacionadas aos pedidos).

## Arquivo app_python.py

O arquivo `app_python.py` é o script principal responsável por iniciar o sistema e interagir com o usuário.

### Iniciando o Sistema

O sistema é iniciado quando o usuário executa o arquivo `app_python.py`. A partir daí, os clientes podem escolher entre pizzas salgadas, pizzas doces e bebidas para fazer seus pedidos.

### Encerrando o Sistema

O sistema é encerrado quando o usuário decide finalizar seus pedidos. Não é necessário fechar manualmente o sistema, pois ele lida com esse processo automaticamente.

## Arquivo module.py

O arquivo `module.py` contém funções relacionadas aos pedidos de pizza e bebidas, bem como funções auxiliares.

### Funções Principais

- `pedidoss()`: Verifica se ainda existem pedidos a serem feitos.
- `salgados()`: Permite aos clientes fazer pedidos de pizzas salgadas.
- `doces()`: Permite aos clientes fazer pedidos de pizzas doces.
- `bebidas()`: Permite aos clientes fazer pedidos de bebidas.

### Adicionando Coberturas Extras

Os clientes podem adicionar coberturas extras aos seus pedidos, como bacon, requeijão, milho e azeitona. O sistema oferece a opção de adicionar essas coberturas aos pedidos.

### Outras Funções

- `repetir()`: Pergunta se o cliente deseja fazer mais pedidos ou finalizar o pedido atual.
- `true_false()`: Pergunta se o cliente deseja finalizar o pedido por completo.
- `outras(sugar_drink_finished_salgado)`: Direciona o cliente para fazer mais pedidos, escolhendo entre pizzas doces, bebidas ou finalização.

### Explicação Detalhada

O sistema permite aos clientes escolher entre três categorias de itens: pizzas salgadas, pizzas doces e bebidas. Para cada categoria, os clientes podem selecionar os sabores desejados e, se desejarem, adicionar coberturas extras, como bacon, requeijão, milho e azeitona. O sistema pergunta aos clientes se desejam fazer mais pedidos ou finalizar o pedido atual. Se escolherem finalizar, podem decidir se desejam encerrar completamente o processo de pedido.

Este é um resumo da estrutura do sistema e de suas funções. Certifique-se de adaptar os nomes de arquivos e caminhos conforme a estrutura do seu projeto.

---

*Nota: Certifique-se de adaptar os caminhos de importação e outras configurações de acordo com a estrutura do seu projeto.*

Esta documentação fornece uma visão geral das funcionalidades e do funcionamento de um Sistema de Pedido de Pizza básico.
