
README: Ruby Parser using Lex and Yacc (Python Tools)

Overview
This project implements a Ruby parser using Lex and Yacc, which are tools commonly used for lexical analysis and parsing in programming languages. The parser is capable of parsing various constructs in the Ruby language, including while loops, do-while loops, comments, function definitions, and for loops.

Features
Lexical Analysis: The parser performs lexical analysis to tokenize input Ruby code into meaningful elements such as identifiers, keywords, operators, and literals.
Syntax Parsing: Using Yacc, the parser constructs a syntax tree based on the grammar rules of Ruby, allowing it to understand the structure and hierarchy of statements and expressions.
Supported Constructs:
while loops: Handles while loops along with their corresponding conditions and code blocks.
do-while loops: Supports do-while loops, ensuring proper parsing of the loop body and condition.
Comments: Recognizes and ignores comments in Ruby code, ensuring they do not affect parsing.
Function Definitions: Parses function definitions including parameters, return types, and function bodies.
for loops: Handles for loops with iterable objects and loop bodies.
