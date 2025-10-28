#  ===========================================================
# PROPRIETÁRIO: Ramirez M  
# PROJETO: REAPER 1.0 - Assistente de Cibersegurança e Pentest
# DATA: 23/10/2025
# ============================================================

import os
import speech_recognition as sr
from google import genai
from google.genai import types

#Fala para texto (por enquanto)

def ouvir_falar():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("\n Ouvindo...")
        r.adjust_for_ambient_noise(source)
        try:
            audio= r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print ("Nenhuma fala detectada.")
            return None

# Google Speech Recognitio
    try:
        print(" Processando o áudio...")
        texto = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError as e:
        print(f"Erro na requisição do serviço de fala: {e}")
        return None
    
# interação com o Gemini
def obter_resposta_ia(prompt):
    if not prompt:
        return "Desculpe, não entendi"
    
#Configuração do modelo e do prompt (contexto da IA)
system_instruction = (
    "Você é um assistente de cibersegurança e pentest chamado REAPER. "
        "Sua função é ser útil, informativo e focado em segurança ofensiva e defensiva. "
        "Mantenha as respostas concisas e no tom de um especialista em segurança. "
        "Responda à pergunta do usuário a seguir."
    )
config = types.GenerateContentConfig(
    system_instruction=system_instruction
)
