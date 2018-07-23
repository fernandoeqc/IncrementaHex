# IncrementaHex
Incrementa a primeira linha da EEPROM em hexadecimais para Microcontroladores Pic. Pode ser utilizado para criar um número de série para pics.
1 - pega o arquivo hexadecimal original,(pode ser  retirado importando o arquivo hex no pickit e exportando como hex em outro arquivo hex)
copiar a parte inicial do código,que vai até  o inicio do código da EEPROM. cola no arquivo 'inicio'.
2 - Copia a linha  a partir da primeira linha do código da EEPROM. cola em arquivo 'fim'.
3 - o arquivo 'app' é o arquivo de saída.
4 - o arquivo 'codigo' tem o codigo hexadecimal que vai ser gravado e incrementado. Por padrão ele começa com 0x01, 0x01.
