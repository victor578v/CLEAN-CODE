import random, time

def init(t, m):
    b, mc = [[' ' for _ in range(t)] for _ in range(t)], 0
    while mc < m:
        r, c = random.randint(0, t - 1), random.randint(0, t - 1)
        if b[r][c] != '*':
            b[r][c], mc = '*', mc + 1
    return b

def cnt(b, r, c):
    t, n = len(b), 0
    for i in range(max(0, r - 1), min(t, r + 2)):
        for j in range(max(0, c - 1), min(t, c + 2)):
            if b[i][j] == '*': n += 1
    return n

def print_board(b, v):
    for i in range(len(b)):
        for j in range(len(b)):
            print(b[i][j] if v[i][j] else '■', end=' ')
        print()

# Inicio Victor

def save_score(n, p):
    with open('ranking.txt', 'a') as f:
        f.write(f'{n} {p}\n')

def show_ranking():
    try:
        with open('ranking.txt', 'r') as f:
            r = f.readlines()
        r.sort(key=lambda x: int(x.split()[1]), reverse=True)
        print("Ranking (👑 Top 5 👑):\n====================================")
        for x in r[:5]: print(x.strip())
        print("====================================")
    except:
        print("Nenhum ranking encontrado.")

# Fim Victor

# Inicio Éverson

    # Função principal do jogo Campo Minado
def jogo_campo_minado():
    tamanho = 8
    numero_de_minas = 10
    tabuleiro = inicializar_tabuleiro(tamanho, numero_de_minas)
    visivel = [[False for _ in range(tamanho)] for _ in range(tamanho)]

    nome = input("Digite seu nome: ")
    inicio_tempo = time.time()
    pontos = 0

    while True:
        imprimir_tabuleiro(tabuleiro, visivel)
        linha = obter_entrada_valida(f"Digite a linha (0 a {tamanho - 1}): ", tamanho)
        coluna = obter_entrada_valida(f"Digite a coluna (0 a {tamanho - 1}): ", tamanho)

        if tabuleiro[linha][coluna] == '*':
            print("====================================")
            print("💣 Você pisou em uma mina! Fim de jogo. 💣")
            break
        else:
            if not visivel[linha][coluna]:
                visivel[linha][coluna] = True
                minas_ao_redor = contar_minas_ao_redor(tabuleiro, linha, coluna)
                tabuleiro[linha][coluna] = str(minas_ao_redor)
                pontos += 10

            if all(all(c == '*' or v for c, v in zip(linha, visivel_linha)) for linha, visivel_linha in zip(tabuleiro, visivel)):
                print("====================================")
                print("🎉🎉 Parabéns, você venceu! 🎉🎉")
                break

    fim_tempo = time.time()
    tempo_total = fim_tempo - inicio_tempo

    salvar_pontuacao(nome, pontos)
    print(f"🕘 Seu tempo foi de {tempo_total:.2f} segundos. 🕒")
    print(f"🚩 Sua pontuação foi de {pontos} pontos. 🚩")
    exibir_ranking()

if __name__ == "__main__":
    jogo_campo_minado()

    #Fim Éverson