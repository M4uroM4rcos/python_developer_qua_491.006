# Função

def fibonacci_recursivo(n):
    """
    Gera a sequência de Fibonacci usando recursão (abordagem recursiva).
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)