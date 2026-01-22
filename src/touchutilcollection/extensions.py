from typing import Any, TypeVar, Type, overload, ClassVar, cast, List, Union
from abc import abstractmethod
from dataclasses import dataclass



from .par_def import partypes
from .par_def import pargrouptypes



## Utils Start
lookupdict = {}


def _pop_default_kwarsg( target_dict:dict ):
    return {
        key : value for key, value in target_dict.items() if key not in  ["page"]
    }

@dataclass
class _ParProxy():
    data : dict
    par_type : Type[partypes._Par]

    def __call__(self, ownerComp) -> Any:
        target_par = ensure_parameter(
            ownerComp, 
            self.data["name"], 
            self.data["page"], 
            f"append{self.par_type.style}", 
            self.par_type.style
        )  

        for attrname, attrvalue in self.data.items():
            if attrname in ("name", "page"): continue
            setattr( target_par, attrname, attrvalue )

        #One can dram. Pleas derivative senpai.
        #_dependency_object = tdu.Dependency( target_par.eval() )
        #_dependency_object.bindMaster = target_par
        #_dependency_object.callbacks.append( self.data.get("callback", lambda *args: None) )

        return target_par
    
@dataclass
class _ParGroupProxy():
    data : dict
    par_type : Type[partypes._Par]

    def __call__(self, ownerComp) -> Any:
        target_par = ensure_pargroup(
            ownerComp, 
            self.data["name"], 
            self.data["page"], 
            f"append{self.par_type.style}", 
            self.par_type.style
        )  

        for attrname, attrvalue in self.data.items():
            if attrname in ("name", "page"): continue
            setattr( target_par, attrname, attrvalue )
        return target_par


def ensure_page(ownerComp, pagename):
    for page in ownerComp.pages:
        if page.name == pagename: return page
    return ownerComp.appendCustomPage( pagename )

from .parameter import is_legal_name

def ensure_parameter(ownerComp, par_name:str, pagename:str, adder_method_name:str, par_style:str):
    if not is_legal_name( par_name ): raise Exception("Illegal CustomPar Name.")
    page = ensure_page( ownerComp, pagename )
    if (par := ownerComp.par[par_name]) is not None:
        # lets validate the partype itself.
        if par.style != par_style: par.destroy()

    if ownerComp.par[par_name] is None:
        # now lets check if the par already exists, if not    
        getattr(page, adder_method_name)( par_name )
    resulting_par = ownerComp.par[par_name] # This noteably only works with single value parameters!
    resulting_par.page = page
    return resulting_par

def ensure_pargroup(ownerComp, par_name:str, pagename:str, adder_method_name:str, par_style:str):
    if not is_legal_name( par_name ): raise Exception("Illegal CustomPar Name.")
    page = ensure_page( ownerComp, pagename )
    if (parGroup := ownerComp.parGroup[par_name]) is not None:
        # lets validate the partype itself.
        if parGroup.style != par_style: parGroup.destroy()

    if ownerComp.parGroup[par_name] is None:
        # now lets check if the par already exists, if not    
        getattr(page, adder_method_name)( par_name )
    resulting_pargroup = ownerComp.parGroup[par_name]
    resulting_pargroup.page = page
    return resulting_pargroup


## Utils End

from typing import Unpack

T = TypeVar("T") 

### Overlods for typehinting.
@overload
def parfield(field_type:Type[partypes.ParStr], page:str = "Custom", **kwargs:Unpack[ partypes.ParStr._args]) -> partypes.ParStr: 
    pass

@overload
def parfield(field_type:Type[partypes.ParFloat], page:str = "Custom", **kwargs:Unpack[ partypes.ParFloat._args]) -> partypes.ParFloat: 
    pass

@overload
def parfield(field_type:Type[partypes.ParInt], page:str = "Custom",**kwargs:Unpack[ partypes.ParInt._args]) -> partypes.ParInt: 
    pass
@overload
def parfield(field_type:Type[partypes.ParToggle], page:str = "Custom", **kwargs:Unpack[ partypes.ParToggle._args]) -> partypes.ParToggle: 
    pass

@overload
def parfield(field_type:Type[partypes.ParMomentary], page:str = "Custom",**kwargs:Unpack[ partypes.ParMomentary._args ]) -> partypes.ParMomentary: 
    pass

@overload
def parfield(field_type:Type[partypes.ParPulse], page:str = "Custom",**kwargs:Unpack[ partypes.ParPulse._args ]) -> partypes.ParPulse: 
    pass

@overload
def parfield(field_type:Type[partypes.ParMenu], page:str = "Custom",**kwargs:Unpack[ partypes.ParMenu._args]) -> partypes.ParMenu: 
    pass

@overload
def parfield(field_type:Type[partypes.ParStrMenu], page:str = "Custom",**kwargs:Unpack[ partypes.ParStrMenu._args]) -> partypes.ParStrMenu: 
    pass

@overload
def parfield(field_type:Type[partypes.ParOP], page:str = "Custom",**kwargs:Unpack[ partypes.ParOP._args]) -> partypes.ParOP: 
    pass

@overload
def parfield(field_type:Type[partypes.ParCOMP], page:str = "Custom",**kwargs:Unpack[ partypes.ParCOMP._args]) -> partypes.ParCOMP: 
    pass

@overload
def parfield(field_type:Type[partypes.ParObject], page:str = "Custom",**kwargs:Unpack[ partypes.ParObject._args]) -> partypes.ParObject: 
    pass

@overload
def parfield(field_type:Type[partypes.ParSOP], page:str = "Custom",**kwargs:Unpack[ partypes.ParSOP._args]) -> partypes.ParSOP: 
    pass

