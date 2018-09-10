def load_data(item_handle):
    #put import statements inside this Function
    #import json or Csv
    import csv
    import random

    #with open('../corpora/csv-alles.csv', newline='') as csvfile:
    with open('../corpora/annotations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            obj={}
            obj['korpus.id'] = row[0]
            obj['hit'] = row[1]
            obj['task'] = row[2]
            obj['ad.mace'] = row[3]
            obj['ad.annotation'] = row[4]
            obj['cutoff.annotation'] = row[6]
            obj['cutoff.mace'] = row[5]
            obj['loading.annotation'] = row[8]
            obj['loading.mace'] = row[7]
            obj['pornographic.annotation'] = row[10]
            obj['pornographic.mace'] = row[9]
            obj['popup.annotation'] = row[12]
            obj['popup.mace'] = row[11]
            obj['captcha.annotation'] = row[14]
            obj['captcha.mace'] = row[13]
            obj['error.annotation'] = row[16]
            obj['error.mace'] = row[15]

            item_handle.add(obj)

#    for x in range(0,100):
#        obj={}
#        obj['id'] = x
#        obj['Input.hit'] = x
#        obj['item'] = str(x)
#        obj['prediction'] = 'no or yes' + str(x)
        #register item to viewer
#        item_handle.add(obj)

#this is the main dictionary containing the necessary information to load and display your corpus
DICT_SETTINGS_VIEWER = {
    'name': 'Annotation',
    'description': 'This Corpus contains Webpages and their Annotation',
    'data_type': 'csv-file',
    'load_data_function': load_data,
    #'data_path': '../corpora/csv-alles.csv',
    'data_path': '../corpora/annotations-test.csv',
    #'data_path': '../corpora/testbatch1.csv',
    #'data_path':'../../../web-archive-page-annotation/data/error-annotation/batch1-mace-prediction-before-review.csv', #path to json or csv
    'data_structure': ['korpus.id','hit','task','ad.mace','ad.annotation', 'cutoff.mace', 'cutoff.annotation', 'loading.mace', 'loading.annotation', 'pornographic.mace', 'pornographic.annotation', 'popup.mace', 'popup.annotation', 'captcha.mace', 'captcha.annotation', 'error.mace', 'error.annotation'],

    'data_fields': {
        #'id': {
        #    'type': 'number',
        #    'display_name': 'ID'
        #},
        'korpus.id': {
            'type': 'number',
            'display_name': 'KorpusID'
        },
        'hit': {
            'type': 'number',
            'display_name': 'HitID'
        },
        'task': {
            'type': 'number',
            'display_name': 'Task'
        },
        'ad.mace': {
            'type': 'string',
            'display_name': 'Ad Mace'
        },
        'ad.annotation': {
            'type': 'string',
            'display_name': 'Ad Annotation'
        },
        'cutoff.mace': {
            'type': 'string',
            'display_name': 'Cutoff Mace'
        },
        'cutoff.annotation': {
            'type': 'string',
            'display_name': 'Cutoff Annotation'
        },
        'loading.mace': {
            'type': 'string',
            'display_name': 'Loading Mace'
        },
        'loading.annotation': {
            'type': 'string',
            'display_name': 'Loading Annotation'
        },
        'pornographic.mace': {
            'type': 'string',
            'display_name': 'Pornographic Mace'
        },
        'pornographic.annotation': {
            'type': 'string',
            'display_name': 'Pornographic Annotation'
        },
        'popup.mace': {
            'type': 'string',
            'display_name': 'Popup Mace'
        },
        'popup.annotation': {
            'type': 'string',
            'display_name': 'Popup Annotation'
        },
        'captcha.mace': {
            'type': 'string',
            'display_name': 'Captcha Mace'
        },
        'captcha.annotation': {
            'type': 'string',
            'display_name': 'Captcha Annotation'
        },
        'error.mace': {
            'type': 'string',
            'display_name': 'Error Mace'
        },
        'error.annotation': {
            'type': 'string',
            'display_name': 'Error Annotation'
        }
    },
    'id': 'korpus.id',
    'displayed_fields': [
        'korpus.id','hit','task', 'ad.mace','ad.annotation', 'cutoff.mace', 'cutoff.annotation', 'loading.mace', 'loading.annotation','pornographic.mace', 'pornographic.annotation', 'popup.mace', 'popup.annotation', 'captcha.mace', 'captcha.annotation', 'error.mace', 'error.annotation'
    ],
    'page_size': 25,
    'secret_token': 'test',
    'secret_token_editing': '',
    'template': '../corpora/index.html',
    'secret_token_help': None,


}
