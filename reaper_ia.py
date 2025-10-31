#  ===========================================================
# PROPRIETÁRIO: Ramirez M  
# PROJETO: REAPER 1.0 - Assistente de Cibersegurança e Pentest
# DATA: 23/10/2025
# ============================================================

import os
import speech_recognition as sr
from google import genai
from google.genai import types

# Config. da chave Gemini

try:
 
    client = genai.Client()
    print(" Cliente Gemini inicializado com sucesso.")
except Exception as e:
    print(" ERRO: Não foi possível inicializar o cliente Gemini.")
    print("Por favor, verifique se a variável de ambiente 'GEMINI_API_KEY' está configurada corretamente.")
    print(f"Detalhes do erro: {e}")
    exit()

# Fala para texto (por enquanto)

def ouvir_fala():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Ouvindo...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Tempo limite de escuta excedido. Nenhuma fala detectada.")
            return None
        
# Google Speech Recognition

    try:
        print(" Processando o áudio...")
        texto = r.recognize_google(audio, language="pt-BR")
        print(f" Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print(" Desculpe, não entendi.")
        return None
    except sr.RequestError as e:
        print(f" Erro no serviço de fala: {e}")
        return None

# Interação com o Gemini

def obter_resposta_ia(prompt):  
    if not prompt:
        return "Desculpe, não entendi ."

# Configuração do modelo e do prompt (contexto da IA)

    system_instruction = (
        "Você é um assistente de cibersegurança e pentest chamado REAPER. "
        "Sua função é ser útil, informativo e focado em segurança ofensiva e defensiva. "
        "Mantenha as respostas concisas e no tom de um especialista em segurança. "
        "Responda à pergunta do usuário a seguir."
    )

    config = types.GenerateContentConfig(
        system_instruction=system_instruction
    )
    
# Chamada à API
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Rápido e ideal para conversação
            contents=prompt,
            config=config
        )
        return response.text
    except Exception as e:
        return f" ERRO na API Gemini: {e}. Tente novamente."

# Função Principal
def main():
    """Loop principal de conversação da IA."""
    print("="*50)
    print("         REAPER 1.0 - Assistente de Segurança")
    print("="*50)
    print("Inicie falando. Pressione Ctrl+C para sair a qualquer momento.")

    while True:
        # 1. Entrada de Fala
        texto_usuario = ouvir_fala()

        if texto_usuario:
            # 2. Processamento e Resposta da IA
            print("\n Pensando...")
            resposta_ia = obter_resposta_ia(texto_usuario)
            
            # 3. Saída no Terminal (Passo atual)
            print("\n--------------------------------------------------")
            print(f" REAPER: {resposta_ia}")
            print("--------------------------------------------------")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n REAPER encerrado. Até a próxima!")
        # Garante que o ambiente virtual seja desativado ao sair
        # (Você ainda precisará fazer isso manualmente com 'deactivate' se não fechar o terminal)