"""
Author: Carlijn Fransen
Date: 11 June 2020
Project: functions for querying mongodb database
"""
import pymongo

from web import API_logic



def main():
    """

    :return:
    """
    input_attribute = API_logic.read_input_file()
    id_list = API_logic.structure_list(input_attribute)
    collection = connection_db()
    doc_list = create_query(id_list, collection)


def connection_db():
    """

    :return:
    """
    client = pymongo.MongoClient("mongodb://localhost/")
    db = client['cancer_api']
    col = db['exomes13v2_data']
    return col


def create_query(api_input_list, col):
    """

    :param api_input_list: list with ids
    :param col: connection collection
    :return: json for
    """
    doc_list = []
    for x in api_input_list:
        query = {"_id": x}
        print(query)
        document = get_query(col, query)
        doc_list.append(document)
    return doc_list


def get_query(col, query):
    """ creates search query of database

    :param col: collection of database
    :param query: search query
    :return: returns document
    """
    d= " "
    doc = col.find(query)
    for d in doc:
        print(True)
    return d

main()
