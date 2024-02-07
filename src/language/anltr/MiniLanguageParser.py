# Generated from MiniLanguage.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,161,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,72,8,4,1,4,1,4,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,3,8,97,8,8,1,9,1,9,1,
        10,1,10,1,10,5,10,104,8,10,10,10,12,10,107,9,10,1,11,1,11,1,11,5,
        11,112,8,11,10,11,12,11,115,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,126,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,
        14,135,8,14,10,14,12,14,138,9,14,1,15,1,15,1,15,5,15,143,8,15,10,
        15,12,15,146,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,
        16,157,8,16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,0,3,1,0,15,20,1,0,21,22,1,0,23,24,163,0,39,1,0,
        0,0,2,50,1,0,0,0,4,52,1,0,0,0,6,57,1,0,0,0,8,64,1,0,0,0,10,75,1,
        0,0,0,12,84,1,0,0,0,14,89,1,0,0,0,16,96,1,0,0,0,18,98,1,0,0,0,20,
        100,1,0,0,0,22,108,1,0,0,0,24,125,1,0,0,0,26,127,1,0,0,0,28,131,
        1,0,0,0,30,139,1,0,0,0,32,156,1,0,0,0,34,158,1,0,0,0,36,38,3,2,1,
        0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,
        1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,51,3,4,2,0,45,
        51,3,6,3,0,46,51,3,8,4,0,47,51,3,10,5,0,48,51,3,12,6,0,49,51,3,14,
        7,0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,
        1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,53,5,25,0,0,53,54,5,1,0,0,
        54,55,3,16,8,0,55,56,5,2,0,0,56,5,1,0,0,0,57,58,5,3,0,0,58,59,5,
        4,0,0,59,60,3,18,9,0,60,61,5,5,0,0,61,62,3,10,5,0,62,63,5,2,0,0,
        63,7,1,0,0,0,64,65,5,6,0,0,65,66,5,4,0,0,66,67,3,18,9,0,67,68,5,
        5,0,0,68,71,3,10,5,0,69,70,5,7,0,0,70,72,3,10,5,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,2,0,0,74,9,1,0,0,0,75,79,5,8,
        0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,
        1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,9,0,0,83,11,1,0,0,0,
        84,85,3,34,17,0,85,86,5,1,0,0,86,87,5,10,0,0,87,88,5,2,0,0,88,13,
        1,0,0,0,89,90,5,11,0,0,90,91,5,1,0,0,91,92,3,16,8,0,92,93,5,2,0,
        0,93,15,1,0,0,0,94,97,3,20,10,0,95,97,3,28,14,0,96,94,1,0,0,0,96,
        95,1,0,0,0,97,17,1,0,0,0,98,99,3,20,10,0,99,19,1,0,0,0,100,105,3,
        22,11,0,101,102,5,12,0,0,102,104,3,22,11,0,103,101,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,21,1,0,0,0,107,105,1,
        0,0,0,108,113,3,24,12,0,109,110,5,13,0,0,110,112,3,24,12,0,111,109,
        1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,23,1,
        0,0,0,115,113,1,0,0,0,116,126,5,26,0,0,117,126,3,34,17,0,118,119,
        5,14,0,0,119,126,3,24,12,0,120,121,5,4,0,0,121,122,3,20,10,0,122,
        123,5,5,0,0,123,126,1,0,0,0,124,126,3,26,13,0,125,116,1,0,0,0,125,
        117,1,0,0,0,125,118,1,0,0,0,125,120,1,0,0,0,125,124,1,0,0,0,126,
        25,1,0,0,0,127,128,3,28,14,0,128,129,7,0,0,0,129,130,3,28,14,0,130,
        27,1,0,0,0,131,136,3,30,15,0,132,133,7,1,0,0,133,135,3,30,15,0,134,
        132,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,
        29,1,0,0,0,138,136,1,0,0,0,139,144,3,32,16,0,140,141,7,2,0,0,141,
        143,3,32,16,0,142,140,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,
        145,1,0,0,0,145,31,1,0,0,0,146,144,1,0,0,0,147,157,3,34,17,0,148,
        157,5,27,0,0,149,157,5,28,0,0,150,151,5,4,0,0,151,152,3,28,14,0,
        152,153,5,5,0,0,153,157,1,0,0,0,154,155,5,22,0,0,155,157,3,32,16,
        0,156,147,1,0,0,0,156,148,1,0,0,0,156,149,1,0,0,0,156,150,1,0,0,
        0,156,154,1,0,0,0,157,33,1,0,0,0,158,159,5,25,0,0,159,35,1,0,0,0,
        11,39,50,71,79,96,105,113,125,136,144,156
    ]

