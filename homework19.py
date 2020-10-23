import json
import yaml


#Task1
with open("sample_json.json", "r") as file:
	file_1 = json.load(file)

# with open("txt_file.txt", "w") as file_2:
# 	file_2.write(str(file_1))

#Task2

# with open("yaml_file.yaml", "w") as file_3:
# 	yaml.dump(file_1, file_3)

#Task3

with open("yaml_file.yaml", "r") as file_4:
	file_5 = yaml.load(file_4)

with open("json_file.json", "w") as file_6:
	json.dump(file_5, file_6)

#Task4

with open("new_text_file.txt", "w") as file_7:
	file_7.write(str(file_5))