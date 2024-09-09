# UniCourt Python SDK
The UniCourt SDK provides simplified access to the UniCourt API for applications written in the Python programming language.


## Documentation

See the API documentation here : [UniCourt API docs](https://docs.unicourt.com/direct-links/download-api-specification).

See the UniCourt data model here (requires UniCourt account): [UniCourt Data Model](https://docs.unicourt.com/enterpriseapi/unicourt_data_model_ui).

### Requirements

-   Python >=3.7

## Installation
You can use the source code if you want to modify the package and use it as per your need. If you just want to use the package, just run:
```sh
pip install --upgrade unicourt
```

Install from source :

```sh
python setup.py install
```

## Pre-request and Configuration
You need a UniCourt account with API access :  [Subscription Plans](https://unicourt.com/pricing)

You will find clientId and secret here: [Client Secrets](https://app.unicourt.com/developers/enterpriseAPI)

## Getting Started
The Python script you see here takes two command line arguments i.e clientId and secret, to execute the script copy and paste the code to a file (sample.py) and run the script in a terminal as shown in the example below.

Example : 
- python sample.py [your client id] [your secret]
- python sample.py G3cfixgetVzfaoszGOBp5LPGtih1nMJ9 u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw

```python
import unicourt
from unicourt import *

# Get CLIENT_ID and CLIENT_SECRET from your account
unicourt.CLIENT_ID = "G3cfixgetVzfaoszGOBp5LPGtih1nMJ9"
unicourt.CLIENT_SECRET = "u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw"

# Authenticate to generate a access token, below line will return
# a tuple consisting of authentication object and http status code.
# You can generate up to 10 authentication tokens so be sure to use
# invalidate_token() method to invalidate the token once you are done
# or store the token securely and use it for subsequent requests.
auth_obj, http_status_code = Authentication.generate_new_token()

# Get Area Of Law details.
court_standards_obj, http_status_code = CourtStandards.get_areas_of_law(
    q='name:"Personal Injury"',
    page_number=1,
    sort="name",
    order="asc")
for court_standard_obj in court_standards_obj.area_of_law_array:
    print("Area Of Law Id : ", court_standard_obj.area_of_law_id)


# Get Judge details.
judge_obj, http_status_code = JudgeAnalytics.search_normalized_judges(
    q="name:(ANN H. PARK)")
for judge in judge_obj.norm_judge_search_result_array:
    print("Norm Judge Id :", judge.norm_judge_id)

# Get Attorney details.
attorney_obj, http_status_code = AttorneyAnalytics.search_normalized_attorneys(
    q="name:(PURDY STUART JAMES)",
    page_number=1
)
for attorney in attorney_obj.norm_attorney_search_result_array:
    print("Attorney Name :", attorney.name)
    print("Norm Attorney Id :", attorney.norm_attorney_id)

# Invalidate the generated access token
Authentication.invalidate_token()
```

## Python Error Exceptions
SDK will throw Python error exceptions in the below mentioned scenario's.
- When the request agruments or data passed to the SDK functions are incorrect.

    Example :
    ```
    Callback.get_callbacks() got an unexpected keyword argument 'vardate'
    ```
- When the sever sends any error response.

    Example :
    ```
    Reason: Internal Server Error
    HTTP response headers: HTTPHeaderDict({'Date': 'Tue, 13 Aug 2024 09:31:41 GMT', 'Content-Type': 'application/json', 'Content-Length': '145', 'Connection': 'keep-alive', 'Apigw-Requestid': 'ccMvJhfYoAMEWzA='})
    HTTP response body: {"object": "Exception", "code": "UN500", "message": "INTERNAL_SERVER_ERROR", "details": "Has encountered a situation which needs to be handled."}
    ```
- When the response has any new values which are not supported by the SDK. This can occur only when using the older version of SDK.

    Example :
    ```
    1 validation error for ServiceStatusDownDetails
    reason
      Value error, must be one of enum values ('issueAtTheCourtSource', 'notIntegrated', 'brokenIntegration') [type=value_error, input_value='underMaintenance', input_type=str]
        For further information visit https://errors.pydantic.dev/2.8/v/value_error
    ```