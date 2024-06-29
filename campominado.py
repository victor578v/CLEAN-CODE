# import random
# import time

# def inicializar_tabuleiro(tamanho, numero_de_minas):
#     tabuleiro = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
#     minas_colocadas = 0

#     while minas_colocadas < numero_de_minas:
#         linha = random.randint(0, tamanho - 1)
#         coluna = random.randint(0, tamanho - 1)
#         if tabuleiro[linha][coluna] != '*':
#             tabuleiro[linha][coluna] = '*'
#             minas_colocadas += 1
#     return tabuleiro

# def contar_minas_ao_redor(tabuleiro, linha, coluna):
#     tamanho = len(tabuleiro)
#     minas_ao_redor = 0
#     for i in range(max(0, linha - 1), min(tamanho, linha + 2)):
#         for j in range(max(0, coluna - 1), min(tamanho, coluna + 2)):
#             if tabuleiro[i][j] == '*':
#                 minas_ao_redor += 1
#     return minas_ao_redor

# def imprimir_tabuleiro(tabuleiro, visivel):
#     tamanho = len(tabuleiro)
#     for i in range(tamanho):
#         for j in range(tamanho):
#             if visivel[i][j]:
#                 print(tabuleiro[i][j], end=' ')
#             else:
#                 print('■', end=' ')
#         print()

# def salvar_pontuacao(nome, pontos):
#     with open('ranking.txt', 'a') as arquivo:
#         arquivo.write(f'{nome} {pontos}\n')

# def exibir_ranking():
#     try:
#         with open('ranking.txt', 'r') as arquivo:
#             rankings = arquivo.readlines()
#         rankings.sort(key=lambda x: int(x.split()[1]), reverse=True)
#         print("Ranking (👑 Top 5 👑):")
#         print("====================================")
#         for ranking in rankings[:5]:
#             print(ranking.strip())
#         print("====================================")
#     except FileNotFoundError:
#         print("Nenhum ranking encontrado.")

# def obter_entrada_valida(mensagem, tamanho):
#     while True:
#         try:
#             valor = int(input(mensagem))
#             if 0 <= valor < tamanho:
#                 return valor
#             else:
#                 print(f"❌ Posição inválida, deve ser entre 0 e {tamanho - 1}. ❌")
#         except ValueError:
#             print("❌ Entrada inválida, por favor insira um número. ❌")

# def jogo_campo_minado():
#     tamanho = 8
#     numero_de_minas = 10
#     tabuleiro = inicializar_tabuleiro(tamanho, numero_de_minas)
#     visivel = [[False for _ in range(tamanho)] for _ in range(tamanho)]

#     nome = input("Digite seu nome: ")
#     inicio_tempo = time.time()
#     pontos = 0

#     while True:
#         imprimir_tabuleiro(tabuleiro, visivel)
#         linha = obter_entrada_valida(f"Digite a linha (0 a {tamanho - 1}): ", tamanho)
#         coluna = obter_entrada_valida(f"Digite a coluna (0 a {tamanho - 1}): ", tamanho)

#         if tabuleiro[linha][coluna] == '*':
#             print("====================================")
#             print("💣 Você pisou em uma mina! Fim de jogo. 💣")
#             break
#         else:
#             if not visivel[linha][coluna]:
#                 visivel[linha][coluna] = True
#                 minas_ao_redor = contar_minas_ao_redor(tabuleiro, linha, coluna)
#                 tabuleiro[linha][coluna] = str(minas_ao_redor)
#                 pontos += 10

#             if all(all(c == '*' or v for c, v in zip(linha, visivel_linha)) for linha, visivel_linha in zip(tabuleiro, visivel)):
#                 print("====================================")
#                 print("🎉🎉 Parabéns, você venceu! 🎉🎉")
#                 break

#     fim_tempo = time.time()
#     tempo_total = fim_tempo - inicio_tempo

#     salvar_pontuacao(nome, pontos)
#     print(f"🕘 Seu tempo foi de {tempo_total:.2f} segundos. 🕒")
#     print(f"🚩 Sua pontuação foi de {pontos} pontos. 🚩")
#     exibir_ranking()

