COMMENT_CHAR = '#'
INPUT_FILE = 'test3.asm'

DEBUG = True


# Preprocess the lines to remove comments and whitespace
def preprocess_lines(lines_list:list):

  # remove comments and trailing whitespace
  for i in range(len(lines_list)):
    lines_list[i] = lines_list[i].split(COMMENT_CHAR, 1)[0].strip()

  # remove empty lines
  new_lines_list = list(filter(lambda x: x != '', lines_list))

  if DEBUG: print(new_lines_list)

  return new_lines_list



# Use the preprocessed program to build data table
def build_data_table(lines_list:list):
  data_table = {}
  data_list = []
  data_lines_list = []
  text_lines_list = []

  # split instructions based on headers
  text_header_index = 0
  try:
    text_header_index = lines_list.index('.text')
    text_lines_list = lines_list[text_header_index+1:]
  except:
    if DEBUG:
      print('.text absent')
      print(data_table)
      print(data_list)
    return data_table, data_list, lines_list

  data_header_index = -1
  try: data_header_index = lines_list.index('.data')
  except: 
    if DEBUG:
      print('.data absent')
      print(data_table)
      print(data_list)
    return data_table, data_list, text_lines_list

  data_lines_list = lines_list[data_header_index+1:text_header_index]
  
  # return if data section is empty
  if len(data_lines_list) == 0:
    if DEBUG:
      print('.data empty')
      print(data_table)
      print(data_list)
    return data_table, data_list, text_lines_list
  
  for i in range(len(data_lines_list)):
    split_line = data_lines_list[i].split(':')
    for part in split_line: part.strip()
    data_table.update({split_line[0]: i})

    data_list.append(split_line[1])
  

  if DEBUG:
    print(data_table)
    print(data_list)
  
  return data_table, data_list, text_lines_list



# TODO: Build a label table and strip out the labels from the code
def create_label_table(lines:list):
  return lines, lines




# TODO: Encode the program into a list of binary strings
def encode_program(encoded_program):
  pass




def post_process(asdasd):
  pass




def main():
  # Defining the assembly file to read from
  filename = INPUT_FILE

  # Read all lines from the assembly file, and store them in a list
  with open(filename, "r") as infile:
    lines:list = infile.readlines()

  lines = preprocess_lines(lines)

  data_table, data_list, lines = build_data_table(lines)

  # label_table, lines = create_label_table(lines)

  # encoded_program = encode_program(lines, label_table, data_table)

  # # Convert the strings to hexadecimal and write them to a file
  # hex_program = post_process(encoded_program)
  # with open("output.hex", "w") as outfile:
  #     outfile.write("v3.0 hex words addressed\n00: ")
  #     outfile.writelines(hex_program)

  # # Convert the data list to hexadecimal and write it to a file
  # with open("data.hex", "w") as outfile:
  #     outfile.write("v3.0 hex words addressed\n00: ")
  #     outfile.writelines([f"{d:04x} " for d in data_list])





main()