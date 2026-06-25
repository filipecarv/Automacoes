from playwright.sync_api import sync_playwright
from urllib.parse import quote
#esse codigo e para automatizar o navegador usando o python

print("eae meu mano, Filipe!")

while True:
    comando = input("\no que tem de bom pra fazer hoje meu parceiro ? (Digite 'sair' para fechar!)\n> ").lower()

    if comando == "sair":
        break

    with sync_playwright() as pw:
        contexto = pw.chromium.launch_persistent_context(user_data_dir=r"C:\Users\Educação\AppData\Local\Google\Chrome\User Data",channel="chrome",headless=False,args=["--start-maximized"],no_viewport=True)
        pagina = contexto.pages[0]

        if "youtube" in comando:
            pesquisa = comando.replace("youtube", "").strip()
            pagina.goto(
                f"https://www.youtube.com/results?search_query={quote(pesquisa)}"
            )
        else:
            pagina.goto(
                f"https://www.google.com/search?q={quote(comando)}"
            )

        print("Pronto meu parceiro!")

        input("Pressione 'Enter' para continuar meu mano...")
        contexto.close()