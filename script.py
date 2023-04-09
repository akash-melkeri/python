print("==============STARTING SETUP==============")
import requests,pickle

base_url = "https://192.168.229.146/BeyondTrust/api/public/v3/"
api_key = "37e3c62a5c329e54bdf2247e4a50f37c7546d3a9ce16423ad335d6ecd1ad962c1d8e5d4398b755246be08886e7c9993a70bbf5e2f3604991ad35c6829a6c9223"
runas = "apiuser"
header_login = {
    "Authorization":"PS-Auth key="+api_key +"; runas="+runas+";"
}

foundManagedSystems = {}

ses = requests.session()

def main():
    print("======= Execution Start =======")
    print("trying to restore previous session")
    restoreSession()
    
    getManagedSystems()
    
    print("saving current session")
    storeSession()
    print("======= Execution End =======")

def createEntity(data):
    return {
        "EntityTypeID" : data.get("EntityTypeID",None),
        "HostName" : data.get("HostName",None),
        "IPAddress" : data.get("IPAddress","172.16.26.2"),
        "DnsName" : data.get("DnsName",None),
        "InstanceName" : data.get("InstanceName",None),
        "IsDefaultInstance" : data.get("IsDefaultInstance",None),
        "Template" : data.get("Template",None),
        "ForestName" : data.get("ForestName",None),
        "UseSSL" : data.get("UseSSL",None),
        "PlatformID" : data.get("PlatformID",None),
        "NetBiosName" : data.get("NetBiosName",None),
        "ContactEmail" : data.get("ContactEmail",None),
        "Description" : data.get("Description","For Test, to be deleted"),
        "Port" : data.get("Port",None),
        "Timeout" : data.get("Timeout",30),
        "SshKeyEnforcementMode" : data.get("SshKeyEnforcementMode",0),
        "PasswordRuleID" : data.get("PasswordRuleID",0),
        "DSSKeyRuleID" : data.get("DSSKeyRuleID",0),
        "LoginAccountID" : data.get("LoginAccountID",None),
        "AccountNameFormat" : data.get("AccountNameFormat",0),
        "OracleInternetDirectoryID" : data.get("OracleInternetDirectoryID",None),
        "OracleInternetDirectoryServiceName" : data.get("OracleInternetDirectoryServiceName",None),
        "ReleaseDuration" : data.get("ReleaseDuration",120),
        "MaxReleaseDuration" : data.get("MaxReleaseDuration",10079),
        "ISAReleaseDuration" : data.get("ISAReleaseDuration",120),
        "AutoManagementFlag" : data.get("AutoManagementFlag",True),
        "FunctionalAccountID" : data.get("FunctionalAccountID",4),
        "ElevationCommand" : data.get("ElevationCommand",None),
        "CheckPasswordFlag" : data.get("CheckPasswordFlag",False),
        "ChangePasswordAfterAnyReleaseFlag" : data.get("ChangePasswordAfterAnyReleaseFlag",False),
        "ResetPasswordOnMismatchFlag" : data.get("ResetPasswordOnMismatchFlag",False),
        "ChangeFrequencyType" : data.get("ChangeFrequencyType","first"),
        "ChangeFrequencyDays" : data.get("ChangeFrequencyDays",30),
        "ChangeTime" : data.get("ChangeTime","23:30"),
        "AccessURL" : data.get("AccessURL",None)
    }
    


def getManagedSystems():
    print("getting managed systems")
    response = ses.get(url=base_url+"ManagedSystems",verify=False)
    foundManagedSystems = response.json()
    print(len(foundManagedSystems))

def login():
    print("trying to login")
    response = ses.post(url=base_url+"Auth/SignAppin",headers=header_login,verify=False)
    print(response.content,"con")
    print(response.text,"tex")

def restoreSession():
    try:
        with open('session', 'rb') as f:
            ses.cookies.update(pickle.load(f))
    except:
        print("error restoring previous session")
        login()

def storeSession():
    try:
        with open('session', 'wb') as f:
            pickle.dump(ses.cookies, f)
    except:
        print("error saving current session")

print("==============FINISHED SETUP==============")   
main()

def test():
    print("hello")
    data = [{
        "name":"umar"
    },{
        "name":"jatin"
    },{
        "name":"akash"
    }]
    
    print("data : ", data)
    for i in data:
        print(i['name'])
    pass