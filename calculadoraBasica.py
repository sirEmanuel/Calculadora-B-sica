def soma(a, b):
  a = numero
  b = numero2
  c = a + b
  return round(c, 2)

def subtracao(a, b):
  a = numero
  b = numero2
  c = a - b
  return round(c, 2)

def multiplicacao(a, b):
  a = numero
  b = numero2
  c = a * b
  return round(c, 2)

def divisao(a, b):
  a = numero
  b = numero2
  c = a / b
  return round(c, 2)

def formatacao(a, b, c):
  print(" ")
  print(f"{a} {c} {b}")


operadores = ["+", "-", "x", "/" ]


#STATUS - (OFF) - DESLIGADA
operando = input("LIGAR CALCULADOR: (C)  ").upper()
print( 35 * "-=")
while operando == "C":
  ligar = input("\nINICIAR CALCULADORA (L) | STAND BY (ENTER):   ").upper()
  if ligar  != "L":
    print("\nDESLIGADA!")
    break
  while ligar == "L":
    operacao = input("\nNOVO CALCULO (S/N) - DESLIGAR CALCULADORA (ENTER)  ").upper()
    if operacao == "":
      print("\nCALCULADORA DESLIGADA!\n")
      break
    else:
      print("\n" + 35 * "-=")
      numero = float(input("\nPRIMEIRO NÚMERO:  "))
      numero2 = float(input("SEGUNDO NÚMERO:  "))
      operador = input("OPERADOR MATEMÁTICO: (use: ( + - x  / ))  ").lower()
      print("\n" + 35 * "-=")

# -- COMEÇANDO O CALCULO SOMANDO:
      while operador in operadores:
          if operador == "+":
              resultado = round(soma(numero, numero2), 2)
              formatacao(numero, numero2, operador)
              print(f" = {resultado:.2f}\n")
              continuar = input("DESEJA FAZER UMA NOVA OPERAÇÃO? (S/N)  ").upper()
              print("\n" + 35 * "-=")
              if continuar == "N":
                  break
              else:
                # -- OPTANDO POR NÃO LIMPAR | DESLIGAR, O USUÁRIO TEM DUAS NOVAS OPÇÕES
                novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                while novaOp != "E" or novaOp == " ":
                    print("\n" + 35 *"-=")
                    novoNumero = float(input("\nNOVO NUMERO:  "))
                    operador = input("OPERADOR MATEMÁTICO: (use: ( + - x  / ))  ").lower()
                    # -- CONTINUE SOMANDO
                    while operador == "+":
                        formatacao(resultado, novoNumero, operador)
                        resultadoSoma = round((resultado + novoNumero), 2)
                        print(f" = {resultadoSoma:.2f}")
                        novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                        resultado = resultadoSoma
                        break
                    # -- SUBTRAIR A PARTIR DO RESULTADO ANTERIOR
                    if operador == "-":
                      print("\n" + 35 * "-=")
                      resultadoSub = resultado - novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoSub:.2f}")
                      #limparTela = input("\nDESEJA LIMPAR TELA (C):  ").upper()
                      print("\n" + 35 * "-=")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      resultado = resultadoSub
                      continue
                      # -- MULTIPLICAR A PARTIR DO RESULTADO ANTERIOR
                    elif operador == "x":
                      print("\n" + 35 * "-=")
                      resultadoMult = round((resultado * novoNumero),2)
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoMult:.2f}")
                      #limparTela = input("\nDESEJA LIMPAR TELA (C):  ").upper()
                      print("\n" + 35 * "-=")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      resultado = resultadoMult
                      continue
                    # -- DIVIDIR A PARTIR DO RESULTADO ANTERIOR
                    elif operador == "/":
                      print("\n" + 35 * "-=")
                      resultadoDiv = round((resultado / novoNumero), 2)
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoDiv:.2f}")
                      #limparTela = input("\nDESEJA LIMPAR TELA (C):  ").upper()
                      print("\n" + 35 * "-=")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      resultado = resultadoDiv
                      continue
                if novaOp == "E":
                  print("\n" + 35 * "-=")
                  operacao = input("\nLIMPAR TELA (L) | DESLIGAR CALCULADORA (ENTER):  ").upper()
                  if operacao == "L":
                        for c in range(0, 10):
                          c -+ 1
                          print("0")
                        print("AGUARDANDO VALORES!")
                        print(35 * "-=")
                        break
                  else:
                    #print("\n DESEJA DESLIGAR A CALCULADORA (ENTER)")
                    break