# if __name__ == "__main__":
#     jogo_campo_minado()






# import random, time

# def init(t, m):
#     b = [[' ' for _ in range(t)] for _ in range(t)]
#     mc = 0
#     while mc < m:
#         r, c = random.randint(0, t - 1), random.randint(0, t - 1)
#         if b[r][c] != '*':
#             b[r][c] = '*'
#             mc += 1
#     return b

# def cnt(b, r, c):
#     t, n = len(b), 0
#     for i in range(max(0, r - 1), min(t, r + 2)):
#         for j in range(max(0, c - 1), min(t, c + 2)):
#             if b[i][j] == '*':
#                 n += 1
#     return n

# def print_board(b, v):
#     t = len(b)
#     for i in range(t):
#         for j in range(t):
#             if v[i][j]:
#                 print(b[i][j], end=' ')
#             else:
#                 print('■', end=' ')
#         print()

# def save_score(n, p):
#     with open('ranking.txt', 'a') as f:
#         f.write(f'{n} {p}\n')

# def show_ranking():
#     try:
#         with open('ranking.txt', 'r') as f:
#             r = f.readlines()
#         r.sort(key=lambda x: int(x.split()[1]), reverse=True)
#         print("Ranking (👑 Top 5 👑):\n====================================")
#         for x in r[:5]:
#             print(x.strip())
#         print("====================================")
#     except FileNotFoundError:
#         print("Nenhum ranking encontrado.")

# def game():
#     t, m = 8, 10
#     b, v = init(t, m), [[False for _ in range(t)] for _ in range(t)]
#     n = input("Digite seu nome:")
#     s, p = time.time(), 0

#     while True:
#         print_board(b, v)
#         try:
#             r, c = int(input(f"Digite a linha (0 a {t - 1}): ")), int(input(f"Digite a coluna (0 a {t - 1}): "))
#             if r < 0 or r >= t or c < 0 or c >= t:
#                 print("❌ Posição inválida, tente novamente. ❌")
#                 continue
#         except ValueError:
#             print("❌ Entrada inválida, por favor insira números. ❌")
#             continue

#         if b[r][c] == '*':
#             print("====================================\n💣 Você pisou em uma mina! Fim de jogo. 💣")
#             break
#         else:
#             if not v[r][c]:
#                 v[r][c] = True
#                 b[r][c] = str(cnt(b, r, c))
#                 p += 10
#             if all(all(c == '*' or v for c, v in zip(l, vl)) for l, vl in zip(b, v)):
#                 print("\n🎉🎉 Parabéns, você venceu! 🎉🎉")
#                 break

#     e = time.time()
#     save_score(n, p)
#     print(f"\n🕘 Seu tempo foi de {e - s:.2f} segundos. 🕒\n\n🚩 Sua pontuação foi de {p} pontos. 🚩\n")
#     show_ranking()

# if __name__ == "__main__":
#     game()





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

def game():
    b, v, t, m = init(8, 10), [[False for _ in range(8)] for _ in range(8)], 8, 10
    n, s, p = input("Digite seu nome:"), time.time(), 0
    while True:
        print_board(b, v)
        try:
            r, c = int(input(f"Digite a linha (0 a {t - 1}): ")), int(input(f"Digite a coluna (0 a {t - 1}): "))
            if r < 0 or r >= t or c < 0 or c >= t: print("❌ Posição inválida, tente novamente. ❌"); continue
        except: print("❌ Entrada inválida, por favor insira números. ❌"); continue
        if b[r][c] == '*': print("====================================\n💣 Você pisou em uma mina! Fim de jogo. 💣"); break
        if not v[r][c]: v[r][c], b[r][c], p = True, str(cnt(b, r, c)), p + 10
        if all(all(c == '*' or v for c, v in zip(l, vl)) for l, vl in zip(b, v)): print("\n🎉🎉 Parabéns, você venceu! 🎉🎉"); break
    e = time.time()
    save_score(n, p)
    print(f"\n🕘 Seu tempo foi de {e - s:.2f} segundos. 🕒\n\n🚩 Sua pontuação foi de {p} pontos. 🚩\n")
    show_ranking()

if __name__ == "__main__":
    game()
