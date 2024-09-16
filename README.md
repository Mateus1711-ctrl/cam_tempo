
# Projeto Câmera

## Descrição

Este projeto implementa um processador de vídeo em tempo real usando **Python** e **NumPy** para aplicar efeitos de **rotação** e **cisalhamento** sobre o feed da câmera. As transformações são controláveis pelo usuário via **teclado**, proporcionando interatividade e personalização das transformações geométricas aplicadas ao vídeo.

### Principais Funcionalidades

- **Rotação em tempo real**: A imagem é rotacionada continuamente ao redor do centro da tela.
- **Cisalhamento (Shearing)**: O usuário pode aplicar um efeito de cisalhamento controlado, distorcendo a imagem horizontalmente.
- **Controle interativo**: A rotação e o cisalhamento podem ser ajustados em tempo real usando o teclado.
- **Fácil execução**: Basta rodar o script para começar a aplicar os efeitos diretamente na saída de vídeo da sua webcam.

## Como Funciona

Este projeto usa **matrizes de transformação** para aplicar as operações de rotação e cisalhamento. As transformações são feitas usando a álgebra linear, sem o uso de bibliotecas externas que façam as transformações geométricas por você. A câmera é capturada em tempo real, e as transformações são aplicadas frame a frame, criando um efeito visual dinâmico e responsivo.

### Matemática por trás

#### Rotação

A rotação é realizada utilizando a seguinte matriz de rotação:

$$
R(\theta) =
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta)  & 0 \\
0            & 0             & 1
\end{bmatrix}
$$

Para rotacionar em torno do centro da imagem, aplicamos uma **translação** para mover o centro para a origem, realizamos a rotação, e então desfazemos a translação para restaurar a posição original.

#### Cisalhamento

O cisalhamento é aplicado usando a matriz de cisalhamento, que distorce a imagem horizontalmente:

$$
S = 
\begin{bmatrix}
1 & shear\_factor & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Esta transformação distorce a imagem ao longo do eixo x, criando um efeito de "inclinação".

## Instruções de Uso

### Requisitos

Para rodar este projeto, você precisa instalar as seguintes bibliotecas:

- [OpenCV](https://opencv.org/) para capturar o feed da webcam.
- [NumPy](https://numpy.org/) para lidar com operações matemáticas.

Execute o seguinte comando para instalar as dependências:

```bash
pip install opencv-python numpy
```

### Rodando o Projeto

1. Clone o repositório.
2. No terminal, navegue até o diretório do arquivo.
3. Execute o script com o seguinte comando:

```bash
python demo.py
```

### Controles do Teclado

- **W**: Aumenta a velocidade de rotação.
- **S**: Diminui a velocidade de rotação.
- **A**: Aumenta o cisalhamento horizontal.
- **D**: Diminui o cisalhamento horizontal.
- **Q**: Fecha a aplicação.

## Estrutura do Código

O código é estruturado em três partes principais:

1. **Transformações geométricas**: Funções responsáveis por calcular as matrizes de rotação e cisalhamento.
2. **Aplicação das transformações**: Aplica as transformações em cada frame da câmera.
3. **Loop principal**: Onde o vídeo é capturado e as transformações são exibidas em tempo real. Aqui, também lidamos com os controles do usuário.

## Autor

Desenvolvido por [João Delomo](https://github.com/JoaoDelomo) e [Mateus Porto](https://github.com/Mateus1711-ctrl)

---

