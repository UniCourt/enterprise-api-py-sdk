# UniCourt Python SDK Tests


## Getting started 
To run the SDK tests you need python >= 3.6 and Git installed. 

## Test Parameters
- Run all tests
  - python3 enterprise-api-py-sdk/test/base.py
- Exclude given test cases using --exclude
  - python3 enterprise-api-py-sdk/test/base.py --exclude TestPacer,TestPacerCredentials
- Run only specific test cases using --include
  - python3 enterprise-api-py-sdk/test/base.py --include TestCaseSearch,TestCourtStandards



**Method 1 :**  Execute below given steps in the terminal

```
  pip install unicourt

  git clone https://github.com/UniCourt/enterprise-api-py-sdk.git

  EXPORT CLIENT_ID=”G3cfixgetVzfaoszGOBp5LPGtih1nMJ9”

  EXPORT CLIENT_SECRET=”u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gf”

  EXPORT PACER_CLIENT_CODE=”xyz_client_code”

  EXPORT PACER_USER_ID=”pcrid”
  
  EXPORT CLIENT_ID=”client_id”

  python3 enterprise-api-py-sdk/test/base.py --exclude TestPacer
```

**Method 2 :** Use the Dockerfile in the test directory. Open up the terminal and run the below given command

```
docker build -t test_unicourt_sdk --build-arg SDK_VERSION=1.0 --build-arg CLIENT_ID=G3cfixgetVzfaoszGOBp5LPGtih1nMJ9 --build-arg CLIENT_SECRET=u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw --build-arg PACER_CLIENT_CODE=xyz_client_code --build-arg PACER_USER_ID=pcrid .
```

  Above command will execute the tests and the results are printed out on the terminal.