# -- 1º CALCULO SUBTRAÇÃO:

          elif operador == "-":
              resultado = subtracao(numero, numero2)
              formatacao(numero, numero2, operador)
              print(f" = {resultado:.2f}\n")
              continuar = input("DESEJA FAZER UMA NOVA OPERAÇÃO? (S/N)  ").upper()
              print("\n" + 35 * "-=")
              if continuar == "N":
                break
              else:
              # -- OPTANDO POR NÃO LIMPAR | DESLIGAR, O USUÁRIO TEM DUAS NOVAS OPÇÕES
                novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA | DESLIGAR CALCULADORA (E):  ").upper()
                while novaOp != "E" or novaOp == " ":
                    print("\n" + 35 *"-=")
                    novoNumero = float(input("\nNOVO NUMERO:  "))
                    operador = input("OPERADOR MATEMÁTICO: (use: ( + - x  / ))  ").lower()
                    # -- CONTINUE SOMANDO
                    while operador == "-":
                        formatacao(resultado, novoNumero, operador)
                        resultadoSub = resultado - novoNumero
                        print(f" = {resultadoSub:.2f}")
                        novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                        resultado = resultadoSub
                        break
                    # -- SUBTRAIR A PARTIR DO RESULTADO ANTERIOR
                    if operador == "+":
                      print("\n" + 35 * "-=")
                      resultadoSoma = resultado + novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoSoma:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      print("\n" + 35 * "-=")
                      resultado = resultadoSoma
                      continue
                      # -- MULTIPLICAR A PARTIR DO RESULTADO ANTERIOR
                    elif operador == "x":
                      print("\n" + 35 * "-=")
                      resultadoMult = resultado * novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoMult:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      print("\n" + 35 * "-=")
                      resultado = resultadoMult
                      continue
                    # -- DIVIDIR A PARTIR DO RESULTADO ANTERIOR
                    elif operador == "/":
                      print("\n" + 35 * "-=")
                      resultadoDiv = resultado / novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoDiv:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      print("\n" + 35 * "-=")
                      resultado = resultadoDiv
                      continue
                if novaOp == "E":
                  print("\n" + 35 * "-=")
                  operacao = input("\nLIMPAR CALCULADORA (L) | DESLIGAR CALCULADORA (ENTER):  ").upper()
                  if operacao == "L":
                        for c in range(0, 10):
                          c -+ 1
                          print("0")
                        print("AGUARDANDO VALORES!")
                        print(35 * "-=")
                        break
                  else:
                    print("\nDESEJA DESLIGAR A CALCULADORA (ENTER)")
                    break

