#!/usr/bin/env python

from numpy.distutils.core import setup
#from setuptools import setup

setup(name='pyglow',\
        version='0.5',\
        url='github.com/timduly4/pyglow',\
        author='Timothy M. Duly',\
        author_email='duly2@illinois.edu',\
        packages=[
            'pyglow', 
            ], \
        data_files=[ \
        ('pyglow_trash',['pyglow/models/Makefile']),
        ('pyglow_trash',['pyglow/models/get_models.py']),
        ('pyglow_trash',['pyglow/models/dl_models/hwm07/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/hwm93/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/igrf/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/iri/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/msis/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/hwm14/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/hwm07/hwm07e.patch']),
        ('pyglow_trash',['pyglow/models/f2py/hwm07/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/hwm93/hwm93.patch']),
        ('pyglow_trash',['pyglow/models/f2py/hwm93/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/hwm93/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/igrf/igrf11.patch']),
        ('pyglow_trash',['pyglow/models/f2py/igrf/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/igrf/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/iri/delete_iriflip_comments.py']),
        ('pyglow_trash',['pyglow/models/f2py/iri/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/iri/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/msis/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/msis/nrlmsise00_sub.patch']),
        ('pyglow_trash',['pyglow/models/f2py/msis/sig.patch']),
        ('',['pyglow/models/dl_models/igrf/igrf11py.so']),
        ('',['pyglow/models/dl_models/hwm93/hwm93py.so']),
        ('',['pyglow/models/dl_models/msis/msis00py.so']),
        ('',['pyglow/models/dl_models/hwm07/hwm07py.so']),
        ('',['pyglow/models/dl_models/hwm14/hwm14py.so']),
        ('',['pyglow/models/dl_models/iri/iri12py.so']),
        ('pyglow/hwm07_data/',[
            'pyglow/models/dl_models/hwm07/apexgrid.dat',
            'pyglow/models/dl_models/hwm07/dwm07b_104i.dat',
            'pyglow/models/dl_models/hwm07/hwm071308e.dat',
            ]),
        ('pyglow/hwm14_data/',[
            'pyglow/models/dl_models/hwm14/gd2qd.dat',
            'pyglow/models/dl_models/hwm14/dwm07b_104i.dat',
            'pyglow/models/dl_models/hwm14/hwm14-beta.bin',
            'pyglow/models/dl_models/hwm14/hwm14.f90',
            ]),
        ('pyglow/iri_data/',[
            'pyglow/models/dl_models/iri/apf107.dat',
            'pyglow/models/dl_models/iri/ccir11.asc',
            'pyglow/models/dl_models/iri/ccir12.asc',
            'pyglow/models/dl_models/iri/ccir13.asc',
            'pyglow/models/dl_models/iri/ccir14.asc',
            'pyglow/models/dl_models/iri/ccir15.asc',
            'pyglow/models/dl_models/iri/ccir16.asc',
            'pyglow/models/dl_models/iri/ccir17.asc',
            'pyglow/models/dl_models/iri/ccir18.asc',
            'pyglow/models/dl_models/iri/ccir19.asc',
            'pyglow/models/dl_models/iri/ccir20.asc',
            'pyglow/models/dl_models/iri/ccir21.asc',
            'pyglow/models/dl_models/iri/ccir22.asc',
            'pyglow/models/dl_models/iri/dgrf1945.dat',
            'pyglow/models/dl_models/iri/dgrf1950.dat',
            'pyglow/models/dl_models/iri/dgrf1955.dat',
            'pyglow/models/dl_models/iri/dgrf1960.dat',
            'pyglow/models/dl_models/iri/dgrf1965.dat',
            'pyglow/models/dl_models/iri/dgrf1970.dat',
            'pyglow/models/dl_models/iri/dgrf1975.dat',
            'pyglow/models/dl_models/iri/dgrf1980.dat',
            'pyglow/models/dl_models/iri/dgrf1985.dat',
            'pyglow/models/dl_models/iri/dgrf1990.dat',
            'pyglow/models/dl_models/iri/dgrf1995.dat',
            'pyglow/models/dl_models/iri/dgrf2000.dat',
            'pyglow/models/dl_models/iri/dgrf2005.dat',
            'pyglow/models/dl_models/iri/ig_rz_IPS.dat',
            'pyglow/models/dl_models/iri/ig_rz_SEC.dat',
            'pyglow/models/dl_models/iri/ig_rz.dat',
            'pyglow/models/dl_models/iri/igrf2010.dat',
            'pyglow/models/dl_models/iri/igrf2010s.dat',
            'pyglow/models/dl_models/iri/ursi11.asc',
            'pyglow/models/dl_models/iri/ursi12.asc',
            'pyglow/models/dl_models/iri/ursi13.asc',
            'pyglow/models/dl_models/iri/ursi14.asc',
            'pyglow/models/dl_models/iri/ursi15.asc',
            'pyglow/models/dl_models/iri/ursi16.asc',
            'pyglow/models/dl_models/iri/ursi17.asc',
            'pyglow/models/dl_models/iri/ursi18.asc',
            'pyglow/models/dl_models/iri/ursi19.asc',
            'pyglow/models/dl_models/iri/ursi20.asc',
            'pyglow/models/dl_models/iri/ursi21.asc',
            'pyglow/models/dl_models/iri/ursi22.asc',
            ]),
        ('pyglow/kpap/', [
            'pyglow/kpap/1932',\
            'pyglow/kpap/1933',\
            'pyglow/kpap/1934',\
            'pyglow/kpap/1935',\
            'pyglow/kpap/1936',\
            'pyglow/kpap/1937',\
            'pyglow/kpap/1938',\
            'pyglow/kpap/1939',\
            'pyglow/kpap/1940',\
            'pyglow/kpap/1941',\
            'pyglow/kpap/1942',\
            'pyglow/kpap/1943',\
            'pyglow/kpap/1944',\
            'pyglow/kpap/1945',\
            'pyglow/kpap/1946',\
            'pyglow/kpap/1947',\
            'pyglow/kpap/1948',\
            'pyglow/kpap/1949',\
            'pyglow/kpap/1950',\
            'pyglow/kpap/1951',\
            'pyglow/kpap/1952',\
            'pyglow/kpap/1953',\
            'pyglow/kpap/1954',\
            'pyglow/kpap/1955',\
            'pyglow/kpap/1956',\
            'pyglow/kpap/1957',\
            'pyglow/kpap/1958',\
            'pyglow/kpap/1959',\
            'pyglow/kpap/1960',\
            'pyglow/kpap/1961',\
            'pyglow/kpap/1962',\
            'pyglow/kpap/1963',\
            'pyglow/kpap/1964',\
            'pyglow/kpap/1965',\
            'pyglow/kpap/1966',\
            'pyglow/kpap/1967',\
            'pyglow/kpap/1968',\
            'pyglow/kpap/1969',\
            'pyglow/kpap/1970',\
            'pyglow/kpap/1971',\
            'pyglow/kpap/1972',\
            'pyglow/kpap/1973',\
            'pyglow/kpap/1974',\
            'pyglow/kpap/1975',\
            'pyglow/kpap/1976',\
            'pyglow/kpap/1977',\
            'pyglow/kpap/1978',\
            'pyglow/kpap/1979',\
            'pyglow/kpap/1980',\
            'pyglow/kpap/1981',\
            'pyglow/kpap/1982',\
            'pyglow/kpap/1983',\
            'pyglow/kpap/1984',\
            'pyglow/kpap/1985',\
            'pyglow/kpap/1986',\
            'pyglow/kpap/1987',\
            'pyglow/kpap/1988',\
            'pyglow/kpap/1989',\
            'pyglow/kpap/1990',\
            'pyglow/kpap/1991',\
            'pyglow/kpap/1992',\
            'pyglow/kpap/1993',\
            'pyglow/kpap/1994',\
            'pyglow/kpap/1995',\
            'pyglow/kpap/1996',\
            'pyglow/kpap/1997',\
            'pyglow/kpap/1998',\
            'pyglow/kpap/1999',\
            'pyglow/kpap/2000',\
            'pyglow/kpap/2001',\
            'pyglow/kpap/2002',\
            'pyglow/kpap/2003',\
            'pyglow/kpap/2004',\
            'pyglow/kpap/2005',\
            'pyglow/kpap/2006',\
            'pyglow/kpap/2007',\
            'pyglow/kpap/2008',\
            'pyglow/kpap/2009',\
            'pyglow/kpap/2010',\
            'pyglow/kpap/2011',\
            'pyglow/kpap/2012',\
            'pyglow/kpap/2013',\
            ]),\
        ('pyglow/dst/', [
            'pyglow/dst/1957_1969',\
            'pyglow/dst/1970_1989',\
            'pyglow/dst/1990_2004',\
            ]),\
        ('pyglow/ae/', [
            ]),\
            ],\
        )




print "Let's try to update the indices..."
from pyglow.pyglow import update_indices
update_indices()
print "... all done!"
