import argparse
import importlib
import os
import re
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
        obj, _ = unicourt.Authentication.generate_new_token()

    def log(self, func_name,  status):
        pass

    def run(self):
        args = self.parser.parse_args()
        for module_name in [re.sub("\.py", "", module)
                            for module in os.listdir() if module.startswith("test") and module.endswith("py")]:

            module = __import__(module_name)
            class_name = [class_name for class_name in dir(
                module) if class_name.startswith('Test')][0]
            #print(class_name, args.exclude.split())
            if args.exclude:
                if class_name in args.exclude.split(","):
                    continue
            if args.include:
                if class_name not in args.include.split(","):
                    continue
            instance_obj = getattr(module, class_name)

            method_list = [meth for meth in dir(
                instance_obj) if meth.startswith('test') is True]
            for method_name in method_list:
                if hasattr(instance_obj, method_name) and callable(function := getattr(instance_obj, method_name)):
                    try:
                        _, status_code = function()
                        print(method_name, status_code)
                        #instance_obj.log(method_name, status_code)
                    except Exception as e:
                        #instance_obj.log(method_name, status_code)
                        Authentication.invalidate_token()


def main():
    TestBase().run()


if __name__ == "__main__":
    main()