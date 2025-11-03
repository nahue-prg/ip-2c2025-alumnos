# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j
    
    # Verificar si ya terminamos
    if i >= n - 1:
        return {"done": True}
    
    # 1) Elegir índices a y b a comparar en este micro-paso
    a = j
    b = j + 1
    swap = False
    
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b]
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True
    
    # 3) Avanzar punteros (preparar el próximo paso)
    j += 1
    if j >= n - 1 - i:
        i += 1
        j = 0
    
    # 4) Devolver el estado actual
    return {"a": a, "b": b, "swap": swap, "done": False}
