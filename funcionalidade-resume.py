import google.generativeai as genai
import os
import gradio as gr
from automatizando_home import set_light_values, intruction_alert
import pdb
import time

# ===============>
# PROJETO TRYBE CHATBOT DE EMOÇÕES:

os.environ["GEMINI_API_KEY"]  # trazendo a chave

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

initial_prompt = (
    "chat, você é Coach de Carreira ajudará ajustar currículo"
    "Caso aja algum anexo verificar a melhor edição currícular"
    "Área de especialização para melhorar starcks do currículo"
    )

model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=initial_prompt,
            tools=[set_light_values, intruction_alert],
    )
chat = model.start_chat(enable_automatic_function_calling=True)

# De acordo com exercicio é quebra o problema em partes


def prompt_chat(prompt):
    try:
        text = [prompt["text"]]
        up_files = uploads_files(prompt)  # função do anexo
        if not isinstance(up_files, (list, tuple)):
            raise TypeError("up_files não é uma lista ou tupla")

        text.extend(up_files)
        return text
    except Exception as err:
        print(err)
        return []

# CARREGANDO IMAGEM


def uploads_files(arquivs_files):  # função do anexo
    uploader_file = []

    if arquivs_files['files']:
        # TENTATIVA DE VERIFICAR O ARQUIVO PELO MIMETYPE

        # mime_type, _ = mimetypes.guess_type(prompt['files'])
        # if mime_type in ["text/plain", "application/pdf"]:
        #     with open(prompt['files'][0]['path'], "r") as file:
        #         resume = genai.upload_file(path=file)

        # elif mime_type in ["image/jpeg", "image/png"]:
        #     resume = genai.upload_file(path=prompt['files'])

        # else:
        #     print("não reconheci nada")
        for file_path in arquivs_files['files']:
            load_files_path = genai.upload_file(path=file_path["path"])
            while load_files_path.state.name == "PROCESSING":
                time.sleep(6)
                uploader_file = genai.get_file(load_files_path.name)
            uploader_file.append(load_files_path)
    return uploader_file


def start_chat(prompt, _history):
    while prompt is None:
        pdb.set_trace()
        return chat.send_message("Precisa de ajuda com currículo?")
    prompt = prompt_chat(prompt)
    try:
        response = chat.send_message(prompt)
        return response.text
    except IndentationError as e:
        print(e)
        response = f"Não entendi o que você falou, pode tentar novamente? {e}"
        # pdb.set_trace()
    return prompt_chat(prompt)

    response = chat.send_message()


chat_interface = gr.ChatInterface(
    fn=start_chat,
    title="Criação e ajustes de currículos",
    description="Atua como um analisador de curriculo.",
    multimodal=True,  # habilita o suporte a multimodal
    # retry_btn=None,  # desabilita o botão de tentar novamente
    # undo_btn="Apagar",  # altera o texto do botão de desfazer
    # clear_btn="Limpar",  # altera o texto do botão de limpar
    # submit_btn="Enviar",  # altera o texto do botão de enviar
    # theme="soft",  # altera o tema para mais claro
    # css="footer {visibility: hidden}"  # esconde o rodapé
    )
chat_interface.launch()


# initial = chat.send_message("Você é o mestre criador de historias D&D")
# def create_story(prompt, _history):
#     response = [prompt['files']]
#     # import pdb; pdb.set_trace() # verificar se prompt está vindo como
#       esperado
#     return response.text


# caso queira exporta documento como curriculo:
# with open("resume.txt", "r") as file:
#     resume = file.read()

# caso seja imagem, planilha foto
# students_spreadsheet = genai.upload_file(
#    path="desempenho_estudantes_enem.csv",
#    display_name="Notas do Enem"
# )
