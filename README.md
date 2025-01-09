# **Projeto Gemini - Análise Inteligente de Currículos**  

## 🧠 **Descrição**  
O **Projeto Gemini** é uma aplicação que utiliza **Inteligência Artificial Generativa** para responder perguntas relacionadas a currículos. Desenvolvido com a biblioteca **Gradio**, o sistema é capaz de processar arquivos anexados e fornecer feedback personalizado para melhorar o perfil profissional do usuário.  

## ⚙️ **Funcionalidades**  
- **Análise de Arquivos:** Upload de currículos em formatos como PDF ou DOCX para análise.  
- **Sugestões Inteligentes:** Identifica áreas de melhoria no currículo, como habilidades, formatação e organização de informações.  
- **Respostas Personalizadas:** Responde perguntas diretamente relacionadas ao conteúdo do currículo anexado.  
- **Interface Interativa:** Sistema simples e intuitivo, baseado em componentes do Gradio para upload de arquivos e exibição de respostas.  

## 🔧 **Tecnologias Utilizadas**  
- **Biblioteca** Biblioteca Gradio para criação de interfaces amigáveis.  
- **Inteligência Artificial:** Modelo generativo da OpenAI para processamento de linguagem natural.  
- **Outras Dependências:**  
  - Manipulação de arquivos (PDF e outros formatos).  
  - Integração dinâmica com o Gradio para interfaces interativas.  


## 🚀 **Como Executar o Projeto**  

### 1. **Crie e ative um ambiente virtual**  
```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  
```

### 2. **Instale as dependências**  
```bash
pip install gradio
```

### 3. **Execute a aplicação**  
```bash
python funcionalidade-resume.py
```

### 4. **Acesse no navegador**  
O Gradio abrirá automaticamente uma aba no navegador com a interface da aplicação. Se não abrir, acesse o link indicado no terminal (ex.: [http://127.0.0.1:7860](http://127.0.0.1:7860)).  

## 🕵️ **Notas Importantes**  
- Certifique-se de que as bibliotecas necessárias para manipulação de arquivos (como PyPDF2) estejam instaladas.  
- O modelo generativo requer uma API configurada para funcionar corretamente. Adicione sua chave de API no código ou arquivo de configuração.  

## 🛡️ **Contribuições e Melhorias**  
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no projeto.
