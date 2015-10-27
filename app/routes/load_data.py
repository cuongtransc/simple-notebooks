#!/usr/bin/env python

# import csv
# import titlecase
from elasticsearch import Elasticsearch

from app import app

# PATH_FILE = 'data/dict_financial_accounting.csv'
# PATH_FILE = 'data/dict_economics.csv'
# PATH_FILE = 'data/dict_accounting.csv'
# PATH_FILE = 'data/dict_digital-marketing-terms.csv'
# PATH_FILE = 'data/dict_project_management.csv'


ID_FIELD = 'en_term'

# def create_bulk_data():
#     """create bulk data"""
#
#     bulk_data = []
#
#     with open(PATH_FILE) as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=';')
#
#         for row in reader:
#             op_dict = {
#                 "index": {
#                     "_index": ES_INDEX_NAME,
#                     "_type": app.config.get('ES_TYPE_NAME'),
#                     "_id": row[ID_FIELD].strip().lower()
#                 }
#             }
#
#             data = dict()
#             data['en_term'] = titlecase.titlecase(row['en_term'].strip())
#             data['en_desc'] = row['en_desc'].strip().capitalize()
#             data['vi_term'] = row['vi_term'].strip().capitalize()
#             data['vi_desc'] = row['vi_desc'].strip().capitalize()
#             # data['vi_term_no_accent'] = remove_diacritic(data['vi_term'])
#             # data['vi_desc_no_accent'] = remove_diacritic(data['vi_desc'])
#             bulk_data.append(op_dict)
#             bulk_data.append(data)
#
#     return bulk_data

from app import Entry

def create_bulk_data():
    entries = Entry
    pass

def create_index():
    """create ES client, create index"""
    es = Elasticsearch(hosts=[app.config.get('ES_HOST')])

    if es.indices.exists(app.config.get('ES_INDEX_NAME')):
        print("deleting '%s' index..." % (app.config.get('ES_INDEX_NAME')))
        res = es.indices.delete(index=app.config.get('ES_INDEX_NAME'))
        print(" response: '%s'" % (res))

    request_body = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "default": {
                        "tokenizer": "standard",
                        "filter": ["lowercase", "asciifolding"]
                    },
                    "vietnamese": {
                        "tokenizer": "vi_tokenizer"
                    },
                    "folding": {
                        "tokenizer": "standard",
                        "filter": ["lowercase", "asciifolding"]
                    }
                }
            }
        }
    }
    # "type": "custom",
    # request_body = {
    #     "settings": {
    #         "number_of_shards": 1,
    #         "number_of_replicas": 0,
    #         "analysis": {
    #             "analyzer": {
    #                 "folding": {
    #                     "tokenizer": "standard",
    #                     "filter": ["lowercase", "asciifolding"]
    #                 }
    #             }
    #         }
    #     }
    # }


    print("creating '%s' index..." % (app.config.get('ES_INDEX_NAME')))
    res = es.indices.create(index=app.config.get('ES_INDEX_NAME'), body=request_body)
    print(" response: '%s'" % (res))


    # bulk_data = create_bulk_data()
    #
    # # bulk index the data
    # print("bulk indexing...")
    # res = es.bulk(index=app.config.get('ES_INDEX_NAME'), body=bulk_data, refresh=True)
    # # print(" response: '%s'" % (res))


def update_data_index():
    """Update data index"""
    es = Elasticsearch(hosts=[app.config.get('ES_HOST')])
    bulk_data = create_bulk_data()

    # bulk index the data
    print("bulk indexing...")
    res = es.bulk(index=app.config.get('ES_INDEX_NAME'), body=bulk_data, refresh=True)
    # print(" response: '%s'" % (res))


def test_search():
    # sanity check
    es = Elasticsearch(hosts=[app.config.get('ES_HOST')])

    print("searching...")
    res = es.search(index=app.config.get('ES_INDEX_NAME'),
                    size=2, body={"query": {"match_all": {}}})
    print(" response: '%s'" % (res))

    print("results:")
    for hit in res['hits']['hits']:
        print(hit["_source"])


if __name__ == '__main__':
    create_index()
    # test_search()
    # update_data_index()
