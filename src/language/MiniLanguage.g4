grammar MiniLanguage;

program: statement* EOF;

statement: assignment
         | loop
         | conditional
         | block
         | input
         | output;

// Zmienna, bez jawnej deklaracji
assignment: VAR_ID '<-' expression ';';

// Instrukcja pętli
loop: 'while' '(' condition ')' block ';';

// Instrukcja warunkowa
conditional: 'if' '(' condition ')' block ('else' block)? ';';

// Instrukcja złożona
block: '{' statement* '}';

// Operacje wejścia/wyjścia
input: id '<-' 'input' ';';

output: 'output' '<-' expression ';';

expression: logicExpression
          | numericalExpression;

condition: logicExpression;

logicExpression: logicTerm ('and' logicTerm)*;

logicTerm: logicFactor ('or' logicFactor)*;

logicFactor: BOOL
           | id
           | 'not' logicFactor
           | '(' logicExpression ')'
           | relationalExpression;

relationalExpression: numericalExpression ( ('==' | '!=' | '<' | '>' | '<=' | '>=') numericalExpression );

numericalExpression: term (( '+' | '-' ) term)*;

term: factor (( '*' | '/' ) factor)*;

factor: id
      | INT
      | FLOAT
      | '(' numericalExpression ')'
      | '-' factor;

id: VAR_ID;

VAR_ID: 'VAR_' [0-9]+;

// Literały
BOOL: 'True' | 'False';

INT: ('-'?)[0-9]+;

FLOAT: ('-'?)[0-9]+ '.' [0-9]+;

// np.
// 1.5 => 1 <=> True
// 0 <=> False

WS: [ \t\r\n]+ -> skip;