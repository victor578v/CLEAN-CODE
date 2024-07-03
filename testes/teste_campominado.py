import pytest
from campominado import (
    inicializar_tabuleiro, 
    contar_minas_ao_redor, 
    imprimir_tabuleiro, 
    salvar_pontuacao, 
    exibir_ranking,
    obter_entrada_valida
)
import os

def test_inicializar_tabuleiro():
    tamanho = 5
    numero_de_minas = 5
    tabuleiro = inicializar_tabuleiro(tamanho, numero_de_minas)
    
    # Verifica se o tabuleiro tem o tamanho correto
    assert len(tabuleiro) == tamanho
    assert all(len(linha) == tamanho for linha in tabuleiro)

    # Conta o número de minas
    minas_no_tabuleiro = sum(linha.count('*') for linha in tabuleiro)
    assert minas_no_tabuleiro == numero_de_minas

def test_contar_minas_ao_redor():
    tabuleiro = [
        ['*', ' ', ' '],
        [' ', '*', ' '],
        [' ', ' ', '*']
    ]
    
    # Testa algumas posições específicas
    assert contar_minas_ao_redor(tabuleiro, 0, 0) == 2  # Deve contar 2 minas ao redor de (0, 0)
    assert contar_minas_ao_redor(tabuleiro, 1, 1) == 3  # Deve contar 3 minas ao redor de (1, 1)
    assert contar_minas_ao_redor(tabuleiro, 1, 0) == 2  # Deve contar 2 minas ao redor de (1, 0)
    assert contar_minas_ao_redor(tabuleiro, 2, 0) == 1  # Deve contar 1 mina ao redor de (2, 0)
    assert contar_minas_ao_redor(tabuleiro, 2, 2) == 2  # Deve contar 1 mina ao redor de (2, 2)
    assert contar_minas_ao_redor(tabuleiro, 0, 2) == 1  # Deve contar 0 minas ao redor de (0, 2)

def test_imprimir_tabuleiro(capsys):
    tabuleiro = [
        ['*', '1', ' '],
        ['1', '*', '1'],
        [' ', '1', '*']
    ]
    visivel = [
        [False, True, False],
        [True, False, True],
        [False, True, False]
    ]
    imprimir_tabuleiro(tabuleiro, visivel)
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')
    
    assert [line.strip() for line in output] == [
        '■ 1 ■', 
        '1 ■ 1', 
        '■ 1 ■'
    ]

def test_salvar_pontuacao():
    nome = "Teste"
    pontos = 100
    salvar_pontuacao(nome, pontos)
    
    with open('ranking.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    assert f"{nome} {pontos}\n" in linhas

def test_exibir_ranking(capsys):
    with open('ranking.txt', 'w') as arquivo:
        arquivo.write("Teste1 100\n")
        arquivo.write("Teste2 200\n")
    
    exibir_ranking()
    captured = capsys.readouterr()
    output = captured.out.strip()
    
    assert "Ranking (👑 Top 5 👑):" in output
    assert "Teste2 200" in output
    assert "Teste1 100" in output

def test_obter_entrada_valida(monkeypatch):
    inputs = iter(["5", "abc", "-1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert obter_entrada_valida("Digite um número: ", 3) == 2

# Limpa o arquivo de ranking após os testes
def teardown_module(module):
    os.remove('ranking.txt')

if __name__ == "__main__":
    pytest.main()


