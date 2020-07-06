# Desafio da aula 5 Módulo 4
import shutil
import os


class Bot:
    def __init__(self):
        pass

    def criarArquivo(self, nome):
        with open(nome, 'w')as aquivo:
            pass

    def criarPasta(self, nome):
        if not os.path.isdir(nome):
            os.mkdir(nome)
        else:
            print('Diretório já foi criado')

    def mover(self, atual, destino):
        shutil.move(os.getcwd() + os.sep + atual,
                    os.getcwd() + os.sep + destino)

    def copiar(self, atual, destino):
        shutil.copy(os.getcwd() + os.sep + atual,
                    os.getcwd() + os.sep + destino)

    def copiarTudo(self, atual, destino):
        shutil.copytree(os.getcwd() + os.sep + atual,
                        os.getcwd() + os.sep + destino)

    def compactar(self, nome):
        shutil.make_archive(nome, 'zip', os.getcwd())

    def excluir(self, nome):
        shutil.rmtree(os.getcwd() + os.sep + nome)

    def compactarTodoDiretorio(self, nome):
        shutil.make_archive(nome, 'zip', root_dir=os.getcwd())


bot = Bot()
bot.criarPasta('Arquivos 2010')
bot.criarPasta('Documentação')
bot.criarPasta('Backup')
bot.criarArquivo('nomes.txt')
bot.criarArquivo('inscrições.pdf')
bot.criarArquivo('relatórios.xlsx')
bot.copiar('nomes.txt', 'Arquivos 2010')
bot.mover('inscrições.pdf', 'Documentação')
bot.copiarTudo('Arquivos 2010', 'Backup Arquivos 2010')
bot.compactar('Documentação')
bot.mover('Documentação.zip', 'Backup')
bot.excluir('Arquivos 2010')
bot.excluir('Documentação')
bot.compactarTodoDiretorio('Backup Arquivos Python')
