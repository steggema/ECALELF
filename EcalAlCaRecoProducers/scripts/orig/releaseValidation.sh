#!/bin/bash
bold=$(tput bold)
normal=$(tput sgr0)

function testStep(){
	stepIndex=$1
	stepString=$2
	stepLog=$3
	stepCommand=$4
	
	dir=tmp/releaseValidation/$CMSSW_VERSION/$stepIndex
	if [ ! -d "$dir" ];then mkdir $dir; fi

	if [ -e "$dir/done" ]; then
		echo  "[`basename $0`] $stepString OK "
		return 0
	fi
	if [ ! -e "$dir/$stepLog.log" ];then
		echo -n "[`basename $0`] $stepString ... "
		cd $dir
		$stepCommand &> $stepLog.err || {
			echo "\n\t\t${bold}ERROR${normal}"
			echo "See $dir/$stepLog.err"
			cat $stepLog.err
			exit 1
		}
		cd -
		mv $dir/$stepLog.{err,log}
		echo "OK"
	else
		echo "[`basename $0`] $stepString already done and OK"
	fi
	return 1
}
	
############################################################
# script to make sure that the new release is not breaking things
############################################################

echo "[`basename $0`] CMSSW RELEASE: $CMSSW_VERSION"
if [ ! -d "tmp/releaseValidation/$CMSSW_VERSION" ];then mkdir tmp/releaseValidation/$CMSSW_VERSION -p; fi

case $CMSSW_VERSION in
	CMSSW_8_0_*|CMSSW_9_2_*|CMSSW_9_4_*|CMSSW_10_*_*)
		case $USER in
			##gitlab-runner)
			##	fileMINIAOD=file:$HOME/fileMINIAOD.root
			##	fileMINIAODData=file:$HOME/fileMINIAODData.root
			##	fileALCARAWData=file:$HOME/fileALCARAWData.root
			##	;;
		    *)
			#fileMINIAOD=/store/mc/RunIISpring16MiniAODv1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/008099CA-5501-E611-9AAE-24BE05BDCEF1.root
			#fileMINIAODData=/store/data/Run2016B/DoubleEG/MINIAOD/23Sep2016-v3/00000/F48EC9B9-A197-E611-BBBE-001E6739753A.root
			#fileALCARAWData=/store/data/Run2016B/DoubleEG/ALCARECO/EcalUncalZElectron-PromptReco-v2/000/275/376/00000/6EB9C0F0-E639-E611-AAD9-02163E014492.root
			#fileAODSIM=/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/20000/F28F765D-A3FB-E511-B7F4-3417EBE64699.root

			fileMINIAOD=/store/mc/RunIISpring18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/100X_upgrade2018_realistic_v10-v2/10000/F24C5C06-FF47-E811-9C2F-FA163EC3CAD1.root
			fileMINIAODData=/store/data/Run2018A/EGamma/MINIAOD/PromptReco-v1/000/315/252/00000/40343760-464B-E811-ACC9-02163E00B0CB.root
			fileALCARAWData=/store/data/Run2018A/EGamma/ALCARECO/EcalUncalZElectron-PromptReco-v1/000/315/357/00000/104293B5-5A4D-E811-97B4-FA163E6E3B50.root
			fileAODSIM=/store/mc/RunIISpring18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/100X_upgrade2018_realistic_v10-v2/10000/34E5F3D5-B847-E811-9F35-FA163E88F090.root
		;;
		esac
		json=$PWD/test/releaseValidation.json
#/store/data/Run2016H/DoubleEG/ALCARECO/EcalUncalZElectron-PromptReco-v3/000/284/036/00000/240108A1-599F-E611-A3A5-FA163E7F2F56.root
		;;
	*)
		echo "CMSSW RELEASE not supported" >> /dev/stderr
		exit 1
		;;
esac


