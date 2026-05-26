# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

from pathlib import Path
import pandas

script_dir = Path(__file__).resolve().parent
data = pandas.read_csv(script_dir / "nato_phonetic_alphabet.csv")

phonetic_dict = data.set_index("letter")["code"].to_dict()
print(data.to_dict())

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Pon una palabra: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
