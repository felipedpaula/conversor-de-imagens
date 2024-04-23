## Visão Geral do Programa:

O programa é uma ferramenta de conversão de imagens que permite aos usuários converter imagens de um formato para outro de forma simples e eficiente. Ele suporta a conversão de uma única imagem específica ou de todas as imagens em uma pasta. Os formatos de imagem suportados para conversão incluem PNG, JPG (ou JPEG) e WEBP. O usuário pode selecionar o formato desejado e escolher entre converter uma imagem específica ou todas as imagens em uma pasta de origem para uma pasta de destino.

O processo de conversão é realizado utilizando a biblioteca Python Pillow (PIL), que oferece funcionalidades para manipulação de imagens. O programa verifica se a imagem está no modo 'RGBA' ou 'P' e a converte para o modo 'RGB' antes de realizar a conversão, garantindo compatibilidade com os formatos de destino. Em caso de erro durante a conversão, o programa exibe uma mensagem de erro indicando o problema encontrado.

## Configuração do Ambiente Virtual e Instalação de Dependências

**1. Instale o pacote python3.8-venv usando o comando:**
```shell
sudo apt install python3.8-venv
```

**2. Navegue até o diretório onde o programa está localizado e crie um ambiente virtual usando o comando (Dentro da pasta py):**
```shell
python3 -m venv venv
```

**3. Ative o ambiente virtual utilizando o comando adequado ao seu sistema operacional (Dentro da pasta py):**
```shell
source venv/bin/activate
```

**4. Com o ambiente virtual ativado, instale a biblioteca Pillow usando o pip:**
```shell
pip install Pillow
```

## Executando o Programa:
Após configurar o ambiente virtual e instalar as dependências necessárias, você pode executar o programa seguindo estes passos:

Certifique-se de que o ambiente virtual esteja ativado.
Execute o programa Python usando o seguinte comando:
```shell
python3 conversor_imagem.py
```

## Explicação das Importações:

As importações `from PIL import Image` e `import os` são utilizadas para acessar funcionalidades específicas das bibliotecas PIL (Python Imaging Library) e os (sistema operacional).

- **PIL (Python Imaging Library):**
  - A importação `from PIL import Image` permite o acesso à classe `Image` da biblioteca PIL. Essa classe fornece métodos para abrir, manipular e salvar imagens em vários formatos de arquivo. No contexto deste programa, a biblioteca PIL é utilizada para realizar operações de conversão de formatos de imagem.

- **OS (Sistema Operacional):**
  - A importação `import os` permite o acesso às funcionalidades relacionadas ao sistema operacional. O módulo `os` fornece métodos para interagir com o sistema de arquivos, como listar arquivos em um diretório, verificar a existência de um arquivo, manipular caminhos de arquivos, entre outros. No programa, a biblioteca `os` é utilizada para lidar com arquivos e diretórios, como localizar imagens a serem convertidas e definir os caminhos de saída para as imagens convertidas.

## Função convert_image(input_path, output_path, output_format):

Esta função é responsável por converter uma única imagem de um formato para outro e salvar o resultado no destino especificado.

- **Parâmetros:**
  - `input_path`: O caminho do arquivo de imagem de entrada que será convertido.
  - `output_path`: O caminho do arquivo de imagem de saída onde a imagem convertida será salva.
  - `output_format`: O formato de arquivo desejado para a imagem de saída (por exemplo, 'PNG', 'JPEG', 'WEBP').

- **Funcionamento:**
  - A função utiliza uma estrutura de controle `try-except` para lidar com possíveis erros que possam ocorrer durante o processo de conversão da imagem.
  - Dentro do bloco `try`, a função abre a imagem de entrada usando o método `Image.open()` da biblioteca PIL. A imagem é aberta em um contexto de bloco `with`, garantindo que o arquivo seja fechado corretamente após o uso.
  - Em seguida, a função verifica se o modo da imagem está entre 'RGBA' (RGB com canal alfa) ou 'P' (imagem paletizada). Se a imagem estiver em um desses modos, ela é convertida para o modo 'RGB' usando o método `convert('RGB')`.
  - Após a conversão, a imagem convertida é salva no caminho de saída especificado usando o método `save()` da classe `Image`. O parâmetro `format` é utilizado para especificar o formato do arquivo de saída.
  - Por fim, uma mensagem é exibida indicando que a imagem foi convertida e salva com sucesso, juntamente com o caminho do arquivo de saída.

