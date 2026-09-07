import numpy as np

# 1. Zaman vektörü oluşturma (0'dan 60. saniyeye 1'er saniye aralıkla)
zaman = np.arange(0, 61, 1)

# 2. Tank sıcaklığının zamana bağlı düşüşünü tek satırda modelleme
T_baslangic = 75.0  # °C
soguma_katsayisi = 0.05

# Tüm saniyeler için sıcaklık dizisini anında hesaplar:
sicakliklar = T_baslangic * np.exp(-soguma_katsayisi * zaman)

print(f"5. saniyedeki sıcaklık: {sicakliklar[5]:.2f}°C")
print(f"60. saniyedeki sıcaklık: {sicakliklar[-1]:.2f}°C")