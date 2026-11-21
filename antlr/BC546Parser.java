// Generated from c:/Users/ml246/OneDrive/Desktop/CC/analisador_lexico/BC546Parser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BC546Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PV=1, PA=2, PF=3, CHA=4, CHF=5, V=6, AND=7, OR=8, NOT=9, IGUAL=10, DIF=11, 
		MAIORIG=12, MENORIG=13, MAIOR=14, MENOR=15, ATRIB=16, ADD_OP=17, SUB_OP=18, 
		MULT_OP=19, DIV_OP=20, MOD_OP=21, T_NUM=22, T_STR=23, T_BOOL=24, VOID=25, 
		NULL=26, TRUE=27, FALSE=28, PRINT=29, WHILE=30, IF=31, INPUT=32, RETURN=33, 
		FUNC=34, INT=35, TEXT=36, ID=37, WS=38;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_bloco = 2, RULE_print = 3, 
		RULE_input = 4, RULE_tipo = 5, RULE_tipoRet = 6, RULE_varDecl = 7, RULE_atrib = 8, 
		RULE_funcDecl = 9, RULE_params = 10, RULE_param = 11, RULE_return = 12, 
		RULE_if = 13, RULE_while = 14, RULE_expr = 15, RULE_exprOr = 16, RULE_exprAnd = 17, 
		RULE_exprNot = 18, RULE_exprRel = 19, RULE_exprArt = 20, RULE_termo = 21, 
		RULE_chFun = 22, RULE_fator = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "bloco", "print", "input", "tipo", "tipoRet", 
			"varDecl", "atrib", "funcDecl", "params", "param", "return", "if", "while", 
			"expr", "exprOr", "exprAnd", "exprNot", "exprRel", "exprArt", "termo", 
			"chFun", "fator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'('", "')'", "'{'", "'}'", "','", "'and'", "'or'", "'not'", 
			"'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'='", "'+'", "'-'", "'*'", 
			"'/'", "'%'", "'num'", "'str'", "'bool'", "'void'", "'null'", "'true'", 
			"'false'", "'print'", "'while'", "'if'", "'input'", "'return'", "'func'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PV", "PA", "PF", "CHA", "CHF", "V", "AND", "OR", "NOT", "IGUAL", 
			"DIF", "MAIORIG", "MENORIG", "MAIOR", "MENOR", "ATRIB", "ADD_OP", "SUB_OP", 
			"MULT_OP", "DIV_OP", "MOD_OP", "T_NUM", "T_STR", "T_BOOL", "VOID", "NULL", 
			"TRUE", "FALSE", "PRINT", "WHILE", "IF", "INPUT", "RETURN", "FUNC", "INT", 
			"TEXT", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BC546Parser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BC546Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BC546Parser.EOF, 0); }
		public List<FuncDeclContext> funcDecl() {
			return getRuleContexts(FuncDeclContext.class);
		}
		public FuncDeclContext funcDecl(int i) {
			return getRuleContext(FuncDeclContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 253398876692L) != 0)) {
				{
				setState(50);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(48);
					funcDecl();
					}
					break;
				case 2:
					{
					setState(49);
					statement();
					}
					break;
				}
				}
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(55);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public TerminalNode PV() { return getToken(BC546Parser.PV, 0); }
		public AtribContext atrib() {
			return getRuleContext(AtribContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public ReturnContext return_() {
			return getRuleContext(ReturnContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public WhileContext while_() {
			return getRuleContext(WhileContext.class,0);
		}
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(75);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(57);
				varDecl();
				setState(58);
				match(PV);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(60);
				atrib();
				setState(61);
				match(PV);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(63);
				print();
				setState(64);
				match(PV);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(66);
				return_();
				setState(67);
				match(PV);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(69);
				expr();
				setState(70);
				match(PV);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(72);
				if_();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(73);
				while_();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(74);
				bloco();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlocoContext extends ParserRuleContext {
		public TerminalNode CHA() { return getToken(BC546Parser.CHA, 0); }
		public TerminalNode CHF() { return getToken(BC546Parser.CHF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloco; }
	}

	public final BlocoContext bloco() throws RecognitionException {
		BlocoContext _localctx = new BlocoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(CHA);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 253365322260L) != 0)) {
				{
				{
				setState(78);
				statement();
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(84);
			match(CHF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(BC546Parser.PRINT, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(PRINT);
			setState(87);
			match(PA);
			setState(88);
			expr();
			setState(89);
			match(PF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputContext extends ParserRuleContext {
		public TerminalNode INPUT() { return getToken(BC546Parser.INPUT, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public InputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input; }
	}

	public final InputContext input() throws RecognitionException {
		InputContext _localctx = new InputContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_input);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(INPUT);
			setState(92);
			match(PA);
			setState(93);
			expr();
			setState(94);
			match(PF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode T_STR() { return getToken(BC546Parser.T_STR, 0); }
		public TerminalNode T_NUM() { return getToken(BC546Parser.T_NUM, 0); }
		public TerminalNode T_BOOL() { return getToken(BC546Parser.T_BOOL, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoRetContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VOID() { return getToken(BC546Parser.VOID, 0); }
		public TipoRetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipoRet; }
	}

	public final TipoRetContext tipoRet() throws RecognitionException {
		TipoRetContext _localctx = new TipoRetContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tipoRet);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T_NUM:
			case T_STR:
			case T_BOOL:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				tipo();
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(BC546Parser.ID, 0); }
		public TerminalNode ATRIB() { return getToken(BC546Parser.ATRIB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			tipo();
			setState(103);
			match(ID);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ATRIB) {
				{
				setState(104);
				match(ATRIB);
				setState(105);
				expr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtribContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BC546Parser.ID, 0); }
		public TerminalNode ATRIB() { return getToken(BC546Parser.ATRIB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AtribContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atrib; }
	}

	public final AtribContext atrib() throws RecognitionException {
		AtribContext _localctx = new AtribContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_atrib);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(ID);
			setState(109);
			match(ATRIB);
			setState(110);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncDeclContext extends ParserRuleContext {
		public TipoRetContext tipoRet() {
			return getRuleContext(TipoRetContext.class,0);
		}
		public TerminalNode FUNC() { return getToken(BC546Parser.FUNC, 0); }
		public TerminalNode ID() { return getToken(BC546Parser.ID, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public FuncDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcDecl; }
	}

	public final FuncDeclContext funcDecl() throws RecognitionException {
		FuncDeclContext _localctx = new FuncDeclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_funcDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			tipoRet();
			setState(113);
			match(FUNC);
			setState(114);
			match(ID);
			setState(115);
			match(PA);
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) {
				{
				setState(116);
				params();
				}
			}

			setState(119);
			match(PF);
			setState(120);
			bloco();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> V() { return getTokens(BC546Parser.V); }
		public TerminalNode V(int i) {
			return getToken(BC546Parser.V, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			param();
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==V) {
				{
				{
				setState(123);
				match(V);
				setState(124);
				param();
				}
				}
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(BC546Parser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			tipo();
			setState(131);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BC546Parser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return; }
	}

	public final ReturnContext return_() throws RecognitionException {
		ReturnContext _localctx = new ReturnContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_return);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			match(RETURN);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 240987931140L) != 0)) {
				{
				setState(134);
				expr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BC546Parser.IF, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(IF);
			setState(138);
			match(PA);
			setState(139);
			expr();
			setState(140);
			match(PF);
			setState(141);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BC546Parser.WHILE, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while; }
	}

	public final WhileContext while_() throws RecognitionException {
		WhileContext _localctx = new WhileContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(WHILE);
			setState(144);
			match(PA);
			setState(145);
			expr();
			setState(146);
			match(PF);
			setState(147);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprOrContext exprOr() {
			return getRuleContext(ExprOrContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			exprOr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprOrContext extends ParserRuleContext {
		public List<ExprAndContext> exprAnd() {
			return getRuleContexts(ExprAndContext.class);
		}
		public ExprAndContext exprAnd(int i) {
			return getRuleContext(ExprAndContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(BC546Parser.OR); }
		public TerminalNode OR(int i) {
			return getToken(BC546Parser.OR, i);
		}
		public ExprOrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprOr; }
	}

	public final ExprOrContext exprOr() throws RecognitionException {
		ExprOrContext _localctx = new ExprOrContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_exprOr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			exprAnd();
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(152);
				match(OR);
				setState(153);
				exprAnd();
				}
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprAndContext extends ParserRuleContext {
		public List<ExprNotContext> exprNot() {
			return getRuleContexts(ExprNotContext.class);
		}
		public ExprNotContext exprNot(int i) {
			return getRuleContext(ExprNotContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(BC546Parser.AND); }
		public TerminalNode AND(int i) {
			return getToken(BC546Parser.AND, i);
		}
		public ExprAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprAnd; }
	}

	public final ExprAndContext exprAnd() throws RecognitionException {
		ExprAndContext _localctx = new ExprAndContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_exprAnd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			exprNot();
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(160);
				match(AND);
				setState(161);
				exprNot();
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprNotContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(BC546Parser.NOT, 0); }
		public ExprNotContext exprNot() {
			return getRuleContext(ExprNotContext.class,0);
		}
		public ExprRelContext exprRel() {
			return getRuleContext(ExprRelContext.class,0);
		}
		public ExprNotContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprNot; }
	}

	public final ExprNotContext exprNot() throws RecognitionException {
		ExprNotContext _localctx = new ExprNotContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_exprNot);
		try {
			setState(170);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(NOT);
				setState(168);
				exprNot();
				}
				break;
			case PA:
			case NULL:
			case TRUE:
			case FALSE:
			case INT:
			case TEXT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(169);
				exprRel();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprRelContext extends ParserRuleContext {
		public List<ExprArtContext> exprArt() {
			return getRuleContexts(ExprArtContext.class);
		}
		public ExprArtContext exprArt(int i) {
			return getRuleContext(ExprArtContext.class,i);
		}
		public TerminalNode IGUAL() { return getToken(BC546Parser.IGUAL, 0); }
		public TerminalNode DIF() { return getToken(BC546Parser.DIF, 0); }
		public TerminalNode MAIORIG() { return getToken(BC546Parser.MAIORIG, 0); }
		public TerminalNode MENORIG() { return getToken(BC546Parser.MENORIG, 0); }
		public TerminalNode MENOR() { return getToken(BC546Parser.MENOR, 0); }
		public TerminalNode MAIOR() { return getToken(BC546Parser.MAIOR, 0); }
		public ExprRelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprRel; }
	}

	public final ExprRelContext exprRel() throws RecognitionException {
		ExprRelContext _localctx = new ExprRelContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_exprRel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			exprArt();
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 64512L) != 0)) {
				{
				setState(173);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 64512L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(174);
				exprArt();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprArtContext extends ParserRuleContext {
		public List<TermoContext> termo() {
			return getRuleContexts(TermoContext.class);
		}
		public TermoContext termo(int i) {
			return getRuleContext(TermoContext.class,i);
		}
		public List<TerminalNode> ADD_OP() { return getTokens(BC546Parser.ADD_OP); }
		public TerminalNode ADD_OP(int i) {
			return getToken(BC546Parser.ADD_OP, i);
		}
		public List<TerminalNode> SUB_OP() { return getTokens(BC546Parser.SUB_OP); }
		public TerminalNode SUB_OP(int i) {
			return getToken(BC546Parser.SUB_OP, i);
		}
		public ExprArtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprArt; }
	}

	public final ExprArtContext exprArt() throws RecognitionException {
		ExprArtContext _localctx = new ExprArtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_exprArt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			termo();
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ADD_OP || _la==SUB_OP) {
				{
				{
				setState(178);
				_la = _input.LA(1);
				if ( !(_la==ADD_OP || _la==SUB_OP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(179);
				termo();
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermoContext extends ParserRuleContext {
		public List<FatorContext> fator() {
			return getRuleContexts(FatorContext.class);
		}
		public FatorContext fator(int i) {
			return getRuleContext(FatorContext.class,i);
		}
		public List<TerminalNode> MULT_OP() { return getTokens(BC546Parser.MULT_OP); }
		public TerminalNode MULT_OP(int i) {
			return getToken(BC546Parser.MULT_OP, i);
		}
		public List<TerminalNode> DIV_OP() { return getTokens(BC546Parser.DIV_OP); }
		public TerminalNode DIV_OP(int i) {
			return getToken(BC546Parser.DIV_OP, i);
		}
		public List<TerminalNode> MOD_OP() { return getTokens(BC546Parser.MOD_OP); }
		public TerminalNode MOD_OP(int i) {
			return getToken(BC546Parser.MOD_OP, i);
		}
		public TermoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo; }
	}

	public final TermoContext termo() throws RecognitionException {
		TermoContext _localctx = new TermoContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_termo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			fator();
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) {
				{
				{
				setState(186);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(187);
				fator();
				}
				}
				setState(192);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChFunContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BC546Parser.ID, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> V() { return getTokens(BC546Parser.V); }
		public TerminalNode V(int i) {
			return getToken(BC546Parser.V, i);
		}
		public ChFunContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chFun; }
	}

	public final ChFunContext chFun() throws RecognitionException {
		ChFunContext _localctx = new ChFunContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_chFun);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(ID);
			setState(194);
			match(PA);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 240987931140L) != 0)) {
				{
				setState(195);
				expr();
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==V) {
					{
					{
					setState(196);
					match(V);
					setState(197);
					expr();
					}
					}
					setState(202);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(205);
			match(PF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FatorContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BC546Parser.INT, 0); }
		public TerminalNode TEXT() { return getToken(BC546Parser.TEXT, 0); }
		public TerminalNode TRUE() { return getToken(BC546Parser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(BC546Parser.FALSE, 0); }
		public TerminalNode NULL() { return getToken(BC546Parser.NULL, 0); }
		public ChFunContext chFun() {
			return getRuleContext(ChFunContext.class,0);
		}
		public TerminalNode ID() { return getToken(BC546Parser.ID, 0); }
		public TerminalNode PA() { return getToken(BC546Parser.PA, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PF() { return getToken(BC546Parser.PF, 0); }
		public FatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator; }
	}

	public final FatorContext fator() throws RecognitionException {
		FatorContext _localctx = new FatorContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_fator);
		try {
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(207);
				match(INT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(208);
				match(TEXT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(209);
				match(TRUE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(210);
				match(FALSE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(211);
				match(NULL);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(212);
				chFun();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(213);
				match(ID);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(214);
				match(PA);
				setState(215);
				expr();
				setState(216);
				match(PF);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u00dd\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0005\u00003\b\u0000\n\u0000\f\u00006\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001L\b\u0001\u0001\u0002\u0001\u0002\u0005\u0002P\b\u0002\n\u0002"+
		"\f\u0002S\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0003"+
		"\u0006e\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007k\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\tv\b\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0005\n~\b\n\n\n\f\n\u0081\t\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0003\f\u0088\b\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0005\u0010\u009b\b\u0010\n\u0010\f\u0010\u009e\t\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0005\u0011\u00a3\b\u0011\n\u0011\f\u0011\u00a6"+
		"\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00ab\b\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00b0\b\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0005\u0014\u00b5\b\u0014\n\u0014\f\u0014\u00b8"+
		"\t\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0005\u0015\u00bd\b\u0015"+
		"\n\u0015\f\u0015\u00c0\t\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0005\u0016\u00c7\b\u0016\n\u0016\f\u0016\u00ca\t\u0016"+
		"\u0003\u0016\u00cc\b\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00db\b\u0017\u0001\u0017"+
		"\u0000\u0000\u0018\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.\u0000\u0004\u0001\u0000\u0016"+
		"\u0018\u0001\u0000\n\u000f\u0001\u0000\u0011\u0012\u0001\u0000\u0013\u0015"+
		"\u00e2\u00004\u0001\u0000\u0000\u0000\u0002K\u0001\u0000\u0000\u0000\u0004"+
		"M\u0001\u0000\u0000\u0000\u0006V\u0001\u0000\u0000\u0000\b[\u0001\u0000"+
		"\u0000\u0000\n`\u0001\u0000\u0000\u0000\fd\u0001\u0000\u0000\u0000\u000e"+
		"f\u0001\u0000\u0000\u0000\u0010l\u0001\u0000\u0000\u0000\u0012p\u0001"+
		"\u0000\u0000\u0000\u0014z\u0001\u0000\u0000\u0000\u0016\u0082\u0001\u0000"+
		"\u0000\u0000\u0018\u0085\u0001\u0000\u0000\u0000\u001a\u0089\u0001\u0000"+
		"\u0000\u0000\u001c\u008f\u0001\u0000\u0000\u0000\u001e\u0095\u0001\u0000"+
		"\u0000\u0000 \u0097\u0001\u0000\u0000\u0000\"\u009f\u0001\u0000\u0000"+
		"\u0000$\u00aa\u0001\u0000\u0000\u0000&\u00ac\u0001\u0000\u0000\u0000("+
		"\u00b1\u0001\u0000\u0000\u0000*\u00b9\u0001\u0000\u0000\u0000,\u00c1\u0001"+
		"\u0000\u0000\u0000.\u00da\u0001\u0000\u0000\u000003\u0003\u0012\t\u0000"+
		"13\u0003\u0002\u0001\u000020\u0001\u0000\u0000\u000021\u0001\u0000\u0000"+
		"\u000036\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u000045\u0001\u0000"+
		"\u0000\u000057\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000078\u0005"+
		"\u0000\u0000\u00018\u0001\u0001\u0000\u0000\u00009:\u0003\u000e\u0007"+
		"\u0000:;\u0005\u0001\u0000\u0000;L\u0001\u0000\u0000\u0000<=\u0003\u0010"+
		"\b\u0000=>\u0005\u0001\u0000\u0000>L\u0001\u0000\u0000\u0000?@\u0003\u0006"+
		"\u0003\u0000@A\u0005\u0001\u0000\u0000AL\u0001\u0000\u0000\u0000BC\u0003"+
		"\u0018\f\u0000CD\u0005\u0001\u0000\u0000DL\u0001\u0000\u0000\u0000EF\u0003"+
		"\u001e\u000f\u0000FG\u0005\u0001\u0000\u0000GL\u0001\u0000\u0000\u0000"+
		"HL\u0003\u001a\r\u0000IL\u0003\u001c\u000e\u0000JL\u0003\u0004\u0002\u0000"+
		"K9\u0001\u0000\u0000\u0000K<\u0001\u0000\u0000\u0000K?\u0001\u0000\u0000"+
		"\u0000KB\u0001\u0000\u0000\u0000KE\u0001\u0000\u0000\u0000KH\u0001\u0000"+
		"\u0000\u0000KI\u0001\u0000\u0000\u0000KJ\u0001\u0000\u0000\u0000L\u0003"+
		"\u0001\u0000\u0000\u0000MQ\u0005\u0004\u0000\u0000NP\u0003\u0002\u0001"+
		"\u0000ON\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000"+
		"\u0000\u0000QR\u0001\u0000\u0000\u0000RT\u0001\u0000\u0000\u0000SQ\u0001"+
		"\u0000\u0000\u0000TU\u0005\u0005\u0000\u0000U\u0005\u0001\u0000\u0000"+
		"\u0000VW\u0005\u001d\u0000\u0000WX\u0005\u0002\u0000\u0000XY\u0003\u001e"+
		"\u000f\u0000YZ\u0005\u0003\u0000\u0000Z\u0007\u0001\u0000\u0000\u0000"+
		"[\\\u0005 \u0000\u0000\\]\u0005\u0002\u0000\u0000]^\u0003\u001e\u000f"+
		"\u0000^_\u0005\u0003\u0000\u0000_\t\u0001\u0000\u0000\u0000`a\u0007\u0000"+
		"\u0000\u0000a\u000b\u0001\u0000\u0000\u0000be\u0003\n\u0005\u0000ce\u0005"+
		"\u0019\u0000\u0000db\u0001\u0000\u0000\u0000dc\u0001\u0000\u0000\u0000"+
		"e\r\u0001\u0000\u0000\u0000fg\u0003\n\u0005\u0000gj\u0005%\u0000\u0000"+
		"hi\u0005\u0010\u0000\u0000ik\u0003\u001e\u000f\u0000jh\u0001\u0000\u0000"+
		"\u0000jk\u0001\u0000\u0000\u0000k\u000f\u0001\u0000\u0000\u0000lm\u0005"+
		"%\u0000\u0000mn\u0005\u0010\u0000\u0000no\u0003\u001e\u000f\u0000o\u0011"+
		"\u0001\u0000\u0000\u0000pq\u0003\f\u0006\u0000qr\u0005\"\u0000\u0000r"+
		"s\u0005%\u0000\u0000su\u0005\u0002\u0000\u0000tv\u0003\u0014\n\u0000u"+
		"t\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000"+
		"\u0000wx\u0005\u0003\u0000\u0000xy\u0003\u0004\u0002\u0000y\u0013\u0001"+
		"\u0000\u0000\u0000z\u007f\u0003\u0016\u000b\u0000{|\u0005\u0006\u0000"+
		"\u0000|~\u0003\u0016\u000b\u0000}{\u0001\u0000\u0000\u0000~\u0081\u0001"+
		"\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000"+
		"\u0000\u0000\u0080\u0015\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0003\n\u0005\u0000\u0083\u0084\u0005%\u0000"+
		"\u0000\u0084\u0017\u0001\u0000\u0000\u0000\u0085\u0087\u0005!\u0000\u0000"+
		"\u0086\u0088\u0003\u001e\u000f\u0000\u0087\u0086\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0019\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0005\u001f\u0000\u0000\u008a\u008b\u0005\u0002\u0000\u0000"+
		"\u008b\u008c\u0003\u001e\u000f\u0000\u008c\u008d\u0005\u0003\u0000\u0000"+
		"\u008d\u008e\u0003\u0002\u0001\u0000\u008e\u001b\u0001\u0000\u0000\u0000"+
		"\u008f\u0090\u0005\u001e\u0000\u0000\u0090\u0091\u0005\u0002\u0000\u0000"+
		"\u0091\u0092\u0003\u001e\u000f\u0000\u0092\u0093\u0005\u0003\u0000\u0000"+
		"\u0093\u0094\u0003\u0002\u0001\u0000\u0094\u001d\u0001\u0000\u0000\u0000"+
		"\u0095\u0096\u0003 \u0010\u0000\u0096\u001f\u0001\u0000\u0000\u0000\u0097"+
		"\u009c\u0003\"\u0011\u0000\u0098\u0099\u0005\b\u0000\u0000\u0099\u009b"+
		"\u0003\"\u0011\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u009e\u0001"+
		"\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001"+
		"\u0000\u0000\u0000\u009d!\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000"+
		"\u0000\u0000\u009f\u00a4\u0003$\u0012\u0000\u00a0\u00a1\u0005\u0007\u0000"+
		"\u0000\u00a1\u00a3\u0003$\u0012\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000"+
		"\u00a3\u00a6\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5#\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005\t\u0000\u0000\u00a8\u00ab"+
		"\u0003$\u0012\u0000\u00a9\u00ab\u0003&\u0013\u0000\u00aa\u00a7\u0001\u0000"+
		"\u0000\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00ab%\u0001\u0000\u0000"+
		"\u0000\u00ac\u00af\u0003(\u0014\u0000\u00ad\u00ae\u0007\u0001\u0000\u0000"+
		"\u00ae\u00b0\u0003(\u0014\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af"+
		"\u00b0\u0001\u0000\u0000\u0000\u00b0\'\u0001\u0000\u0000\u0000\u00b1\u00b6"+
		"\u0003*\u0015\u0000\u00b2\u00b3\u0007\u0002\u0000\u0000\u00b3\u00b5\u0003"+
		"*\u0015\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000\u00b5\u00b8\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000"+
		"\u0000\u0000\u00b7)\u0001\u0000\u0000\u0000\u00b8\u00b6\u0001\u0000\u0000"+
		"\u0000\u00b9\u00be\u0003.\u0017\u0000\u00ba\u00bb\u0007\u0003\u0000\u0000"+
		"\u00bb\u00bd\u0003.\u0017\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bd"+
		"\u00c0\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0001\u0000\u0000\u0000\u00bf+\u0001\u0000\u0000\u0000\u00c0\u00be"+
		"\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005%\u0000\u0000\u00c2\u00cb\u0005"+
		"\u0002\u0000\u0000\u00c3\u00c8\u0003\u001e\u000f\u0000\u00c4\u00c5\u0005"+
		"\u0006\u0000\u0000\u00c5\u00c7\u0003\u001e\u000f\u0000\u00c6\u00c4\u0001"+
		"\u0000\u0000\u0000\u00c7\u00ca\u0001\u0000\u0000\u0000\u00c8\u00c6\u0001"+
		"\u0000\u0000\u0000\u00c8\u00c9\u0001\u0000\u0000\u0000\u00c9\u00cc\u0001"+
		"\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00cb\u00c3\u0001"+
		"\u0000\u0000\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001"+
		"\u0000\u0000\u0000\u00cd\u00ce\u0005\u0003\u0000\u0000\u00ce-\u0001\u0000"+
		"\u0000\u0000\u00cf\u00db\u0005#\u0000\u0000\u00d0\u00db\u0005$\u0000\u0000"+
		"\u00d1\u00db\u0005\u001b\u0000\u0000\u00d2\u00db\u0005\u001c\u0000\u0000"+
		"\u00d3\u00db\u0005\u001a\u0000\u0000\u00d4\u00db\u0003,\u0016\u0000\u00d5"+
		"\u00db\u0005%\u0000\u0000\u00d6\u00d7\u0005\u0002\u0000\u0000\u00d7\u00d8"+
		"\u0003\u001e\u000f\u0000\u00d8\u00d9\u0005\u0003\u0000\u0000\u00d9\u00db"+
		"\u0001\u0000\u0000\u0000\u00da\u00cf\u0001\u0000\u0000\u0000\u00da\u00d0"+
		"\u0001\u0000\u0000\u0000\u00da\u00d1\u0001\u0000\u0000\u0000\u00da\u00d2"+
		"\u0001\u0000\u0000\u0000\u00da\u00d3\u0001\u0000\u0000\u0000\u00da\u00d4"+
		"\u0001\u0000\u0000\u0000\u00da\u00d5\u0001\u0000\u0000\u0000\u00da\u00d6"+
		"\u0001\u0000\u0000\u0000\u00db/\u0001\u0000\u0000\u0000\u001224KQdju\u007f"+
		"\u0087\u009c\u00a4\u00aa\u00af\u00b6\u00be\u00c8\u00cb\u00da";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}