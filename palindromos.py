def es_palindromo(texto):
  
  texto_procesado = texto.lower().replace(" ", "")

  for i in range(len(texto_procesado) // 2):
    if texto_procesado[i] != texto_procesado[-i-1]:
      return False

  return True

#Ejemplo de uso
texto = "Anita lava la tina"
resultado = es_palindromo(texto)

if resultado:
  print(f"El texto '{texto}' es un palíndromo.")
else:
  print(f"El texto '{texto}' no es un palíndromo.")
