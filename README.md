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

# Etapas de análise

Pasta 0.Base: leitura e download da base de dados via API do Kaggle; análise descritiva e exploratória da base completa e, por fim, a divisão da base em treino, validação e teste.

Pasta 1.Variaveis: com o uso da base de treino, estudos de variáveis correlacionadas e IV foram feitos; posteriormente, o pré-processamento foi feito e já aplicado nas bases de validação e teste.

Pasta 2.Modelagem: estudo de modelos e escolha de um destes para a aplicação nas bases futuras.