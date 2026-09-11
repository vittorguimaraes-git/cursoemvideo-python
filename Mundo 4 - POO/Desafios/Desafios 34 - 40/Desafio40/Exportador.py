import json
import dicttoxml
from xml.dom.minidom import parseString

from functools import singledispatchmethod

class Aluno:
    def __init__(self, nome, curso, serie):

        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:

    def __init__(self, user, email):

        self.usuario = user
        self.email = email


class JSON:


    @singledispatchmethod
    def exportar(self, obj):
        raise NotImplementedError(f"Tipo {type(obj)} não suportado")

    @exportar.register
    def _(self, obj:Aluno):
        return json.dumps(obj.__dict__, indent=4)

    @exportar.register
    def _(self, obj: Usuario):
        return json.dumps(obj.__dict__, indent=4)


class XML:

    @singledispatchmethod
    def exportar(self, obj):
        raise NotImplementedError(f"Tipo {type(obj)} não suportado")

    @exportar.register

    def _(self, obj:Aluno):
        xml = dicttoxml.dicttoxml(obj.__dict__, attr_type=False)
        xml_string = xml.decode("utf-8")
        xml_formatado = parseString(xml_string).toprettyxml(indent='  ')
        return xml_formatado

    @exportar.register
    def _(self, obj: Usuario):
        xml = dicttoxml.dicttoxml(obj.__dict__, attr_type=False)
        xml_string = xml.decode("utf-8")
        xml_formatado = parseString(xml_string).toprettyxml(indent='  ')
        return xml_formatado


def exportar_dados(formato, dado):
    try:
        return formato.exportar(dado)
    except Exception as e:
        print("Algo deu errado:", e)



