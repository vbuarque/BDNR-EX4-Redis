import controllers.cartController as cartController

cartController.insert('vinicius', '[{"nome": "Teclado gamer", "preco": "R$250.00"}]')
cartController.findCart('vinicius')
cartController.deleteCart('vinicius')
cartController.findCart('vinicius')