- **Tratamento de Erros:**
  - Se ocorrer algum erro durante o processo de conversão da imagem, ele será capturado pelo bloco `except` e uma mensagem de erro será exibida informando o problema encontrado.

Essa função desempenha um papel fundamental no processo de conversão de imagens e é chamada tanto quando o usuário escolhe converter uma imagem específica quanto quando todas as imagens em uma pasta são convertidas.

## Função convert_all_images(source_folder, output_folder, output_format):

Esta função é responsável por percorrer todos os arquivos de imagem em uma pasta de origem, converter cada imagem para o formato especificado e salvar os arquivos convertidos em uma pasta de destino.

- **Parâmetros:**
  - `source_folder`: O caminho para a pasta que contém as imagens a serem convertidas.
  - `output_folder`: O caminho para a pasta onde os arquivos de imagem convertidos serão salvos.
  - `output_format`: O formato de arquivo desejado para as imagens de saída (por exemplo, 'PNG', 'JPEG', 'WEBP').

- **Funcionamento:**
  - A função utiliza um loop `for` para percorrer cada arquivo na pasta especificada em `source_folder`.
  - Para cada arquivo, a função verifica se o nome do arquivo termina com uma das extensões de imagem suportadas ('.png', '.jpg', '.jpeg', '.bmp' ou '.gif'). Isso é feito utilizando o método `endswith()` da string `filename` em letras minúsculas.
  - Se o arquivo for uma imagem suportada, a função monta o caminho completo para o arquivo de entrada (`input_path`) e o caminho para o arquivo de saída (`output_path`). O nome do arquivo de saída é construído alterando a extensão do arquivo original para o formato de saída desejado.
  - Em seguida, a função chama a função `convert_image()` com os caminhos de entrada e saída, bem como o formato de saída especificado. Isso efetivamente realiza a conversão da imagem e salva o arquivo convertido na pasta de destino.

Essa função é útil para converter todas as imagens em uma pasta de uma só vez, seguindo as mesmas etapas de conversão definidas na função `convert_image()`.

## Função main():

Esta função é o ponto de entrada principal do programa. Ela controla a interação com o usuário, permite que o usuário escolha entre converter uma imagem específica ou todas as imagens em uma pasta e direciona o fluxo de execução do programa com base na escolha do usuário.

- **Funcionamento:**
  - A função inicia solicitando ao usuário que escolha entre duas opções: converter uma imagem específica (digitando '1') ou todas as imagens na pasta (digitando '2'). Isso é feito usando a função `input()`.
  - Se o usuário escolher converter uma imagem específica (opção '1'), o programa solicita ao usuário que insira o nome da imagem, incluindo a extensão do arquivo. Em seguida, verifica se o arquivo de imagem especificado existe no diretório 'toConvert'. Se não existir, exibe uma mensagem de erro e retorna.
  - Em seguida, o programa solicita ao usuário que selecione o formato para a conversão da imagem, apresentando uma lista de opções numeradas ('1' para PNG, '2' para JPG e '3' para WEBP'). O usuário fornece o número correspondente ao formato desejado.
  - O programa utiliza um dicionário `format_dict` para mapear os números de escolha do formato para os formatos de saída correspondentes ('PNG', 'JPEG' e 'WEBP').
  - Se o formato escolhido pelo usuário estiver presente no dicionário `format_dict`, o programa determina o caminho de saída para o arquivo convertido com base no nome da imagem de entrada e no formato de saída escolhido. Em seguida, chama a função `convert_image()` para realizar a conversão da imagem especificada.
  - Se o usuário escolher converter todas as imagens na pasta (opção '2'), o programa exibe uma mensagem indicando que todas as imagens da pasta 'toConvert' serão convertidas. Em seguida, o programa solicita ao usuário que selecione o formato para a conversão de todas as imagens, seguindo o mesmo processo descrito acima.
  - Se o usuário inserir uma opção inválida que não seja '1' ou '2', o programa exibe uma mensagem de erro pedindo ao usuário que escolha entre as opções válidas.

Essa função coordena o fluxo de execução do programa, permitindo que o usuário interaja com ele e escolha as operações desejadas de forma intuitiva.
