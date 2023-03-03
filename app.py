from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j://localhost:7687",
                              auth=("Mishin", "Mishin040189"))


def find_info_in_db(tx, name):
    query = ("MATCH (event:Event) WHERE event.Namefirst = $name "
             "RETURN {EventID: event.eventID, Namefirst: event.Namefirst, "
             "Namesecond:event.Namesecond} as Event")
    print(list(tx.run(query, name=name)))


def print_info(name):
    with driver.session(database="mindsetdb") as session:
        data = session.execute_read(find_info_in_db, name)

    driver.close()
    return data


print_info('Скулкин Глеб Альбертович')