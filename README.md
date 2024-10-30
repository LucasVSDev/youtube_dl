# YouTube Video & Audio Downloader

Este projeto é uma aplicação em Python para download de vídeos e áudios do YouTube em diferentes formatos e qualidades, usando uma interface gráfica desenvolvida com Tkinter. 

## Funcionalidades

- **Pesquisar Vídeos**: Insere-se um link do YouTube e é feita a busca das informações do vídeo.
- **Download de Vídeos e Áudio**:
  - **HD** (720p)
  - **SD** (360p)
  - **MP3** (áudio)
- **Interface Gráfica**: Layout intuitivo, com barra de progresso e status do download.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para o desenvolvimento.
- **Tkinter**: Biblioteca para construção da interface gráfica.
- **Pytube**: Biblioteca para download de vídeos do YouTube.
- **Pillow**: Para processamento de imagens.
- **Requests**: Para download da thumbnail do vídeo.

## Estrutura do Código

- **Função `pesquisar`**: Responsável por buscar as informações do vídeo (título, duração e thumbnail) e exibi-las na interface.
- **Funções de Download**:
  - `download_mp3`: Download do áudio em formato MP3.
  - `download_mp4_hd`: Download do vídeo em alta resolução (HD).
  - `download_mp4_sd`: Download do vídeo em baixa resolução (SD).
- **Função `on_progress`**: Atualiza a barra de progresso e exibe o status do download.

## Requisitos

Certifique-se de instalar as seguintes dependências antes de executar o programa:

```bash
pip install pytube pillow requests
```

## Como Usar

1. **Execute o script**: Abra o terminal e execute o arquivo.
2. **Insira o link**: Cole o link do vídeo do YouTube na barra de pesquisa e clique em "Pesquisar".
3. **Escolha o formato**: Selecione o formato desejado (HD, SD ou MP3) e clique no botão correspondente.
4. **Download em Progresso**: A barra de progresso será exibida. Ao final, uma mensagem indicará a conclusão do download.

## Observações

- O arquivo é salvo automaticamente na área de trabalho do usuário.
- Em caso de arquivo duplicado, é feita a renomeação automática com um número incremental.