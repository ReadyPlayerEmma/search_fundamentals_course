from flask import g, current_app
from opensearchpy import OpenSearch

# Create an OpenSearch client instance and put it into Flask shared space for use by the application
def get_opensearch():
    if 'opensearch' not in g:
        #### Step 4.a:
        # Implement a client connection to OpenSearch so that the rest of the application can communicate with OpenSearch
        host = 'localhost'
        port = 9200
        hosts = [{'host': host, 'port': port}]
        auth = ('admin', 'admin')

        g.opensearch = OpenSearch(hosts=hosts, http_auth=auth, use_ssl=True, verify_certs=False, ssl_show_warn=False)


    return g.opensearch
