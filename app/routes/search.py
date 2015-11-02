# -*- coding: utf-8 -*-
"""
Created on 2015-10-27 19:34:00

@author: Tran Huu Cuong <tranhuucuong91@gmail.com>

"""
# -*- coding: utf-8 -*-

from app import app
# from app.models import term
from flask import abort, jsonify, request


# from pprint import pprint
# from elasticsearch import Elasticsearch
# es = Elasticsearch(hosts=[app.config.get('ES_HOST')])
from app import es


# @app.route('/glossary')
# def glossary():
#     return app.send_static_file('glossary.html')

#
# @app.route('/api/glossary/<string:id>', methods=['GET'])
# def get_term(id):
#     entity = term.Term.query.get(id)
#
#     if not entity:
#         abort(404)
#     return jsonify(entity.to_dict())


# @app.route('/api/search', methods=['GET'])
# def search():
#     max_results = request.args.get('max_results', 10)
#     max_results = int(max_results)
#
#     query = request.args.get('query')
#     entities = term.Term.query.filter(term.Term.id.ilike('%{}%'.format(query))).all()
#
#     if not entities:
#         abort(404)
#
#     # return json.dumps([entity.to_dict() for entity in entities[:max_results]])
#     return jsonify({'results': [entity.to_dict() for entity in entities[:max_results]]})


@app.route('/api/search', methods=['GET'])
def es_search():
    # max_results = request.args.get('max_results', 10)
    # max_results = int(max_results)
    #
    # query = request.args.get('query')
    # entities = term.Term.query.filter(term.Term.id.ilike('%{}%'.format(query))).all()
    #
    # if not entities:
    #     abort(404)
    #
    # # return json.dumps([entity.to_dict() for entity in entities[:max_results]])
    # return jsonify({'results': [entity.to_dict() for entity in entities[:max_results]]})

    # remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    app.logger.info('{} - {}'.format(request.remote_addr, request.url))

    query = request.args.get('q')

    results = es.search(index=app.config.get('INDEX_NAME'), q=query)

    hits = results['hits']['hits']

    if not hits:
        abort(404)

    return jsonify({'results': hits})
