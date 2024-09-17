1 / 2 - Filtragem de Visuais
Descrição
Você tem uma lista de tipos de visuais e precisa processar essa lista para remover duplicatas e normalizar os nomes dos visuais. O objetivo é garantir que cada visual apareça apenas uma vez na lista e que todos os nomes estejam em um formato uniforme.

Remover Duplicatas: É comum em listas que certos itens apareçam mais de uma vez. Para evitar isso, precisamos garantir que cada tipo de visual apareça apenas uma vez na lista final.

Normalizar Nomes: Quando os usuários digitam nomes, eles podem usar diferentes formatos de capitalização (maiúsculas e minúsculas). Por exemplo, "gráfico de barras" e "Gráfico de Barras" são essencialmente o mesmo visual, mas escritos de maneiras diferentes. Precisamos padronizar esses nomes para que todos sigam o mesmo formato, facilitando a comparação e a remoção de duplicatas.

Para normalizar os nomes, vamos usar a capitalização do tipo "Título Capitalizado", onde a primeira letra de cada palavra é maiúscula e as demais letras são minúsculas. Por exemplo, "gráfico de barras" se tornará "Gráfico De Barras".

Entrada
O usuário irá fornecer uma lista de tipos de visuais como uma única string, onde cada visual é separado por vírgulas. A lista pode conter visuais repetidos ou escritos de maneira inconsistente.

Saída
Uma lista com visuais únicos e normalizados.

def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # Normalize os nomes dos visuais e remova duplicatas usando um conjunto
    visuais_normalizados = {visual.title() for visual in visuais}
    
    # Converta o conjunto de volta para uma lista ordenada
    lista_final = sorted(visuais_normalizados)
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)
############################
2 / 2 - Extração de Anos
Descrição
Neste desafio, você precisa processar uma lista de datas fornecida pelo usuário para extrair o ano de cada uma delas. A extração de anos pode ser útil para diversas aplicações, como a realização de análises anuais em grandes volumes de dados temporais.

Passo a Passo:

Entrada de Dados: O usuário fornecerá uma sequência de datas no formato "YYYY-MM-DD", onde "YYYY" representa o ano, "MM" o mês, e "DD" o dia. Todas as datas serão fornecidas em uma única linha, separadas por vírgula e espaço. Por exemplo: "2024-01-15, 2023-11-22, 2024-05-10".

Processamento dos Dados: O objetivo é isolar a parte correspondente ao ano de cada data. Isso pode ser feito dividindo cada string de data pelo caractere - e selecionando a primeira parte, que corresponde ao ano.

Formatação da Saída: Após extrair os anos, você deve retorná-los como uma nova lista, onde os anos estão separados por vírgulas. É importante manter a ordem original das datas fornecidas pelo usuário.

Entrada
Uma lista de datas no formato "YYYY-MM-DD" separados por vírgula.

Saída
Uma lista com os anos extraídos.

def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    
    # Extraia o ano de cada data e cria uma nova lista com os anos
    anos = [data.split("-")[0] for data in lista_datas]
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)

# Captura a entrada do usuário
entrada = input()

# Chama a função para processar a entrada e imprime o resultado
saida = extrair_anos(entrada)
print(saida)
