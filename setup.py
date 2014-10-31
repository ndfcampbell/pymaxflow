from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy as np

#ext_modules = [Extension("pymaxflow", ["pymaxflow.pyx", "./graph.cpp", "./maxflow.cpp"])]

exts = Extension( name='pymaxflow',
                  sources=['pymaxflow.pyx'],
                  extra_compile_args=['-stdlib=libstdc++', '-O2', '-ffast-math'],
                  extra_link_args=['-lm', '-stdlib=libstdc++', '-lstdc++'])

setup(
    name = 'pymaxflow',
    include_dirs = [np.get_include()],
    ext_modules = cythonize( exts )
)

