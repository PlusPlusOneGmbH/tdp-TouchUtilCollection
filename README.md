# TouchUtilCollection
A collection of (hopefully) useful python-functions, methods and other trinkets.

Install via PIP, UV, Conda or whatever you like. 

Not all are isted in the readme, see this as a list of "highlights"

## tdasync
Bring asyncio to TD in this minimal wrapper.
```python
from touchutilcollection.tdasync import execute
from asyncio import sleep
async def coro( waittime ):
    op("text1").text = "Starting Coro"
    await sleep(waittime)
    op("text1").text = "Done"
execute( coro(5) )
```
Powerfull with TauCetiTweener and the .Resolve() functionality.

## Extension
Makes your live with extensions easier by allowing for autocreation of custompars.
```python
class extExample( 
    EnsureExtension # Required
     ):
    class par:
        Foo = parfield(partypes.ParFloat)
        Bar = parfield(partypes.ParFloat, page ="Different", min = 0, max = 10)
        Baba = parfield( 
            partypes.ParMenu, 
            menuLabels=["Eins", "Zwei", "Drei" ], 
            menuNames=["1", "2", "3"], 
            bindExpr="op.Settings.par.Baba" 
        )

        def __init__(self, ownerComp) -> None:
            super().__init__(ownerComp) # Also required
            self.par.Foo.val = 23
```

## Ensure
Ensure existence of components without having to manualy create them (or even see them. )
### Ensure Tox
Ensure the existence of the given TOX-COMP using a global op shortcut.
```python
from touchutilcollection.ensure import ensure_global_tox
from TauCeti import Tweener
TweenerComp = ensure_global_tox( Tweener.ToxFile, "TAUCETI_TWEENER" )
```
### Ensure TDP
Takes values from a TDP and applies the same Logic.
```python
from touchutilcollection.ensure import ensure_global_tox
from TauCeti import Tweener
TweenerComp = ensure_global_tox( Tweener )
```