#!/bin/bash
trap "kill 0" SIGINT

#DOCHECK=( --check)
DOCHECK=( '')

json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt
jsonName=271036_276811-ICHEP

json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-279588_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt
jsonName=271036_279588-Prompt


json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-305364_13TeV_PromptReco_Collisions17_JSON.txt
jsonName=294927-305364_Prompt_v1

json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
jsonName=271036_284044-23Sep2016

json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306126_13TeV_PromptReco_Collisions17_JSON.txt
jsonName=294927-306126_Prompt_v1

json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt
jsonName=294927-306462_Prompt_v1

json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/DCSOnly/json_DCSONLY.txt
jsonName=2018_2May_json_DCS

#json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt
#jsonName=294927-306462_EOY2017_ReReco
##
PERIOD=LEGACY2016
PERIOD=RUN2017EF
#PERIOD=RUN2017BCDE
PERIOD=RUN2017E
PERIOD=RUN2017F
#PERIOD=RUN2017
#PERIOD=RUN2017MCALCARECO
#
#PERIOD=RUN2018A_2018-05-04 # DATA#

#PERIOD=RUN2018A_2018-05-08 # DATA#
#PERIOD=RUN2018A_2018-05-10 # DATA#
#PERIOD=RUN2018A_2018-05-14 # DATA#
#PERIOD=RUN2018A_2018-05-16 # DATA#
#PERIOD=RUN2018A_2018-05-17 # DATA#
#PERIOD=RUN2018A_2018-05-20 # DATA#
#PERIOD=RUN2018A_2018-05-22 # DATA#
#PERIOD=RUN2018A_2018-05-25 # DATA#
#PERIOD=RUN2018A_2018-05-31_NPT # DATA#
#PERIOD=RUN2018A_2018-05-31_PP # DATA# ---> till here
#PERIOD=RUN2018A_2018-05-31_NT # DATA#
#PERIOD=RUN2018A_2018-06-06 # DATA#
#PERIOD=RUN2018B_2018-06-06 # DATA#
#PERIOD=RUN2018A_NPT_rerecoAndrea # DATA#

#PERIOD=RUN2018A_2018-05-1_AT # DATA#
#PERIOD=RUN2018A_2018-05-3_AT # DATA#
#PERIOD=RUN2018A_2018-05-6_AT # DATA#
#PERIOD=RUN2018A_2018-05-10_AT # DATA#
#PERIOD=RUN2018A_2018-05-17_AT # DATA#
#PERIOD=RUN2018A_2018-05-24_AT # DATA#
#PERIOD=RUN2018A_2018-05-31_AT # DATA#

#PERIOD=ESCalibHG_316766
#PERIOD=ESCalibLG_316766


#PERIOD=RUN2018Av1Rereco_2018
#PERIOD=RUN2018Av1v2_2018
#PERIOD=RUN2018Av3_2018
#PERIOD=RUN2018Bv1_2018
#PERIOD=RUN2018Bv2_2018
#PERIOD=RUN2018C_2018


#PERIOD=RUN2018Bv1_missingRuns
#PERIOD=RUN2018Bv2_missingRuns


#PERIOD=RUN2018D_2018-08-16

#PERIOD=RUN2018D_preshowerOffChecks322088
#
PERIOD=RUN2018Dv1HG
#PERIOD=RUN2018Dv1LG
#PERIOD=RUN2018Dv2HG
#PERIOD=RUN2018Dv2LG

#PERIOD=RUN2018MCALCARECOv1

#PERIOD=RUN2018D_2018-10-09
PERIOD=RUN2018D_2018-10-22

tags=(  config/reRecoTags/Cal_Nov2017_{ref,IC}_v1.py  )
tags=(  config/reRecoTags/Cal_Oct2017_cand_v6.py )
tags=(  config/reRecoTags/Cal_Oct2017_cand_v7.py )
tags=(  config/reRecoTags/94X_EOY17V2_ICTag_eopPNEB_etaScalePNEE_v9.py )
tags=(  config/reRecoTags/Cal_Feb2018_cand_v1.py)
tags=(  config/reRecoTags/Cal_Feb2018_cand_v2.py)
tags=(  config/reRecoTags/Cal_Feb2018_cand_v3.py)
#tags=(  config/reRecoTags/Cal_Mar2018_NewComb_cand_v1.py)
#tags=(  config/reRecoTags/Cal_Mar2018_NewComb_cand_v2.py)
#tags=(  config/reRecoTags/Cal_Mar2018_cand_v3.py)
#tags=(  config/reRecoTags/Cal_Mar2018_cand_v4.py)
#tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v3.py)
#tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v4.py)
#tags=(  config/reRecoTags/Cal_Mar2018_cand_v5.py)
tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v5.py)
tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v6.py)
tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v7.py)
tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v8.py)
#tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v9.py)
#tags=(  config/reRecoTags/94X_mc2017_realistic_v10.py)

#######tags in 2018
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_correctRunRange.py)
#tags=(  config/reRecoTags/EcalPedestals_timestamp_10May2018_collisions_blue_laser_cRR.py)

#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9.py)
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10.py)
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v11.py)
#tags=(  config/reRecoTags/EcalPedestals_timestamp_10May2018_collisions_blue_laser.py)
#tags=(  config/reRecoTags/EcalPedestals_10May2018_collisions_blue_laser_Rereco.py)


