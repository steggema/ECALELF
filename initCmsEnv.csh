#!/bin/tcsh

source /cvmfs/cms.cern.ch/crab3/crab.csh

switch ($USER)
    default:
       voms-proxy-init -voms cms -out $HOME/gpi.out    
endsw

#PATH=$PATH:/afs/cern.ch/project/eos/installation/pro/bin/
setenv PATH ${PATH}:${CMSSW_BASE}/src/Calibration/EcalAlCaRecoProducers/bin
#PATH=$PATH:$HOME/scratch0/LSFsubmit
echo "[CMSSW] " ${CMSSW_BASE}
#echo "[CRAB3] " $(which crab) 

setenv ECALELFINIT y

