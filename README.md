# Custom MIPS Assembler

A MIPS assembler that translates `.asm` files into `.hex` machine code for a custom processor.

Demonstrates parsing, instruction encoding, symbol resolution, and output generation; hardware access is not required.

## Technical Focus

- Parsing, lexing, and tokenization of MIPS assembly
- Symbol table management and label resolution
- Instruction encoding into `.hex` format
- Input validation and error handling
- Modular design for future instruction set extensions

## Constraints & Limitations

- Targets a custom processor; physical hardware not required
- Only a subset of instructions is supported, scoped specifically for this project
- Testing is done via provided `.asm` files and expected `.hex` output
- Design prioritizes correctness and clarity, with future extensibility considered

## Example Usage

1. Clone repository:

```bash
git clone https://github.com/SearParsley/mips-assembler.git
cd mips-assembler
```

2. Assemble a file:

```bash
python assembler.py tests/task1_test1.asm
```

3. Output:

`output.hex`:

```bash
v3.0 hex words addressed
00: 5040 508a 3282 5241 4002
```

> Reviewers can inspect `output.hex` and `data.hex` to verify the assembler logic without needing the processor.
