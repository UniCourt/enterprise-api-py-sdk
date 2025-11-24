# UniCourt Python SDK
The UniCourt SDK provides simplified access to the UniCourt API for applications written in the Python programming language.


## Documentation

See the API documentation here : [UniCourt API docs](https://docs.unicourt.com/direct-links/download-api-specification).

See the UniCourt data model here (requires UniCourt account): [UniCourt Data Model](https://docs.unicourt.com/enterpriseapi/unicourt_data_model_ui).

### Requirements

- Python >=3.7

## Installation
To customize the package, you can modify the source code as needed.
If you simply want to use the package, install it with:

```shell
pip install --upgrade unicourt
```

Install from source:

```shell
python setup.py install
```

## Pre-request and Configuration
Requires UniCourt account with API access :  [Subscription Plans](https://unicourt.com/pricing)

ClientId and Client secrets can be found here: [Client Secrets](https://app.unicourt.com/developers/enterpriseAPI)

## Getting Started
This Python script accepts two command-line arguments: clientId and ClientSecret.
To run it, copy the code into a file (e.g., sample.py) and execute it in your terminal as shown below:

Example : 
- `python sample.py [your client id] [your client secret]`
- `python sample.py G3cfixgetVzfaoszGOBp5LPGtih1nMJ9 u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw`

```python
import sys

import unicourt
from unicourt import AttorneyAnalytics, Authentication, CourtStandards, JudgeAnalytics

# Get CLIENT_ID and CLIENT_SECRET from command line arguments
if len(sys.argv) >= 3:
    unicourt.CLIENT_ID = sys.argv[1]
    unicourt.CLIENT_SECRET = sys.argv[2]
else:
    raise ValueError("CLIENT_ID and CLIENT_SECRET must be provided via command line arguments.")

# Generate new access token using CLIENT_ID and CLIENT_SECRET,  the generate_new_token() 
# method will return a tuple consisting of authentication object and http status code.
# Note: A maximum of 10 authentication tokens can be active at a time.
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

## Important Note On Merging & Release
The below process for merge and release is necessary because all pull requests from forks cannot access repository secrets, causing GitHub Actions workflows to fail. The Github Actions will be successfully completed only if pull requests are merged from the branches within the https://github.com/UniCourt/enterprise-api-py-sdk repository.

### Merging and Release Process

1. Create a pull request targeting the [dev-1.1.x](https://github.com/UniCourt/enterprise-api-py-sdk/tree/dev-1.1.x) branch.
2. Repository maintainer will review and merge the PR into the [dev-1.1.x](https://github.com/UniCourt/enterprise-api-py-sdk/tree/dev-1.1.x) branch.
   - **Note:** Before merging, the maintainer ensures the [main](https://github.com/UniCourt/enterprise-api-py-sdk/tree/main) and [dev-1.1.x](https://github.com/UniCourt/enterprise-api-py-sdk/tree/dev-1.1.x) branches are in sync.
3. Repository maintainer will create a PR from [dev-1.1.x](https://github.com/UniCourt/enterprise-api-py-sdk/tree/dev-1.1.x) to the [main](https://github.com/UniCourt/enterprise-api-py-sdk/tree/main) branch.
   - Merging this PR triggers a GitHub Actions workflow that verifies the changes.
4. After Github Actions is completed, repository maintainer will create a tag and release.


### GitHub Actions

The GitHub Actions workflow builds and installs the SDK from source, then runs tests that call the APIs using the SDK.

**Github Actions Test Account:**
- Account Name: Enterprise API Team SDK Github Test Account
- Account ID: p1651099774