from lexer import Lexer
from bobparser import Parser
from codegen import CodeGen


fname = "input.bob"
with open(fname) as f:
    text_input = f.read

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()
module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_file("output.ll")