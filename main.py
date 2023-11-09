pelo = ('c', 'm', 'l')

def cachorro_peso ():
  peso = int(input('Digite o peso do cachorro: '))
  try:
    if peso >= 50:
     peso = int(input('Digite o peso novamente, Não aceitamos cães grandes: '))
    if peso <= 2:
      peso = int(input('Digite o peso válido,: '))
  except ValueError:
            print('Entrada inválida! Digite um valor numérico para o peso do cachorro.')
  return peso

def cachorro_pelo():
    pelo = input('Digite o pelo do cachorro: ')
    if pelo == 'c':
        return 1
    if pelo == 'm':
        return 1.5
    if pelo == 'l':
        return 2
    if pelo not in pelo:
        pelo = input('INVALIDO. Digite o tipo de pelo do cachorro: ')

def cachorro_extra():
    adcional = int(input('Deseja algum serviço adicional?'))
    try:
      if adcional == 1:
        return + 10
      if adcional == 2:
       return + 12
      if adcional == 3:
        return + 15
      if adcional == 0:
        return + 0
      else:
        print('Digite uma opção válida')
    except ValueError:
            print('Entrada inválida! Digite um valor válido')


def calc():
  calculo = ((peso * pelo) + adcional1 + adcional2 + adcional3)
  return calculo

while True:
  print('Bem vindo ao pet shop da Bruna Santos')
  peso = cachorro_peso()
  print('O peso do cachorro é {}: kg'.format(peso))
  
  print('Entre com o pelo do cachorro: c - curto | m - medio | l- longo')
  pelo = cachorro_pelo()
  print('escolha do pelo concluida')

  print('1 - corte de unhas | 2 - escovar dentes | 3 - limpar orelhas | 0 - Mais nada ')
  adcional1 = cachorro_extra()
  adcional2 = cachorro_extra()
  adcional3 = cachorro_extra()

  calculo = calc()

  print('Total de tudo é {}: '.format(calculo))
  
  
  break
    




    
    
  
    
  
