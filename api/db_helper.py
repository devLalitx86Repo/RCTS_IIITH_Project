import json
from pymongo import errors
import bson.json_util as json_util


from .db_connection import Database

class DbHelper():
    def __init__(self):
        self.db = Database()

    def list_docs(self):
        config_names_list = list()
        # db = Database()
        db = self.db
        status = db.connect()
        if not status[0]:
            return json.dumps({"Issue": status[1]}), 500
        # else:
        #     return json.dumps({"Issue": status[1]}), 200
        try:
            
            #get the doc count from the collection
            # count = db.client.count_documents({})
            # return json.dumps({"count": count})


            status = db.list_documents()
            if status[0]:
                print("This is fun",status)
                return json.dumps({"Status": "Success"}) , 200                
            #     for data in status[2]:
            #         # data = json.stringfy(data)
            #         config_names_list.append(data)
            # #         if data['Meta']['type'] == 'logic_head':
            # #             #convert to string
            # #             data['children'] = list(map(str, data['children']))
            # #         # json_doc = json.dumps(data,default=json_util.default)
            # #         # config_names_list.append(json_doc)
            #     return json.dumps(dict({"records": config_names_list}))
            # #     # return config_names_list
            else:
                return json.dumps({"Issue": status[1]}), 500
        except errors.ServerSelectionTimeoutError:
            return json.dumps(dict({"Issue": " >> Failed to Connect DB"}))