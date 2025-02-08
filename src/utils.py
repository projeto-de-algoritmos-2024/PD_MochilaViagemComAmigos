from typing import List


def validar_peso(peso):
    try:
        peso = int(peso)
        if peso <= 0:
            raise ValueError
        return peso
    except ValueError:
        raise ValueError("O peso deve ser um número inteiro positivo.")
    
def validar_peso_list(peso_str: str) -> List[int]:
    pesos = []
    for p in peso_str.split(','):
        p = p.strip()
        if p.isdigit():
            pesos.append(validar_valor(p))
        else:
            raise ValueError(f"Peso inválido: {p}. Deve ser um número inteiro não negativo.")
    return pesos

def validar_valor(valor):
    try:
        
        valor = int(valor)
        if valor < 0:
            raise ValueError
        return valor
    except ValueError:
        raise ValueError("O valor deve ser um número inteiro não negativo.")
    


