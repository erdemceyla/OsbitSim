import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from celestial_body import Body
from physics_engine import update_physics

# Global değişkenler
time_scale = 1.0

def run_ultimate_solar_system():
    global time_scale
    
    # 1. GÜNEŞ VE GEZEGENLERİN TANIMLANMASI
    sun = Body("Güneş", 15000, [0, 0], [0, 0], "gold")
    
    # Dünya ve Ay (Hiyerarşik Kütleçekimi)
    earth = Body("Dünya", 12, [160, 0], [0, 100], "royalblue")
    moon  = Body("Ay", 0.6, [168, 0], [0, 138], "lightgray")
    
    # Satürn ve Halkaları (Buz parçacıkları simülasyonu)
    saturn = Body("Satürn", 35, [430, 0], [0, 60], "khaki")
    bodies = [sun, earth, moon, saturn]
    
    # Satürn Halkası Parçacıkları ekleme
    for i in range(10): # Performans için 60 adet idealdir
        angle = random.uniform(0, 2 * np.pi)
        dist = random.uniform(45, 65)
        px = 430 + dist * np.cos(angle)
        py = dist * np.sin(angle)
        v_orbit = 25 
        vx = -v_orbit * np.sin(angle)
        vy = 60 + v_orbit * np.cos(angle)
        bodies.append(Body(f"Ring-{i}", 0.01, [px, py], [vx, vy], "gray"))

    # Diğer Gezegenlerin Eklenmesi
    bodies.extend([
        Body("Merkür", 5, [60, 0], [0, 160], "gray"),
        Body("Venüs", 10, [110, 0], [0, 120], "orange"),
        Body("Mars", 8, [210, 0], [0, 85], "red"),
        Body("Jüpiter", 45, [320, 0], [0, 70], "tan"),
        Body("Uranüs", 20, [550, 0], [0, 52], "lightblue"),
        Body("Neptün", 18, [660, 0], [0, 46], "blue")
    ])

    # --- TAM EKRAN VE MERKEZLEME AYARLARI ---
    fig = plt.figure(facecolor='#000000')
    # add_axes([0,0,1,1]) grafiği pencerenin her köşesine yayar
    ax = fig.add_axes([0, 0, 1, 1])
    
    # Pencereyi otomatik büyüt (Maximize)
    mng = plt.get_current_fig_manager()
    try: mng.window.state('zoomed')
    except: pass

    # Koordinat sınırlarını eşitleyerek Güneş'i merkeze çivile
    limit = 800
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect('equal') # SAĞA KAYMAYI ÖNLEYEN KRİTİK AYAR
    ax.axis('off')

    # Görsel nesneler
    plots = {b: ax.plot([], [], 'o', color=b.color, 
               markersize=14 if b.name=="Güneş" else (8 if b.mass > 30 else 4))[0] 
             for b in bodies}
    
    # Sadece ana gezegenler için yörünge izi (Halkalar için çizmiyoruz - Performans)
    trails = {b: ax.plot([], [], '-', color=b.color, alpha=0.15, linewidth=0.7)[0] 
              for b in bodies if "Ring" not in b.name}

    # --- ETKİLEŞİM VE ZAMAN KONTROLÜ ---
    def on_key(event):
        global time_scale
        if event.key == 'up': time_scale *= 1.2    # Yukarı Ok: Hızlandır
        elif event.key == 'down': time_scale /= 1.2 # Aşağı Ok: Yavaşlat
        elif event.key == 'r': time_scale = 1.0     # R Tuşu: Reset
        print(f"⏱️ Zaman Akış Hızı: {time_scale:.2f}x")

    def on_click(event):
        if event.xdata is None: return
        ast = Body("Ast", 2, [event.xdata, event.ydata], 
                   [random.uniform(-40, 40), random.uniform(-40, 40)], "white")
        bodies.append(ast)
        plots[ast] = ax.plot([], [], 'o', color="white", markersize=2)[0]

    fig.canvas.mpl_connect('key_press_event', on_key)
    fig.canvas.mpl_connect('button_press_event', on_click)

    # --- ANİMASYON DÖNGÜSÜ ---
    def animate(frame):
        global time_scale
        dt_base = 0.05 
        
        # 1. OPTİMİZASYON: Fiziği güncelle
        update_physics(bodies, dt=dt_base * time_scale)
        
        updated_plots = []
        for b in bodies[:]:
            # Güneş'e çarpanları temizle
            if b.name != "Güneş" and np.linalg.norm(b.pos) < 25:
                if b in plots:
                    plots[b].remove()
                    del plots[b]
                if b in trails:
                    trails[b].remove()
                    del trails[b]
                bodies.remove(b)
                continue

            # 2. OPTİMİZASYON: Konumu güncelle
            plots[b].set_data([b.pos[0]], [b.pos[1]])
            updated_plots.append(plots[b])
            
            # 3. KRİTİK OPTİMİZASYON: Yörünge izi yönetimi
            # Sadece ana gezegenler için ve her 3 karede bir çizim yap (Donmayı önler)
            if b in trails and frame % 3 == 0:
                # Bellek yönetimi: Sadece son 50 konumu tut (Daha fazlası donma yapar)
                if len(b.path) > 50:
                    b.path = b.path[-50:]
                
                path_x, path_y = zip(*b.path)
                trails[b].set_data(path_x, path_y)
                updated_plots.append(trails[b])
        
        return updated_plots

    # 4. BLIT AYARI: blit=True performansı artırır ancak bazı sistemlerde 
    # donmaya sebep olabilir. Eğer yine donarsa blit=False yap.
    ani = FuncAnimation(fig, animate, interval=10, blit=True, cache_frame_data=False)
    plt.show()

if __name__ == "__main__":
    run_ultimate_solar_system()