import unicourt
from collections import namedtuple

# access client config through this function.
def api_client():
    if not unicourt.configuration:
        unicourt.configuration = unicourt.Configuration(
            access_token=unicourt.ACCESS_TOKEN)
    if not unicourt.api_client:
        unicourt.api_client = unicourt.ApiClient(unicourt.configuration)
    return unicourt.api_client
