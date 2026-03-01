import numpy as np

class Body:
    def __init__(self, name, mass, pos, vel, color):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype=float)  # [x, y] konumu
        self.vel = np.array(vel, dtype=float)  # [vx, vy] hızı
        self.acc = np.zeros(2, dtype=float)    # İvme
        self.color = color
        self.path = [] # Yörünge izi için geçmiş konumlar

    def update_position(self, dt):
        """Hız ve ivmeyi kullanarak konumu günceller."""
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        self.path.append(self.pos.copy())
        # Yörünge izini sınırlı tutalım (hafıza yönetimi)
        if len(self.path) > 200:
            self.path.pop(0)