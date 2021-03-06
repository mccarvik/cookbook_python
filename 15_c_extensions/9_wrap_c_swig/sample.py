# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sample', [dirname(__file__)])
        except ImportError:
            import _sample
            return _sample
        if fp is not None:
            try:
                _mod = imp.load_module('_sample', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sample = swig_import_helper()
    del swig_import_helper
else:
    import _sample
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def gcd(*args) -> "int" :
  return _sample.gcd(*args)
gcd = _sample.gcd

def in_mandel(*args) -> "int" :
  return _sample.in_mandel(*args)
in_mandel = _sample.in_mandel

def divide(*args) -> "int *" :
  return _sample.divide(*args)
divide = _sample.divide

def avg(*args) -> "double" :
  return _sample.avg(*args)
avg = _sample.avg
class Point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _sample.Point_x_set
    __swig_getmethods__["x"] = _sample.Point_x_get
    if _newclass:x = _swig_property(_sample.Point_x_get, _sample.Point_x_set)
    __swig_setmethods__["y"] = _sample.Point_y_set
    __swig_getmethods__["y"] = _sample.Point_y_get
    if _newclass:y = _swig_property(_sample.Point_y_get, _sample.Point_y_set)
    def __init__(self, *args): 
        this = _sample.new_Point(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sample.delete_Point
    __del__ = lambda self : None;
Point_swigregister = _sample.Point_swigregister
Point_swigregister(Point)


def distance(*args) -> "double" :
  return _sample.distance(*args)
distance = _sample.distance
# This file is compatible with both classic and new-style classes.