@overload
def parfield(field_type:Type[partypes.ParPOP], page:str = "Custom",**kwargs:Unpack[ partypes.ParPOP._args]) -> partypes.ParPOP: 
    """2025 or higher. Add vesioncheck"""
    pass

@overload
def parfield(field_type:Type[partypes.ParMAT], page:str = "Custom",**kwargs:Unpack[ partypes.ParMAT._args]) -> partypes.ParMAT: 
    pass

@overload
def parfield(field_type:Type[partypes.ParCHOP], page:str = "Custom",**kwargs:Unpack[ partypes.ParCHOP._args]) -> partypes.ParCHOP: 
    pass

@overload
def parfield(field_type:Type[partypes.ParTOP], page:str = "Custom",**kwargs:Unpack[ partypes.ParTOP._args]) -> partypes.ParTOP: 
    pass

@overload
def parfield(field_type:Type[partypes.ParDAT], page:str = "Custom",**kwargs:Unpack[ partypes.ParDAT._args]) -> partypes.ParDAT: 
    pass

@overload
def parfield(field_type:Type[partypes.ParPanelCOMP], page:str = "Custom",**kwargs:Unpack[ partypes.ParPanelCOMP._args]) -> partypes.ParPanelCOMP: 
    pass

@overload
def parfield(field_type:Type[partypes.ParFile], page:str = "Custom",**kwargs:Unpack[ partypes.ParFile._args]) -> partypes.ParFile: 
    pass

@overload
def parfield(field_type:Type[partypes.ParFolder], page:str = "Custom",**kwargs:Unpack[ partypes.ParFolder._args]) -> partypes.ParFolder: 
    pass

# parGroups
@overload
def pargroupfield(field_type:Type[pargrouptypes.ParGroupFloat], page:str = "Custom",**kwargs:Unpack[ pargrouptypes.ParGroupFloat._args]) -> pargrouptypes.ParGroupFloat: 
    pass

@overload
def pargroupfield(field_type:Type[pargrouptypes.ParGroupInt], page:str = "Custom",**kwargs:Unpack[ pargrouptypes.ParGroupInt._args]) -> pargrouptypes.ParGroupInt: 
    pass

@overload
def pargroupfield(field_type:Type[pargrouptypes.ParGroupRGBA], page:str = "Custom",**kwargs:Unpack[ pargrouptypes.ParGroupRGBA._args]) -> pargrouptypes.ParGroupRGBA: 
    pass

@overload
def pargroupfield(field_type:Type[pargrouptypes.ParGroupUVW], page:str = "Custom",**kwargs:Unpack[ pargrouptypes.ParGroupUVW._args]) -> pargrouptypes.ParGroupUVW: 
    pass

@overload
def pargroupfield(field_type:Type[pargrouptypes.ParGroupWH], page:str = "Custom",**kwargs:Unpack[ pargrouptypes.ParGroupWH._args]) -> pargrouptypes.ParGroupWH: 
    pass

@overload
def pargroupfield(field_type:Type[pargrouptypes.ParGroupXYZW], page:str = "Custom",**kwargs:Unpack[ pargrouptypes.ParGroupXYZW._args]) -> pargrouptypes.ParGroupXYZW: 
    pass


## Actual Implementation.

from sys import _getframe

def parfield(field_type:Type[T], page:str = "Custom", **kwargs) -> T: 
    pass_args = {
        "page" : page,
        **_pop_default_kwarsg( kwargs )
    }
    return cast( T, _ParProxy(pass_args, field_type) )  # pyright: ignore[reportArgumentType]

from typing import Literal

def pargroupfield( field_type:Type[T], page:str = "Custom", **kwargs) -> T:
    pass_args = {
        "page" : page,
        "size" : kwargs.get("size", 2),
        **_pop_default_kwarsg( kwargs )
    }
    return cast( T, _ParGroupProxy(pass_args, field_type) )  # pyright: ignore[reportArgumentType]


class _empty():
    pass

class EnsureExtension():
    par:ClassVar
    parGroup:ClassVar

    def __init__(self, ownerComp) -> None:
        self.par = getattr( self, "par", _empty)() # pyright: ignore[reportAttributeAccessIssue]
        for attr_name in dir(self.par):
            attr_object = getattr( self.par, attr_name )
            if not isinstance( attr_object, _ParProxy): continue
            # Set name HERE!
            attr_object.data["name"] = attr_name
            setattr( self.par, attr_name, attr_object(ownerComp) )
            

        self.parGroup = getattr( self, "parGroup", _empty)() # pyright: ignore[reportAttributeAccessIssue]

        for attr_name in dir(self.parGroup):
            attr_object = getattr( self.parGroup, attr_name )
            if not isinstance( attr_object, _ParGroupProxy): continue
            # Set name HERE!
            attr_object.data["name"] = attr_name
            setattr( self.parGroup, attr_name, attr_object(ownerComp) )


__all__ = [ "EnsureExtension", "parfield", "partypes" ]



demo = None
if demo:

    class extExample( EnsureExtension ):
        class par:
            Foo = parfield(partypes.ParFloat)
            Bar = parfield(partypes.ParFloat, page ="Different", min = 0, max = 10)
            Baba = parfield( partypes.ParMenu, menuLabels=["Eins", "Zwei", "Drei" ], menuNames=["1", "2", "3"], bindExpr="Hello World" )

        class parGroup:
            Hello = pargroupfield( pargrouptypes.ParGroupRGBA, size = 3 )
            Group = pargroupfield( pargrouptypes.ParGroupRGBA, size = 2)

        def __init__(self, ownerComp) -> None:
            super().__init__(ownerComp)
            self.par.Foo.val = 23

    something = extExample(None)
    something.par.Baba.default = 123 # pyright: ignore[reportAttributeAccessIssue] # Errors
    something.par.Baba.default = "123" # Works!
    something.parGroup.Group.eval()[0]
