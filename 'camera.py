import cv2
import numpy as np

def rotacionar_imagem(imagem, angulo):
    (h, w) = imagem.shape[:2]
    centro = (w // 2, h // 2)

    theta = np.radians(angulo)
    cos_val = np.cos(theta)
    sin_val = np.sin(theta)

    matriz_rotacao = np.array([
        [cos_val, -sin_val, (1 - cos_val) * centro[0] - sin_val * centro[1]],
        [sin_val, cos_val, (1 - cos_val) * centro[1] + sin_val * centro[0]]
    ])

    imagem_rotacionada = np.zeros_like(imagem)

    for y in range(h):
        for x in range(w):
            coords_destino = np.array([x, y, 1])
            coords_origem = np.dot(np.linalg.inv(matriz_rotacao), coords_destino)
            src_x, src_y = int(coords_origem[0]), int(coords_origem[1])

            if 0 <= src_x < w and 0 <= src_y < h:
                imagem_rotacionada[y, x] = imagem[src_y, src_x]

    return imagem_rotacionada

def main():
    cap = cv2.VideoCapture(0)
    angulo = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        angulo = (angulo + 1) % 360
        frame_rotacionado = rotacionar_imagem(frame, angulo)
        cv2.imshow('Rotação de Vídeo em Tempo Real', frame_rotacionado)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
