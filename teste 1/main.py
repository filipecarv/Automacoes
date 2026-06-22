#esse codigo e para automatizar o navegador usando o python
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()

    #abre o navegador
    pagina = contexto.new_page()

    #navegar para a pagina do google
    pagina.goto("https://www.google.com")

    #pegar informações da pagina
    print(pagina.title())

    #selecionar elemento na tela
    botao = pagina.get_by_role("combobox", name="Pesquisar")
    botao.fill(input("Digite o que deseja pesquisar:"))
    botao.press("Enter")

    #Nao sou um robo
    pagina.get_by_role("button", name="Não sou um robô").click()
    pagina.get_by_role("button", name="Enviar").click()
    print(pagina.title())

    #Clicar no primeiro link da pesquisa
    pagina.get_by_role("link", name="Python.org").click()
    print(pagina.title())

    time.sleep(5)
    navegador.close()