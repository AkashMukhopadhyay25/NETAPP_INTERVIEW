import logging
import warnings
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, Response, abort, request

warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

# fetching Configurations from resource/config.ini

ENDPOINT_URL = "https://ec2-3-25-117-144.ap-southeast-2.compute.amazonaws.com/api"
USERNAME = "squiggle"
PASSWORD = "GoLangRocks77"
CREDENTIALS = HTTPBasicAuth(USERNAME, PASSWORD)
# To Fetch Aggregate Data using UUID.


def getAggregateData(uuid):
    # Since we only require Statistics IOPS Raw, we are filtering the fields to fetch it.
    # Alternatively, we could fetch the entire data and then capture IOPS Raw through it.

    queryString="fields=statistics.iops_raw.total"
    aggregateEndpoint = "{}/storage/aggregates/{}?{}".format(ENDPOINT_URL, uuid, queryString)
    
    try:
        req = requests.get(aggregateEndpoint, auth=CREDENTIALS, verify=False)
    except:
        app.logger.error("Error at /storage/aggregates api")
        abort(500)
    # converting the response to a JSON format.
    data = req.json()

    # Extracting the IOPS RAW from data.
    totalRawIOPS = data["statistics"]["iops_raw"]["total"]
    return totalRawIOPS


@app.errorhandler(404)
def pageNotFound(error):
    return Response("PageNotFound", status=404, mimetype='application/json')


@app.errorhandler(500)
def serverError(error):
    return Response("Invalid Server Endpoint, UserName or Password", status=500, mimetype='application/json')


@app.route('/getVolume',  methods=['GET'])
def getVolumeData():
    #As an improvement, we could accept filters from the user and fetch only what's required. 
    queryString="fields=uuid,name,state,size,aggregates.uuid,qos.policy"

    volumeEndpoint = "{}/storage/volumes?{}".format(ENDPOINT_URL, queryString)
    try:
        req = requests.get(volumeEndpoint, auth=CREDENTIALS, verify=False)
    except Exception:
        app.logger.error("Error at /storage/volumes api")
        abort(500)

    app.logger.info("SuccessFully Fetched Volume Data")

    # resp will store the Response.
    resp = {}
    data = req.json()
    resp["Total Number of Volumes"] = 0
    resp["Volumes"] = []

    for val in data["records"]:
        resp["Total Number of Volumes"] += 1

        # Handles Error in case of Server side Field Changes.
        try:
            volumeName = val["name"]
            volumeUuid = val["uuid"]
            volumeState = val["state"]
            volumeSize = val["size"]/(1024*1024*1024)
        except:
            app.logger.error("Invalid Volume Field Queried")
            return Response("Client Server Error", status=503, mimetype='application/json')

        iopsDensity = 0.0

        # inCase VolumeSize is 0, iopsDensity would not be divided by 0.
        if volumeSize > 0:
            if(val["qos"]["policy"]["max_throughput_iops"] != 0):
                iopsDensity = val["qos"]["policy"]["max_throughput_iops"]/volumeSize
            else:
                app.logger.info("QOS Policy Unavailable for " +
                                volumeUuid+". Fetching IOPS RAW Aggregate Data.")
                totalRawIOPS = 0

                # loop through all the aggregates of the UUID.
                for aggr in val["aggregates"]:
                    totalRawIOPS += getAggregateData(aggr["uuid"])

                iopsDensity = totalRawIOPS/volumeSize
        resp["Volumes"].append(
            {"Volume UUID": volumeUuid, "Volume Name": volumeName, "Volume State": volumeState, "IOPS Density": iopsDensity})
    return resp, 200
