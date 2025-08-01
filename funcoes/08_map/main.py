# Lambda
pg = lambda x: x*2
pa = lambda x: x+3

# algoritmo principal
if __name__ == "__main__":
    #lista
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # exibe a pg
    print(f"Progressão Geometrica{list(map(pg, numeros))}")
    print(f"Progressão Aritmética{list(map(pa, numeros))}")