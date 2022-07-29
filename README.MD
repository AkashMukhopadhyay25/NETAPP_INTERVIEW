# AKASH MUKHOPADHYAY | NETAPP

## 1. SETUP

```
The Main File: src/main/main.py
The Test File: src/test/test_app.py

Virtual Environment Used: netApp
To directly run the server, you can activate the virtual environment <<netApp>> file present in the current working directory.
To activate the virtual Environment, run:
source ./kfs-exercise/netApp/bin/activate

Once, the virtual environment is Active, run:
export FLASK_APP=./src/main/main.py

Alternatively, you could run:
pip install -r resource/requirements.txt
```

## 2. Configurations

```
You can configure the endpoint, the UserName and the Password used to fetch data from the server.
```

## 3. API's Supported

```
/getVolume
sampleRequest: http://localhost:5000/getVolume
sampleResponse:
{
    "Total Number of Volumes": 3,
    "Volumes": [
        {
            "IOPS Density": 84366.3,
            "Volume Name": "test",
            "Volume State": "online",
            "Volume UUID": "5bff7933-07cb-11ed-9826-01cc1cebff23"
        },
        {
            "IOPS Density": 1000.0,
            "Volume Name": "my_svm_root",
            "Volume State": "online",
            "Volume UUID": "746d2a06-07d4-11ed-9826-01cc1cebff23"
        },
        {
            "IOPS Density": 843663.0,
            "Volume Name": "svm_newhire_root",
            "Volume State": "online",
            "Volume UUID": "9f6588b9-07c0-11ed-a6ab-cd6da7b9d310"
        }
    ]
}
```

# 4. Testing the Application:

```
Before you execute the test, make sure the server is running.
Once confirmed, execute python3 ./src/test/test_app.py
```
