import os
import platform
from lista_encadeada import ListaEncadeada

def limpar_terminal():
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(comando)

def mostrar_menu():
    print("--- MENU ---")
    print("1. Inserir elemento")
    print("2. Remover elemento")
    print("3. Obter elemento")
    print("4. Modificar elemento")
    print("5. Verificar se está vazia")
    print("6. Obter tamanho")
    print("7. Imprimir lista")
    print("8. Sair")

def main():
    lista = ListaEncadeada()

    while True:
        limpar_terminal()
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        try:
            limpar_terminal()
            if opcao == "1":
                pos = int(input("Posição para inserir (1 a tamanho+1): "))
                val = int(input("Valor: "))
                lista.inserir(pos, val)
                print("Inserido com sucesso.")
            elif opcao == "2":
                pos = int(input("Posição para remover: "))
                removido = lista.remover(pos)
                print(f"Removido: {removido}")
            elif opcao == "3":
                pos = int(input("Posição para obter: "))
                print("Valor:", lista.obter_elemento(pos))
            elif opcao == "4":
                pos = int(input("Posição para modificar: "))
                val = int(input("Novo valor: "))
                lista.modificar_elemento(pos, val)
                print("Modificado com sucesso.")
            elif opcao == "5":
                print("Lista está vazia?", lista.esta_vazia())
            elif opcao == "6":
                print("Tamanho atual:", lista.obter_tamanho())
            elif opcao == "7":
                lista.imprimir()
            elif opcao == "8":
                print("Encerrando...")
                break
            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()