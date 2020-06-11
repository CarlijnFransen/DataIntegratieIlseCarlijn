"""
Author: Carlijn Fransen
date: 11 June 2020
project: convert vcf to mongodb

"""
import pymongo
import vcf


def main():
    """ calls other functions
    """
    con = create_db_connection()
    read_vcf(con)


def read_vcf(con):
    """

    :param con: connection
    :return: none
    """
    vcf_reader = vcf.Reader(open('gnomad.exomes.r2.1.1.sites.13.vcf'))
    for record in vcf_reader:
        alt = ""
        chrom = record.CHROM
        pos = record.POS
        ref = record.REF
        if len(record.ALT) > 1 and len(
                record.INFO['non_cancer_AF'] > 1 and len(record.ALT) == len(record.INFO['non_cancer_AF'])):
            print(True)
            for i in range(len(record.ALT)):
                non_cancer_af = record.INFO[i]
                alt = str(record.ALT[i])
                cancer_af = calculate_cancer_af(non_cancer_af)
                # alt.append(str(element))
                benign = filter_for_benign(cancer_af)
                if benign:
                    db_id = str(chrom) + "_" + str(pos) + "_" + str(ref) + "_" + str(alt)
                    document = create_document(db_id, chrom, pos, ref, alt, cancer_af)
                    add_document(document, con)

        else:
            try:
                alt = str(record.ALT[0])
                non_cancer_af = record.INFO['non_cancer_AF'][0]
            except KeyError:
                pass
            cancer_af = calculate_cancer_af(non_cancer_af)
            benign = filter_for_benign(cancer_af)
            if benign:
                db_id = str(chrom) + "_" + str(pos) + "_" + str(ref) + "_" + str(alt)
                document = create_document(db_id, chrom, pos, ref, alt, cancer_af)
                add_document(document, con)


def create_db_connection():
    """ creates connection with db

    :return: collection
    """
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['cancer_api']
    col = db['exomes13v2_data']
    return col


def calculate_cancer_af(non_cancer_af):
    """calculates the cancer alele frequency

    :param non_cancer_af: non cancer alele frequency
    :return: cancer alele frequency
    """
    cancer_af = 1 - non_cancer_af
    # calculates the cancer AF by doing a 1-non_cancer_AF
    return cancer_af


def filter_for_benign(cancer_af):
    """ filters all benign mutations out

    :param cancer_af: filters if cancer alele frequency is benign
    :return: boolean
    """
    # True =  Keep
    # False =  Discard
    if 0 < cancer_af < 0.01:
        return True
    else:
        return False
    # filters variants which have an cancer_AF>0.01


def create_document(db_id, chrom, pos, ref, alt, cancer_af):
    """ creates document for database insertion

    :param db_id: database identifier
    :param chrom: chromosome number
    :param pos: position on chormosome
    :param ref: reference nucleotide
    :param alt: alternative nucleotide
    :param cancer_af: cancer alele frequency
    :return: document in dictionary format
    """
    doc_dict = {}
    doc_dict["_id"] = db_id
    doc_dict["chromosome"] = chrom
    doc_dict["positon"] = pos
    doc_dict["ref"] = ref
    doc_dict["alt"] = alt
    doc_dict["cancer_af"] = cancer_af
    return doc_dict


def add_document(document, con):
    """

    :param document: dictionary format
    :param con: connection to database
    :return: none
    """
    # adds document as json/dictionary style format to the MongoDB database
    print(document)
    con.insert_one(document)


main()
