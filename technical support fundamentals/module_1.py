"""
///FIRST ATTEMPT
Question 1:
Which of the following roles are typically considered part of IT?
X Business analyst
✅ Network engineer
✅ Desktop support personnel
✅ Hardware technician

(All are part of IT roles.)

Question 2:
Fill in the blank: A(n) ____ is a device that stores and processes data by performing calculations.
✅ computer

Question 3:
Which of these devices can be used to control electricity voltages in computers?
✅ Transistors
X Computer chips
✅ Vacuum tubes
❌ CD-Roms

Question 4:
Fill in the blank: There are ___ bits in a byte.
✅ 8

Question 5:
Fill in the blank: ____ is the oldest character encoding standard and it uses 127 of the 256 possible bytes.
✅ ASCII

Question 6:
Fill in the blank: In a binary system, an electrical signal indicates a value of ___.
✅ 1

Question 7:
Convert decimal 123 to binary:
✅ 01111011
(128: 0, 64: 1, 32: 1, 16: 1, 8: 1, 4: 0, 2: 1, 1: 1)

Question 8:
Convert binary 00100001 to decimal:
✅ 33
(32 + 1 = 33)

Question 9:
Convert binary 10001001 to decimal:
✅ 137
(128 + 8 + 1 = 137)

Question 10:
Which of these things were designed to facilitate abstraction?
✅ A car steering wheel
X Logic gates
✅ An error message from your computer’s browser
❌ A textbook

(A textbook explains abstraction, but isn’t a system abstraction itself.)

"""

def binario_a_decimal(binario):
  """Convierte un byte binario (string de 8 bits) a su valor decimal.

  Args:
    binario: Un string de 8 caracteres representando un byte binario.

  Returns:
    Un entero representando el valor decimal del byte.
    Retorna -1 si la entrada no es un string de 8 bits.
  """
  if not isinstance(binario, str) or len(binario) != 8 or not all(bit in '01' for bit in binario):
    return -1
  decimal = 0
  potencia = 0
  for bit in reversed(binario):
    if bit == '1':
      decimal += 2**potencia
    potencia += 1
  return decimal

def decimal_a_binario(decimal):
  """Convierte un valor decimal (entero entre 0 y 255) a su representación binaria de 8 bits.

  Args:
    decimal: Un entero entre 0 y 255.

  Returns:
    Un string de 8 caracteres representando el byte binario.
    Retorna None si el valor decimal está fuera del rango.
  """
  if not isinstance(decimal, int) or decimal < 0 or decimal > 255:
    return None
  binario = bin(decimal)[2:]  # Convertir a binario y remover el prefijo "0b"
  return binario.zfill(8)   # Rellenar con ceros a la izquierda para asegurar 8 bits

# Código para la pregunta 7 (convertir decimal 142 a binario)
decimal_7 = 142
binario_7 = decimal_a_binario(decimal_7)
print(f"Pregunta 7: El valor decimal {decimal_7} en binario es: {binario_7}")

# Código para la pregunta 8 (convertir binario 00100001 a decimal)
binario_8 = "00100001"
decimal_8 = binario_a_decimal(binario_8)
print(f"Pregunta 8: El byte binario {binario_8} en decimal es: {decimal_8}")

# Código para la pregunta 9 (convertir binario 00011001 a decimal)
binario_9 = "00011001"
decimal_9 = binario_a_decimal(binario_9)
print(f"Pregunta 9: El byte binario {binario_9} en decimal es: {decimal_9}")

"""
////SECOND ATTEMPT
Information technology is the use of digital technology like computers and the internet to store and process data into useful information.

Algorithms can be programmed into computers.

Vacuum tubes and Transistors can be used to control electricity voltages in computers.

One byte can encode  
256
​
  unique values.

ASCII
​
  is the oldest character encoding standard and it uses 127 of the 256 possible bytes.

The current method used to communicate in binary is Electrical signals that flow through transistors.

To convert the decimal value 142 into binary format:

128 goes into 142 once (142 - 128 = 14) -> 1st bit: On
64 does not go into 14 -> 2nd bit: Off
32 does not go into 14 -> 3rd bit: Off
16 does not go into 14 -> 4th bit: Off
8 goes into 14 once (14 - 8 = 6) -> 5th bit: On
4 goes into 6 once (6 - 4 = 2) -> 6th bit: On
2 goes into 2 once (2 - 2 = 0) -> 7th bit: On
1 does not go into 0 -> 8th bit: Off
Therefore, the binary representation of 142 is 10001110.

To convert the byte 00100001 into a decimal value:

1st bit (128): Off (0 * 128 = 0)
2nd bit (64): Off (0 * 64 = 0)
3rd bit (32): On (1 * 32 = 32)
4th bit (16): Off (0 * 16 = 0)
5th bit (8): Off (0 * 8 = 0)
6th bit (4): Off (0 * 4 = 0)
7th bit (2): Off (0 * 2 = 0)
8th bit (1): On (1 * 1 = 1)
The decimal value is 0 + 0 + 32 + 0 + 0 + 0 + 0 + 1 =  
33
​
 .

To convert the byte 00011001 into a decimal value:

1st bit (128): Off (0 * 128 = 0)
2nd bit (64): Off (0 * 64 = 0)
3rd bit (32): Off (0 * 32 = 0)
4th bit (16): On (1 * 16 = 16)
5th bit (8): On (1 * 8 = 8)
6th bit (4): Off (0 * 4 = 0)
7th bit (2): Off (0 * 2 = 0)
8th bit (1): On (1 * 1 = 1)
The decimal value is 0 + 0 + 0 + 16 + 8 + 0 + 0 + 1 =  
25
​
 .

Abstraction takes a relatively complex system and breaks it apart into simpler ideas to make it easier to think about.
""""
