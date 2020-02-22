import requests

def getallvehicleheaders():
    getallvehicleheaders = {
        "X-Api-Key": "bpEUTJEBTf74oGRWxaIcW7aeZMzDDODe1yBoSxi2"
    }
    return getallvehicleheaders

def getallvehicles():
    import pdb;
    pdb.set_trace()
    getallvehiclesresult = requests.get("https://platform.tier-services.io/vehicle?", headers=getallvehicleheaders())
    import pdb; pdb.set_trace()


def main():
    getallvehicles()


if __name__ == "__main__":
    main()
