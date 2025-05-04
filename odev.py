import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# Resim boyutu
size = 512

# Koordinat gridi oluşturma
x = np.linspace(-5, 5, size)
y = np.linspace(-5, 5, size)
X, Y = np.meshgrid(x, y)

# Matematiksel formüllerle RGB kanalları oluşturma
R = np.sin(X**2 + Y**2) * np.cos(X)
G = np.cos(X) * np.sin(Y) * (X**2 - Y**2)
B = np.tanh(X*Y) * np.sin(X+Y)

# Değerleri 0-1 aralığına normalize etme
R = (R - R.min()) / (R.max() - R.min())
G = (G - G.min()) / (G.max() - G.min())
B = (B - B.min()) / (B.max() - B.min())

# RGB resmi oluşturma
rgb_image = np.dstack((R, G, B))

# Resmi gösterme
plt.figure(figsize=(10, 10))
plt.imshow(rgb_image)
plt.axis('off')
plt.title('Matematiksel RGB Desen')
plt.show()

# Matematiksel fonksiyonları ayrı ayrı görselleştirme
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Kırmızı kanal fonksiyonu
axes[0].imshow(R, cmap='Reds')
axes[0].set_title('Kırmızı Kanal: sin(x²+y²)*cos(x)')
axes[0].axis('off')

# Yeşil kanal fonksiyonu
axes[1].imshow(G, cmap='Greens')
axes[1].set_title('Yeşil Kanal: cos(x)*sin(y)*(x²-y²)')
axes[1].axis('off')

# Mavi kanal fonksiyonu
axes[2].imshow(B, cmap='Blues')
axes[2].set_title('Mavi Kanal: tanh(x*y)*sin(x+y)')
axes[2].axis('off')

plt.tight_layout()
plt.show()

# 3D yüzey grafikleri
fig = plt.figure(figsize=(15, 5))

# Kırmızı kanal 3D
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, R, cmap='Reds')
ax1.set_title('Kırmızı Kanal 3D')

# Yeşil kanal 3D
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, G, cmap='Greens')
ax2.set_title('Yeşil Kanal 3D')

# Mavi kanal 3D
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, B, cmap='Blues')
ax3.set_title('Mavi Kanal 3D')

plt.tight_layout()
plt.show()