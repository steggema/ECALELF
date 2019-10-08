#!/bin/bash
trap "kill 0" SIGINT

#DOCHECK=( --check)
DOCHECK=( '')


fileList=alcareco_datasets.dat

#PERIOD=RUN2018Av1v2Scale
#PERIOD=RUN2018Av3Bv1Scale
#PERIOD=RUN2018Bv2CScale

#PERIOD=RUN2018MCScale

#######2018 Jan SS
#PERIOD=RUN2018DScale
#PERIOD=RUN2018EScale
#PERIOD=RUN2018ABCRereco
#PERIOD=RUN2018MCAutumnScale
#PERIOD=RUN2018MCMADAutumnScale
#######2018 Jan SS

######PERIOD=RUN2018MCGTChecks



#json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt
json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt
jsonName=2018_314472-325175_Prompt



tagfileAv1v2=config/reRecoTags/101X_dataRun2_Prompt_v9.py  ###  RUN2018Av1v2Scale
tagfileAv3Bv1=config/reRecoTags/101X_dataRun2_Prompt_v10.py  ###  RUN2018Av3Bv1Scale
tagfileBv2C=config/reRecoTags/101X_dataRun2_Prompt_v11.py  ###  RUN2018Bv2CScale
tagfileMC=config/reRecoTags/102X_upgrade2018_realistic_v12.py

#######2018 Jan SS
tagfileD=config/reRecoTags/102X_dataRun2_Prompt_v1.py  ###  RUN2018D
tagfileE=config/reRecoTags/102X_dataRun2_Prompt_v11.py  ###  RUN2018E
tagfileRerecoABC=config/reRecoTags/102X_dataRun2_Sep2018Rereco_v1.py ###RUN2018ABCRereco
tagfileAutumnMC=config/reRecoTags/102X_upgrade2018_realistic_v15.py
#######2018 Jan SS

tagfileMCGTChecks=config/reRecoTags/103X_mc2017_realistic_v2_AB_v01.py




# set IFS to newline in order to divide using new line the datasets
IFS=$'\n'
datasetsData=(`./scripts/parseDatasetFile.sh $fileList | grep VALID | sed 's|$|,|' | grep "${PERIOD}," | grep -v SIM`)
datasetsMC=(`./scripts/parseDatasetFile.sh $fileList | grep VALID | sed 's|$|,|' | grep "${PERIOD}," | grep SIM`)



echo $datasetsData
echo $datasetsMC

#if  git status --porcelain -uno | grep -v launch | grep -v ZFitter | grep -q -v _datasets  ; then
#	echo "You have uncommitted changes, please commit everything before making a production" 
##	exit 1
#else
#	GITCOMMIT=`git rev-parse HEAD`
#	if [ "`git rev-parse HEAD`" != "`git rev-parse origin/master`" ];then
#		echo "[ERROR] You are not allowed to make any production if all commits are propagated to the master branch of the repository" >> /dev/stderr
##		exit 2
#	fi
#fi

istep=0

#for dataset in ${datasetsData[@]} 
for dataset in ${datasetsMC[@]} 
do
    datasetName=`echo $dataset | awk '{print $6}'`
    echo $datasetName

    for CHECK in  '' --check
    do
	case $datasetName in 
	    *A-noSkim-Prompt-v1*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileAv1v2} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *A-noSkim-Prompt-v2*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileAv1v2} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;
	    *A-noSkim-Prompt-v3*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileAv3Bv1} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *B-noSkim-Prompt-v1*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileAv3Bv1} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *B-noSkim-Prompt-v2*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileBv2C} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *C-noSkim-Prompt-v1*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileBv2C} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *C-noSkim-Prompt-v2*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileBv2C} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;
	    *C-noSkim-Prompt-v3*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileBv2C} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *D-noSkim-Prompt-v1*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileD} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *D-noSkim-Prompt-v2*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileD} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;

	    *E-noSkim-Prompt-v1*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileE} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    DYJetsToLL_M50_CP5madgraphMLM-RunIIFall18MiniAOD)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileMC} -s noSkim --isMC --scheduler=caf --extraName=Moriond18_Scale $CHECK  ${dataset}  
			;;	
	
	    *17Sep2018*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileRerecoABC} -s noSkim --scheduler=caf --json=$json --json_name=$jsonName --extraName=Moriond18_Scale $CHECK  ${dataset}  --doEleIDTree
			;;	

	    *MLMAutumn18Mini*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileAutumnMC} -s noSkim --isMC --scheduler=caf --extraName=Moriond18_Scale $CHECK  ${dataset}   --doEleIDTree
		;;	

	    *MADAutumn18Mini*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileAutumnMC} -s noSkim --isMC --scheduler=caf --extraName=Moriond18_Scale $CHECK  ${dataset}   --doEleIDTree
		;;	

	    *RelValZEE_13*)
		echo "Running the script for dataset "$datasetName
		./scripts/prodNtuples.sh --type=MINIAOD -t ${tagfileMCGTChecks} -s noSkim --isMC --scheduler=caf --extraName=Moriond18MCChecks $CHECK  ${dataset}   --doEleIDTree
		;;	

	    
	
	esac
    done
    
done
exit 0


		#./scripts/prodNtuples.sh --type=MINIAOD --isMC -t $tagfile -s noSkim --scheduler=caf --extraName=Moriond18_Scale --doEleIDTree $CHECK  ${dataset}
