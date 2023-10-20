<h1 align="center">Eden</h1>

# Language|Linguagem
- [English](#english)
- [Português](#português)

# Português
:question: Modelo para um assistente residencial
> Este é um modelo de aprendizado profundo projetado para lidar com espectrogramas sonoros, que são representações bidimensionais do som, visando a identificação dos tipos de som presentes nesses espectrogramas. O modelo é baseado em uma Convolutional Neural Network (CNN) com ativação ReLU, composta por duas camadas 2D convolucionais, seguidas por uma camada de redução de dimensionalidade e outra de dropout para evitar overfitting. O objetivo é mapear características dos dados de entrada (espectrogramas) para categorias de saída (classes de áudio) por meio do treinamento. Esse modelo é eficaz na classificação de áudio com base nas características extraídas dos espectrogramas, tornando-se uma ferramenta valiosa para identificar tipos de som em dados de áudio.
## Como clonar o repositório
```bash
$ git clone https://github.com/periclesbgf/home-assistant-model.git
```
## Como executar o programa
```bash
$ cd "model" 
$ python main.py
```
## Como compilar o modelo
1. Escolha o kernel que o python especificado
2. Rode o notebook

*Não esqueça de ter habilitado a extensão jupyter*
### Sobre os arquivos:
- sample_generator.py (Gravar o som para preencher o banco de dados)
### Pacotes instalados na venv:
- numpy
- tensorflow
- pyaudio
- matplotlib (versão: 3.7.2)
- seaborn
- librosa
- pydub

*Caso haja algum problema no pyaudio, tente instalar o pacote portaudio*
### Lembrete:
- *Esse modelo foi baseado no modelo do Tensorflow, ele reconhecerá uma palavra de cada vez*
- *O formato do arquivo de áudio é .wav a 16.000 Hz*
- *Foram utilizados 80% dos dados para treinamento e 20% para validação*
