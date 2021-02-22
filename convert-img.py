from PIL import Image

# Carrega Imagem #
image_file = Image.open(r".\colorida.png")

# Converte Imagem para preto e branco #
image_file = image_file.convert('L')

# Salva imagem em preto e branco #
image_file.save(r".\preta-e-branca.png")