#tags=(  config/reRecoTags/ESIntercalibConstants_LG_Run2018A_EcalPed10May_GTv9.py)
#tags=(  config/reRecoTags/ESIntercalibConstants_LG_Run2018A_v9.py)
#tags=(  config/reRecoTags/ESIntercalibConstants_LG_Run2018A_v10.py)

####Alpha tags from Francesco
###0095
#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_laser_AT095.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_AT095.py)  ##10th till 24th
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10_AT095.py)  ##after 31st may

#####08
#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_laser_AT08.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_AT08.py)  ##10th till 24th
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10_AT08.py)  ##after 31st may

#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_laser_AT05.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_AT05.py)  ##10th till 24th
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10_AT05.py)  ##after 31st may


#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_laser_AT075.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_AT075.py)  ##10th till 24th
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10_AT075.py)  ##after 31st may

#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_laser_AT07.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_AT07.py)  ##10th till 24th
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10_AT07.py)  ##after 31st may


#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_EB152-150_EEbyring.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_EB152-150_EEbyring.py)  ##10th till 24th

#tags=(  config/reRecoTags/EcalPedestals_10May2018_blue_EB152-150_EE100-1-075.py)  ##1st may till 6th may
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_EB152-150_EE100-1-075.py)  ##10th till 24th

#tags=(  config/reRecoTags/ESIntercalibConstants_HG_GTv10.py)  ##HG MIP
#tags=(  config/reRecoTags/ESIntercalibConstants_LG_GTv10.py)  ##LG MIP


#tags=(  config/reRecoTags/EcalPedestals_31May2018_collisions_blue_laser_v9.py)  ##

#tags=(  config/reRecoTags/102X_dataRun2_Prompt_v1.py)
#tags=(  config/reRecoTags/102X_dataRun2_Prompt_v4.py)  ### RUN2018D_preshowerOffChecks322088 

#tags=(  config/reRecoTags/102X_dataRun2_Prompt_v6.py)  ### RUN2018D_preshowerOffChecks322088 

#tags=(  config/reRecoTags/ESIntercalibConstants_HG_Run2018D1.py)  ###  RUN2018Dv1HG
#tags=(  config/reRecoTags/ESIntercalibConstants_LG_Run2018D1.py)  ###  RUN2018Dv1LG
#tags=(  config/reRecoTags/ESIntercalibConstants_HG_Run2018D2.py)  ###  RUN2018Dv2HG
#tags=(  config/reRecoTags/ESIntercalibConstants_LG_Run2018D2.py)  ###  RUN2018Dv2LG

#tags=(  config/reRecoTags/102X_upgrade2018_realistic_v11.py)  ###  RUN2018MCALCARECOv1

#tags=(  config/reRecoTags/102X_dataRun2_Prompt_v6.py)  ####RUN2018MCALCARECOv1

tags=(  config/reRecoTags/102X_dataRun2_Prompt_v7.py)  ####RUN2018D_2018-10-22


####RERECO, PED, PULSE SHAPE etc
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_forECALReReco_Ped17July_PSJuly2018.py)  ##RUN2018Av1Rereco_2018
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v9_Ped17July_PSJuly2018.py)  ##RUN2018Av1v2_2018
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v10_Ped17July_PSJuly2018.py)  ##RUN2018Av3_2018, RUN2018Bv1_2018
#tags=(  config/reRecoTags/101X_dataRun2_Prompt_v11_Ped25July_PSJuly2018.py)  ##RUN2018Bv2_2018, RUN2018C_2018

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

for tagfile in ${tags[@]}
do
	echo
#	./scripts/removeRereco.sh -t $tagfile -f alcarereco_datasets.dat
#	./scripts/removeRereco.sh -t $tagfile -f ntuple_datasets.dat --json_name=$jsonName
#	continue

	for CHECK in '' --check
#	for CHECK in ${DOCHECK[@]}
	do
		case $tagfile in 
			*/Cal_Mar2018_Comb_cand_v9.py)
				#./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name="noJSON" ${CHECK} --alcarerecoOnly  --singleEle --weightsReco
#				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name="noJSON" ${CHECK} --alcarerecoOnly --singleEle
                                ./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name="noJSON" ${CHECK} --alcarerecoOnly
#				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName  ${CHECK} --alcarerecoOnly
				#./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name="noJSON" ${CHECK} --alcarerecoOnly 
#				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name="noJSON" ${CHECK} --alcarerecoOnly  --weightsReco
				;;
		    *)
			echo "tagfile is "$tagfile
			echo "CHECK is " $CHECK
			echo "Running:  ./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name=$jsonName ${CHECK} --alcarerecoOnly --singleEle "
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name=$jsonName ${CHECK} --alcarerecoOnly --singleEle 
			
			
		        echo "Running:  ./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name=$jsonName ${CHECK} --alcarerecoOnly "
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name=$jsonName ${CHECK} --alcarerecoOnly 
			;;
		esac
	done

	for CHECK in  '' --check
	do
		case $tagfile in 
		    */Cal_Mar2018_cand_v1.py)
#				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK --singleEle --weightsReco
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK 
#				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK 
#				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK --weightsReco 
			;;

		    *)
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK --singleEle
			;;	
		esac
	done

done
exit 0
