import cv2
import os

# Caminho para o diretório do banco de dados de faces
database_path = "\orl_faces"

# Função para carregar imagens do banco de dados
def carregar_imagens(caminho):
    imagens = []
    labels = []
    
    # Percorrer todas as pastas do banco de dados
    for pasta in os.listdir(caminho):
        pasta_path = os.path.join(caminho, pasta)
        
        # Verificar se é um diretório
        if os.path.isdir(pasta_path):
            # Percorrer todas as imagens da pasta
            for imagem_nome in os.listdir(pasta_path):
                imagem_path = os.path.join(pasta_path, imagem_nome)
                
                # Carregar a imagem como escala de cinza
                imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
                
                if imagem is not None:
                    # Adicionar a imagem e o rótulo correspondente às listas
                    imagens.append(imagem)
                    labels.append(pasta)  # Usando o nome da pasta como rótulo
    
    return imagens, labels

# Carregar imagens do banco de dados de faces
imagens, labels = carregar_imagens(database_path)

# Exemplo de uso das imagens carregadas
print("Total de imagens:", len(imagens))
print("Total de rótulos:", len(labels))
print("Exemplo de imagem:", imagens[0].shape)
print("Exemplo de rótulo:", labels[0])
