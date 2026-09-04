from pessoa import Aluno
from rich import inspect, print

def main():
    
    a = Aluno("Vittor", 2004, "ADS")
    a.add_curso("DIR")
    a.curso = "DIR"
    inspect(a, private=True, methods=True)


if __name__ == "__main__":
    main()
