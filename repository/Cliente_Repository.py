from datetime import date

class Cliente_Repository:

    @staticmethod
    def save(driver, cliente, costureira, medidas, roupa, valor):
        dia = date.today()

        driver.execute_query(
            """
            MERGE (d:dia {data:$dia})
            MERGE (c:cliente {name:$cliente})
            MERGE (cs:costureira {name:$costureira})
            MERGE (m:medidas {descricao:$medidas})
            MERGE (r:roupa {descricao:$roupa})
            MERGE (v:valor {valor:$valor})
            MERGE (p:pagamento {tipo:'PIX'})
            
            // Cadeia completa conectada
            MERGE (d)-[:DIA_DA_VENDA]->(c)
            MERGE (c)-[:COSTURAR_COM]->(cs)
            MERGE (cs)-[:MEDIU]->(m)
            MERGE (m)-[:PARA_FAZER]->(r)
            MERGE (r)-[:TEM_VALOR]->(v)
            MERGE (v)-[:PAGO_COM]->(p)
            """,
            dia=dia.isoformat(),  # Corrigido para ISO 8601
            cliente=cliente,
            costureira=costureira,
            medidas=medidas,
            roupa=roupa,
            valor=float(valor)
        )
    @staticmethod
    def find_costureira (driver,nome_costureira):
         driver.execute_query(
            """
            MATCH (cs:costureira {name: $nome_costureira})
            RETURN cs
            """,
            costureira=nome_costureira
            )
