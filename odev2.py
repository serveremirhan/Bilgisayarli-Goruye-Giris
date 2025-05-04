import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from PIL import Image
import random
import io

class JigsawPuzzleCreator:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 6))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Lütfen bir resim yükleyin', fontsize=12)
        self.ax.axis('off')
        
        # Yükleme butonu
        self.ax_button = plt.axes([0.35, 0.05, 0.3, 0.075])
        self.button = Button(self.ax_button, 'Resim Yükle')
        self.button.on_clicked(self.upload_image)
        
        self.uploaded_image = None
        plt.tight_layout()
        plt.show()
    
    def upload_image(self, event):
        # Kullanıcıdan dosya seçmesini iste
        from tkinter import Tk, filedialog
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Resim seçin",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        
        if file_path:
            try:
                # Resmi yükle ve göster
                img = Image.open(file_path)
                self.uploaded_image = np.array(img)
                
                # Orijinal resmi göster
                self.show_original_image()
                
                # Jigsaw oluştur
                self.create_jigsaw_puzzles()
                
            except Exception as e:
                print(f"Hata: {e}")
    
    def show_original_image(self):
        plt.figure(figsize=(6, 6))
        plt.imshow(self.uploaded_image)
        plt.title('Yüklenen Orijinal Resim', fontsize=12)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def create_jigsaw_puzzles(self):
        if self.uploaded_image is None:
            return
        
        rows, cols = 3, 3  # 3x3 puzzle
        
        # 4 farklı jigsaw oluştur
        plt.figure(figsize=(12, 10))
        for i in range(4):
            puzzle = self.make_jigsaw(self.uploaded_image, rows, cols)
            plt.subplot(2, 2, i+1)
            plt.imshow(puzzle)
            plt.title(f'Jigsaw Bulmaca {i+1}', fontsize=10)
            plt.axis('off')
        
        plt.tight_layout()
        plt.suptitle('Oluşturulan Jigsaw Bulmacaları', y=1.02, fontsize=14)
        plt.show()
        
        # Parçaları göster
        self.show_puzzle_pieces(rows, cols)
    
    def make_jigsaw(self, image, rows, cols):
        h, w = image.shape[0], image.shape[1]
        tile_h, tile_w = h // rows, w // cols
        
        tiles = []
        for i in range(rows):
            for j in range(cols):
                tile = image[i*tile_h:(i+1)*tile_h, j*tile_w:(j+1)*tile_w]
                tiles.append(tile)
        
        random.shuffle(tiles)
        
        # Parçaları birleştir
        puzzle = np.zeros_like(image)
        for idx, tile in enumerate(tiles):
            i = idx // cols
            j = idx % cols
            puzzle[i*tile_h:(i+1)*tile_h, j*tile_w:(j+1)*tile_w] = tile
        
        return puzzle
    
    def show_puzzle_pieces(self, rows, cols):
        h, w = self.uploaded_image.shape[0], self.uploaded_image.shape[1]
        tile_h, tile_w = h // rows, w // cols
        
        plt.figure(figsize=(8, 8))
        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j + 1
                tile = self.uploaded_image[i*tile_h:(i+1)*tile_h, j*tile_w:(j+1)*tile_w]
                plt.subplot(rows, cols, idx)
                plt.imshow(tile)
                plt.axis('off')
                plt.title(f'Parça {idx}', fontsize=8)
        
        plt.tight_layout()
        plt.suptitle('Orijinal Resmin Parçaları', y=1.02, fontsize=12)
        plt.show()

# Uygulamayı başlat
if __name__ == "__main__":
    puzzle_creator = JigsawPuzzleCreator()