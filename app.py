from flask import Flask, jsonify, Response, make_response, request
import requests
from bs4 import BeautifulSoup
import html
import json
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

@app.route("/api/v1/getDoctorDetails", methods=["POST"])
def getDoctorDetails():
    try:
        registrationNumber = request.json.get("registrationNumber")
        registrationDate = request.json.get("registrationDate")
        session = requests.Session()

        initialPostData = {
            "registrationNo": registrationNumber
        }

        response = session.post(
            "https://www.nmc.org.in/MCIRest/open/getDataFromService?service=searchDoctor",
            data = json.dumps(initialPostData)
        )

        doctors = response.json()

        doctorIndex = -1
        for i in range(len(doctors)):
            if(registrationDate == doctors[i]['regDate']):
                doctorIndex = i

        if(doctorIndex==-1):
            return jsonify({"status": "Doctor Not Found"})
        
        doctor = doctors[doctorIndex]
        
        jsonResponse = {
            "personal": {
                "doctorName": doctor['firstName'],
                "dateOfBirth": doctor['birthDateStr'],
                "fatherName": doctor['parentName'],
                "address": doctor['address'],
                "doctorId": doctor['doctorId']
            },
            "registrationNumber": doctor['registrationNo'],
            "registrationDate": doctor['regDate'],
            "stateMedicalCouncil": doctor['smcName'],
            "stateMedicalCouncilId": doctor['smcId'],
            "education": {
                "doctorDegree": doctor['doctorDegree'],
                "university": doctor['university'],
                "college": doctor['college'],
                "yearOfInfo": doctor['yearInfo'],
                "yearOfPassing": doctor['yearOfPassing']
            }
        }
        return jsonify(jsonResponse)
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching Doctor Details"})
    

@app.route("/api/v1/getDentistDetails", methods=["POST"])
def getDentistDetails():
    try:
        name = request.json.get("name")
        regNo = request.json.get("registrationNumber")
        state = request.json.get("state")
        session = requests.Session()

        response1 = session.get(
            "https://dciindia.gov.in/DentistDetails.aspx"
        )

        soup = BeautifulSoup(response1.text, 'html.parser')
        
        __VIEWSTATE = soup.find('input', id='__VIEWSTATE').get('value')
        __VIEWSTATEGENERATOR = soup.find('input', id='__VIEWSTATEGENERATOR').get('value')
        __EVENTVALIDATION = soup.find('input', id='__EVENTVALIDATION').get('value')

        initialPostData = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE":__VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "__EVENTVALIDATION": __EVENTVALIDATION,
            "ctl00$MainContent$txtName": name,
            "ctl00$MainContent$txtRegNo": regNo,
            "ctl00$MainContent$ddlSDC": state,
            "ctl00$MainContent$btnSearch": "Search"
        }

        response = session.post(
            "https://dciindia.gov.in/DentistDetails.aspx", data=initialPostData
        )

        htmlString = response.text
        cleaned_html_string = htmlString.replace('\n', '').replace('\r', '').replace('\t', '').replace('\\', '')
        cleaned_html_string = html.unescape(cleaned_html_string)

        soup = BeautifulSoup(cleaned_html_string, 'html.parser')
        table = soup.find('table', class_='boxtxt')
        if(not table):
            return jsonify({"status": "Doctor Not Found"})

        doctorRow = table.find_all('tr')[1]

        doctorName = doctorRow.find_all('td')[1].get_text()
        registrationNumber = doctorRow.find_all('td')[2].get_text()
        dentalStateCouncil = doctorRow.find_all('td')[3].get_text()

        if(registrationNumber!=regNo):
            return jsonify({"status": "Doctor Not Found"})
        
        jsonResponse = {
            "registrationNumber": regNo,
            "doctorName": doctorName,
            "dentalStateCouncil": dentalStateCouncil
        }
        return jsonify(jsonResponse)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching Dentist Details"})


@app.route("/api/v1/getNurseDetails", methods=["POST"])
def getNurseDetails():
    try:
        nuid = request.json.get("nurseId(nuid)")
        session = requests.Session()

        initialPostData = {
            "nuid": nuid
        }

        session.get(
            "https://nrts.indiannursingcouncil.gov.in/login.nic"
        )

        response = session.post(
            "https://nrts.indiannursingcouncil.gov.in/getvalidusername.nic?method=getvalidnuid_nuid", data=initialPostData
        )

        return jsonify(response.json())

    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching Nurse Details"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5001)