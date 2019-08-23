from pyspark.sql import Row

def main():

  #pasta com os arquivos
  textfile = sc.texFile("nasa")
  
  #textfile.take(10)
  
  separet = textfile.flapMap(lambda line: line.split(",")).map(lambda l: l.split(" "))
  
  separet.cache
  
  #separet.take(10)
  
  df = separet.map(lambda line: Row(host=line[0], timestamp=line[3], erro=line[4], requisicao=line[5]+line[6]+line[7], codigo=line[8], bytesc=line[9])).toDF()
  
  #df.show(10)
  
  #1. Número de hosts únicos.
  qtd_host = df.groupBy("host").count().sort("host", ascendind=False)
  qtd_host.count()
  #Resposta: 138505
  #2. O total de erros 404.
  separet33 = textfile.map(lambda line: line.split(" ")).filter(lambda l: l[8] == '404')
  separet33.take(10)
  df7 = separet33.map(lambda line: Row(timestamp=line[3], requisicao=line[6], codigo=line[8], bytesc=line[9])).toDF()
  result = df7.groupBy("codigo").count()
  R: ####
  #3. Os 5 URLs que mais causaram erro 404.
  result = df7.groupBy("requisicao").count().sort("requisicao", ascendind=False)
  R: ####
  #4. Quantidade de erros 404 por dia.
  R: ####
  #5. O total de bytes retornados.
  separet33 = textfile.map(lambda line: line.split(" ")).filter(lambda l: l[8] != '404')
  df7 = separet33.map(lambda line: Row(bytesc=line[9])).filter(lambda l: int(l)).toDF()
  df7.sum()
  R: #### 
  
 As respostas em #### não foram conclusivas, ou apresentaram algum erro que pode ser corrigido realizando o pré-processamento dos dados,
 alguns erros se deram por conta do tipo do dado não estar preenchido ou com caracteres inválidos.

if __name__== "__main__":
  main()
