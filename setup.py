#!/usr/bin/env python

from numpy.distutils.core import setup

setup(
    name='pyglow',
    version='0.6',
    url='github.com/timduly4/pyglow',
    author='Timothy M. Duly',
    author_email='duly2@illinois.edu',
    packages=['pyglow', ],
    data_files=[
        ('pyglow_trash',['pyglow/models/Makefile']),
        ('pyglow_trash',['pyglow/models/get_models.py']),
        ('pyglow_trash',['pyglow/models/dl_models/hwm07/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/hwm93/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/igrf11/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/igrf12/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/iri12/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/iri16/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/msis/dummy.txt']),
        ('pyglow_trash',['pyglow/models/dl_models/hwm14/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/hwm07/hwm07e.patch']),
        ('pyglow_trash',['pyglow/models/f2py/hwm07/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/hwm93/hwm93.patch']),
        ('pyglow_trash',['pyglow/models/f2py/hwm93/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/hwm93/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/igrf11/igrf11.patch']),
        ('pyglow_trash',['pyglow/models/f2py/igrf11/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/igrf11/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/igrf12/igrf12.patch']),
        ('pyglow_trash',['pyglow/models/f2py/igrf12/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/igrf12/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/iri12/delete_iriflip_comments.py']),
        ('pyglow_trash',['pyglow/models/f2py/iri12/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/iri12/sig.patch']),
        ('pyglow_trash',['pyglow/models/f2py/iri12/iridreg.patch']),
        ('pyglow_trash',['pyglow/models/f2py/msis/Makefile']),
        ('pyglow_trash',['pyglow/models/f2py/msis/nrlmsise00_sub.patch']),
        ('pyglow_trash',['pyglow/models/f2py/msis/sig.patch']),
        ('',['pyglow/models/dl_models/igrf11/igrf11py.so']),
        ('',['pyglow/models/dl_models/igrf12/igrf12py.so']),
        ('',['pyglow/models/dl_models/hwm93/hwm93py.so']),
        ('',['pyglow/models/dl_models/msis/msis00py.so']),
        ('',['pyglow/models/dl_models/hwm07/hwm07py.so']),
        ('',['pyglow/models/dl_models/hwm14/hwm14py.so']),
        ('',['pyglow/models/dl_models/iri12/iri12py.so']),
        ('',['pyglow/models/dl_models/iri16/iri16py.so']),
        ('pyglow/hwm07_data/',[
            'pyglow/models/dl_models/hwm07/apexgrid.dat',
            'pyglow/models/dl_models/hwm07/dwm07b_104i.dat',
            'pyglow/models/dl_models/hwm07/hwm071308e.dat',
        ]),
        (
            'pyglow/hwm14_data/',
            [
                'pyglow/models/dl_models/hwm14/gd2qd.dat',
                'pyglow/models/dl_models/hwm14/dwm07b_104i.dat',
                'pyglow/models/dl_models/hwm14/hwm14-beta.bin',
                'pyglow/models/dl_models/hwm14/hwm14.f90',
            ],
        ),
        (
            'pyglow/iri12_data/',
            [
                'pyglow/models/dl_models/iri12/apf107.dat',
                'pyglow/models/dl_models/iri12/ccir11.asc',
                'pyglow/models/dl_models/iri12/ccir12.asc',
                'pyglow/models/dl_models/iri12/ccir13.asc',
                'pyglow/models/dl_models/iri12/ccir14.asc',
                'pyglow/models/dl_models/iri12/ccir15.asc',
                'pyglow/models/dl_models/iri12/ccir16.asc',
                'pyglow/models/dl_models/iri12/ccir17.asc',
                'pyglow/models/dl_models/iri12/ccir18.asc',
                'pyglow/models/dl_models/iri12/ccir19.asc',
                'pyglow/models/dl_models/iri12/ccir20.asc',
                'pyglow/models/dl_models/iri12/ccir21.asc',
                'pyglow/models/dl_models/iri12/ccir22.asc',
                'pyglow/models/dl_models/iri12/dgrf1945.dat',
                'pyglow/models/dl_models/iri12/dgrf1950.dat',
                'pyglow/models/dl_models/iri12/dgrf1955.dat',
                'pyglow/models/dl_models/iri12/dgrf1960.dat',
                'pyglow/models/dl_models/iri12/dgrf1965.dat',
                'pyglow/models/dl_models/iri12/dgrf1970.dat',
                'pyglow/models/dl_models/iri12/dgrf1975.dat',
                'pyglow/models/dl_models/iri12/dgrf1980.dat',
                'pyglow/models/dl_models/iri12/dgrf1985.dat',
                'pyglow/models/dl_models/iri12/dgrf1990.dat',
                'pyglow/models/dl_models/iri12/dgrf1995.dat',
                'pyglow/models/dl_models/iri12/dgrf2000.dat',
                'pyglow/models/dl_models/iri12/dgrf2005.dat',
                'pyglow/models/dl_models/iri12/ig_rz_IPS.dat',
                'pyglow/models/dl_models/iri12/ig_rz_SEC.dat',
                'pyglow/models/dl_models/iri12/ig_rz.dat',
                'pyglow/models/dl_models/iri12/igrf2010.dat',
                'pyglow/models/dl_models/iri12/igrf2010s.dat',
                'pyglow/models/dl_models/iri12/ursi11.asc',
                'pyglow/models/dl_models/iri12/ursi12.asc',
                'pyglow/models/dl_models/iri12/ursi13.asc',
                'pyglow/models/dl_models/iri12/ursi14.asc',
                'pyglow/models/dl_models/iri12/ursi15.asc',
                'pyglow/models/dl_models/iri12/ursi16.asc',
                'pyglow/models/dl_models/iri12/ursi17.asc',
                'pyglow/models/dl_models/iri12/ursi18.asc',
                'pyglow/models/dl_models/iri12/ursi19.asc',
                'pyglow/models/dl_models/iri12/ursi20.asc',
                'pyglow/models/dl_models/iri12/ursi21.asc',
                'pyglow/models/dl_models/iri12/ursi22.asc',
            ],
        ),
        (
            'pyglow/iri16_data/',
            [
                'pyglow/models/dl_models/iri16/apf107.dat',
                'pyglow/models/dl_models/iri16/ccir11.asc',
                'pyglow/models/dl_models/iri16/ccir12.asc',
                'pyglow/models/dl_models/iri16/ccir13.asc',
                'pyglow/models/dl_models/iri16/ccir14.asc',
                'pyglow/models/dl_models/iri16/ccir15.asc',
                'pyglow/models/dl_models/iri16/ccir16.asc',
                'pyglow/models/dl_models/iri16/ccir17.asc',
                'pyglow/models/dl_models/iri16/ccir18.asc',
                'pyglow/models/dl_models/iri16/ccir19.asc',
                'pyglow/models/dl_models/iri16/ccir20.asc',
                'pyglow/models/dl_models/iri16/ccir21.asc',
                'pyglow/models/dl_models/iri16/ccir22.asc',
                'pyglow/models/dl_models/iri16/dgrf1945.dat',
                'pyglow/models/dl_models/iri16/dgrf1950.dat',
                'pyglow/models/dl_models/iri16/dgrf1955.dat',
                'pyglow/models/dl_models/iri16/dgrf1960.dat',
                'pyglow/models/dl_models/iri16/dgrf1965.dat',
                'pyglow/models/dl_models/iri16/dgrf1970.dat',
                'pyglow/models/dl_models/iri16/dgrf1975.dat',
                'pyglow/models/dl_models/iri16/dgrf1980.dat',
                'pyglow/models/dl_models/iri16/dgrf1985.dat',
                'pyglow/models/dl_models/iri16/dgrf1990.dat',
                'pyglow/models/dl_models/iri16/dgrf1995.dat',
                'pyglow/models/dl_models/iri16/dgrf2000.dat',
                'pyglow/models/dl_models/iri16/dgrf2005.dat',
                'pyglow/models/dl_models/iri16/dgrf2010.dat',
                'pyglow/models/dl_models/iri16/ig_rz.dat',
                'pyglow/models/dl_models/iri16/igrf2015.dat',
                'pyglow/models/dl_models/iri16/igrf2015s.dat',
                'pyglow/models/dl_models/iri16/mcsat11.dat',
                'pyglow/models/dl_models/iri16/mcsat12.dat',
                'pyglow/models/dl_models/iri16/mcsat13.dat',
                'pyglow/models/dl_models/iri16/mcsat14.dat',
                'pyglow/models/dl_models/iri16/mcsat15.dat',
                'pyglow/models/dl_models/iri16/mcsat16.dat',
                'pyglow/models/dl_models/iri16/mcsat17.dat',
                'pyglow/models/dl_models/iri16/mcsat18.dat',
                'pyglow/models/dl_models/iri16/mcsat19.dat',
                'pyglow/models/dl_models/iri16/mcsat20.dat',
                'pyglow/models/dl_models/iri16/mcsat21.dat',
                'pyglow/models/dl_models/iri16/mcsat22.dat',
                'pyglow/models/dl_models/iri16/ursi11.asc',
                'pyglow/models/dl_models/iri16/ursi12.asc',
                'pyglow/models/dl_models/iri16/ursi13.asc',
                'pyglow/models/dl_models/iri16/ursi14.asc',
                'pyglow/models/dl_models/iri16/ursi15.asc',
                'pyglow/models/dl_models/iri16/ursi16.asc',
                'pyglow/models/dl_models/iri16/ursi17.asc',
                'pyglow/models/dl_models/iri16/ursi18.asc',
                'pyglow/models/dl_models/iri16/ursi19.asc',
                'pyglow/models/dl_models/iri16/ursi20.asc',
                'pyglow/models/dl_models/iri16/ursi21.asc',
                'pyglow/models/dl_models/iri16/ursi22.asc',
            ],
        ),
        (
            'pyglow/kpap/',
            [
                'pyglow/kpap/1932',
                'pyglow/kpap/1933',
                'pyglow/kpap/1934',
                'pyglow/kpap/1935',
                'pyglow/kpap/1936',
                'pyglow/kpap/1937',
                'pyglow/kpap/1938',
                'pyglow/kpap/1939',
                'pyglow/kpap/1940',
                'pyglow/kpap/1941',
                'pyglow/kpap/1942',
                'pyglow/kpap/1943',
                'pyglow/kpap/1944',
                'pyglow/kpap/1945',
                'pyglow/kpap/1946',
                'pyglow/kpap/1947',
                'pyglow/kpap/1948',
                'pyglow/kpap/1949',
                'pyglow/kpap/1950',
                'pyglow/kpap/1951',
                'pyglow/kpap/1952',
                'pyglow/kpap/1953',
                'pyglow/kpap/1954',
                'pyglow/kpap/1955',
                'pyglow/kpap/1956',
                'pyglow/kpap/1957',
                'pyglow/kpap/1958',
                'pyglow/kpap/1959',
                'pyglow/kpap/1960',
                'pyglow/kpap/1961',
                'pyglow/kpap/1962',
                'pyglow/kpap/1963',
                'pyglow/kpap/1964',
                'pyglow/kpap/1965',
                'pyglow/kpap/1966',
                'pyglow/kpap/1967',
                'pyglow/kpap/1968',
                'pyglow/kpap/1969',
                'pyglow/kpap/1970',
                'pyglow/kpap/1971',
                'pyglow/kpap/1972',
                'pyglow/kpap/1973',
                'pyglow/kpap/1974',
                'pyglow/kpap/1975',
                'pyglow/kpap/1976',
                'pyglow/kpap/1977',
                'pyglow/kpap/1978',
                'pyglow/kpap/1979',
                'pyglow/kpap/1980',
                'pyglow/kpap/1981',
                'pyglow/kpap/1982',
                'pyglow/kpap/1983',
                'pyglow/kpap/1984',
                'pyglow/kpap/1985',
                'pyglow/kpap/1986',
                'pyglow/kpap/1987',
                'pyglow/kpap/1988',
                'pyglow/kpap/1989',
                'pyglow/kpap/1990',
                'pyglow/kpap/1991',
                'pyglow/kpap/1992',
                'pyglow/kpap/1993',
                'pyglow/kpap/1994',
                'pyglow/kpap/1995',
                'pyglow/kpap/1996',
                'pyglow/kpap/1997',
                'pyglow/kpap/1998',
                'pyglow/kpap/1999',
                'pyglow/kpap/2000',
                'pyglow/kpap/2001',
                'pyglow/kpap/2002',
                'pyglow/kpap/2003',
                'pyglow/kpap/2004',
                'pyglow/kpap/2005',
                'pyglow/kpap/2006',
                'pyglow/kpap/2007',
                'pyglow/kpap/2008',
                'pyglow/kpap/2009',
                'pyglow/kpap/2010',
                'pyglow/kpap/2011',
                'pyglow/kpap/2012',
                'pyglow/kpap/2013',
            ],
        ),
        (
            'pyglow/dst/',
            [
                'pyglow/dst/1957_1969',
                'pyglow/dst/1970_1989',
                'pyglow/dst/1990_2004',
            ],
        ),
        (
            'pyglow/ae/',
            [
                'pyglow/ae/1975',
                'pyglow/ae/1978',
                'pyglow/ae/1979',
                'pyglow/ae/1980',
                'pyglow/ae/1981',
                'pyglow/ae/1982',
                'pyglow/ae/1983',
                'pyglow/ae/1984',
                'pyglow/ae/1985',
                'pyglow/ae/1986',
                'pyglow/ae/1987',
                'pyglow/ae/1988',
                'pyglow/ae/1989',
                'pyglow/ae/1990',
                'pyglow/ae/1991',
                'pyglow/ae/1992',
                'pyglow/ae/1993',
                'pyglow/ae/1994',
                'pyglow/ae/1995',
                'pyglow/ae/1996',
                'pyglow/ae/1997',
                'pyglow/ae/1998',
                'pyglow/ae/1999',
            ],
        ),
    ],
)

print("... All done!")
