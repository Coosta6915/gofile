import requests


def response_handler(response):
    if response["status"] == "ok":
        return response["data"]

    elif "error-" in response["status"]:
        error = response["status"].split("-")[1]
        raise Exception(error)


def checkAccountExists(token):
    checkAccountExists_response = requests.get(
        url=f"https://api.gofile.io/getAccountDetails?token={token}"
    ).json()

    if checkAccountExists_response["status"] == "ok":
        return True
    elif checkAccountExists_response["status"] == "error-wrongToken":
        return False
    else:
        response_handler(checkAccountExists_response)


def checkApi():
    checkApi_response = requests.get(
        url="https://api.gofile.io/"
    ).json()

    return response_handler(checkApi_response)


def getServer():
    getServer_response = requests.get(
        url="https://api.gofile.io/getServer"
    ).json()

    return response_handler(getServer_response)


def uploadFile(file: str, token: str = None, folderId: str = None, description: str = None, password: str = None, tags: str = None, expire: int = None, server: str = getServer()["server"]):
    # GoFile doesn't set a password if it is less than 4 characters
    if password != None and len(password) < 4:
        raise Exception("passwordLength")

    # file_name = file.replace("\\", "/").split("/")[-1]

    uploadFile_response = requests.post(
        url=f"https://{server}.gofile.io/uploadFile",
        data={
            "token": token,
            "folderId": folderId,
            "description": description,
            "password": password,
            "tags": tags,
            "expire": expire
        },
        files={"upload_file": open(file, "rb")}
    ).json()

    return response_handler(uploadFile_response)


def getContent(contentId, token):
    getContent_response = requests.get(
        url=f"https://api.gofile.io/getContent?contentId={contentId}&token={token}"
    )

    return response_handler(getContent_response)


def createFolder(parentFolderId, folderName, token):
    createFolder_response = requests.put(
        url="https://api.gofile.io/createFolder",
        data={
            "parentFolderId": parentFolderId,
            "folderName": folderName,
            "token": token
        }
    ).json()

    return response_handler(createFolder_response)


def setFolderOption(token, folderId, option, value):
    setFolderOptions_response = requests.put(
        url="https://api.gofile.io/setFolderOption",
        data={
            "token": token,
            "folderId": folderId,
            "option": option,
            "value": value
        }
    ).json()

    return response_handler(setFolderOptions_response)


def copyContent(contentsId, folderIdDest, token):
    copyContent_reponse = requests.put(
        url="https://api.gofile.io/copyContent",
        data={
            "contentsId": contentsId,
            "folderIdDest": folderIdDest,
            "token": token
        }
    ).json()

    return response_handler(copyContent_reponse)


def deleteFolder(folderId, token):  # deprecated
    print("Deprecated, use deleteContent() instead")
    deleteFolder_response = requests.delete(
        url="https://api.gofile.io/deleteContent",
        data={
            "folderId": folderId,
            "token": token
        }
    ).json()

    return response_handler(deleteFolder_response)


def deleteFile(fileId, token):  # deprecated
    print("Deprecated, use deleteContent() instead")
    deleteFile_response = requests.delete(
        url="https://api.gofile.io/deleteContent",
        data={
            "fileId": fileId,
            "token": token
        }
    ).json()

    return response_handler(deleteFile_response)


def deleteContent(contentId, token):
    deleteContent_response = requests.delete(
        url="https://api.gofile.io/deleteContent",
        data={
            "contentId": contentId,
            "token": token
        }
    ).json()

    return response_handler(deleteContent_response)


def getAccountDetails(token: str, allDetails: bool = False):
    if allDetails:
        getAccountDetails_response = requests.get(
            url=f"https://api.gofile.io/getAccountDetails?token={token}&allDetails=true"
        ).json()
    else:
        getAccountDetails_response = requests.get(
            url=f"https://api.gofile.io/getAccountDetails?token={token}"
        ).json()

    return response_handler(getAccountDetails_response)
