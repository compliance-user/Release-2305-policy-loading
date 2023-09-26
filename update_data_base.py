
import os
import json

current_file_path = current_directory = os.path.dirname(os.path.abspath(__file__))
policy_name= {}
file_path_dict = {}
def extract_names_from_json(directory_path):
    if directory_path.endswith('.json'):
        try:
            with open(directory_path, 'r') as json_file:
                json_data = json.load(json_file)
                name = json_data.get('name')
                if name:
                    head, tail = os.path.split(directory_path)
                    head, tail = os.path.split(head)
                    try:
                        file_path_dict[tail] = name
                        policy_name[name] = directory_path
                    except TypeError:
                       return
                return


        except FileNotFoundError:
            print(directory_path)
            print(f"Error reading JSON file: {str(e)}")
            return
        except AttributeError:
           print(f"'list' object has no attribute 'get' {directory_path}")
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {directory_path}")
            return
    else:
        try:
            file_list = os.listdir(directory_path)
        except NotADirectoryError:
            return
        for file_name in file_list:
            file_path = os.path.join(directory_path, file_name)
            extract_names_from_json(file_path)
        return

def update_data():
    global file_name_dict
    global policy_name_dict
    if os.path.exists(f'{current_file_path}/data_base.py'):
        os.remove(f'{current_file_path}/data_base.py')
    with open(f'{current_file_path}/data_base.py', 'w') as file:
        file.write(f"policy_name_dict = {repr(policy_name)}\n")
        file.write(f"file_name_dict = {repr(file_path_dict)}\n")



def main():
    directory_path = '/opt/core/core-resources/policy'
    extract_names_from_json(directory_path)
    update_data()



if __name__ == "__main__":
    main()
