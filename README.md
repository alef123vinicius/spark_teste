# spark_teste

Uma breve descrição e implementação utilizando o Spark e Python para análise dos dados fornecidos pela NASA Space Center WWW server.

## Algumas questões sobre funções e parâmetros do Spark:

  Pergunta 1. Qual o objetivo do comando cache em Spark?
  
R: Por padrão, o RDD transformado pode ser recalculado toda vez que uma ação for executada nele. O comando cache é utilizado para persistir um RDD na memória usando o método cache (ou persist). Assim, o spark manterá os elementos no cluster para acessá-los de forma mais rápida na próxima consulta.

  Pergunta 2. O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

R: O MapReduce segue o modelo de programação funcional, e executa a sincronização explícita por meio de etapas computacionais. Apesar de ser simples, o MapReduce possui algumas limitações, como por exemplo, a execução de algoritmos de aprendizado de máquina, que necessitam rodar os mesmos dados várias vezes. Isso pode representar uma sobrecarga no MapReduce. O que já não acontece no spark, por que possui a característica principal de executar o processamento em memória, ou seja, como os dados já ficam na memória para fácil acesso, graças ao RDD que faz essa implementação das estruturas de dados em memória. Dessa forma, os algoritmos podem utilizar os dados várias vezes e de forma eficiente.

  Pergunta 3. Qual é a função do SparkContext?
  
R: A função sparkContext informa ao spark como acessar um cluster. Ela possui um parâmetro de configuração que é preciso ser criado com a função sparkConf, onde irá conter as informações do aplicativo. Essa função sparkConf possui dois parâmetros que são o nome do aplicativo (appName) e o (master) que seria uma url para ser executado em modo local.


  Pergunta 4. Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
  
R: É uma coleção distribuída de elementos paralelizados no cluster. Possui dois tipos de operações, sendo elas transformação e ação. A transformação, são aquelas funções que não retornam um valor e o spark apenas cria os grafos acíclicos, que são avaliados em tempo de execução. As ações ocorrem quando as transformações são avaliadas junto com a ação que é chamada no RDD. 

  Pergunta 5. GroupByKey​ ​é menos eficiente que reduceByKey em grandes dataset. Por quê?
  
R: Em grandes conjuntos de dados, é melhor usar outras funções, como reduceByKey(), combineByKey()ou foldByKey(). Quando você usa groupByKey(), todos os pares de valores-chave são misturados no cluster. Muitos dados desnecessários estão sendo transferidos pela rede. Além disso, isso também significa que, se mais dados forem embaralhados em uma única máquina que podem caber na memória, os dados serão lançados no disco. Isso afeta muito o desempenho do seu trabalho do Spark.
Quando você usa reduceByKey(), por exemplo, os pares com a mesma chave já estão combinados antes que os dados sejam embaralhados. Como resultado, você precisará enviar menos dados pela rede. Em seguida, a função reduzir é chamada novamente para que todos os valores de cada partição sejam reduzidos.

## Questões Práticas
Pergunta 6. Explique o que o código Scala abaixo faz.

val textFile = sc.textFile("hdfs://...")
val counts = textFile.flatMap(line => line.split(" "))
.map(word => (word, 1))
.reduceByKey(_ + _)
counts.saveAsTextFile("hdfs://...")

Pergunta 7. 
HTTP​ ​requests​ ​to​ ​the​ ​NASA​ ​Kennedy​ ​Space​ ​Center​ ​WWW​ ​server

Fonte​ ​oficial​ ​do​ ​dateset​: http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html
Dados​:
● Jul 01 to Jul 31, ASCII format, 20.7 MB gzip compressed, 205.2 MB.
● Aug 04 to Aug 31, ASCII format, 21.8 MB gzip compressed, 167.8 MB.
Sobre o dataset​: Esses dois conjuntos de dados possuem todas as requisições HTTP para o servidor da NASA Kennedy
Space Center WWW na Flórida para um período específico.

Os logs estão em arquivos ASCII com uma linha por requisição com as seguintes colunas:
● Host fazendo a requisição​. Um hostname quando possível, caso contrário o endereço de internet se o nome não puder ser identificado.
● Timestamp​ ​no formato "DIA/MÊS/ANO:HH:MM:SS TIMEZONE"
● Requisição​ ​(entre​ ​aspas)
● Código​ ​do​ ​retorno​ ​HTTP
● Total​ ​de​ ​bytes​ ​retornados

Questões
Responda às seguintes questões devem ser desenvolvidas em Spark utilizando a sua linguagem de preferência.

1. Número de hosts únicos.
2. O total de erros 404.
3. Os 5 URLs que mais causaram erro 404.
4. Quantidade de erros 404 por dia.
5. O total de bytes retornados.
