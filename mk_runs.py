#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2014ARSRCommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['I10565'] = [ 33551, 33552, 33848, 33849, 33905, 33906]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['I10565']   = "linecheck=1"

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2['I10565']   = "srdp=1 admit=0"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
