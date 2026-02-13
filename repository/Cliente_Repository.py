from datetime import date

class Cliente_Repository:

    @staticmethod
    def save(driver, cliente, costureira, medidas, roupa, valor):
        dia = date.today()

        if cliente:
            driver.execute_query(
                """
                MERGE (d:dia {data:$dia})
                MERGE (c:cliente {name:$cliente})
                MERGE (cs:costureira {name:$costureira})
                MERGE (m:medidas {name:$medida, medida:$medida})
                MERGE (r:roupa {name:$roupa, descricao:$roupa})
                MERGE (v:valor {name:$valor})
                MERGE (p:pagamento {name:'PIX'})
                
                MERGE (d)-[:DIA_DA_VENDA]->(c)
                MERGE (c)-[:COSTURAR_COM]->(cs)
                MERGE (cs)-[:MEDIU]->(m)
                MERGE (m)-[:PARA_FAZER]->(r)
                MERGE (v)-[:VALOR_DE]->(p)
                """,
                dia=dia,
                cliente=cliente,
                costureira=costureira,
                medida=medidas,
                roupa=roupa,
                valor=valor,
                database_="neo4j"
            )
