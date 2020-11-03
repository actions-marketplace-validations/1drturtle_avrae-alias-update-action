import os
import requests
import json


def main():
    alias_id_file_name = os.environ.get('INPUT_ALIAS_ID_FILE_NAME')
    avrae_token = os.environ.get('INPUT_AVRAE_TOKEN')
    modified_files = os.environ.get('INPUT_MODIFIED-FILES', '[]')

    # alias_ids = {}
    # with open(alias_id_file_name, 'r') as f:
    #     alias_ids = json.loads(f.read())

    print(alias_id_file_name, modified_files, os.listdir('..'+os.path.dirname(os.path.realpath(__file__))))


if __name__ == '__main__':
    main()
