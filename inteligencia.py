import google.generativeai as genai

def teste(chave, info):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"Verifique se a seguinte informação sobre mudanças climáticas está correta: {info}. Responda com 'Correto' ou 'Errado', seguido de uma explicação."

    resposta = modelo.generate_content(prompt)

    texto_resposta = resposta.text.strip().split("\n")

    veracidade = texto_resposta[0]
    explicacao = "\n".join(texto_resposta[1:])

    return veracidade, explicacao

def verificar_link(chave, link):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"Verifique a autenticidade do seguinte link sobre mudanças climáticas: {link}. Analise se ele contém informações falsas ou incorretas e forneça uma explicação detalhada sobre as inconsistências científicas."

    resposta = modelo.generate_content(prompt)

    texto_resposta = resposta.text.strip().split("\n")

    veracidade_link = texto_resposta[0]
    explicacao_link = "\n".join(texto_resposta[1:])

    return veracidade_link, explicacao_link
