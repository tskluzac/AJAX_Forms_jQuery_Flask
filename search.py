import sys, os, json
import globus_auth




globus_url = "https://search.api.globus.org/"
globus_domain = "ripple-test"

def search(query_string, verbose=False):
    ''' Ingests feedstock from file.
        Arguments:
            mdf_source_names (str or list of str): Dataset name(s) to ingest.
            batch_size (int): Max size of a single ingest operation. -1 for unlimited. Default 100.
            verbose (bool): Print status messages? Default False.
        '''
    if verbose:
        print("\nSearching for string:", query_string, "\n")

    globus_client = globus_auth.login(globus_url, globus_domain)

    #TODO: Make this slightly more flexible.
    # super_list = get_list_from_json()
    #
    # for listy in super_list:
    #     gmeta = gmeta_entry(listy)
    #     print gmeta

    output = ''

    #print 'indexing it'

    # with open('cdiac_gmeta_index2.json', 'r') as json_data:
    #     gmeta = json.load(json_data)
    #     json_data.close()

    output = globus_client.search(query_string, limit=25)

    #print(output)
    return output

###### Uncomment this for in-file testing ######
# if __name__ == "__main__":
#
#     all_source_names = [
#
#         ]
#     search(all_source_names, verbose=True)

search_result = search('lat')
print(search_result["count"])
# stripped = (str(search_result)[19:])[:-1]
# print(stripped)
# print(json.loads(stripped))

