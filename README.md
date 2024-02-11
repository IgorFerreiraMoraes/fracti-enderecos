# Fracti: 
Desafio de Separação de Ruas e Números em Endereços Concatenados.

## Funcionalidade
Esta solução visa ser capaz de processar entradas com endereços concatenados e retornar campos separados de rua e número.

Isso inclui lidar com uma variedade de casos, alguns simples como "[Augusta 1475](https://maps.app.goo.gl/95ka2sDefBSYcCaH9)", outros mais complexos como "4, Rue de la République".

## Desafio

Um provedor de endereços os fornece em uma única string com nome e número da rua, porém nosso sistema precisa dessas informações separadas em campos distintos.

Portanto, a tarefa é desenvolver um código simples que possa processar essa entrada e extrair os campos necessários para produzir a saída desejada.

### Objetivo
Entregar um Exexcutável, incluindo testes, que atenda os exemplos informados abaixo:

1. Casos Simples: Ruas com uma palavra
    - 'Miritiba 339' -> {'Miritiba', '339'}
    - 'Babaçu 500' -> { 'Babaçu', '500'}
    - 'Cambuí 804B' -> {'Cambuí', '804B'}

2. Casos mais Complicados: Ruas com múltiplas palavras
    - 'Rio Branco 23' -> {'Rio Branco', '23'}
    - 'Quirino dos Santos 23 b' -> {'Quirino dos Santos', '23 b'}

3. Casos Complexos: Endereços de outros países
    - '4, Rue de la République' -> {'Rue de la République', '4'}
    - '100 Broadway Av' -> {'Broadway Av', '100'}
    - 'Calle Sagasta, 26' -> {'Calle Sagasta', '26'}
    - 'Calle 44 No 1991' -> {'Calle 44', 'No 1991'}
## Uso

### Python
Para usar a função de separar endereços, certifique-se de ter o [Python](https://www.python.org/) instalado em seu sistema.

É possível abrir os arquivos diretamente do explorador de arquivos (dois cliques) ou usar o terminal no diretório com o arquivo desejado:

```bash
python fracti.py

python python test_split_address.py
```

### Executáveis
Também estão disponíveis versões compiladas da aplicação como arquivos executáveis (.exe). Para utilizá-los, basta  baixar e executar o arquivo em um PC com Windows.

OBS: Esses arquivos foram fornecidos apenas para avaliação do desafio. **NÃO É RECOMENDADO RODAR ARQUIVOS DESSE TIPO VINDOS DE DESCOHECIDOS!**

## O Nome
Devido ao processo de dividir os endereços em suas partes componentes, batizei de "Fracti".
