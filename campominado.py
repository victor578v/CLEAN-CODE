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