class MiniLanguageParser ( Parser ):

    grammarFileName = "MiniLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "';'", "'while'", "'('", "')'", 
                     "'if'", "'else'", "'{'", "'}'", "'input'", "'output'", 
                     "'and'", "'or'", "'not'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR_ID", "BOOL", "INT", "FLOAT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_loop = 3
    RULE_conditional = 4
    RULE_block = 5
    RULE_input = 6
    RULE_output = 7
    RULE_expression = 8
    RULE_condition = 9
    RULE_logicExpression = 10
    RULE_logicTerm = 11
    RULE_logicFactor = 12
    RULE_relationalExpression = 13
    RULE_numericalExpression = 14
    RULE_term = 15
    RULE_factor = 16
    RULE_id = 17

    ruleNames =  [ "program", "statement", "assignment", "loop", "conditional", 
                   "block", "input", "output", "expression", "condition", 
                   "logicExpression", "logicTerm", "logicFactor", "relationalExpression", 
                   "numericalExpression", "term", "factor", "id" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    VAR_ID=25
    BOOL=26
    INT=27
    FLOAT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniLanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33556808) != 0):
                self.state = 36
                self.statement()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(MiniLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MiniLanguageParser.AssignmentContext,0)


        def loop(self):
            return self.getTypedRuleContext(MiniLanguageParser.LoopContext,0)


        def conditional(self):
            return self.getTypedRuleContext(MiniLanguageParser.ConditionalContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLanguageParser.BlockContext,0)


        def input_(self):
            return self.getTypedRuleContext(MiniLanguageParser.InputContext,0)


        def output(self):
            return self.getTypedRuleContext(MiniLanguageParser.OutputContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.loop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.conditional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.input_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.output()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_ID(self):
            return self.getToken(MiniLanguageParser.VAR_ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniLanguageParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MiniLanguageParser.VAR_ID)
            self.state = 53
            self.match(MiniLanguageParser.T__0)
            self.state = 54
            self.expression()
            self.state = 55
            self.match(MiniLanguageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MiniLanguageParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLanguageParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MiniLanguageParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiniLanguageParser.T__2)
            self.state = 58
            self.match(MiniLanguageParser.T__3)
            self.state = 59
            self.condition()
            self.state = 60
            self.match(MiniLanguageParser.T__4)
            self.state = 61
            self.block()
            self.state = 62
            self.match(MiniLanguageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MiniLanguageParser.ConditionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.BlockContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = MiniLanguageParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniLanguageParser.T__5)
            self.state = 65
            self.match(MiniLanguageParser.T__3)
            self.state = 66
            self.condition()
            self.state = 67
            self.match(MiniLanguageParser.T__4)
            self.state = 68
            self.block()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 69
                self.match(MiniLanguageParser.T__6)
                self.state = 70
                self.block()


            self.state = 73
            self.match(MiniLanguageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MiniLanguageParser.T__7)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33556808) != 0):
                self.state = 76
                self.statement()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(MiniLanguageParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = MiniLanguageParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.id_()
            self.state = 85
            self.match(MiniLanguageParser.T__0)
            self.state = 86
            self.match(MiniLanguageParser.T__9)
            self.state = 87
            self.match(MiniLanguageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = MiniLanguageParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MiniLanguageParser.T__10)
            self.state = 90
            self.match(MiniLanguageParser.T__0)
            self.state = 91
            self.expression()
            self.state = 92
            self.match(MiniLanguageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.LogicExpressionContext,0)


        def numericalExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.NumericalExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniLanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.logicExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.numericalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.LogicExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniLanguageParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.logicExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.LogicTermContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.LogicTermContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_logicExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpression" ):
                listener.enterLogicExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpression" ):
                listener.exitLogicExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpression" ):
                return visitor.visitLogicExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicExpression(self):

        localctx = MiniLanguageParser.LogicExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.logicTerm()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 101
                self.match(MiniLanguageParser.T__11)
                self.state = 102
                self.logicTerm()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.LogicFactorContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.LogicFactorContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_logicTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicTerm" ):
                listener.enterLogicTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicTerm" ):
                listener.exitLogicTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicTerm" ):
                return visitor.visitLogicTerm(self)
            else:
                return visitor.visitChildren(self)




    def logicTerm(self):

        localctx = MiniLanguageParser.LogicTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logicTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.logicFactor()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 109
                self.match(MiniLanguageParser.T__12)
                self.state = 110
                self.logicFactor()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(MiniLanguageParser.BOOL, 0)

        def id_(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdContext,0)


        def logicFactor(self):
            return self.getTypedRuleContext(MiniLanguageParser.LogicFactorContext,0)


        def logicExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.LogicExpressionContext,0)


        def relationalExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.RelationalExpressionContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_logicFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicFactor" ):
                listener.enterLogicFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicFactor" ):
                listener.exitLogicFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicFactor" ):
                return visitor.visitLogicFactor(self)
            else:
                return visitor.visitChildren(self)




    def logicFactor(self):

        localctx = MiniLanguageParser.LogicFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicFactor)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(MiniLanguageParser.BOOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(MiniLanguageParser.T__13)
                self.state = 119
                self.logicFactor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.match(MiniLanguageParser.T__3)
                self.state = 121
                self.logicExpression()
                self.state = 122
                self.match(MiniLanguageParser.T__4)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.relationalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.NumericalExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.NumericalExpressionContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = MiniLanguageParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.numericalExpression()

            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 129
            self.numericalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.TermContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.TermContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_numericalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericalExpression" ):
                listener.enterNumericalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericalExpression" ):
                listener.exitNumericalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericalExpression" ):
                return visitor.visitNumericalExpression(self)
            else:
                return visitor.visitChildren(self)




    def numericalExpression(self):

        localctx = MiniLanguageParser.NumericalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_numericalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.term()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.term()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLanguageParser.FactorContext)
            else:
                return self.getTypedRuleContext(MiniLanguageParser.FactorContext,i)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniLanguageParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.factor()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 140
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self.factor()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(MiniLanguageParser.IdContext,0)


        def INT(self):
            return self.getToken(MiniLanguageParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniLanguageParser.FLOAT, 0)

        def numericalExpression(self):
            return self.getTypedRuleContext(MiniLanguageParser.NumericalExpressionContext,0)


        def factor(self):
            return self.getTypedRuleContext(MiniLanguageParser.FactorContext,0)


        def getRuleIndex(self):
            return MiniLanguageParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MiniLanguageParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_factor)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.id_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(MiniLanguageParser.INT)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.match(MiniLanguageParser.FLOAT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.match(MiniLanguageParser.T__3)
                self.state = 151
                self.numericalExpression()
                self.state = 152
                self.match(MiniLanguageParser.T__4)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.match(MiniLanguageParser.T__21)
                self.state = 155
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_ID(self):
            return self.getToken(MiniLanguageParser.VAR_ID, 0)

        def getRuleIndex(self):
            return MiniLanguageParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = MiniLanguageParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MiniLanguageParser.VAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





