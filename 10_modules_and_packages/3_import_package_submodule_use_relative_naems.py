
# mypackage/A/spam.py

# grok in the same package as spam
# mypackage/A/grok.py
from . import grok


# bar one level up and then one over from spam
# mypackage/B/bar.py
from ..B import bar


from mypackage.A import grok # OK
from . import grok # OK
import grok # Error (not found)


# relative import only works with "from" not "import"
from . import grok # OK
import .grok # ERROR