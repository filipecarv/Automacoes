from playwright.sync_api import sync_playwright
from urllib.parse import quote
import speech_recognition as sr
import pyttsx3

# Voz da assistente
engine = pyttsx3.init()

def falar(texto):
    print("Parceira:", texto)
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Estou escutando meu mano...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
        return texto.lower()

    except sr.UnknownValueError:
        falar("Não entendi o que você disse meu parceiro.")
        return ""

    except Exception as erro:
        print(erro)
        return ""

falar("Eae meu mano Filipe. O que tem de bom pra fazer hoje meu parceiro?")

comando = ouvir()

if comando:

    with sync_playwright() as pw:

        contexto = pw.chromium.launch_persistent_context(user_data_dir="./perfil",headless=False,args=["--start-maximized"],no_viewport=True)
        pagina = contexto.pages[0] if contexto.pages else contexto.new_page()

        #Pagina do Youtube
        if "youtube" in comando:
            pesquisa = comando.replace("youtube", "").strip()

            falar(f"Pesquisando {pesquisa} no YouTube meu mano")

            pagina.goto(
                f"https://www.youtube.com/results?search_query={quote(pesquisa)}"
            )

        #Pagina Padrão
        else:
            pesquisa = comando.replace("google", "").strip()

            falar(f"Pesquisando {pesquisa} no Google meu mano")

            pagina.goto(
                f"https://www.google.com/search?q={quote(pesquisa)}"
            )

        input("Pressione ENTER para fechar meu parceiro...")
        contexto.close()