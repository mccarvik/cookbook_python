# setup.py
from distutils.core import setup, Extension

setup(name="sample_4", 
      ext_modules=[
        Extension("sample_4",
                  ["./sample.c", "pysample_4.c"],
                  include_dirs = ['..'],
                  )
        ]
)