import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import cv2

class MinhaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Criar widgets
        self.buttonAbrir = QPushButton('Abrir imagem')
        self.buttonAbrir.setFixedSize(100, 50)
        
        # Criar layout
        layout = QVBoxLayout()
        layout.addWidget(self.buttonAbrir)
        self.buttonAbrir.clicked.connect(self.abrirDialog)

        self.label = QLabel()
        layout.addWidget(self.label)
        
        self.buttonBlurMedio = QPushButton("Aplicar Suavização Média")
        self.buttonBlurMedio.setFixedSize(300, 50)
        self.buttonBlurMedio.clicked.connect(self.suavizacaoMedia)
        
        self.buttonBlurGaussiano = QPushButton("Aplicar Suavização Gaussiana")
        self.buttonBlurGaussiano.setFixedSize(300, 50)
        self.buttonBlurGaussiano.clicked.connect(self.suavizacaoGaussiana)
        
        self.buttonBlurMediana = QPushButton("Aplicar Suavização Mediana")
        self.buttonBlurMediana.setFixedSize(300, 50)
        self.buttonBlurMediana.clicked.connect(self.suavizacaoMediana)
        
        layout.addWidget(self.buttonBlurMedio) 
        layout.addWidget(self.buttonBlurGaussiano)
        layout.addWidget(self.buttonBlurMediana)
        
        self.setLayout(layout)

        # Configurar janela principal
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle('Processamento de Imagens do Caio')
        
        self.show()

    def abrirDialog(self):
        # Ao clicar no botão de abrir imagem, esse método sera invocado
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Selecionar Imagem', '', 'Imagens (*.png *.jpg *.bmp *.gif)')

        if self.fname:
            pixmap = QPixmap(self.fname)
            
            tamanho_tela_minimizada = self.label.size()

            pixmap_redimensionado = pixmap.scaled(tamanho_tela_minimizada, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
            self.label.setPixmap(pixmap_redimensionado)
    
    def suavizacaoMedia(self) :
        imagem = cv2.imread(self.fname)
        # Define o tamanho do kernel
        kernel_size = (25, 25)

        # Aplica a suavização por média
        imagem_suavizada = cv2.blur(imagem, kernel_size)

        cv2.imshow('Original', imagem)
        cv2.imshow('Suavizada por Média', imagem_suavizada)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def suavizacaoGaussiana(self):
        imagem = cv2.imread(self.fname)
        # Define o tamanho do kernel
        kernel_size = (25, 25)
        sigmaX = 0

        # Aplica a suavização por média
        imagem_suavizada = cv2.GaussianBlur(imagem, kernel_size, sigmaX)

        cv2.imshow('Original', imagem)
        cv2.imshow('Suavização Gaussiana', imagem_suavizada)  
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def suavizacaoMediana(self):
        imagem = cv2.imread(self.fname)
        # Define o tamanho do kernel
        kernel_size = 25
        # Aplica a suavização por média
        imagem_suavizada = cv2.medianBlur(imagem, kernel_size)

        cv2.imshow('Original', imagem)
        cv2.imshow('Suavização por Mediana', imagem_suavizada)  
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    minha_app = MinhaApp()
    sys.exit(app.exec_())