# -- 1º CALCULO MULTIPLICAÇÃO:

          elif operador == "x":
              resultado = multiplicacao(numero, numero2)
              formatacao(numero, numero2, operador)
              print(f" = {resultado:.2f}\n")
              continuar = input("DESEJA FAZER UMA NOVA OPERAÇÃO? (S/N)  ").upper()
              print("\n" + 35 * "-=")
              if continuar == "N":
                break
              else:
              # -- OPTANDO POR NÃO LIMPAR | DESLIGAR, O USUÁRIO TEM DUAS NOVAS OPÇÕES
                novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  REINICIAR | DESLIGAR CALCULADORA (E):  ").upper()
                while novaOp != "E" or novaOp == " ":
                    print("\n" + 35 *"-=")
                    novoNumero = float(input("\nNOVO NUMERO:  "))
                    operador = input("OPERADOR MATEMÁTICO: (use: ( + - x  / ))  ").lower()
                    # -- CONTINUE SOMANDO
                    while operador == "x":
                        formatacao(resultado, novoNumero, operador)
                        resultadoMult = resultado * novoNumero
                        print(f" = {resultadoMult:.2f}")
                        novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                        resultado = resultadoMult
                        break
                    # -- SUBTRAIR A PARTIR DO RESULTADO ANTERIOR
                    if operador == "+":
                      print("\n" + 35 * "-=")
                      resultadoSoma = resultado + novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoSoma:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      print("\n" + 35 * "-=")
                      resultado = resultadoSoma
                      continue
                      # -- MULTIPLICAR A PARTIR DO RESULTADO ANTERIOR
                    elif operador == "-":
                      print("\n" + 35 * "-=")
                      resultadoSub = resultado - novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoSub:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      print("\n" + 35 * "-=")
                      resultado = resultadoSub
                      continue
                    # -- DIVIDIR A PARTIR DO RESULTADO ANTERIOR
                    elif operador == "/":
                      print("\n" + 35 * "-=")
                      resultadoDiv = resultado / novoNumero
                      formatacao(resultado, novoNumero, operador)
                      print(f" = {resultadoDiv:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      print("\n" + 35 * "-=")
                      resultado = resultadoDiv
                      break
                if novaOp == "E":
                  print("\n" + 35 * "-=")
                  operacao = input("\nLIMPAR CALCULADORA (L) | DESLIGAR CALCULADORA (ENTER):  ").upper()
                  if operacao == "L6":
                        for c in range(0, 10):
                          c -+ 1
                          print("0")
                        print("AGUARDANDO VALORES!")
                        print(35 * "-=")
                        break
                  else:
                    print("\nDESEJA DESLIGAR A CALCULADORA (ENTER)")
                    break
# -- 1º CALCULO DIVISÃO:

          elif operador == "/":
            resultado = divisao(numero, numero2)
            formatacao(numero, numero2, operador)
            print(f" = {resultado:.2f}\n")
            continuar = input("DESEJA FAZER UMA NOVA OPERAÇÃO? (S/N)  ").upper()
            print("\n" + 35 * "-=")
            if continuar == "N":
              break
            else:
            # -- OPTANDO POR NÃO LIMPAR | DESLIGAR, O USUÁRIO TEM DUAS NOVAS OPÇÕES
              novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  REINICIAR | DESLIGAR CALCULADORA (E):  ").upper()
              while novaOp != "E" or novaOp == " ":
                  print("\n" + 35 *"-=")
                  novoNumero = float(input("\nNOVO NUMERO:  "))
                  operador = input("OPERADOR MATEMÁTICO: (use: ( + - x  / ))  ").lower()
                  # -- CONTINUE SOMANDO
                  while operador == "/":
                      formatacao(resultado, novoNumero, operador)
                      resultadoDiv = resultado / novoNumero
                      print(f" = {resultadoDiv:.2f}")
                      novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                      resultado = resultadoDiv
                      break
                  # -- SUBTRAIR A PARTIR DO RESULTADO ANTERIOR
                  if operador == "+":
                    print("\n" + 35 * "-=")
                    resultadoSoma = resultado + novoNumero
                    formatacao(resultado, novoNumero, operador)
                    print(f" = {resultadoSoma:.2f}")
                    novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                    print("\n" + 35 * "-=")
                    resultado = resultadoSoma
                    continue
                    # -- MULTIPLICAR A PARTIR DO RESULTADO ANTERIOR
                  elif operador == "-":
                    print("\n" + 35 * "-=")
                    resultadoSub = resultado - novoNumero
                    formatacao(resultado, novoNumero, operador)
                    print(f" = {resultadoSub:.2f}")
                    novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                    print("\n" + 35 * "-=")
                    resultado = resultadoSub
                    continue
                  # -- DIVIDIR A PARTIR DO RESULTADO ANTERIOR
                  elif operador == "x":
                    print("\n" + 35 * "-=")
                    resultadoMult = resultado * novoNumero
                    formatacao(resultado, novoNumero, operador)
                    print(f" = {resultadoMult:.2f}")
                    novaOp = input("\nNOVA OPERAÇÃO A PARTIR DO RESULTADO (QUALQUER TECLA) -  LIMPAR TELA  | DESLIGAR CALCULADORA (E):  ").upper()
                    print("\n" + 35 * "-=")
                    resultado = resultadoMult
                    continue
              if novaOp == "E":
                print("\n" + 35 * "-=")
                operacao = input("\nLIMPAR CALCULADORA (L) | DESLIGAR CALCULADORA (ENTER):  ").upper()
                if operacao == "L":
                      for c in range(0, 10):
                        c -+ 1
                        print("0")
                      print("AGUARDANDO VALORES!")
                      print(35 * "-=")
                      break
                else:
                  print("\nDESEJA DESLIGAR A CALCULADORA (ENTER)")
                  break
      else:
        print("OPERADOR INCORRETO!")