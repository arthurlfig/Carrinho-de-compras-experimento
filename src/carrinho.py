"""Carrinho com frete calculado sobre o subtotal dos itens."""

from math import isfinite


class Carrinho:
    def __init__(self):
        self._itens = {}

    def adicionar_item(self, nome, preco, quantidade=1):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido")
        if (isinstance(preco, bool) or not isinstance(preco, (int, float))
                or not isfinite(preco) or preco < 0):
            raise ValueError("Preço inválido")
        if (isinstance(quantidade, bool) or not isinstance(quantidade, int)
                or quantidade <= 0):