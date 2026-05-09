import os

def limpar_tela():
    """Limpa o console de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro atual na tela."""
    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador atual venceu o jogo."""
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for v in vitorias:
        if tabuleiro[v[0]] == tabuleiro[v[1]] == tabuleiro[v[2]] == jogador:
            return True
    return False

def jogo():
    """Função principal que controla o fluxo do jogo."""
    tabuleiro = [str(i+1) for i in range(9)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        limpar_tela()
        print("="*20)
        print("   JOGO DA VELHA")
        print("="*20)
        imprimir_tabuleiro(tabuleiro)
        
        try:
            escolha_str = input(f"Jogador {jogador_atual}, escolha uma posição (1-9) ou 'q' para sair: ").strip().lower()
            
            if escolha_str == 'q':
                print("Saindo do jogo...")
                break
                
            escolha = int(escolha_str) - 1
            
            if escolha < 0 or escolha > 8:
                print("Erro: Escolha um número entre 1 e 9.")
                input("Pressione Enter para tentar novamente...")
                continue
                
            if tabuleiro[escolha] in ["X", "O"]:
                print("Erro: Essa posição já está ocupada!")
                input("Pressione Enter para tentar novamente...")
                continue
                
            tabuleiro[escolha] = jogador_atual
            jogadas += 1
            
            if verificar_vitoria(tabuleiro, jogador_atual):
                limpar_tela()
                print("="*20)
                print("   FIM DE JOGO!")
                print("="*20)
                imprimir_tabuleiro(tabuleiro)
                print(f"PARABÉNS! O jogador '{jogador_atual}' venceu!\n")
                break
            
            if jogadas == 9:
                limpar_tela()
                print("="*20)
                print("   FIM DE JOGO!")
                print("="*20)
                imprimir_tabuleiro(tabuleiro)
                print("EMPATE! Não houve vencedores.\n")
                break
                
            # Alterna o jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
            
        except ValueError:
            print("Erro: Entrada inválida. Digite um número de 1 a 9.")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    jogo()
