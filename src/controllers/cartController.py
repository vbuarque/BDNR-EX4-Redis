import connectBd as Db
from pprint import pprint

def insert(userName, product):
    myRedis = Db.connect()
    key = f'carrinho:{userName}' 
    value = {f'"produtos": {product}'}
    myRedis.set(key, f'{value}')
    pprint('===== ADICIONANDO O CARRINHO =====')
    pprint('==Carrinho inserido com sucesso!==')
    pprint(myRedis.get(key))
    print('\n')

def findCart(userName):
    myRedis = Db.connect()
    key = f'carrinho:{userName}' 
    carts = myRedis.get(key)
    pprint(f'===== CARRINHO DE COMPRAS DE {userName.upper()} =====')
    pprint(carts)
    print('\n')

def deleteCart(userName):
    myRedis = Db.connect()
    key = f'carrinho:{userName}' 
    myRedis.delete(key)
    pprint(f'===== DELETAR CARRINHO =====')
    pprint('==Carrinho deletado com sucesso!==')
    print('\n')