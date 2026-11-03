import sqlite3
from datetime import datetime

busca = input("Digite o nome do amigo: ").strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))
        total = 0

        for total, amigo in enumerate(cursor, start=1):

            try:
                datetime.strptime(str(amigo['nascimento']), "%Y-%m-%d")
                nascimento = datetime.strptime((amigo['nascimento']), '%Y-%m-%d').strftime('%d/%m/%Y')
                idade = datetime.now().year - datetime.strptime(str(amigo['nascimento']), '%Y-%m-%d').year
                print(f"[{total}] - {amigo['nome']} nasceu em {nascimento} e tem {idade} anos.")
            except ValueError:
                print(f"Data de nascimento inválida para {amigo['nome']}: {amigo['nascimento']}")


        if total == 0:
            print(f"Nenhum registro encontrado com o nome '{busca}'.")
        else:
            print(f"Foram encontrados {total} registros com o nome '{busca}'.")





except Exception as erro:
    print(f"Erro: {erro}")
