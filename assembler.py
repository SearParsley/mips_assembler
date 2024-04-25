COMMENT_CHAR = '#'
INPUT_FILE = 'task4_test2.asm'

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




# Encode the program into a list of binary strings
def encode_instruction(line_num:int, instruction:str, label_table:dict, data_table:dict):

  # if DEBUG: print(f'{instruction}: ', end=None)

  match instruction.split(' ', 1):
    case ['add', args]:
      args_list = strip_args(args)

      rd = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      rt = register_to_binary(args_list[2])
      
      opcode = '0000'

      funct = '010'

      output = opcode + rs + rt + rd + funct

      if DEBUG: print(f'{opcode} {rs} {rt} {rd} {funct}')

    case ['sub', args]:
      args_list = strip_args(args)

      rd = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      rt = register_to_binary(args_list[2])
      
      opcode = '0000'

      funct = '110'

      output = opcode + rs + rt + rd + funct

      if DEBUG: print(f'{opcode} {rs} {rt} {rd} {funct}')
      
    case ['and', args]:
      args_list = strip_args(args)

      rd = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      rt = register_to_binary(args_list[2])
      
      opcode = '0000'

      funct = '000'

      output = opcode + rs + rt + rd + funct

      if DEBUG: print(f'{opcode} {rs} {rt} {rd} {funct}')

    case ['or', args]:
      args_list = strip_args(args)

      rd = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      rt = register_to_binary(args_list[2])
      
      opcode = '0000'

      funct = '001'

      output = opcode + rs + rt + rd + funct

      if DEBUG: print(f'{opcode} {rs} {rt} {rd} {funct}')

    case ['slt', args]:
      args_list = strip_args(args)

      rd = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      rt = register_to_binary(args_list[2])
      
      opcode = '0000'

      funct = '111'

      output = opcode + rs + rt + rd + funct

      if DEBUG: print(f'{opcode} {rs} {rt} {rd} {funct}')

    case ['addi', args]:
      args_list = strip_args(args)

      rt = register_to_binary(args_list[0])
      rs = register_to_binary(args_list[1])
      imm = decimal_to_binary(int(args_list[2]), 6)
      
      opcode = '0101'

      output = opcode + rs + rt + imm

      if DEBUG: print(f'{opcode} {rs} {rt} {imm}')

    case ['beq', args]:
      args_list = strip_args(args)

      rs = register_to_binary(args_list[0])
      rt = register_to_binary(args_list[1])
      label = args_list[2]

      label_num = label_table[label]

      label_location = decimal_to_binary(label_num - line_num - 1, 6)
      
      opcode = '0011'

      output = opcode + rs + rt + label_location

      if DEBUG: print(f'{opcode} {rs} {rt} {label_location}')

    case ['bne', args]:
      args_list = strip_args(args)

      rs = register_to_binary(args_list[0])
      rt = register_to_binary(args_list[1])
      label = args_list[2]

      label_num = label_table[label]

      label_location = decimal_to_binary(label_num - line_num - 1, 6)
      
      opcode = '0110'

      output = opcode + rs + rt + label_location

      if DEBUG: print(f'{opcode} {rs} {rt} {label_location}')

    case ['lw', args]:
      args_list = strip_args(args, 2)

      rt = register_to_binary(args_list[0])

      opcode = '0001'

      if len(args_list) == 2:
        data = decimal_to_binary(data_table[args_list[1]], 6)
        output = opcode + '000' + rt + data

        if DEBUG: print(f'{opcode} 000 {rt} {data}')

      else:
        imm = decimal_to_binary(int(args_list[1]), 6)
        rs = register_to_binary(args_list[2])
        output = opcode + rs + rt + imm

        if DEBUG: print(f'{opcode} {rs} {rt} {imm}')


    case ['sw', args]:
      args_list = strip_args(args, 2)

      rt = register_to_binary(args_list[0])

      opcode = '0010'

      if len(args_list) == 2:
        data = decimal_to_binary(data_table[args_list[1]], 6)
        output = opcode + '000' + rt + data

        if DEBUG: print(f'{opcode} 000 {rt} {data}')

      else:
        imm = decimal_to_binary(int(args_list[1]), 6)
        rs = register_to_binary(args_list[2])
        output = opcode + rs + rt + imm
        
        if DEBUG: print(f'{opcode} {rs} {rt} {imm}')

    case ['j', args]:
      args_list = strip_args(args)

      label = args_list[0]

      label_location = decimal_to_binary(label_table[label], 12)
      
      opcode = '0100'

      output = opcode + label_location

      if DEBUG: print(f'{opcode} {label_location}')

    case ['jr', args]:
      args_list = strip_args(args)

      rs = register_to_binary(args_list[0])
      
      opcode = '0111'

      output = opcode + rs + '000000000'

      if DEBUG: print(f'{opcode} {rs} 000 000 000')

    case ['jal', args]:
      args_list = strip_args(args)

      label = args_list[0]

      label_location = decimal_to_binary(label_table[label], 12)
      
      opcode = '1000'

      output = opcode + label_location

      if DEBUG: print(f'{opcode} {label_location}')

    case _:
      raise Exception('Invalid instruction given')
  
  return output



def strip_args(args:str, instruction_type:int=1):
  output = []

  if instruction_type == 1 :

    args_list = args.split(',')
    for i in range(len(args_list)):
      output.append(args_list[i].strip())
  
  elif instruction_type == 2 :

    args_list = args.split(',')
    output.append(args_list[0].strip())
    temp = args_list[1].split('(')
    output.append(temp[0].strip())
    if len(temp) == 2:
      output.append(temp[1].strip('() '))
  
  return output




def encode_program(lines_list:list, label_table:dict, data_table:dict):
  encoded_lines_list = []
  for i in range(len(lines_list)):
    encoded_lines_list.append(encode_instruction(i, lines_list[i], label_table, data_table))
  return encoded_lines_list



def register_to_binary(reg:str):
  num = int(reg[1])
  if reg[0] != 'R' or num > 7: raise Exception('Incorrect register string')
  output = f'{num:03b}'
  return output




def decimal_to_binary(num:int, length:int=16):
  output = f"{(1 << length) + num:0{length}b}" if num < 0 else f"{num:0{length}b}"
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