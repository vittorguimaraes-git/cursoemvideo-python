class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:

    def __init__(self):
        self.produtos = []

    def __add__(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)
        elif isinstance(produto, list):
            self.produtos.extend(produto)
        else:
            raise TypeError("Só aceito Produto ou lista de Produto")
        return self

    def __str__(self):
        texto = ["-" * 30]
        for produto in self.produtos:
            texto.append(f"{produto.arquivo}  (R${produto.preco:,.2f})")
        texto.append("-" * 30)
        texto.append(f"TOTAL: R${self.total:,.2f}")
        return "\n".join(texto)

    @property
    def total(self):
        return sum(produto.preco for produto in self.produtos)