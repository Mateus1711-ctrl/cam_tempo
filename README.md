
# Projeto Câmera

## Descrição

Este projeto implementa um processador de vídeo em tempo real que aplica efeitos de **rotação** e **cisalhamento**, com interpolação bilinear, sobre o feed da câmera. O código foi desenvolvido em **Python** usando **NumPy** para as transformações geométricas e **OpenCV** para a captura do feed de vídeo. As transformações são aplicadas de maneira contínua e fluida, com controles interativos via teclado para ajuste da rotação e do cisalhamento.

### Principais Funcionalidades

- **Rotação contínua**: A imagem gira continuamente ao redor do centro da tela.
- **Cisalhamento horizontal**: Um efeito de distorção horizontal pode ser aplicado e ajustado em tempo real.
- **Interpolação Bilinear**: Utilizada para suavizar a imagem durante as transformações, evitando artefatos visuais.
- **Controle dinâmico**: O usuário pode ajustar a velocidade da rotação e a intensidade do cisalhamento em tempo real.
- **Execução simples**: Basta rodar o script para começar a aplicar os efeitos no feed da sua webcam.

## Como Funciona

O sistema utiliza **matrizes de transformação** para realizar rotação e cisalhamento da imagem em tempo real. A rotação acontece ao redor do centro da imagem, utilizando translações para mover o centro para a origem e, após a rotação, devolvê-lo à posição original. A interpolação bilinear suaviza a transição entre os pixels durante a transformação, melhorando a qualidade da imagem.

### Matemática por trás

#### Rotação

A rotação é feita com a seguinte matriz de rotação:

\[
R(\theta) =
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

#### Cisalhamento

O cisalhamento horizontal é realizado com a seguinte matriz:

\[
S =
\begin{bmatrix}
1 & \text{shear\_factor} & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

#### Interpolação Bilinear

A interpolação bilinear é usada para suavizar os pixels transformados, calculando uma média ponderada entre os pixels adjacentes, evitando artefatos visuais.

## Instruções de Uso
### Execução via setup.py

Este projeto foi configurado para ser instalado via o arquivo `setup.py`. Para instalar e rodar o projeto, siga os seguintes passos:

1. No terminal, navegue até o diretório do projeto onde está o arquivo `setup.py`.
2. Instale o projeto localmente com o comando:

   ```
   pip install .
   ```

3. Após a instalação, você pode rodar o programa com o comando:

   ```
   cam_tempo
   ```

### Controles

- **W**: Aumenta a velocidade da rotação.
- **S**: Diminui a velocidade da rotação.
- **A**: Aumenta o cisalhamento horizontal.
- **D**: Diminui o cisalhamento horizontal.
- **Q**: Fecha o programa.

## Autores

Desenvolvido por [João Delomo](https://github.com/JoaoDelomo) e [Mateus Porto](https://github.com/Mateus1711-ctrl).