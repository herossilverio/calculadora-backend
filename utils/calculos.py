def calcular_resina(dados):
    total_resina = 0.0
    layup = []

    for camada in dados['camadas']:
        tipo = camada['tipo']
        peso = float(camada['peso'])
        espessura = float(camada['espessura'])

        if tipo == 'reforco':
            resina = peso * 1.1
        elif tipo == 'nucleo':
            resina = espessura * 100
        else:
            resina = 0.0

        total_resina += resina
        layup.append({**camada, 'resina': resina})

    return {'total_resina': total_resina, 'layup': layup}
