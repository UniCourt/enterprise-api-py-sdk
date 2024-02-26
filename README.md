# UniCourt Python SDK 
The UniCourt SDK provides simplified access to the UniCourt API for applications written in the Python programming language.


## Documentation

See the API documentation here : [UniCourt API docs](https://docs.unicourt.com/direct-links/download-api-specification).

See the UniCourt data model here (requires UniCourt account): [UniCourt Data Model](https://docs.unicourt.com/enterpriseapi/unicourt_data_model_ui).

### Requirements

-   Python >=3.6

## Installation
You can use the source code if you want to modify the package and use it as per your need. If you just want to use the package, just run:
```sh
pip install --upgrade unicourt
```

Install from source :

```sh
export SDK_VERSION=<new sdk version>
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