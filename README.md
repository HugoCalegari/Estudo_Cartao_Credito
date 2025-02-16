# Estudo_Cartao_Credito

Estudo de churn de cartão de crédito

# Link para as bases

- https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

# Contexto

Um gerente de um banco está preocupado com o fato de clientes estarem deixando de usar os serviços de cartão de crédito. O gerente não quer mais perder clientes para esse produto de crédito, mas se não for possível "zerar esssa perda", ele entende que reduzir a evasão já é um ótimo sinal. 

Além disso, dois pontos importantes foram destacados: 
    
    1. em conjunto com a área de marketing, ele avaliou que o custo de aquisição de novos clientes teve um aumento de 20% comparado com o mesmo período do ano passado. Dessa forma, manter o cliente no banco evitaria esse gasto;
       
       De acordo com Philip Kotler, especialista e referência em Marketing no mundo, a conquista de um novo cliente custa entre 5 e 7 vezes mais do que manter/reter um cliente atual.

       Outro ponto importante é o perfil dos clientes ou novos clientes conquistados. O time de marketing está desenvolvendo um estudo que avalia a relação entre um único uso do cartão com o perfil selecionado do cliente. Será isso um teste feito pelo cliente para avaliação do serviço de cartão? 
       
       Além disso, de acordo com a reportagem feita pela Exame (https://exame.com/colunistas/relacionamento-antes-do-marketing/a-segunda-compra-do-cliente-e-mais-importante-do-que-a-primeira/), pode-se estabelecer um paralelo com o conceito de segunda compra, ou seja, o segundo uso e posteriores usos do cartão de crédito depende de aspectos qualitativos. O cliente conseguiu se auto-servir, por exemplo, antecipação de pagamento de fatura do cartão?
    
    2. em conjunto com alguns analistas de dados, notou-se que cerca de 10% dos clientes que deixaram de usar os serviços de cartão já estavam com pelo menos 20 dias de atraso na fatura do cartão de crédito; metade desses 10% utilizaram uma única vez o cartão e nunca pagaram a fatura (FPD).

De acordo com o time de negócio, se conseguirmos classificar o público que será churn todos os esforços serão direcionados para "salvá-los" e os atingiremos em sua totalidade, seja 100 clientes ou 2.000 clientes. Algumas estratégias: massificada ou segmentada (por exemplo, por faixa de renda e idade) serão pensadas para reter os clientes do cartão de crédito.

# Etapas das análises

Pasta 0.Base: leitura e download da base de dados via API do Kaggle; análise descritiva e exploratória da base completa e, por fim, a divisão da base em treino, validação e teste.
    
    - Exploracao_Inicial: análise descritiva e exploratórias das variáveis. Avaliação de frequência para as variáveis categóricas, histograma para as variáveis numéricas, tabelas cruzadas entre as variáveis categóricas (incluindo a variável resposta), histograma para as variáveis numéricas agrupado por clientes churn e não churn, **criação de duas novas variáveis** (vfm := valor financeiro médio por transação nos últimos 12 meses, equivalente ao ticket médio por operação em 12 meses; pmcc := proporção média mensal utilizada de cartão de crédito) e gráficos de dispersão entre as variáveis numéricas.

    - Treino_Val_Teste: separação entre bases de treino, validação e teste. 85% para treino, os 15% restantes foram divididos em 85% para validação e 15% para teste, ou seja, 12,75% para validação e 2,25% para teste.

Pasta 1.Variaveis: com o uso da base de treino, estudos de variáveis correlacionadas e IV foram feitos; posteriormente, o pré-processamento foi feito e já aplicado nas bases de validação e teste.

    - Variaveis_Potenciais: passagem por correlação de variáveis numéricas e análise de IV de todas as variáveis.

    - Pré-processmanto: construção de dois pré-processamentos. O primeiro, com o uso da padronização e do One Hot Encoding e, o segundo, com o uso da padronização e do Ordinal Encoding. Toda a parte posterior de modelagem foi usada a primeira versão.

Pasta 2.Modelagem: estudo de modelos e escolha de um destes para a aplicação nas bases futuras.

    - Modelos_baselines: construção de modelos bases sem tunning de hyperparâmetros e log deles no mlflow. Os modelos considerados foram: Random Forest e XGBoost. Foram feitas análises de interpretabilidade, calibragem e análises de métricas.

    - Hiperparametros & CV: procura de melhor conjunto de hiperparâmetros usando Bayesian Optimization, para os modelos destacados na etapa anterior. Uso da validação cruzada no momento da procura do melhor conjunto de hiperparâmetros e na etapa de avaliação de quais seriam os melhores pontos de corte. Nesta etapa, também foi usado o mlflow para o log das métricas de interesse.

    - MLP: teste de uso de uma rede neural Multi-Layer_Perceptron para.

    - Modelos_finais: aplicação dos melhores modelos anteriores na base de teste e as conclusões finais que poderíamos obter com a aplicação do modelo no cenário real/de negócio.

# Escolha de um melhor modelo

Dos modelos avaliados, aquele que melhor se adequou aos dados foi a Random Forest, com otimização de hiperparâmetros. As seguintes métricas foram encontradas na base de teste: Auc_Pr = 0.77; BS_Teste = 0.076; Log_Loss = 0.26; usando o melhor ponto de corte (0.31), F1_Score = 0.72, Precisao = 0.70 e Recall = 0.75. É importante salientar que a procura do modelo foi baseada no direcionamento mais preciso dos investimentos para a retenção do cliente, ou seja, não se tem interesse de aportar em clientes falso positivos e não se quer deixar de aportar em clientes que são falsos negativos.

Não houve desvio das probabilidades obtidas na base de teste e na base de treino, ou seja, o KS das probabilidades preditas ficou baixo. Isso indica que a fonte geradora das probabilidades permanece a mesma.

Com o uso do perfil de eficiência acumulada (CAP), por exemplo, olhar para os primeiros 200 primeiros clientes, significa olhar para os 150 que são altamente prováveis a ser churn. Para a base de teste, isso representa 13% de toda a base e 61% dos clientes maus!

Depois das análises acima, percebeu-se que o Índice de Estabilidade Populacional (IEP ou PSI) das variáveis do modelo na base de treino e teste permaneceram estáveis.