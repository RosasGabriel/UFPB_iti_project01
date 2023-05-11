import main
import time



def Teste(k, filename):
    max_dict_size = 2**k  # Tamanho máximo do dicionário
    data = open(filename, 'rb').read()

    compressed_data, dictSizeCompressao = main.compressor_lzw(data, max_dict_size)

    compressed_filename = 'exemplo_comprimido_' + filename
    with open(compressed_filename, 'wb') as f:
        f.write(compressed_data)

    data2 = open(compressed_filename, 'rb').read()
    decompressed_data, dict_sizeD = main.descompressor_lzw(data2, max_dict_size)
    decompressed_filename = 'exemplo_descomprimido_' + filename
    with open(decompressed_filename, 'wb') as f:
        f.write(decompressed_data)


    print(f'Tamanho máximo do dicionário: {max_dict_size}, tamanho dicionário compressão:{dictSizeCompressao}, taxa de compressão: {len(data)/len(compressed_data):.2f}')


filename = 'disco.mp4'
for k in range(9, 17):
    start_time = time.time()
    Teste(k, filename)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("Para k = ", k , "Tempo: ", execution_time, "segundos")