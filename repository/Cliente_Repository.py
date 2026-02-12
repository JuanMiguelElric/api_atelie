from neo4j import RoutingControl
from datetime import date
class Cliente_Repository:   
    def save(driver, cliente, costureira, medidas, roupa, valor):
        dia= date.today()
        if cliente:
            driver.execute_query(
                """ MERGE(d:date {name:$dia})
                    MERGE (c:cliente {name: $cliente})
                    MERGE (cs:costureira {name: $costureira})
                    MERGE (m:medidas {name:Medida, medida:$medidas})
                    MERGE (r:roupa {name:Roupa, descricao:$roupa})
                    MERGE (v:valor {name:$valor})
                    MERGE (p:pagamento {name:$pagamemento})
                    MERGE (d)->[:DIA_DA_VENDA]->(c)
                    MERGE (c)-[:COSTURAR_COM]->(cs)
                    MERGE (cs)-[:MEDIU]->(m)
                    MERGE (m)-[:Para_fazer]->(r)
                    MERGE (v)-[:VALOR]->(p)
                """,
                dia=dia,
                cliente=cliente,
                costureira=costureira,
                medida = medidas,
                roupa = roupa,
                valor = valor,
                database_="neo4j"
            )
        