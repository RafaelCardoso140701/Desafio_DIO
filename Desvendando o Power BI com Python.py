1 / 2 - Fundamentos de Business Intelligence (BI)
Descrição
Business Intelligence (BI) envolve o uso de ferramentas e técnicas para coletar, processar e analisar dados, com o objetivo de apoiar a tomada de decisões estratégicas em uma organização. Os conceitos fundamentais de BI incluem a integração de dados, armazenamento, análise e visualização. Complete o código associando os fundamentos de BI às suas respectivas descrições para entender melhor cada conceito e sua aplicação prática.

Entrada
A entrada é um termo ou conceito relacionado aos fundamentos de BI para o qual você deve retornar a descrição. Os termos considerados são:

ETL
Data Warehousing
Dashboard
Data Mining
Saída
A saída esperada é a descrição associada ao termo fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

Armazenamento centralizado de dados para análise e relatórios.
Processo de extrair, transformar e carregar dados de diversas fontes.
Ferramenta visual para monitoramento e análise de métricas.
Descoberta de padrões e insights em grandes conjuntos de dados.

def identificar_termo_bi(termo):
    if termo == "ETL":
        return "Processo de extrair, transformar e carregar dados de diversas fontes."
    elif termo == "Data Warehousing":
        return "Armazenamento centralizado de dados para análise e relatórios."
    elif termo == "Dashboard":
        return "Ferramenta visual para monitoramento e análise de métricas."
    elif termo == "Data Mining":
        return "Descoberta de padrões e insights em grandes conjuntos de dados."
    else:
        return "Termo não reconhecido"

entrada = input()

print(identificar_termo_bi(entrada))

######################################################

2 / 2 - Fundamentos Sobre ETL
Descrição
O processo ETL (Extract, Transform, Load) é uma etapa crítica em Business Intelligence que envolve a integração de dados provenientes de diferentes fontes para análises e relatórios. Cada etapa do processo ETL tem um papel específico na preparação dos dados para serem analisados. Complete o código associando os conceitos e etapas do processo ETL às suas respectivas descrições para entender como cada fase contribui para a análise de dados.

Entrada
A entrada é um conceito ou etapa do processo ETL para o qual você deve retornar a descrição. Os conceitos considerados são:

Extract
Transform
Load
Data Integration
Saída
A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

Processo de coletar dados de diversas fontes.
Processo de converter dados para um formato adequado.
Carregamento de dados transformados em banco de dados ou warehouse.
Unificação de dados provenientes de múltiplas fontes.
# Função responsável por receber um conceito de ETL e retornar sua descrição.
def identificar_conceito_etl(conceito):
    if conceito == "Extract":
        return "Processo de coletar dados de diversas fontes."
    elif conceito == "Transform":
        return "Processo de converter dados para um formato adequado."
    elif conceito == "Load":
        return "Carregamento de dados transformados em banco de dados ou warehouse."
    elif conceito == "Data Integration":
        return "Unificação de dados provenientes de múltiplas fontes."
    else:
        return "Conceito não reconhecido"

entrada = input()

print(identificar_conceito_etl(entrada))
