import time
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted


def _gerar_com_retry(modelo, prompt, tentativas=3, espera_inicial=5):
    """Chama o Gemini com retry em caso de estouro de cota (ResourceExhausted)."""
    for i in range(tentativas):
        try:
            return modelo.generate_content(prompt)
        except ResourceExhausted:
            if i == tentativas - 1:
                raise
            time.sleep(espera_inicial * (i + 1))  # espera crescente: 5s, 10s, 15s...
    return None


def teste(chave, info):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-2.0-flash')

    prompt = (
        f"Verifique se a seguinte informação sobre mudanças climáticas está correta: {info}. "
        f"Responda com 'Correto' ou 'Errado', seguido de uma explicação."
    )

    try:
        resposta = _gerar_com_retry(modelo, prompt)
    except ResourceExhausted:
        return (
            "Erro",
            "O limite de requisições da API do Gemini foi atingido. "
            "Aguarde alguns instantes e tente novamente, ou verifique sua cota no Google AI Studio."
        )
    except Exception as e:
        return "Erro", f"Ocorreu um erro ao consultar a IA: {e}"

    texto_resposta = resposta.text.strip().split("\n")
    veracidade = texto_resposta[0]
    explicacao = "\n".join(texto_resposta[1:])

    return veracidade, explicacao


def verificar_link(chave, link):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-2.0-flash')

    prompt = (
        f"Verifique a autenticidade do seguinte link sobre mudanças climáticas: {link}. "
        f"Analise se ele contém informações falsas ou incorretas e forneça uma explicação "
        f"detalhada sobre as inconsistências científicas."
    )

    try:
        resposta = _gerar_com_retry(modelo, prompt)
    except ResourceExhausted:
        return (
            "Erro",
            "O limite de requisições da API do Gemini foi atingido. "
            "Aguarde alguns instantes e tente novamente, ou verifique sua cota no Google AI Studio."
        )
    except Exception as e:
        return "Erro", f"Ocorreu um erro ao consultar a IA: {e}"

    texto_resposta = resposta.text.strip().split("\n")
    veracidade_link = texto_resposta[0]
    explicacao_link = "\n".join(texto_resposta[1:])

    return veracidade_link, explicacao_link
