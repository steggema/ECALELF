#!/bin/bash
trap "kill 0" SIGINT

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

####used for 2017 UL
json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt
jsonName=294927-306462_Prompt_v1


####used for 2018 UL
json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt
jsonName=314472_325175_PromptReco



#####used for 2016 Alpha studies
json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt
jsonName=271036-284044_PromptReco


#json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt
#jsonName=294927-306462_EOY2017_ReReco

##
PERIOD=LEGACY2016
PERIOD=RUN2017EF
#PERIOD=RUN2017BCDE
PERIOD=RUN2017E
PERIOD=RUN2017F
#PERIOD=RUN2017z
#PERIOD=RUN2017MCALCARECO


#PERIOD=TEST
#PERIOD=RUN2017MCALCARECO
#
#PERIOD=RUN2017B


#PERIOD=TEST
#PERIOD=RUN2017UR
#PERIOD=RUN2018AutumnMC
#PERIOD=RUN2017URZEE

#PERIOD=RUN2018_RERECO
#PERIOD=RUN2018MCnewReg

PERIOD=RUN2016Rereco

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
tags=(  config/reRecoTags/Cal_Mar2018_Comb_cand_v9.py)
#tags=(  config/reRecoTags/94X_mc2017_realistic_v10.py)



#tags=(  config/reRecoTags/UltraRereco2017.py) ###RUN2017UR
#tags=(  config/reRecoTags/PromtReco2017_ped_ps.py) ###RUN2017UR
#tags=(  config/reRecoTags/PromptReco2017_pedv1_ps_ICv1_laserv2.py) ###RUN2017UR

#tags=(  config/reRecoTags/MC2017_laser_alpha_ped_IC_adc.py) ###RUN2017MCALCARECO
#tags=(  config/reRecoTags/MC2017.py) ###RUN2017MCALCARECO

#tags=(  config/reRecoTags/PromptReco2017_pedv1_ps_ICv1_laserv2_LC_Alpha1.py) ###RUN2017UR 
#tags=(  config/reRecoTags/PromptReco2017_pedv1_ps_ICv1_laserv2_LC_Alpha2.py) ###RUN2017UR 
#tags=(  config/reRecoTags/PromptReco2017_pedv1_ps_ICv1_laserv2_LC_Alpha3.py) ###RUN2017UR 
#tags=(  config/reRecoTags/PromptReco2017_pedv1_ps_ICv1_laserv2_LC_Alpha4.py) ###RUN2017UR 
#tags=(  config/reRecoTags/PromptReco2017_pedv1_ps_ICv1_laserv3_LC_Alpha4.py) ###RUN2017UR 
#tags=(  config/reRecoTags/UltraRereco2017_22Jan2019_phiCorrections.py) ###RUN2017UR 
#tags=(  config/reRecoTags/UltraRereco2017_2feb2019_AllCorrections.py) ###RUN2017UR 
#tags=(  config/reRecoTags/UltraRereco2017_22Jan2019_phiCorrectionsV2.py) ###RUN2017UR 
#tags=(  config/reRecoTags/PromptReco2017_103X.py) ###RUN2017UR 
#tags=(  config/reRecoTags/PromptReco2017_103X_phiSymmCor.py) ###RUN2017UR 
#tags=( config/reRecoTags/102X_mc2017_realistic_UL_v1.py )
#tags=( config/reRecoTags/102X_mc2017_realistic_UL_v1_updatedSCregression.py )

#tags=( config/reRecoTags/PromptReco2017_103X_PFrechit2018Def.py )
#tags=( config/reRecoTags/PromptReco2017_103X_PFrechit2017UL.py )
#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregression.py )
#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregression_etaScale.py )
#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregression_phiSymm.py )
#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregressionV2.py )

#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregressionV2_IntermediateICsV1.py )  ### faulty name
#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregressionV1_IntermediateICsV1.py )


