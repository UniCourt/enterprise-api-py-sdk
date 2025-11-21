# UniCourt Python SDK Tests


## Getting started 
To run the SDK tests you need python >= 3.7 and Git installed. 

## Test Parameters
Note: Ensure you are in the UniCourt SDK test directory
- Run all tests
  - python3 base.py
- Exclude given test cases using --exclude
  - python3 base.py --exclude TestPacer,TestPacerCredentials
- Run only specific test cases using --include
  - python3 base.py --include TestCaseSearch,TestCourtStandards


**Method 1 :**  Execute below given steps in the terminal

```shell
# Install UniCourt SDK
pip install unicourt

# Clone UniCourt SDK repository from Github
git clone https://github.com/UniCourt/enterprise-api-py-sdk.git

# Replace the below credentials with your credentials
export CLIENT_ID=”G3cfixgetVzfaoszGOBp5LPGtih1nMJ9”
export CLIENT_SECRET=”u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gf”
export PACER_CLIENT_CODE=”xyz_client_code”
export PACER_USER_ID=”pcrid”
export CLIENT_ID=”client_id”

# Move the to the test directory in the UniCourt SDK repository
cd enterprise-api-py-sdk/test/

# Run the tests
python3 base.py --exclude TestPacer
```

**Method 2 :** Use the Dockerfile in the test directory. Open up the terminal and run the below given command

```shell
docker build -t test_unicourt_sdk --build-arg SDK_VERSION=1.0 --build-arg CLIENT_ID=G3cfixgetVzfaoszGOBp5LPGtih1nMJ9 --build-arg CLIENT_SECRET=u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw --build-arg PACER_CLIENT_CODE=xyz_client_code --build-arg PACER_USER_ID=pcrid .
```


