import sqlite3

# banco = sqlite3.connect("meubanco.db")
#banco.row_factory = sqlite3.Row
#cursor = banco.cursor()
# lista = cursor.fetchall()
# print(lista)
#cursor.close()
#banco.close()

busca = input("Digite o nome do amigo: ").strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))
        total = 0
        lista = []
        
        for total, amigo in enumerate(cursor, start=1):
            lista.append({"id": amigo['id'], "nome": amigo['nome'], "nascimento": amigo['nascimento']})
        print(f"Foram encontrados {total} registros com o nome '{busca}'.")

        for dados in lista:
            print(dados)

except Exception as erro:
    print(f"Erro: {erro}")
