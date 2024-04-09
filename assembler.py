COMMENT_CHAR = '#'


# Preprocess the lines to remove comments and whitespace
def preprocess_lines(lines:list):

  # remove comments and trailing whitespace
  for i in range(len(lines)):
    lines[i] = lines[i].split(COMMENT_CHAR, 1)[0].strip()

  # remove empty lines
  lines = filter(lambda x: x != '', lines)

  return lines




# TODO: Use the preprocessed program to build data table
def build_data_table(lines:list):
  return lines, lines, lines



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
  filename = "test1.asm"

  # Read all lines from the assembly file, and store them in a list
  with open(filename, "r") as infile:
    lines:list = infile.readlines()

  lines = preprocess_lines(lines)
  print(lines)

  data_table, data_list, lines = build_data_table(lines)

  label_table, lines = create_label_table(lines)

  encoded_program = encode_program(lines, label_table, data_table)

  # Convert the strings to hexadecimal and write them to a file
  hex_program = post_process(encoded_program)
  with open("output.hex", "w") as outfile:
      outfile.write("v3.0 hex words addressed\n00: ")
      outfile.writelines(hex_program)

  # Convert the data list to hexadecimal and write it to a file
  with open("data.hex", "w") as outfile:
      outfile.write("v3.0 hex words addressed\n00: ")
      outfile.writelines([f"{d:04x} " for d in data_list])
