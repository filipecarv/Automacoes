from playwright.sync_api import sync_playwright
from urllib.parse import quote
import speech_recognition as sr
import pyttsx3

# Voz da assistente
engine = pyttsx3.init()

def falar(texto):
    print("Assistente:", texto)
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Estou ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
        return texto.lower()

    except sr.UnknownValueError:
        falar("Não entendi o que você disse.")
        return ""

    except Exception as erro:
        print(erro)
        return ""

falar("Olá Filipe. O que você quer fazer hoje?")

comando = ouvir()

if comando:

    with sync_playwright() as pw:
        navegador = pw.chromium.launch(headless=False)
        pagina = navegador.new_page()

        if "youtube" in comando:
            pesquisa = comando.replace("youtube", "").strip()

            falar(f"Pesquisando {pesquisa} no YouTube")

            pagina.goto(
                f"https://www.youtube.com/results?search_query={quote(pesquisa)}"
            )

        elif "spotify" in comando:
            pesquisa = comando.replace("spotify", "").strip()

            falar(f"Abrindo Spotify e pesquisando {pesquisa}")

            pagina.goto(
                f"https://open.spotify.com/search/{quote(pesquisa)}"
            )

        elif "google" in comando:
            pesquisa = comando.replace("google", "").strip()

            falar(f"Pesquisando {pesquisa} no Google")

            pagina.goto(
                f"https://www.google.com/search?q={quote(pesquisa)}"
            )

        else:
            falar("Vou pesquisar isso no Google.")

            pagina.goto(
                f"https://www.google.com/search?q={quote(comando)}"
            )

        input("Pressione ENTER para fechar...")
        navegador.close()