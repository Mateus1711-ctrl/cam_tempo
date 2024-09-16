import cv2
import numpy as np

def get_rotation_matrix(theta, center):
    cx, cy = center
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    
    T1 = np.array([[1, 0, -cx],
                   [0, 1, -cy],
                   [0, 0, 1]])
    
    R = np.array([[cos_theta, -sin_theta, 0],
                  [sin_theta, cos_theta, 0],
                  [0, 0, 1]])
    
    T2 = np.array([[1, 0, cx],
                   [0, 1, cy],
                   [0, 0, 1]])
    
    return T2 @ R @ T1

def get_shear_matrix(shear_factor, rows):
    S = np.array([[1, shear_factor, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    return S

def apply_transformation(frame, M):
    rows, cols = frame.shape[:2]
    
    Xd, Yd = np.meshgrid(np.arange(cols), np.arange(rows))
    ones = np.ones_like(Xd)
    
    destination_pixels = np.vstack([Xd.ravel(), Yd.ravel(), ones.ravel()])
    
    origin_pixels = np.linalg.inv(M) @ destination_pixels
    origin_pixels = origin_pixels[:2] / origin_pixels[2]
    
    x_o = np.clip(origin_pixels[0], 0, cols - 1).astype(np.float32)
    y_o = np.clip(origin_pixels[1], 0, rows - 1).astype(np.float32)
    
    map_x = x_o.reshape((rows, cols))
    map_y = y_o.reshape((rows, cols))
    
    transformed_frame = cv2.remap(frame, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    
    return transformed_frame

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        return
    
    angle = 0
    angular_speed = 45
    shear_factor = 0
    
    fps = 30
    delay = int(1000 / fps)
    
    # Ajuste a resolução para melhorar a fluidez
    target_width = 640
    target_height = 480
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.resize(frame, (target_width, target_height))
        rows, cols = frame.shape[:2]
        center = (cols / 2, rows / 2)
        
        angle_rad = np.deg2rad(angle)
        M_rotation = get_rotation_matrix(angle_rad, center)
        
        M_shear = get_shear_matrix(shear_factor, rows)
        
        M_combined = M_shear @ M_rotation
        
        transformed_frame = apply_transformation(frame, M_combined)
        
        cv2.imshow('Rotating and Shearing Video', transformed_frame)
        
        angle += angular_speed / fps
        if angle >= 360:
            angle -= 360
        
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('w'):
            angular_speed += 5
        elif key == ord('s'):
            angular_speed = max(0, angular_speed - 5)
        elif key == ord('a'):
            shear_factor += 0.01
        elif key == ord('d'):
            shear_factor = max(-1, shear_factor - 0.01)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
