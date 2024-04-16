COMMENT_CHAR = '#'
INPUT_FILE = 'test1.asm'

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



# Build a label table and strip out the labels from the code
def create_label_table(lines:list):

  label_table = {}
  instruction_list = []

  instruction_count = 0
  for line in lines:
    if line.endswith(':'): label_table.update({line[:-1]: instruction_count})
    else:
      instruction_list.append(line)
      instruction_count += 1

  if DEBUG:
    print(label_table)
    print(instruction_list)

  return label_table, instruction_list




# TODO: write encoding function
# Encode the program into a list of binary strings
def encode_instruction(line_num:int, instruction:str, label_table:dict, data_table:dict):
  
  format = ''
  
  opcode = '0000'




  match instruction.split('', 1):
    case ['add', args]:
      args_list = strip_args(args, 1)

      rd = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      rt = register_to_binary(args_list[2])
      
      opcode = '0000'

      funct = '010'

      output = opcode + rs + rt + rd + funct

    case ['sub', args]:
      pass
    case ['and', args]:
      pass
    case ['or', args]:
      pass
    case ['slt', args]:
      pass
    case ['addi', args]:
      pass
    case ['beq', args]:
      pass
    case ['bne', args]:
      pass
    case ['lw', args]:
      pass
    case ['sw', args]:
      pass
    case ['j', args]:
      pass
    case ['jr', args]:
      pass
    case ['jal', args]:
      pass
    case _:
      raise Exception('Invalid instruction given')
  
  return output



def strip_args(args:str, instruction_type:int):
  output = []
  if instruction_type == 1 :

    args_list = args.split(',')
    for i in range(len(args_list)):
      output.append(args_list[i].strip())

    return args_list
  
  elif instruction_type == 2 :

    args_list = args.split(',')
    args_list[0] = args_list[0].strip()
    output.append(args_list[0])

    temp = args_list[1]

    return args_list
  
  return []




def encode_program(lines_list:list, label_table:dict, data_table:dict):
  encoded_lines_list = []
  for i in range(len(lines_list)):
    encoded_lines_list.append(encode_instruction(i, lines_list[i], label_table, data_table))




def register_to_binary(reg:str):
  num = int(reg[1])
  if reg[0] != 'R' or num > 7: raise Exception('Incorrect register string')
  output = f'{reg[1]:03b}'
  return output




def decimal_to_binary(num:int):
  output = f"{(1 << 16) + num:016b}" if num < 0 else f"{num:016b}"
  return output




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

  label_table, lines = create_label_table(lines)

  encoded_program = encode_program(lines, label_table, data_table)

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