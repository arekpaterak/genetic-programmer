# Generated from MiniLanguage.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .MiniLanguageParser import MiniLanguageParser
else:
    from MiniLanguageParser import MiniLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MiniLanguageParser.


class MiniLanguageVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by MiniLanguageParser#program.
    def visitProgram(self, ctx: MiniLanguageParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#statement.
    def visitStatement(self, ctx: MiniLanguageParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#assignment.
    def visitAssignment(self, ctx: MiniLanguageParser.AssignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#loop.
    def visitLoop(self, ctx: MiniLanguageParser.LoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#conditional.
    def visitConditional(self, ctx: MiniLanguageParser.ConditionalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#block.
    def visitBlock(self, ctx: MiniLanguageParser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#input.
    def visitInput(self, ctx: MiniLanguageParser.InputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#output.
    def visitOutput(self, ctx: MiniLanguageParser.OutputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#expression.
    def visitExpression(self, ctx: MiniLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#condition.
    def visitCondition(self, ctx: MiniLanguageParser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#logicExpression.
    def visitLogicExpression(self, ctx: MiniLanguageParser.LogicExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#logicTerm.
    def visitLogicTerm(self, ctx: MiniLanguageParser.LogicTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#logicFactor.
    def visitLogicFactor(self, ctx: MiniLanguageParser.LogicFactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#relationalExpression.
    def visitRelationalExpression(
        self, ctx: MiniLanguageParser.RelationalExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#numericalExpression.
    def visitNumericalExpression(
        self, ctx: MiniLanguageParser.NumericalExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#term.
    def visitTerm(self, ctx: MiniLanguageParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#factor.
    def visitFactor(self, ctx: MiniLanguageParser.FactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniLanguageParser#id.
    def visitId(self, ctx: MiniLanguageParser.IdContext):
        return self.visitChildren(ctx)


del MiniLanguageParser
