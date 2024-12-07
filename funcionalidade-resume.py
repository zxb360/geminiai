import google.generativeai as genai
import os
import gradio as gr
# import pdb
import time

# ===============>
# PROJETO TRYBE CHATBOT DE EMOÇÕES:

os.environ["GEMINI_API_KEY"]  # trazendo a chave

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="""Criação
    e melhoria de curriculo.""")
chat = model.start_chat()

# De acordo com exercicio é quebra o problema em partes


def prompt_chat(prompt):
    # função que captura o texto e anexo
    text = [prompt["text"]]
    uploader_file = uploads_files(prompt)  # função do anexo
    text.extend(uploader_file)  # tratando o array
    return text

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
                time.sleep(4)
                uploader_file = genai.get_file(load_files_path.name)
            uploader_file.append(load_files_path)
    return uploader_file


def start_chat(prompt, _history):
    prompt = prompt_chat(prompt)
    try:
        response = chat.send_message(prompt)

    except IndentationError as e:
        print(e)
        response = f"Não entendi o que você falou, pode tentar novamente? {e}"
        # pdb.set_trace()
        #     if file_path['mime_type'] in ["image/jpg", "image/png",
        # "image/gif"]:
        #         capture_file = file_path["path"]
        #         uploader_file.append(load_files_path)
        #     elif file_path['mime_type'] in ["text/plain", "application/pdf",
        #  "application/msword"]:
        #         capture_file = file_path["path"]
        #         load_files_path = genai.upload_file(path=capture_file)
        #         uploader_file.append(load_files_path)
        # text.extend(uploader_file)
    return response.text

    response = chat.send_message()


chat_interface = gr.ChatInterface(
    fn=start_chat,
    title="Intentificado de melhoria do curriculo",
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
