from __future__ import unicode_literals, absolute_import, print_function
import pymongo
import bdblib
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def task(env, action, caseid="None", platform="None", technology="None", feedback="None"):
    """
    1-Retreive and save the LH stats in MongoDB and display with Admin Portal front-end
    """
    result = bdblib.TaskResult()

    dbaas  = get_dbaas(env)
    userid = env.user_name
    admin_status = get_admin_status(dbaas, userid)

    backend_action = action.lower()
    if backend_action == "get_admin_status":
        admin_status = get_admin_status(dbaas, userid)
        result.append(admin_status)
    elif backend_action == "save_entry":
        save_entry(caseid, platform, technology, feedback, dbaas)
    elif backend_action == "get_stats":
        data = get_stats(platform, technology, feedback, dbaas)
        result.append(data)
    else:
        result.append("Action or parameters combination is invalid or submitter is not in admin group")

    return result

def get_dbaas(env):
    # connect to MongoDB, and return pymongo object
    dbaas_mongo_url = "mongodb://" + ",".join([ srv['host'] + ":" + str(srv['port']) for srv in env.task_db['mongoServers'] ]) + "/?replicaSet={}".format(env.task_db['replica'])
    dbaas = pymongo.MongoClient(dbaas_mongo_url)[env.task_db['database']]
    dbaas.authenticate(env.task_db['username'], env.task_db['password'])
    return dbaas

def get_admin_status(dbaas, requestor_name):
    # get the admin status using list of admin in MongoDB
    requestor_admin_status = False
    for doc in dbaas['admin_list'].find():
        admin_names = doc["admin"]
    if requestor_name in admin_names:
        requestor_admin_status = True
    return requestor_admin_status

def get_stats (platform, technology, feedback, dbaas):
    stats = []
    doc = dbaas["lighthouse_statistics"].find()
    for item in doc:
        stats.append(item)
    return stats

def save_entry (caseid, platform, technology, feedback, dbaas):
    entry = {}
    entry["caseid"], entry["platform"], entry["technology"], entry["feedback"] = caseid, platform, technology, feedback
    dbaas["lighthouse_statistics"].insert_one(entry)
