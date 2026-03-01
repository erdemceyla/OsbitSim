import numpy as np

# Evrensel kütleçekim sabiti (Simülasyon ölçeği için ayarlanmıştır)
G = 100 

def calculate_gravitational_force(body1, body2):
    """İki cisim arasındaki çekim kuvvetini hesaplar."""
    # Mesafe vektörü ve skaler uzaklık
    r_vec = body2.pos - body1.pos
    distance = np.linalg.norm(r_vec)
    
    # Çok yakınlaşınca (çarpışma anı) kuvvetin sonsuza gitmesini önlemek için bir sınır
    if distance < 5:
        return np.zeros(2)
    
    # Kuvvetin büyüklüğü: F = G * (m1*m2) / r^2
    force_magnitude = G * (body1.mass * body2.mass) / (distance**2)
    
    # Kuvvetin yönü (birim vektör)
    force_direction = r_vec / distance
    
    return force_magnitude * force_direction

def update_physics(bodies, dt):
    """Tüm cisimlerin birbirine uyguladığı kuvvetleri hesaplayıp ivmeleri günceller."""
    for body in bodies:
        total_force = np.zeros(2)
        for other_body in bodies:
            if body is other_body:
                continue
            force = calculate_gravitational_force(body, other_body)
            total_force += force
        
        # Newton'un 2. Yasası: a = F / m
        body.acc = total_force / body.mass
        
    # Tüm kuvvetler hesaplandıktan sonra konumları güncelle
    for body in bodies:
        body.update_position(dt)