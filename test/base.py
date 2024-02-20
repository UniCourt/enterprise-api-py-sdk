import argparse
import importlib
import os
import re
import time
import unicourt
from unicourt.sdk.Authentication import Authentication

class TestBase:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--exclude", action="store",
                                 help=" exclude test name by passing it in comma separated format")
        self.parser.add_argument("--include", action="store",
                                 help=" include test name by passing it in comma separated format")
        unicourt.CLIENT_ID = os.getenv("CLIENT_ID")
        unicourt.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self.auth_obj = unicourt.Authentication.generate_new_token()

    def run(self):
        args = self.parser.parse_args()
        # getting the list of test file and re-order authentication test file at end to run.
        module_list = [re.sub("\.py", "", module) for module in os.listdir() if module.startswith("test") and module.endswith("py")]
        index = module_list.index('test_authentication_api')
        module_list[index], module_list[-1] = module_list[-1], module_list[index]
        for module_name in module_list:
            module = __import__(module_name)
            class_name = [class_name for class_name in dir(module) if class_name.startswith('Test')][0]
            if args.exclude:
                if class_name in args.exclude.split(","):
                    continue
            if args.include:
                if class_name not in args.include.split(","):
                    continue
            print("########### Testing", class_name, "###########\n")
            instance_obj = getattr(module, class_name)
            method_list = [meth for meth in dir(instance_obj) if meth.startswith('test') is True]
            for method_name in method_list:
                if hasattr(instance_obj, method_name) and callable(function := getattr(instance_obj, method_name)):
                    try:
                        _, status_code = function()
                        print("Method:", method_name, "\nStatus Code:", status_code, "\n")
                        time.sleep(5)
                    except Exception as e:
                        print("Method:", method_name, "\nError", e)

def main():
    print("########### Starting Test for SDK ###########\n")
    TestBase().run()


if __name__ == "__main__":
    main()
