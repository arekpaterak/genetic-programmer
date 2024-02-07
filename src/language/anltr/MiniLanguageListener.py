# Generated from MiniLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLanguageParser import MiniLanguageParser
else:
    from MiniLanguageParser import MiniLanguageParser

# This class defines a complete listener for a parse tree produced by MiniLanguageParser.
class MiniLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLanguageParser#program.
    def enterProgram(self, ctx:MiniLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#program.
    def exitProgram(self, ctx:MiniLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#statement.
    def enterStatement(self, ctx:MiniLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#statement.
    def exitStatement(self, ctx:MiniLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#assignment.
    def enterAssignment(self, ctx:MiniLanguageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#assignment.
    def exitAssignment(self, ctx:MiniLanguageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#loop.
    def enterLoop(self, ctx:MiniLanguageParser.LoopContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#loop.
    def exitLoop(self, ctx:MiniLanguageParser.LoopContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#conditional.
    def enterConditional(self, ctx:MiniLanguageParser.ConditionalContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#conditional.
    def exitConditional(self, ctx:MiniLanguageParser.ConditionalContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#block.
    def enterBlock(self, ctx:MiniLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#block.
    def exitBlock(self, ctx:MiniLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#input.
    def enterInput(self, ctx:MiniLanguageParser.InputContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#input.
    def exitInput(self, ctx:MiniLanguageParser.InputContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#output.
    def enterOutput(self, ctx:MiniLanguageParser.OutputContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#output.
    def exitOutput(self, ctx:MiniLanguageParser.OutputContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#expression.
    def enterExpression(self, ctx:MiniLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#expression.
    def exitExpression(self, ctx:MiniLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#condition.
    def enterCondition(self, ctx:MiniLanguageParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#condition.
    def exitCondition(self, ctx:MiniLanguageParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#logicExpression.
    def enterLogicExpression(self, ctx:MiniLanguageParser.LogicExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#logicExpression.
    def exitLogicExpression(self, ctx:MiniLanguageParser.LogicExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#logicTerm.
    def enterLogicTerm(self, ctx:MiniLanguageParser.LogicTermContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#logicTerm.
    def exitLogicTerm(self, ctx:MiniLanguageParser.LogicTermContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#logicFactor.
    def enterLogicFactor(self, ctx:MiniLanguageParser.LogicFactorContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#logicFactor.
    def exitLogicFactor(self, ctx:MiniLanguageParser.LogicFactorContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MiniLanguageParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MiniLanguageParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#numericalExpression.
    def enterNumericalExpression(self, ctx:MiniLanguageParser.NumericalExpressionContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#numericalExpression.
    def exitNumericalExpression(self, ctx:MiniLanguageParser.NumericalExpressionContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#term.
    def enterTerm(self, ctx:MiniLanguageParser.TermContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#term.
    def exitTerm(self, ctx:MiniLanguageParser.TermContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#factor.
    def enterFactor(self, ctx:MiniLanguageParser.FactorContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#factor.
    def exitFactor(self, ctx:MiniLanguageParser.FactorContext):
        pass


    # Enter a parse tree produced by MiniLanguageParser#id.
    def enterId(self, ctx:MiniLanguageParser.IdContext):
        pass

    # Exit a parse tree produced by MiniLanguageParser#id.
    def exitId(self, ctx:MiniLanguageParser.IdContext):
        pass



del MiniLanguageParser