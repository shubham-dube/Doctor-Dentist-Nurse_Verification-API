# Doctors, Dentists and Nurse Verification API

This API fetches the details of a doctor and nurse with their registration number and nurse id (nuid) to make the easy job for hospitals and other medical institutions to verify the doctor's identity.

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#EndPoints)
- [Support](#Support)
- [Contribution](#Contribution)

## Features

- Send Registration Number and Date (only for Doctors) or Nurse ID (nuid) for fetching their details.
- Return their Education Qualification and Personal details in a structured JSON format.
- Easy to integrate in any of your application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shubham-dube/Doctor-Dentist-Nurse_Verification-API.git
   cd Doctor-Dentist-Nurse_Verification-API
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux use `source venv/bin/activate`
   
3. Install the dependencies:
   ```bash
   pip install flask requests base64 bs4 html json

4. Run the Application:
   ```bash
   python app.py
 *The API will be available at http://127.0.0.1:5000.*
 
## Usage
- Show the User for input of Registration Number and Date (if they want to check Doctor Details) and Nurse ID (if they want search For Nurse).
- Send the entered details according to the below endpoint request bodies.
- You will get all the details related to that Registration number or Nurse ID in the JSON format.
  
## EndPoints

### Fetching Doctor Details

**Endpoint:** `/api/v1/getDoctorDetails`

**Method:** `POST`

**Description:** `This Endpoint fetches all the doctor details along with their education details with their Registration Number and Date`

**Request Body:**
```json
{
  "registrationNumber": "81496",
  "registrationDate": "26/06/2007",
}
```

**Response**
```json
{
    "education": {
        "college": "THANJAVUR",
        "doctorDegree": "MBBS",
        "university": "U.Dr.MGR",
        "yearOfInfo": 2007,
        "yearOfPassing": "2007"
    },
    "personal": {
        "address": "NO.60,SUBHASH MARG,DHANMANDI, RATLAM,MADHYA PRADESH.457001",
        "dateOfBirth": "01/09/1981",
        "doctorId": 812956,
        "doctorName": "PRAVEEN KUMAR VAGHMAR",
        "fatherName": "ANOKHI LAL VAGHMAR"
    },
    "registrationDate": "26/06/2007",
    "registrationNumber": "81496",
    "stateMedicalCouncil": "Tamil Nadu Medical Council",
    "stateMedicalCouncilId": 21
}
```
**Status Codes**
- 200 OK : `Details Fetched Successfully`


### Fetching Dentist Details

**Endpoint:** `/api/v1/getDentistDetails`

**Method:** `POST`

**Description:** `This Endpoint fetches only small details for dentist along with their name with their Registration Number`

**Request Body:**
```json
{
    "registrationNumber": "A302"
}
```
**Response**
```json
{
    "dentalStateCouncil": "Andhra Pradesh State Dental Council",
    "doctorName": "MADHUSUDHANA.",
    "registrationNumber": "A302"
}
```
**Status Codes**
- 200 OK : `Data Retrieved Successfuly`


### Fetching Nurse Details

**Endpoint:** `/api/v1/getNurseDetails`

**Method:** `POST`

**Description:** `This Endpoint fetches the details of a nurse with their nurse id (nuid)`

**Request Body:**
```json
{
    "nurseId(nuid)": "UP9379"
}
```
**Response**
```json
{
    "appl_name": "Seema Gautam",
    "councilname": "Uttar Pradesh Nurses and Midwives Council, Lucknow",
    "email": "seemagautam545@gmail.com",
    "full_name": "Jitendra Yadav",
    "mobile": "8181872359",
    "nuid": "UP9379",
    "registeredas": "RNRM",
    "success": "success",
    "u_statecode": "9"
}
```
**Status Codes**
- 200 OK : `Data Retrieved Successfuly`

## Support
For Support Contact me at itzshubhamofficial@gmail.com
or Mobile Number : `+917687877772`

## Contribution

We welcome contributions to improve this project. Here are some ways you can contribute:

1. **Report Bugs:** If you find any bugs, please report them by opening an issue on GitHub.
2. **Feature Requests:** If you have ideas for new features, feel free to suggest them by opening an issue.
3. **Code Contributions:** 
    - Fork the repository.
    - Create a new branch (`git checkout -b feature-branch`).
    - Make your changes.
    - Commit your changes (`git commit -m 'Add some feature'`).
    - Push to the branch (`git push origin feature-branch`).
    - Open a pull request.

4. **Documentation:** Improve the documentation to help others understand and use the project.
5. **Testing:** Write tests to improve code coverage and ensure stability.

Please make sure your contributions adhere to our coding guidelines and standards.
