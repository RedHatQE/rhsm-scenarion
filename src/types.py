from collections import namedtuple
from functools import singledispatch

StartOfScenario = namedtuple('StartOfScenario',['scenario_name','scenario_id'])
EndOfScenario = namedtuple('EndOfScenario',['scenario_name','scenario_id'])
CmdResult = namedtuple("CmdResult",['cmd','args','exitcode','stdout','stderr'])
NewProductInstalled = namedtuple("NewProductInstalled",["product_id"])
TestwareMSG = namedtuple("TestwareMSG",['time','type','msg'])


@singledispatch
def type_name(x):
    """This method is used to get a str representation of an object type (for json testware message)"""

@type_name.register(CmdResult)
def _(x):
    return "CmdResult"

@type_name.register(StartOfScenario)
def _(x):
    return "StartOfScenario"

@type_name.register(EndOfScenario)
def _(x):
    return "EndOfScenario"

@type_name.register(NewProductInstalled)
def _(x):
    return "NewProductInstalled"

#types_by_name = dict(**[(type_name(tuple_type),tuple_type) for tuple_type in (StartOfScenario, EndOfScenario, CmdResult, TestwareMSG)])