#tags=( config/reRecoTags/PromptReco2017_103X_updatedSCregressionV3.py )
#tags=( config/reRecoTags/102X_mc2017_realistic_UL_v1_updatedSCregressionV3.py )
#tags=( config/reRecoTags/PromptReco2017_103X_phiSymmCor_updatedSCregressionV3.py )
#tags=( config/reRecoTags/test_updatedSCregressionV3.py )
#tags=( config/reRecoTags/PromptReco2017_103X_highEta_updatedSCregressionV3.py )
#tags=( config/reRecoTags/PromptReco2017_103X_IntermediateICsupdatedSCregressionV3.py )

#tags=( config/reRecoTags/PromptReco2017_103X_EtaScaleupdatedSCregressionV3.py )

#tags=( config/reRecoTags/102X_mc2017_realistic_UL_v1_updatedSCregressionV3_newICs.py )

#tags=( config/reRecoTags/102X_dataRun2_Sep2018Rereco_harnessCorr_newReg.py )   ###RUN2018_RERECO

#tags=(  config/reRecoTags/102X_upgrade2018_realistic_UL_v1_newReg.py)  ###  RUN2018MCALCARECOv1

#tags=(  config/reRecoTags/102X_dataRun2_Sep2018Rereco_PrelimCom_EtaScale_newReg.py)  ###  RUN2018_RERECO


#tags=(  config/reRecoTags/103X_upgrade2018_realistic_v9_newReg_ulMcCond.py)  ###  RUN2018MCnewReg
#tags=(  config/reRecoTags/102X_dataRun2_Sep2018Rereco_RefinedCom_EtaScale_newReg.py)  ###  RUN2018_RERECO 
#tags=(  config/reRecoTags/102X_dataRun2_Sep2018Rereco_Comb_PrelimEtaScale_finalMCetascale_newReg.py)  ###  RUN2018_RERECO 
#tags=(  config/reRecoTags/102X_dataRun2_Sep2018Rereco_Comb_PrelimEtaScale_finalMCetascale_newReg_Correctv2.py)  ###  RUN2018_RERECO 
#tags=(  config/reRecoTags/102X_dataRun2_Sep2018Rereco_Comb_PrelimEtaScale_finalMCetascale_newReg_Correctv3.py)  ###  RUN2018_RERECO 

#tags=(  config/reRecoTags/102X_dataRun2_Sep2018Rereco_Comb_PrelimEtaScale_finalMCetascale_newReg_FINAL.py)  ###  RUN2018_RERECO 



tags=(  config/reRecoTags/103X_dataRun2_v6_ULBaseForICs_newRegV1.py)  ###  RUN2018_RERECO 

if  git status --porcelain -uno | grep -v launch | grep -v ZFitter | grep -q -v _datasets  ; then
	echo "You have uncommitted changes, please commit everything before making a production" 
#	exit 1
else
	GITCOMMIT=`git rev-parse HEAD`
	if [ "`git rev-parse HEAD`" != "`git rev-parse origin/master`" ];then
		echo "[ERROR] You are not allowed to make any production if all commits are propagated to the master branch of the repository" >> /dev/stderr
#		exit 2
	fi
fi


for tagfile in ${tags[@]}
do
	echo
#	./scripts/removeRereco.sh -t $tagfile -f alcarereco_datasets.dat
#	./scripts/removeRereco.sh -t $tagfile -f ntuple_datasets.dat --json_name=$jsonName
#	continue

	for CHECK in '' --check
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
				echo 
				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name=$jsonName ${CHECK} --alcarerecoOnly 
				./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json=$json --json_name=$jsonName ${CHECK} --alcarerecoOnly --singleEle 
				#./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile  --json_name="noJSON" ${CHECK} --alcarerecoOnly   ###MC
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
			#./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --ntupleOnly  $CHECK     ###MC
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK 
			./scripts/RerecoQuick.sh -p ${PERIOD} -t $tagfile --json=$json --json_name=$jsonName --ntupleOnly  $CHECK --singleEle
			
				 ;;
		esac
	done

done
exit 0
