import struct

def compressor_lzw(data, max_dict_size):
    dicionario = {bytes([i]): i for i in range(256)} #Cria um dicionário representado por bytes
    dict_size = 256 #Define o tamanho base do dicionário
    resultado = bytearray() #Cria um array de bytes para armazenar o resultado
    buffer = b'' #indica que o buffer armazenará bytes
    i = 0
    while i < len(data):
        symbol = bytes([data[i]])
        if buffer + symbol in dicionario:
            buffer += symbol
        else:
            code = dicionario[buffer]
            resultado += struct.pack('<H', code)
            if dict_size < max_dict_size:
                dicionario[buffer + symbol] = dict_size
                dict_size += 1
                
            buffer = symbol
        i += 1
    code = dicionario[buffer]
    resultado += struct.pack('<H', code)
    return resultado, dict_size

def descompressor_lzw(data, max_dict_size):
    dicionario = {i: bytes([i]) for i in range(256)}
    dict_size = 256
    resultado = bytearray()
    buffer = b'' #buffer em binario
    i = 0
    while i < len(data):
        code = struct.unpack('<H', data[i:i+2])[0]
        i += 2
        if code in dicionario:
            entry = dicionario[code]
        elif code == dict_size:
            entry = buffer + buffer[0:1]
        else:
            raise ValueError('Invalid code')
        resultado += entry
        if buffer:
            if dict_size < max_dict_size:
                dicionario[dict_size] = buffer + entry[0:1]
                dict_size += 1
                
            buffer = entry
        else:
            buffer = entry
    return resultado, dict_size

filename = 'corpus16MB.txt'

k=16 
max_dict_size = 2**k  # Tamanho máximo do dicionário
data = open(filename, 'rb').read()

compressed_data, dict_sizeC = compressor_lzw(data, max_dict_size)


compressed_filename = 'exemplo_comprimido_' + filename
with open(compressed_filename, 'wb') as f:
    f.write(compressed_data)

data2 = open(compressed_filename, 'rb').read()
decompressed_data, dict_sizeD = descompressor_lzw(data2, max_dict_size)
decompressed_filename = 'exemplo_descomprimido_' + filename
with open(decompressed_filename, 'wb') as f:
    f.write(decompressed_data)


print(f'Tamanho máximo do dicionário: {max_dict_size}, dicionário compressão:{dict_sizeC}, dicionário descompressão:{dict_sizeD} taxa de compressão: {len(compressed_data)/len(data):.2f}')
