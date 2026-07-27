from groq import Groq
from groq import RateLimitError


def _perguntar_groq(chave, prompt):
    """Envia o prompt para a Groq e retorna o texto da resposta."""
    cliente = Groq(api_key=chave)

    resposta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return resposta.choices[0].message.content


def teste(chave, info):
    prompt = (
        f"Verifique se a seguinte informação sobre mudanças climáticas está correta: {info}. "
        f"Responda com 'Correto' ou 'Errado', seguido de uma explicação."
    )

    try:
        texto = _perguntar_groq(chave, prompt)
    except RateLimitError:
        return (
            "Erro",
            "O limite de requisições da API foi atingido. Aguarde um pouco e tente novamente."
        )
    except Exception as e:
        return "Erro", f"Ocorreu um erro ao consultar a IA: {e}"

    texto_resposta = texto.strip().split("\n")
    veracidade = texto_resposta[0]
    explicacao = "\n".join(texto_resposta[1:])

    return veracidade, explicacao


def verificar_link(chave, link):
    prompt = (
        f"Verifique a autenticidade do seguinte link sobre mudanças climáticas: {link}. "
        f"Analise se ele contém informações falsas ou incorretas e forneça uma explicação "
        f"detalhada sobre as inconsistências científicas."
    )

    try:
        texto = _perguntar_groq(chave, prompt)
    except RateLimitError:
        return (
            "Erro",
            "O limite de requisições da API foi atingido. Aguarde um pouco e tente novamente."
        )
    except Exception as e:
        return "Erro", f"Ocorreu um erro ao consultar a IA: {e}"

    texto_resposta = texto.strip().split("\n")
    veracidade_link = texto_resposta[0]
    explicacao_link = "\n".join(texto_resposta[1:])

    return veracidade_link, explicacao_lin