############################################################
# production in local of ntuples from MINIAOD
logName=ntuple_miniaodsim_mc
testStep 1 "Testing local production of ntuples from MINIAODSIM (MC)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_mcRun2_asymptotic_2016_miniAODv2.py type=MINIAODNTUPLE maxEvents=-1 doTree=1 doEleIDTree=1 files=$fileMINIAOD outputAll=False isCrab=0" || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump | colordiff --difftype=wdiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}


################
logName=ntuple_miniaodsim_data
echo "python $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=MINIAODNTUPLE maxEvents=-1 doTree=1 doEleIDTree=1 files=$fileMINIAODData outputAll=False jsonFile=$PWD/$json isCrab=0"
testStep 2 "Testing local production of ntuples from MINIAODSIM (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=MINIAODNTUPLE maxEvents=-1 doTree=1 doEleIDTree=1 files=$fileMINIAODData outputAll=False jsonFile=$json isCrab=0" || {
	
	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump | colordiff --difftype=wdiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}


################
logName=alcarereco_data
testStep 3 "Testing local production of alcarereco from DATA" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/Cal_Mar2017_PNcorr_v2_noPed.py type=ALCARERECO maxEvents=-1 doTree=0 doEleIDTree=0 files=$fileALCARAWData outputAll=False jsonFile=$json isCrab=0" || {
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}

################
logName=ntuple_alcarereco_data
#echo "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=ALCARERECO maxEvents=-1 doTree=1 doEleIDTree=1 doTreeOnly=1 files=file:$PWD/$dir/EcalRecalElectron.root outputAll=False jsonFile=$json"
testStep 4 "Testing local production of ntuples from alcarereco (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=ALCARERECO maxEvents=-1 doTree=1 doEleIDTree=1 doTreeOnly=1 files=file:$PWD/$dir/EcalRecalElectron.root outputAll=False jsonFile=$json" || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test/releaseValidation/$CMSSW_VERSION}/${logName}.dump | colordiff --difftype=wdiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}

exit 0
################
logName=alcareco_mc
testStep 5 "Testing local production of ALCARECOSIM from AODSIM (MC)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_mcRun2_asymptotic_2016_v3.py type=ALCARECOSIM maxEvents=-1 doTree=0 doEleIDTree=0 doTreeOnly=0 files=$fileAODSIM outputAll=False jsonFile= skim=ZSkim isCrab=0" || {

	echo -n "[`basename $0`] Checking difference in dump of alcarecosim content ... "
	edmEventSize -v $dir/alcareco.root > $logName.dump || exit 1

	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff --difftype=wdiff  | less -RS"
		exit 1
	}

	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}

################
logName=ntuple_alcareco_mc
testStep 6 "Testing local production of ntuples from alcareco (MC)" $logName "cmsRun $PWD/python/alcaSkimming.py type=ALCARECOSIM doTree=1 doExtraCalibTree=0 doExtraStudyTree=0 doEleIDTree=1 doTreeOnly=1  jsonFile= isCrab=1 skim=ZSkim tagFile=$PWD/config/reRecoTags/80X_mcRun2_asymptotic_2016_v3.py isPrivate=0  bunchSpacing=0 files=file:$PWD/tmp/releaseValidation/5/alcareco.root " || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff --difftype=wdiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}

exit 0
################
logName=alcarereco_data
testStep 5 "Testing local production of ALCARECO from AODSIMalcarereco (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/Cal_Nov2016_ped_v3.py type=ALCARERECO maxEvents=-1 doTree=0 doEleIDTree=0 doTreeOnly=0 files=$fileAODSIM outputAll=False jsonFile=$json  isCrab=0" || {
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}


################
logName=ntuple_alcarereco_data
testStep 6 "Testing local production of ntuples from alcarereco (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/Cal_Nov2016_ped_v3.py type=ALCARERECO maxEvents=-1 doTree=1 doEleIDTree=1 doTreeOnly=1 files=file:$PWD/$dir/EcalRecalElectron.root outputAll=False jsonFile=$json isCrab=0" || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff --difftype=wdiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}





exit 0


