import numpy as np
import cv2 as cv

def calcular_matriz_rotacao(angulo, cx, cy):
    theta = np.radians(angulo)
    cos_val = np.cos(theta)
    sin_val = np.sin(theta)

    matriz_translacao1 = np.array([[1, 0, -cx], [0, 1, -cy], [0, 0, 1]])
    matriz_rotacao = np.array([[cos_val, -sin_val, 0], [sin_val, cos_val, 0], [0, 0, 1]])
    matriz_translacao2 = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]])

    matriz_composta = matriz_translacao2 @ matriz_rotacao @ matriz_translacao1
    return matriz_composta

def aplicar_rotacao(image, angulo):
    h, w = image.shape[:2]
    cx, cy = w // 2, h // 2

    matriz_rotacao = calcular_matriz_rotacao(angulo, cx, cy)
    matriz_rotacao_inv = np.linalg.inv(matriz_rotacao)

    imagem_rotacionada = np.zeros_like(image)

    for y in range(h):
        for x in range(w):
            coords_destino = np.array([x, y, 1])
            coords_origem = matriz_rotacao_inv @ coords_destino
            x_origem, y_origem = int(coords_origem[0]), int(coords_origem[1])

            if 0 <= x_origem < w and 0 <= y_origem < h:
                imagem_rotacionada[y, x] = image[y_origem, x_origem]

    return imagem_rotacionada

def run():
    cap = cv.VideoCapture(0)
    width = 320
    height = 240

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    angulo = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        image = np.array(frame).astype(float) / 255

        angulo = (angulo + 1) % 360
        image_rotacionada = aplicar_rotacao(image, angulo)

        cv.imshow('Rotação de Vídeo em Tempo Real', image_rotacionada)
        
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

run()
