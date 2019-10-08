import FWCore.ParameterSet.Config as cms

process = cms.Process("ALCARERECO")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:20F82BE5-F997-E811-B597-02163E019F46.root'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange( (
        "314472:55-314472:89", "314473:1-314473:18", "314474:1-314474:18", "314475:1-314475:18", "314476:1-314476:17", 
        "314477:1-314477:17", "314478:1-314478:12", "314479:1-314479:12", "314480:1-314480:13", "314481:1-314481:13", 
        "314482:1-314482:12", "314483:1-314483:12", "314485:1-314485:13", "314486:1-314486:13", "314487:1-314487:15", 
        "314488:1-314488:13", "314490:1-314490:13", "314491:1-314491:13", "314492:1-314492:19", "314494:1-314494:22", 
        "314495:1-314495:14", "314496:1-314496:15", "314497:1-314497:12", "314498:1-314498:12", "314499:1-314499:13", 
        "314500:1-314500:12", "314501:1-314501:12", "314502:1-314502:12", "314503:1-314503:12", "314504:1-314504:12", 
        "314506:1-314506:17", "314507:1-314507:13", "314508:1-314508:14", "314509:1-314509:12", "314510:1-314510:12", 
        "314511:1-314511:14", "314512:1-314512:12", "314513:1-314513:12", "314515:1-314515:75", "314521:1-314521:7", 
        "314521:9-314521:48", "314524:1-314524:12", "314527:1-314527:13", "314557:1-314557:23", "314558:1-314558:36", 
        "314559:1-314559:11", "314560:1-314560:11", "314562:1-314562:11", "314563:1-314563:23", "314564:1-314564:25", 
        "314565:1-314565:26", "314566:1-314566:26", "314567:1-314567:27", "314568:1-314568:2", "314570:1-314570:25", 
        "314571:1-314571:27", "314572:1-314572:23", "314573:1-314573:23", "314574:1-314574:9", "314574:13-314574:339", 
        "314575:1-314575:25", "314649:37-314649:64", "314649:67-314649:76", "314649:78-314649:86", "314650:1-314650:23", 
        "314650:26-314650:54", "314650:56-314650:74", "314650:76-314650:84", "314650:86-314650:104", "314650:106-314650:114", 
        "314650:116-314650:145", "314650:147-314650:155", "314650:157-314650:165", "314650:167-314650:175", "314650:177-314650:186", 
        "314650:189-314650:287", "314650:289-314650:297", "314650:299-314650:318", "314650:320-314650:328", "314650:330-314650:340", 
        "314650:344-314650:412", "314650:414-314650:453", "314650:455-314650:473", "314650:475-314650:483", "314650:485-314650:495", 
        "314650:499-314650:537", "314650:539-314650:597", "314650:599-314650:608", "314650:610-314650:618", "314650:620-314650:638", 
        "314650:641-314650:649", "314650:652-314650:664", "314651:1-314651:6", "314652:1-314652:13", "314653:1-314653:12", 
        "314654:1-314654:12", "314655:1-314655:12", "314656:1-314656:12", "314657:1-314657:12", "314658:1-314658:12", 
        "314659:1-314659:12", "314660:1-314660:12", "314661:1-314661:11", "314662:1-314662:13", "314663:1", 
        "314663:5-314663:13", "314663:15-314663:24", "314663:26-314663:34", "314663:36-314663:44", "314663:46-314663:54", 
        "314663:57-314663:75", "314663:77-314663:85", "314663:87-314663:96", "314663:99-314663:127", "314663:129-314663:138", 
        "314663:141-314663:149", "314663:151-314663:160", "314663:162-314663:170", "314663:172-314663:181", "314663:184-314663:198", 
        "314663:201-314663:209", "314663:211-314663:219", "314663:221-314663:229", "314663:231-314663:240", "314663:242-314663:250", 
        "314663:252-314663:260", "314663:262-314663:270", "314663:272-314663:280", "314663:283-314663:291", "314663:293-314663:301", 
        "314663:303-314663:312", "314663:314-314663:322", "314663:325-314663:334", "314663:336-314663:344", "314663:346-314663:354", 
        "314663:356-314663:365", "314663:367-314663:375", "314663:377-314663:385", "314663:387-314663:395", "314663:397-314663:406", 
        "314663:408-314663:416", "314663:418-314663:447", "314663:449-314663:457", "314663:505-314663:526", "314664:1-314664:184", 
        "314665:1-314665:13", "314747:52-314747:62", "314748:1-314748:29", "314750:1-314750:9", "314751:1-314751:9", 
        "314752:1-314752:10", "314753:1-314753:2", "314754:1-314754:12", "314755:1-314755:61", "314755:65-314755:347", 
        "314755:349-314755:352", "314756:1-314756:211", "314758:1-314758:21", "314759:1-314759:680", "314764:1-314764:247", 
        "314810:12-314810:121", "314811:1-314811:784", "314816:33-314816:1082", "314859:22-314859:79", "314860:1-314860:55", 
        "314861:1-314861:16", "314863:1-314863:35", "314864:1-314864:48", "314865:1-314865:28", "314867:1-314867:48", 
        "314870:1-314870:29", "314872:1-314872:10", "314873:1-314873:34", "314874:1-314874:38", "314875:1-314875:151", 
        "314876:1-314876:43", "314878:1-314878:537", "314890:49-314890:1433", "315104:39-315104:266", "315105:1-315105:3", 
        "315106:1-315106:565", "315107:1-315107:455", "315108:1-315108:146", "315150:57-315150:122", "315151:1-315151:77", 
        "315154:1-315154:200", "315157:1-315157:17", "315159:1-315159:154", "315172:1-315172:318", "315179:33-315179:65", 
        "315180:1-315180:21", "315187:38-315187:43", "315188:1-315188:305", "315189:1-315189:383", "315190:1-315190:96", 
        "315257:1-315257:88", "315257:91-315257:92", "315258:1", "315259:1-315259:172", "315264:32-315264:261", 
        "315265:4-315265:58", "315267:1-315267:244", "315268:1-315268:3", "315270:1-315270:633", "315322:23-315322:118", 
        "315322:122-315322:1354", "315339:37-315339:654", "315357:44-315357:732", "315357:736-315357:770", "315357:780-315357:831", 
        "315361:40-315361:623", "315363:1-315363:136", "315365:1-315365:25", "315366:1-315366:750", "315420:28-315420:920", 
        "315420:924-315420:942", "315420:954-315420:1748", "315488:42-315488:1113", "315489:1-315489:709", "315490:1-315490:24", 
        "315506:13-315506:100", "315509:1-315509:53", "315510:1-315510:345", "315512:1-315512:1122", "315543:55-315543:171", 
        "315555:22-315555:97", "315556:1-315556:26", "315557:1-315557:279", "315640:46-315640:87", "315641:1-315641:4", 
        "315642:1-315642:92", "315644:1-315644:184", "315645:1-315645:594", "315646:1-315646:1033", "315647:1-315647:58", 
        "315648:1-315648:111", "315689:24-315689:1186", "315690:1-315690:654", "315702:38-315702:113", "315703:1-315703:545", 
        "315704:1-315704:62", "315705:1-315705:700", "315713:35-315713:1123", "315721:33-315721:626", "315741:34-315741:92", 
        "315764:37-315764:309", "315770:39-315770:332", "315784:29-315784:200", "315785:1-315785:198", "315785:201-315785:305", 
        "315786:1-315786:72", "315788:1-315788:3", "315789:1-315789:3", "315790:1-315790:922", "315800:41-315800:651", 
        "315801:1-315801:344", "315840:33-315840:1154", "315973:39-315973:914", "315974:1-315974:71", "316058:42-316058:405", 
        "316059:1-316059:567", "316060:1-316060:935", "316061:1-316061:23", "316061:194-316061:206", "316062:1-316062:4", 
        "316082:37-316082:407", "316109:34-316109:45", "316110:1-316110:210", "316111:1-316111:48", "316112:1-316112:9", 
        "316113:1-316113:68", "316114:1-316114:777", "316114:779-316114:1562", "316151:5", "316153:1-316153:770", 
        "316186:38-316186:81", "316187:1-316187:1091", "316187:1093-316187:1100", "316187:1207-316187:2077", "316199:33-316199:1197", 
        "316200:1-316200:10", "316201:1-316201:498", "316202:1-316202:403", "316216:25-316216:466", "316217:1-316217:264", 
        "316218:1-316218:1023", "316219:1-316219:283", "316239:38-316239:629", "316240:1-316240:1233", "316241:1-316241:325", 
        "316271:36-316271:122", "316361:22-316361:223", "316362:1-316362:450", "316363:1-316363:49", "316377:19-316377:40", 
        "316378:1-316378:29", "316379:1-316379:70", "316380:1-316380:1213", "316441:1-316441:6", "316455:36-316455:71", 
        "316456:1-316456:2", "316457:1-316457:1455", "316469:17-316469:645", "316470:1-316470:476", "316472:1-316472:333", 
        "316505:44-316505:1364", "316569:20-316569:1945", "316590:17-316590:526", "316613:49-316613:241", "316614:1-316614:2", 
        "316615:1-316615:338", "316664:1-316664:13", "316665:1-316665:247", "316666:1-316666:981", "316667:1-316667:197", 
        "316700:46-316700:346", "316700:388-316700:397", "316701:1-316701:479", "316702:1-316702:388", "316715:33-316715:74", 
        "316716:1-316716:181", "316717:1-316717:192", "316718:1-316718:348", "316719:1-316719:144", "316720:1-316720:182", 
        "316721:1-316721:27", "316722:1-316722:751", "316723:1-316723:64", "316758:11-316758:1609", "316766:51-316766:2199", 
        "316876:34-316876:654", "316877:1-316877:401", "316879:1-316879:156", "316928:40-316928:188", "316944:41-316944:1831", 
        "316985:33-316985:503", "316993:44-316993:254", "316994:1-316994:20", "316995:1-316995:623", "317080:41-317080:66", 
        "317087:43-317087:177", "317087:213-317087:222", "317087:257-317087:852", "317088:1-317088:25", "317089:1-317089:1003", 
        "317182:47-317182:1424", "317212:36-317212:175", "317213:1-317213:375", "317279:43-317279:508", "317291:34-317291:838", 
        "317292:1-317292:350", "317295:1-317295:19", "317296:1-317296:103", "317297:1-317297:760", "317319:44-317319:182", 
        "317320:1-317320:411", "317320:413-317320:1828", "317338:66-317338:107", "317339:1-317339:176", "317340:1-317340:418", 
        "317382:58-317382:128", "317383:1-317383:58", "317391:39-317391:46", "317392:1-317392:1900", "317434:48-317434:257", 
        "317435:1-317435:1397", "317438:1-317438:68", "317438:71-317438:309", "317475:33-317475:89", "317475:105-317475:115", 
        "317478:1-317478:23", "317479:1-317479:18", "317480:1-317480:14", "317481:1-317481:20", "317482:1-317482:25", 
        "317484:1-317484:448", "317484:467-317484:514", "317484:519-317484:545", "317488:1-317488:844", "317509:23-317509:353", 
        "317510:1-317510:11", "317511:1-317511:412", "317512:1-317512:443", "317527:41-317527:1487", "317591:43-317591:334", 
        "317626:40-317626:2045", "317640:29-317640:829", "317641:1-317641:1390", "317648:45-317648:139", "317649:1-317649:621", 
        "317650:1-317650:1304", "317661:35-317661:1336", "317663:1-317663:858", "317683:83-317683:402", "317696:38-317696:682", 
        "318733:1-318733:33", "318816:51-318816:210", "318819:1-318819:34", "318820:1-318820:65", "318828:54-318828:123", 
        "318872:16-318872:287", "318874:1-318874:320", "318876:1-318876:161", "318877:1-318877:615", "318944:1-318944:7", 
        "319077:52-319077:92", "319310:124-319310:125", "319337:48-319337:2240", "319347:40-319347:690", "319348:1-319348:37", 
        "319349:1-319349:148", "319449:35-319449:734", "319450:1-319450:683", "319456:138-319456:346", "319459:1-319459:78", 
        "319486:38-319486:103", "319503:1-319503:317", "319524:36-319524:1459", "319526:1-319526:282", "319527:1-319527:3", 
        "319528:1-319528:259", "319579:41-319579:3168", "319625:17-319625:206", "319639:31-319639:1509", "319656:51-319656:310", 
        "319657:1-319657:167", "319658:1-319658:225", "319659:1-319659:87", "319678:36-319678:294", "319687:46-319687:90", 
        "319697:47-319697:490", "319698:1-319698:312", "319756:44-319756:1966", "319840:41-319840:388", "319841:1-319841:167", 
        "319847:49-319847:51", "319848:1-319848:53", "319849:1-319849:492", "319851:1-319851:13", "319852:1-319852:9", 
        "319853:1-319853:262", "319854:1-319854:225", "319908:1-319908:53", "319909:1-319909:7", "319910:1-319910:989", 
        "319912:1-319912:62", "319913:1-319913:61", "319914:1-319914:37", "319915:1-319915:417", "319941:43-319941:305", 
        "319942:1-319942:51", "319950:38-319950:205", "319991:46-319991:886", "319992:1-319992:268", "319993:1-319993:955", 
        "320002:52-320002:193", "320006:1-320006:344", "320007:1-320007:161", "320008:1-320008:89", "320009:1-320009:127", 
        "320010:1-320010:333", "320011:1-320011:307", "320012:1-320012:100", "320023:17-320023:294", "320024:1-320024:410", 
        "320025:1-320025:113", "320026:1-320026:204", "320038:43-320038:668", "320039:1-320039:36", "320040:1-320040:738", 
        "320058:44-320058:71", "320059:1-320059:113", "320060:1-320060:50", "320061:1-320061:50", "320062:1-320062:24", 
        "320063:1-320063:76", "320064:1-320064:204", "320065:1-320065:921", "320500:127-320500:147", "320500:150-320500:158", 
        "320500:160-320500:168", "320500:170-320500:179", "320500:181-320500:189", "320500:191-320500:199", "320500:201-320500:209", 
        "320500:211-320500:230", "320500:232-320500:240", "320500:243-320500:251", "320500:253-320500:262", "320500:264-320500:273", 
        "320500:275-320500:284", "320500:286-320500:294", "320500:297-320500:304", "320500:306-320500:315", "320500:317-320500:318", 
        "320500:322-320500:350", "320500:352-320500:360", "320500:362-320500:415", "320500:417-320500:469", "320500:471-320500:478", 
        "320569:57-320569:307", "320570:1-320570:13", "320570:16-320570:35", "320570:37-320570:45", "320570:47-320570:115", 
        "320570:117-320570:135", "320570:137-320570:165", "320570:167-320570:175", "320570:177-320570:186", "320570:191-320570:199", 
        "320570:201-320570:229", "320570:231-320570:240", "320570:242-320570:363", "320570:365-320570:419", "320571:1-320571:63", 
        "320673:35-320673:906", "320674:1-320674:600", "320688:49-320688:648", "320712:39-320712:242", "320757:51-320757:383", 
        "320804:46-320804:1283", "320807:1-320807:11", "320809:1-320809:717", "320821:41-320821:225", "320822:1-320822:526", 
        "320823:1-320823:364", "320824:1-320824:1052", "320838:93-320838:358", "320839:1-320839:8", "320840:1-320840:474", 
        "320841:1-320841:206", "320853:41-320853:371", "320854:1-320854:126", "320855:1-320855:577", "320856:1-320856:164", 
        "320857:1-320857:277", "320858:1-320858:239", "320859:1-320859:41", "320887:49-320887:325", "320888:1-320888:124", 
        "320916:2-320916:25", "320917:1-320917:1926", "320920:1-320920:178", "320933:40-320933:214", "320934:1-320934:831", 
        "320936:1-320936:407", "320941:1-320941:93", "320980:44-320980:142", "320995:26-320995:214", "320996:1-320996:380", 
        "321004:39-321004:188", "321005:1-321005:61", "321006:1-321006:162", "321007:1-321007:831", "321009:1-321009:85", 
        "321010:1-321010:342", "321011:1-321011:213", "321012:1-321012:35", "321012:190-321012:201", "321051:58-321051:1179", 
        "321055:1-321055:759", "321067:39-321067:639", "321068:1-321068:715", "321069:1-321069:313", "321119:45-321119:214", 
        "321121:1-321121:47", "321122:1-321122:395", "321123:1-321123:8", "321124:1-321124:819", "321126:1-321126:493", 
        "321134:33-321134:137", "321138:1-321138:741", "321140:1-321140:798", "321149:35-321149:1743", "321162:19-321162:59", 
        "321164:1-321164:72", "321165:1-321165:8", "321166:1-321166:21", "321167:1-321167:923", "321177:38-321177:523", 
        "321178:1-321178:78", "321218:49-321218:962", "321219:1-321219:934", "321221:1-321221:40", "321230:41-321230:124", 
        "321231:1-321231:59", "321232:1-321232:30", "321233:1-321233:727", "321261:44-321261:60", "321262:1-321262:4", 
        "321283:48-321283:357", "321294:1-321294:62", "321295:1-321295:754", "321296:1-321296:67", "321305:20-321305:2659", 
        "321310:1-321310:176", "321311:1-321311:10", "321312:1-321312:768", "321313:1-321313:408", "321393:1-321393:148", 
        "321396:1-321396:1475", "321397:1-321397:365", "321414:31-321414:1283", "321415:1-321415:804", "321431:30-321431:189", 
        "321432:1-321432:47", "321433:1-321433:125", "321434:1-321434:642", "321436:1-321436:710", "321457:43-321457:451", 
        "321457:453-321457:1888", "321461:1-321461:149", "321475:50-321475:2084"
     ) ),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents = cms.untracked.uint32(0)
)
process.AnomalousCellParameters = cms.PSet(
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999)
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.HGCAL_chargeCollectionEfficiencies = cms.PSet(
    values = cms.vdouble(1.0, 1.0, 1.0)
)

process.HGCAL_noise_MIP = cms.PSet(
    value = cms.double(0.142857142857)
)

process.HGCAL_noise_fC = cms.PSet(
    values = cms.vdouble(0.336430626, 0.336430626, 0.256328096)
)

process.HGCAL_noises = cms.PSet(
    values = cms.vdouble(2100.0, 2100.0, 1600.0)
)

process.OutALCARECOEcalCalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*', 
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'drop *_alCaIsolatedElectrons_*_RECO', 
        'keep *_alCaIsolatedElectrons_*_ALCARERECO', 
        'drop *_gedGsfElectrons__RECO', 
        'drop *_gedGsfElectronCores__RECO', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*'
    )
)

process.OutALCARECOEcalCalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*'
    )
)

process.OutALCARECOEcalCalWElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*'
    )
)

process.OutALCARECOEcalCalWElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*'
    )
)

process.OutALCARECOEcalCalZElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*'
    )
)

process.OutALCARECOEcalCalZElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*'
    )
)

process.OutALCARECOEcalRecalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalRecalZElectron', 
            'pathALCARECOEcalRecalZSCElectron', 
            'pathALCARECOEcalRecalWElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'drop *_alCaIsolatedElectrons_*_RECO', 
        'keep *_alCaIsolatedElectrons_*_ALCARERECO', 
        'drop *_gedGsfElectrons__RECO', 
        'drop *_gedGsfElectronCores__RECO', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*'
    )
)

process.OutALCARECOEcalRecalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'drop *_alCaIsolatedElectrons_*_RECO', 
        'keep *_alCaIsolatedElectrons_*_ALCARERECO', 
        'drop *_gedGsfElectrons__RECO', 
        'drop *_gedGsfElectronCores__RECO'
    )
)

process.OutALCARECOEcalUncalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron', 
            'pathALCARECOEcalUncalWElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

process.OutALCARECOEcalUncalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

process.OutALCARECOEcalUncalWElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalWElectron')
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

process.OutALCARECOEcalUncalWElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalWElectron')
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

process.OutALCARECOEcalUncalZElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

process.OutALCARECOEcalUncalZElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron'
        )
    ),
    outputCommands = cms.untracked.vstring(
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

process.PFJetParameters = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

process.SubJetParameters = cms.PSet(
    nFilt = cms.int32(2),
    rcut_factor = cms.double(0.5),
    zcut = cms.double(0.1)
)

process.TrackAssociatorParameterBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(False),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    )
)

process.cleaningAlgoConfig = cms.PSet(
    cThreshold_barrel = cms.double(4),
    cThreshold_double = cms.double(10),
    cThreshold_endcap = cms.double(15),
    e4e1Threshold_barrel = cms.double(0.08),
    e4e1Threshold_endcap = cms.double(0.3),
    e4e1_a_barrel = cms.double(0.02),
    e4e1_a_endcap = cms.double(0.02),
    e4e1_b_barrel = cms.double(0.02),
    e4e1_b_endcap = cms.double(-0.0125),
    e6e2thresh = cms.double(0.04),
    ignoreOutOfTimeThresh = cms.double(1000000000.0),
    tightenCrack_e1_double = cms.double(2),
    tightenCrack_e1_single = cms.double(1),
    tightenCrack_e4e1_single = cms.double(2.5),
    tightenCrack_e6e2_double = cms.double(3)
)

process.ecal_digi_parameters = cms.PSet(
    EBCorrNoiseMatrixG01 = cms.vdouble(
        1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
        0.53082, 0.51916, 0.51097, 0.50732, 0.50409
    ),
    EBCorrNoiseMatrixG06 = cms.vdouble(
        1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
        0.41366, 0.39699, 0.38478, 0.37847, 0.37055
    ),
    EBCorrNoiseMatrixG12 = cms.vdouble(
        1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
        0.35931, 0.33924, 0.32439, 0.31581, 0.30481
    ),
    EBdigiCollection = cms.string(''),
    EECorrNoiseMatrixG01 = cms.vdouble(
        1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
        0.49147, 0.47813, 0.47007, 0.46621, 0.46265
    ),
    EECorrNoiseMatrixG06 = cms.vdouble(
        1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
        0.20287, 0.17734, 0.16256, 0.15618, 0.14443
    ),
    EECorrNoiseMatrixG12 = cms.vdouble(
        1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
        0.14786, 0.11772, 0.10165, 0.09465, 0.08098
    ),
    EEdigiCollection = cms.string(''),
    ESdigiCollection = cms.string(''),
    EcalPreMixStage1 = cms.bool(False),
    EcalPreMixStage2 = cms.bool(False),
    UseLCcorrection = cms.untracked.bool(True)
)

process.ecal_pulse_shape_covariances = cms.PSet(
    EBPulseShapeCovariance = cms.vdouble(
        3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
        -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
        0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
        -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
        -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
        8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
        1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
        0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
        2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
        -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
        6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
        7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
        5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
        1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
        -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
        1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
        3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
        1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
        6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
        0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
        6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
        0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
        7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
        6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
        5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
        3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07
    ),
    EEPulseShapeCovariance = cms.vdouble(
        3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
        -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
        0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
        -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
        -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
        6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
        1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
        0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
        3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
        -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
        6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
        9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
        4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
        1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
        -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
        2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
        4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
        2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
        8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
        0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
        8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
        0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
        9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
        7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
        6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
        3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07
    )
)

process.ecal_pulse_shape_parameters = cms.PSet(
    EBCorrNoiseMatrixG01 = cms.vdouble(
        1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
        0.53082, 0.51916, 0.51097, 0.50732, 0.50409
    ),
    EBCorrNoiseMatrixG06 = cms.vdouble(
        1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
        0.41366, 0.39699, 0.38478, 0.37847, 0.37055
    ),
    EBCorrNoiseMatrixG12 = cms.vdouble(
        1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
        0.35931, 0.33924, 0.32439, 0.31581, 0.30481
    ),
    EBPulseShapeCovariance = cms.vdouble(
        3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
        -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
        0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
        -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
        -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
        8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
        1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
        0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
        2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
        -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
        6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
        7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
        5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
        1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
        -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
        1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
        3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
        1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
        6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
        0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
        6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
        0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
        7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
        6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
        5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
        3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07
    ),
    EBPulseShapeTemplate = cms.vdouble(
        0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
        0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
        0.0693181, 0.0475044
    ),
    EBdigiCollection = cms.string(''),
    EECorrNoiseMatrixG01 = cms.vdouble(
        1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
        0.49147, 0.47813, 0.47007, 0.46621, 0.46265
    ),
    EECorrNoiseMatrixG06 = cms.vdouble(
        1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
        0.20287, 0.17734, 0.16256, 0.15618, 0.14443
    ),
    EECorrNoiseMatrixG12 = cms.vdouble(
        1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
        0.14786, 0.11772, 0.10165, 0.09465, 0.08098
    ),
    EEPulseShapeCovariance = cms.vdouble(
        3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
        -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
        0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
        -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
        -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
        6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
        1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
        0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
        3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
        -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
        6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
        9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
        4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
        1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
        -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
        2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
        4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
        2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
        8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
        0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
        8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
        0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
        9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
        7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
        6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
        3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07
    ),
    EEPulseShapeTemplate = cms.vdouble(
        0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
        0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
        0.0874288, 0.061957
    ),
    EEdigiCollection = cms.string(''),
    ESdigiCollection = cms.string(''),
    EcalPreMixStage1 = cms.bool(False),
    EcalPreMixStage2 = cms.bool(False),
    UseLCcorrection = cms.untracked.bool(True)
)

process.ecal_pulse_shape_templates = cms.PSet(
    EBPulseShapeTemplate = cms.vdouble(
        0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
        0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
        0.0693181, 0.0475044
    ),
    EEPulseShapeTemplate = cms.vdouble(
        0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
        0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
        0.0874288, 0.061957
    )
)

process.ecal_time_digi_parameters = cms.PSet(
    EBtimeDigiCollection = cms.string('EBTimeDigi'),
    EEtimeDigiCollection = cms.string('EETimeDigi'),
    hitsProducerEB = cms.InputTag("g4SimHits","EcalHitsEB"),
    hitsProducerEE = cms.InputTag("g4SimHits","EcalHitsEE"),
    timeLayerBarrel = cms.int32(7),
    timeLayerEndcap = cms.int32(3)
)

process.hgceeDigitizer = cms.PSet(
    accumulatorType = cms.string('HGCDigiProducer'),
    bxTime = cms.double(25),
    digiCfg = cms.PSet(
        chargeCollectionEfficiencies = cms.PSet(
            refToPSet_ = cms.string('HGCAL_chargeCollectionEfficiencies')
        ),
        doTimeSamples = cms.bool(False),
        feCfg = cms.PSet(
            adcNbits = cms.uint32(10),
            adcPulse = cms.vdouble(
                0.0, 0.017, 0.817, 0.163, 0.003, 
                0.0
            ),
            adcSaturation_fC = cms.double(100),
            adcThreshold_fC = cms.double(0.672),
            fwVersion = cms.uint32(2),
            jitterConstant_ns = cms.vdouble(0.0004, 0.0004, 0.0004),
            jitterNoise_ns = cms.vdouble(25.0, 25.0, 25.0),
            pulseAvgT = cms.vdouble(
                0.0, 23.42298, 13.16733, 6.41062, 5.03946, 
                4.532
            ),
            tdcChargeDrainParameterisation = cms.vdouble(
                -919.13, 365.36, -14.1, 0.2, -21.85, 
                49.39, 22.21, 0.8, -0.28, 27.14, 
                43.95, 3.89048
            ),
            tdcForToAOnset_fC = cms.vdouble(12.0, 12.0, 12.0),
            tdcNbits = cms.uint32(12),
            tdcOnset_fC = cms.double(60),
            tdcResolutionInPs = cms.double(0.001),
            tdcSaturation_fC = cms.double(10000),
            thresholdFollowsMIP = cms.bool(False),
            toaLSB_ns = cms.double(0.0244),
            toaMode = cms.uint32(1)
        ),
        keV2fC = cms.double(0.044259),
        noise_fC = cms.PSet(
            refToPSet_ = cms.string('HGCAL_noise_fC')
        )
    ),
    digiCollection = cms.string('HGCDigisEE'),
    digitizationType = cms.uint32(0),
    eVPerEleHolePair = cms.double(3.62),
    geometryType = cms.uint32(0),
    hitCollection = cms.string('HGCHitsEE'),
    makeDigiSimLinks = cms.bool(False),
    maxSimHitsAccTime = cms.uint32(100),
    premixStage1 = cms.bool(False),
    premixStage1MaxCharge = cms.double(1000000.0),
    premixStage1MinCharge = cms.double(0),
    tofDelay = cms.double(5),
    useAllChannels = cms.bool(True),
    verbosity = cms.untracked.uint32(0)
)

process.hgchebackDigitizer = cms.PSet(
    accumulatorType = cms.string('HGCDigiProducer'),
    bxTime = cms.double(25),
    digiCfg = cms.PSet(
        doTimeSamples = cms.bool(False),
        feCfg = cms.PSet(
            adcNbits = cms.uint32(12),
            adcSaturation_fC = cms.double(1024.0),
            adcThreshold_fC = cms.double(0.5),
            fwVersion = cms.uint32(0),
            thresholdFollowsMIP = cms.bool(False)
        ),
        keV2MIP = cms.double(0.00162337662338),
        nPEperMIP = cms.double(11.0),
        nTotalPE = cms.double(1156),
        noise_MIP = cms.PSet(
            refToPSet_ = cms.string('HGCAL_noise_MIP')
        ),
        sdPixels = cms.double(1e-06),
        xTalk = cms.double(0.25)
    ),
    digiCollection = cms.string('HGCDigisHEback'),
    digitizationType = cms.uint32(1),
    geometryType = cms.uint32(0),
    hitCollection = cms.string('HcalHits'),
    makeDigiSimLinks = cms.bool(False),
    maxSimHitsAccTime = cms.uint32(100),
    premixStage1 = cms.bool(False),
    premixStage1MaxCharge = cms.double(1000000.0),
    premixStage1MinCharge = cms.double(0),
    tofDelay = cms.double(1),
    useAllChannels = cms.bool(True),
    verbosity = cms.untracked.uint32(0)
)

process.hgchefrontDigitizer = cms.PSet(
    accumulatorType = cms.string('HGCDigiProducer'),
    bxTime = cms.double(25),
    digiCfg = cms.PSet(
        chargeCollectionEfficiencies = cms.PSet(
            refToPSet_ = cms.string('HGCAL_chargeCollectionEfficiencies')
        ),
        doTimeSamples = cms.bool(False),
        feCfg = cms.PSet(
            adcNbits = cms.uint32(10),
            adcPulse = cms.vdouble(
                0.0, 0.017, 0.817, 0.163, 0.003, 
                0.0
            ),
            adcSaturation_fC = cms.double(100),
            adcThreshold_fC = cms.double(0.672),
            fwVersion = cms.uint32(2),
            jitterConstant_ns = cms.vdouble(0.0004, 0.0004, 0.0004),
            jitterNoise_ns = cms.vdouble(25.0, 25.0, 25.0),
            pulseAvgT = cms.vdouble(
                0.0, 23.42298, 13.16733, 6.41062, 5.03946, 
                4.532
            ),
            tdcChargeDrainParameterisation = cms.vdouble(
                -919.13, 365.36, -14.1, 0.2, -21.85, 
                49.39, 22.21, 0.8, -0.28, 27.14, 
                43.95, 3.89048
            ),
            tdcForToAOnset_fC = cms.vdouble(12.0, 12.0, 12.0),
            tdcNbits = cms.uint32(12),
            tdcOnset_fC = cms.double(60),
            tdcResolutionInPs = cms.double(0.001),
            tdcSaturation_fC = cms.double(10000),
            thresholdFollowsMIP = cms.bool(False),
            toaLSB_ns = cms.double(0.0244),
            toaMode = cms.uint32(1)
        ),
        keV2fC = cms.double(0.044259),
        noise_fC = cms.PSet(
            refToPSet_ = cms.string('HGCAL_noise_fC')
        )
    ),
    digiCollection = cms.string('HGCDigisHEfront'),
    digitizationType = cms.uint32(0),
    geometryType = cms.uint32(0),
    hitCollection = cms.string('HGCHitsHEfront'),
    makeDigiSimLinks = cms.bool(False),
    maxSimHitsAccTime = cms.uint32(100),
    premixStage1 = cms.bool(False),
    premixStage1MaxCharge = cms.double(1000000.0),
    premixStage1MinCharge = cms.double(0),
    tofDelay = cms.double(5),
    useAllChannels = cms.bool(True),
    verbosity = cms.untracked.uint32(0)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)

process.modPSet = cms.PSet(
    ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    electron_config = cms.PSet(
        electronSrc = cms.InputTag("patElectrons"),
        energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
        energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
        energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
        energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar")
    ),
    modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
    photon_config = cms.PSet(

    )
)

process.modPSetEleIDBool = cms.PSet(
    ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    electron_config = cms.PSet(
        electronSrc = cms.InputTag("patElectrons"),
        loose25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
        loose94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
        medium5nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
        medium94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
        tight25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
        tight94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
        veto25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
        veto94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto")
    ),
    modifierName = cms.string('EleIDModifierFromBoolValueMaps'),
    photon_config = cms.PSet(

    )
)

process.modPSetEleIDFloat = cms.PSet(
    ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    electron_config = cms.PSet(
        electronSrc = cms.InputTag("patElectrons")
    ),
    modifierName = cms.string('EleIDModifierFromValueMaps'),
    photon_config = cms.PSet(

    )
)

process.modPSetSlewRate = cms.PSet(
    ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    electron_config = cms.PSet(
        electronSrc = cms.InputTag("patElectrons")
    ),
    modifierName = cms.string('EGSlewRateModifier'),
    photon_config = cms.PSet(

    )
)

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
    )
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.mvaConfigsForEleProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
        )
    )
)

process.EleSCSelector = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string('PassingVetoId eleSC')
)


process.GsfMatchedPhotonCands = cms.EDProducer("ElectronMatchedCandidateProducer",
    ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
    deltaR = cms.untracked.double(0.3),
    src = cms.InputTag("goodPhotons")
)


process.HGCalRecHit = cms.EDProducer("HGCalRecHitProducer",
    HGCEE_cce = cms.PSet(
        refToPSet_ = cms.string('HGCAL_chargeCollectionEfficiencies')
    ),
    HGCEE_fCPerMIP = cms.vdouble(1.25, 2.57, 3.88),
    HGCEE_isSiFE = cms.bool(True),
    HGCEE_keV2DIGI = cms.double(0.044259),
    HGCEE_noise_fC = cms.PSet(
        refToPSet_ = cms.string('HGCAL_noise_fC')
    ),
    HGCEErechitCollection = cms.string('HGCEERecHits'),
    HGCEEuncalibRecHitCollection = cms.InputTag("HGCalUncalibRecHit","HGCEEUncalibRecHits"),
    HGCHEB_isSiFE = cms.bool(False),
    HGCHEB_keV2DIGI = cms.double(0.00162337662338),
    HGCHEB_noise_MIP = cms.PSet(
        refToPSet_ = cms.string('HGCAL_noise_MIP')
    ),
    HGCHEBrechitCollection = cms.string('HGCHEBRecHits'),
    HGCHEBuncalibRecHitCollection = cms.InputTag("HGCalUncalibRecHit","HGCHEBUncalibRecHits"),
    HGCHEF_cce = cms.PSet(
        refToPSet_ = cms.string('HGCAL_chargeCollectionEfficiencies')
    ),
    HGCHEF_fCPerMIP = cms.vdouble(1.25, 2.57, 3.88),
    HGCHEF_isSiFE = cms.bool(True),
    HGCHEF_keV2DIGI = cms.double(0.044259),
    HGCHEF_noise_fC = cms.PSet(
        refToPSet_ = cms.string('HGCAL_noise_fC')
    ),
    HGCHEFrechitCollection = cms.string('HGCHEFRecHits'),
    HGCHEFuncalibRecHitCollection = cms.InputTag("HGCalUncalibRecHit","HGCHEFUncalibRecHits"),
    algo = cms.string('HGCalRecHitWorkerSimple'),
    layerWeights = cms.vdouble(
        0.0, 8.603, 8.0675, 8.0675, 8.0675, 
        8.0675, 8.0675, 8.0675, 8.0675, 8.0675, 
        8.9515, 10.135, 10.135, 10.135, 10.135, 
        10.135, 10.135, 10.135, 10.135, 10.135, 
        11.682, 13.654, 13.654, 13.654, 13.654, 
        13.654, 13.654, 13.654, 38.2005, 55.0265, 
        49.871, 49.871, 49.871, 49.871, 49.871, 
        49.871, 49.871, 49.871, 49.871, 49.871, 
        62.005, 83.1675, 92.196, 92.196, 92.196, 
        92.196, 92.196, 92.196, 92.196, 92.196, 
        92.196, 92.196, 46.098
    ),
    rangeMask = cms.uint32(4294442496),
    rangeMatch = cms.uint32(1161838592),
    thicknessCorrection = cms.vdouble(1.132, 1.092, 1.084)
)


process.HGCalUncalibRecHit = cms.EDProducer("HGCalUncalibRecHitProducer",
    HGCEEConfig = cms.PSet(
        adcNbits = cms.uint32(10),
        adcSaturation = cms.double(100),
        fCPerMIP = cms.vdouble(1.25, 2.57, 3.88),
        isSiFE = cms.bool(True),
        tdcNbits = cms.uint32(12),
        tdcOnset = cms.double(60),
        tdcSaturation = cms.double(10000),
        toaLSB_ns = cms.double(0.0244)
    ),
    HGCEEdigiCollection = cms.InputTag("hgcalDigis","EE"),
    HGCEEhitCollection = cms.string('HGCEEUncalibRecHits'),
    HGCHEBConfig = cms.PSet(
        adcNbits = cms.uint32(12),
        adcSaturation = cms.double(1024.0),
        fCPerMIP = cms.vdouble(1.0, 1.0, 1.0),
        isSiFE = cms.bool(False)
    ),
    HGCHEBdigiCollection = cms.InputTag("hgcalDigis","HEback"),
    HGCHEBhitCollection = cms.string('HGCHEBUncalibRecHits'),
    HGCHEFConfig = cms.PSet(
        adcNbits = cms.uint32(10),
        adcSaturation = cms.double(100),
        fCPerMIP = cms.vdouble(1.25, 2.57, 3.88),
        isSiFE = cms.bool(True),
        tdcNbits = cms.uint32(12),
        tdcOnset = cms.double(60),
        tdcSaturation = cms.double(10000),
        toaLSB_ns = cms.double(0.0244)
    ),
    HGCHEFdigiCollection = cms.InputTag("hgcalDigis","HEfront"),
    HGCHEFhitCollection = cms.string('HGCHEFUncalibRecHits'),
    algo = cms.string('HGCalUncalibRecHitWorkerWeights')
)


process.PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('path( "HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7" )'),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patElectrons")
)


process.PatElectronsTriggerMatch = cms.EDProducer("PATTriggerMatchElectronEmbedder",
    matches = cms.VInputTag("PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7"),
    src = cms.InputTag("PatElectrons")
)


process.WZSelector = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("WenuSelector", "ZeeSelector", "EleSCSelector")
)


process.WenuSelector = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('daughter(0).pt > 25.000000 && daughter(1).pt > 30.000000 && sqrt(2*daughter(0).pt*daughter(1).pt*(1 - cos(daughter(0).phi - daughter(1).phi))) > 50.000000'),
    decay = cms.string('pfMet PassingVetoId')
)


process.ZeeSelector = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string('PassingVetoId PassingVetoId')
)


process.ZmmgCandidates = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('\n        daughter(0).daughter(1).pt + daughter(1).pt > 20 &\n        min(deltaR(daughter(0).daughter(0).eta,\n                   daughter(0).daughter(0).phi,\n                   daughter(1).eta,\n                   daughter(1).phi),\n            deltaR(daughter(0).daughter(1).eta,\n                   daughter(0).daughter(1).phi,\n                   daughter(1).eta,\n                   daughter(1).phi)) < 1.5 &\n        mass + daughter(0).mass < 200 &\n        mass > 40\n        '),
    decay = cms.string('ZmmgDimuons ZmmgPhotons')
)


process.ZmmgDimuons = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(True),
    cut = cms.string('mass > 30'),
    decay = cms.string('ZmmgLeadingMuons@+ ZmmgTrailingMuons@-')
)


process.ZmmgMergedSuperClusters = cms.EDProducer("EgammaSuperClusterMerger",
    src = cms.VInputTag(cms.InputTag("correctedHybridSuperClusters"), cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"))
)


process.ZmmgPhotonCandidates = cms.EDProducer("ConcreteEcalCandidateProducer",
    particleType = cms.string('gamma'),
    src = cms.InputTag("ZmmgMergedSuperClusters")
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("pfNoPileUpJME"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsCS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    csRParam = cms.double(0.4),
    csRho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useConstituentSubtraction = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsPuppi = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsSK = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("softKiller"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(50.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(50.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("pfNoPileUpJME"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCHSConstituents = cms.EDProducer("PFJetConstituentSelector",
    cut = cms.string('pt > 100.0 && abs(rapidity()) < 2.4'),
    src = cms.InputTag("ak8PFJetsCHS")
)


process.ak8PFJetsCHSFiltered = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(3),
    rFilt = cms.double(0.3),
    rParam = cms.double(0.8),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useFiltering = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True)
)


process.ak8PFJetsCHSFilteredMass = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("ak8PFJetsCHSFiltered"),
    src = cms.InputTag("ak8PFJetsCHS"),
    value = cms.string('mass')
)


process.ak8PFJetsCHSMassDropFiltered = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(0.667),
    rParam = cms.double(0.8),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useMassDropTagger = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    yCut = cms.double(0.08)
)


process.ak8PFJetsCHSPruned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(2),
    rParam = cms.double(0.8),
    rcut_factor = cms.double(0.5),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    usePruning = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8PFJetsCHSPrunedMass = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("ak8PFJetsCHSPruned"),
    src = cms.InputTag("ak8PFJetsCHS"),
    value = cms.string('mass')
)


process.ak8PFJetsCHSSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8PFJetsCHSSoftDropMass = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("ak8PFJetsCHSSoftDrop"),
    src = cms.InputTag("ak8PFJetsCHS"),
    value = cms.string('mass')
)


process.ak8PFJetsCHSTrimmed = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rFilt = cms.double(0.2),
    rParam = cms.double(0.8),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    trimPtFracMin = cms.double(0.03),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useTrimming = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCHSTrimmedMass = cms.EDProducer("RecoJetDeltaRValueMapProducer",
    distMax = cms.double(0.8),
    matched = cms.InputTag("ak8PFJetsCHSTrimmed"),
    src = cms.InputTag("ak8PFJetsCHS"),
    value = cms.string('mass')
)


process.ak8PFJetsCS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    csRParam = cms.double(0.4),
    csRho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useConstituentSubtraction = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsCSConstituents = cms.EDProducer("PFJetConstituentSelector",
    cut = cms.string('pt > 100.0'),
    src = cms.InputTag("ak8PFJetsCS")
)


process.ak8PFJetsPuppi = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(50.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PFJetsPuppiConstituents = cms.EDProducer("PFJetConstituentSelector",
    cut = cms.string('pt > 100.0 && abs(rapidity()) < 2.4'),
    src = cms.InputTag("ak8PFJetsPuppi")
)


process.ak8PFJetsPuppiSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("ak8PFJetsPuppiConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.alCaIsolatedElectrons = cms.EDProducer("AlCaECALRecHitReducer",
    EESuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    alcaBarrelHitCollection = cms.string('alcaBarrelHits'),
    alcaBarrelUncalibHitCollection = cms.string('alcaBarrelUncalibHits'),
    alcaCaloClusterCollection = cms.string('alcaCaloCluster'),
    alcaEndcapHitCollection = cms.string('alcaEndcapHits'),
    alcaEndcapUncalibHitCollection = cms.string('alcaEndcapUncalibHits'),
    alcaPreshowerHitCollection = cms.string('alcaPreshowerHits'),
    ebRecHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    electronLabel = cms.InputTag("electronRecalibSCAssociator"),
    esRecHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    etaSize = cms.int32(15),
    minEta_highEtaSC = cms.double(2.4),
    phiSize = cms.int32(61),
    photonLabel = cms.InputTag("gedPhotons"),
    srcLabels = cms.VInputTag("electronRecalibSCAssociator"),
    uncalibRecHitCollectionEB = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
    uncalibRecHitCollectionEE = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE")
)


process.alcaElectronTracksReducer = cms.EDProducer("AlCaElectronTracksReducer",
    alcaTrackCollection = cms.string('alCaElectronTracks'),
    alcaTrackExtraCollection = cms.string('alCaElectronTracksExtra'),
    electronLabel = cms.InputTag("gedGsfElectrons"),
    generalTracksExtraLabel = cms.InputTag("generalTracksExtra"),
    generalTracksLabel = cms.InputTag("generalTracks")
)


process.bunchSpacingProducer = cms.EDProducer("BunchSpacingProducer")


process.ca15PFJetsCHSFiltered = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('CambridgeAachen'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nFilt = cms.int32(3),
    rFilt = cms.double(0.3),
    rParam = cms.double(1.5),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useFiltering = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True)
)


process.ca15PFJetsCHSMassDropFiltered = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('CambridgeAachen'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muCut = cms.double(0.667),
    rParam = cms.double(1.5),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useMassDropTagger = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    yCut = cms.double(0.08)
)


process.cleanedHybridSuperClusters = cms.EDProducer("HybridClusterProducer",
    HybridBarrelSeedThr = cms.double(1.0),
    RecHitFlagToBeExcluded = cms.vstring(
        'kFaultyHardware', 
        'kTowerRecovered', 
        'kDead'
    ),
    RecHitSeverityToBeExcluded = cms.vstring(
        'kWeird', 
        'kBad', 
        'kTime'
    ),
    basicclusterCollection = cms.string('hybridBarrelBasicClusters'),
    clustershapecollection = cms.string(''),
    dynamicEThresh = cms.bool(False),
    dynamicPhiRoad = cms.bool(False),
    eThreshA = cms.double(0.003),
    eThreshB = cms.double(0.1),
    eseed = cms.double(0.35),
    ethresh = cms.double(0.1),
    ewing = cms.double(0.0),
    excludeFlagged = cms.bool(True),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    recHitsCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    shapeAssociation = cms.string('hybridShapeAssoc'),
    step = cms.int32(17),
    superclusterCollection = cms.string(''),
    useEtForXi = cms.bool(True),
    xi = cms.double(0.0)
)


process.cmsTopTagPFJetsCHS = cms.EDProducer("CATopJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    algorithm = cms.int32(1),
    centralEtaCut = cms.double(2.5),
    deltarBins = cms.vdouble(0.19, 0.19, 0.19),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    etFrac = cms.double(0.7),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('CambridgeAachen'),
    jetCollInstanceName = cms.string('caTopSubJets'),
    jetPtMin = cms.double(100.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nCellBins = cms.vdouble(1.9, 1.9, 1.9),
    ptFracBins = cms.vdouble(0.05, 0.05, 0.05),
    rBins = cms.vdouble(0.8, 0.8, 0.8),
    rParam = cms.double(0.8),
    src = cms.InputTag("ak8PFJetsCHSConstituents","constituents"),
    srcPVs = cms.InputTag(""),
    sumEtBins = cms.vdouble(0, 1600, 2600),
    sumEtEtaCut = cms.double(3.0),
    tagAlgo = cms.int32(0),
    useAdjacency = cms.int32(2),
    useDeterministicSeed = cms.bool(True),
    useMaxTower = cms.bool(False),
    verbose = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True)
)


process.combW = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string(''),
    decay = cms.string('genEleFromW genNuFromW')
)


process.combZ = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string('genEleFromZ genEleFromZ')
)


process.correctedHybridSuperClusters = cms.EDProducer("EgammaSCCorrectionMaker",
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(True),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    hyb_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(8.0),
        brLinearLowThr = cms.double(1.1),
        fBremVec = cms.vdouble(-0.04382, 0.1169, 0.9267, -0.0009413, 1.419),
        fEtEtaVec = cms.vdouble(
            0, 1.00121, -0.63672, 0, 0, 
            0, 0.5655, 6.457, 0.5081, 8.0, 
            1.023, -0.00181
        )
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("hybridSuperClusters"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    sigmaElectronicNoise = cms.double(0.03),
    superClusterAlgo = cms.string('Hybrid')
)


process.correctedIslandBarrelSuperClusters = cms.EDProducer("EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string('ERROR'),
    applyEnergyCorrection = cms.bool(True),
    corectedSuperClusterCollection = cms.string(''),
    etThresh = cms.double(0.0),
    isl_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(0.0),
        brLinearLowThr = cms.double(0.0),
        fBremVec = cms.vdouble(0.0),
        fEtEtaVec = cms.vdouble(0.0)
    ),
    rawSuperClusterProducer = cms.InputTag("islandSuperClusters","islandBarrelSuperClusters"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    sigmaElectronicNoise = cms.double(0.03),
    superClusterAlgo = cms.string('Island')
)


process.correctedIslandEndcapSuperClusters = cms.EDProducer("EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string('ERROR'),
    applyEnergyCorrection = cms.bool(True),
    corectedSuperClusterCollection = cms.string(''),
    etThresh = cms.double(0.0),
    isl_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(0.0),
        brLinearLowThr = cms.double(0.0),
        fBremVec = cms.vdouble(0.0),
        fEtEtaVec = cms.vdouble(0.0)
    ),
    rawSuperClusterProducer = cms.InputTag("islandSuperClusters","islandEndcapSuperClusters"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    sigmaElectronicNoise = cms.double(0.15),
    superClusterAlgo = cms.string('Island')
)


process.correctedMulti5x5SuperClustersWithPreshower = cms.EDProducer("EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string('ERROR'),
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(False),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    fix_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(6.0),
        brLinearLowThr = cms.double(0.9),
        fBremVec = cms.vdouble(-0.05228, 0.08738, 0.9508, 0.002677, 1.221),
        fEtEtaVec = cms.vdouble(
            1, -0.4386, -32.38, 0.6372, 15.67, 
            -0.0928, -2.462, 1.138, 20.93
        )
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("multi5x5SuperClustersWithPreshower"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    sigmaElectronicNoise = cms.double(0.15),
    superClusterAlgo = cms.string('Multi5x5')
)


process.ecalBarrelClusterFastTimer = cms.EDProducer("EcalBarrelClusterFastTimer",
    ebClusters = cms.InputTag("particleFlowClusterECALUncorrected"),
    ebTimeHits = cms.InputTag("ecalDetailedTimeRecHit","EcalRecHitsEB"),
    ecalDepth = cms.double(7.0),
    minEnergyToConsider = cms.double(0.0),
    minFractionToConsider = cms.double(0.1),
    resolutionModels = cms.VPSet(cms.PSet(
        modelName = cms.string('PerfectResolutionModel')
    )),
    timedVertices = cms.InputTag("offlinePrimaryVertices4D")
)


process.ecalCompactTrigPrim = cms.EDProducer("EcalCompactTrigPrimProducer",
    inColl = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),
    outColl = cms.string('')
)


process.ecalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("ecalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("ecalDigis"),
    integrityBlockSizeErrors = cms.InputTag("ecalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("ecalDigis","EcalIntegrityTTIdErrors")
)


process.ecalDetailedTimeRecHit = cms.EDProducer("EcalDetailedTimeRecHitProducer",
    EBDetailedTimeRecHitCollection = cms.string('EcalRecHitsEB'),
    EBRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EBTimeDigiCollection = cms.InputTag("mix","EBTimeDigi"),
    EBTimeLayer = cms.int32(7),
    EEDetailedTimeRecHitCollection = cms.string('EcalRecHitsEE'),
    EERecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    EETimeDigiCollection = cms.InputTag("mix","EETimeDigi"),
    EETimeLayer = cms.int32(3),
    correctForVertexZPosition = cms.bool(False),
    recoVertex = cms.InputTag("offlinePrimaryVerticesWithBS"),
    simVertex = cms.InputTag("g4SimHits"),
    useMCTruthVertex = cms.bool(False)
)


process.ecalDigis = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.ecalGlobalUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerGlobal'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBchi2Parameters = cms.vdouble(2.122, 0.022, 2.122, 0.022),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(
            -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621
        ),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEchi2Parameters = cms.vdouble(2.122, 0.022, 2.122, 0.022),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(
            -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277
        ),
        EEtimeNconst = cms.double(31.8),
        amplitudeThresholdEB = cms.double(10),
        amplitudeThresholdEE = cms.double(10),
        chi2ThreshEB_ = cms.double(36.0),
        chi2ThreshEE_ = cms.double(95.0),
        ebPulseShape = cms.vdouble(
            5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194
        ),
        ebSpikeThreshold = cms.double(1.042),
        eePulseShape = cms.vdouble(
            5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194
        ),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5),
        outOfTimeThresholdGain12mEE = cms.double(1000),
        outOfTimeThresholdGain12pEB = cms.double(5),
        outOfTimeThresholdGain12pEE = cms.double(1000),
        outOfTimeThresholdGain61mEB = cms.double(5),
        outOfTimeThresholdGain61mEE = cms.double(1000),
        outOfTimeThresholdGain61pEB = cms.double(5),
        outOfTimeThresholdGain61pEE = cms.double(1000)
    )
)


process.ecalMultiFitUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(
            -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621
        ),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(
            -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277
        ),
        EEtimeNconst = cms.double(31.8),
        EcalPulseShapeParameters = cms.PSet(
            EBCorrNoiseMatrixG01 = cms.vdouble(
                1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
                0.53082, 0.51916, 0.51097, 0.50732, 0.50409
            ),
            EBCorrNoiseMatrixG06 = cms.vdouble(
                1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
                0.41366, 0.39699, 0.38478, 0.37847, 0.37055
            ),
            EBCorrNoiseMatrixG12 = cms.vdouble(
                1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
                0.35931, 0.33924, 0.32439, 0.31581, 0.30481
            ),
            EBPulseShapeCovariance = cms.vdouble(
                3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
                -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
                0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
                -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
                -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
                8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
                1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
                0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
                2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
                -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
                6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
                7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
                5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
                1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
                -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
                1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
                3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
                1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
                6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
                0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
                6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
                0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
                7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
                6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
                5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
                3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07
            ),
            EBPulseShapeTemplate = cms.vdouble(
                0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
                0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
                0.0693181, 0.0475044
            ),
            EBdigiCollection = cms.string(''),
            EECorrNoiseMatrixG01 = cms.vdouble(
                1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
                0.49147, 0.47813, 0.47007, 0.46621, 0.46265
            ),
            EECorrNoiseMatrixG06 = cms.vdouble(
                1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
                0.20287, 0.17734, 0.16256, 0.15618, 0.14443
            ),
            EECorrNoiseMatrixG12 = cms.vdouble(
                1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
                0.14786, 0.11772, 0.10165, 0.09465, 0.08098
            ),
            EEPulseShapeCovariance = cms.vdouble(
                3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
                -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
                0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
                -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
                -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
                6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
                1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
                0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
                3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
                -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
                6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
                9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
                4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
                1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
                -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
                2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
                4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
                2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
                8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
                0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
                8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
                0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
                9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
                7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
                6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
                3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07
            ),
            EEPulseShapeTemplate = cms.vdouble(
                0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
                0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
                0.0874288, 0.061957
            ),
            EEdigiCollection = cms.string(''),
            ESdigiCollection = cms.string(''),
            EcalPreMixStage1 = cms.bool(False),
            EcalPreMixStage2 = cms.bool(False),
            UseLCcorrection = cms.untracked.bool(True)
        ),
        activeBXs = cms.vint32(
            -5, -4, -3, -2, -1, 
            0, 1, 2, 3, 4
        ),
        addPedestalUncertaintyEB = cms.double(0.0),
        addPedestalUncertaintyEE = cms.double(0.0),
        ampErrorCalculation = cms.bool(True),
        amplitudeThresholdEB = cms.double(10),
        amplitudeThresholdEE = cms.double(10),
        chi2ThreshEB_ = cms.double(65.0),
        chi2ThreshEE_ = cms.double(50.0),
        doPrefitEB = cms.bool(False),
        doPrefitEE = cms.bool(False),
        dynamicPedestalsEB = cms.bool(False),
        dynamicPedestalsEE = cms.bool(False),
        ebPulseShape = cms.vdouble(
            5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194
        ),
        ebSpikeThreshold = cms.double(1.042),
        eePulseShape = cms.vdouble(
            5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194
        ),
        gainSwitchUseMaxSampleEB = cms.bool(True),
        gainSwitchUseMaxSampleEE = cms.bool(False),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        mitigateBadSamplesEB = cms.bool(False),
        mitigateBadSamplesEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5),
        outOfTimeThresholdGain12mEE = cms.double(1000),
        outOfTimeThresholdGain12pEB = cms.double(5),
        outOfTimeThresholdGain12pEE = cms.double(1000),
        outOfTimeThresholdGain61mEB = cms.double(5),
        outOfTimeThresholdGain61mEE = cms.double(1000),
        outOfTimeThresholdGain61pEB = cms.double(5),
        outOfTimeThresholdGain61pEE = cms.double(1000),
        prefitMaxChiSqEB = cms.double(25.0),
        prefitMaxChiSqEE = cms.double(10.0),
        selectiveBadSampleCriteriaEB = cms.bool(False),
        selectiveBadSampleCriteriaEE = cms.bool(False),
        simplifiedNoiseModelForGainSwitch = cms.bool(True),
        timealgo = cms.string('RatioMethod'),
        useLumiInfoRunHeader = cms.bool(True)
    )
)


process.ecalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.ecalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("ecalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.ecalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(
        'kDAC', 
        'kNoisy', 
        'kNNoisy', 
        'kFixedG6', 
        'kFixedG1', 
        'kFixedG0', 
        'kNonRespondingIsolated', 
        'kDeadVFE', 
        'kDeadFE', 
        'kNoDataNoTP'
    ),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4),
        cThreshold_double = cms.double(10),
        cThreshold_endcap = cms.double(15),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.02),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(0.02),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2),
        tightenCrack_e1_single = cms.double(1),
        tightenCrack_e4e1_single = cms.double(2.5),
        tightenCrack_e6e2_double = cms.double(3)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk', 
            'kDAC', 
            'kNoLaser', 
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0', 
            'kNonRespondingIsolated', 
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy', 
            'kFixedG6', 
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50),
    logWarningEtThreshold_EE_FE = cms.double(50),
    recoverEBFE = cms.bool(True),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(True),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8),
    skipTimeCalib = cms.bool(False),
    triggerPrimitiveDigiCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives")
)


process.ecalTPSkim = cms.EDProducer("EcalTPSkimmer",
    chStatusToSelectTP = cms.vuint32(13),
    doBarrel = cms.bool(True),
    doEndcap = cms.bool(True),
    skipModule = cms.bool(False),
    tpInputCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),
    tpOutputCollection = cms.string('')
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.031),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.02),
                        dPhiInCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.06),
                        hadronicOverEMCutValueEE = cms.double(0.065),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.013),
                        eInverseMinusPInverseCutValueEE = cms.double(0.013),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_ecalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.16),
                        isoCutEBLowPt = cms.double(0.16),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(0),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_hcalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.12),
                        isoCutEBLowPt = cms.double(0.12),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(1),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.0),
                        constTermEE = cms.double(0.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.08),
                        slopeTermEE = cms.double(0.08)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleNormalizedGsfChi2Cut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        normalizedGsfChi2CutValueEB = cms.double(1e+30),
                        normalizedGsfChi2CutValueEE = cms.double(3.0)
                    )
                ),
                idName = cms.string('cutBasedElectronHLTPreselection-Summer16-V1'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('aef5f00cc25a63b44192c6fc449f7dc0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00387),
                        dEtaInSeedCutValueEE = cms.double(0.0072),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0716),
                        dPhiInCutValueEE = cms.double(0.147),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0356),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0414),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0875),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.133),
                        isoCutEBLowPt = cms.double(0.133),
                        isoCutEEHighPt = cms.double(0.146),
                        isoCutEELowPt = cms.double(0.146),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0b8456d622494441fe713a6858e0f7c1'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00365),
                        dEtaInSeedCutValueEE = cms.double(0.00625),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0588),
                        dPhiInCutValueEE = cms.double(0.0355),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0309),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0327),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0335),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0718),
                        isoCutEBLowPt = cms.double(0.0718),
                        isoCutEEHighPt = cms.double(0.143),
                        isoCutEELowPt = cms.double(0.143),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('a238ee70910de53d36866e89768500e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00353),
                        dEtaInSeedCutValueEE = cms.double(0.00567),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0499),
                        dPhiInCutValueEE = cms.double(0.0165),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0305),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0278),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0158),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0361),
                        isoCutEBLowPt = cms.double(0.0361),
                        isoCutEEHighPt = cms.double(0.094),
                        isoCutEELowPt = cms.double(0.094),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4acb2d2796efde7fba75380ce8823fc2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00523),
                        dEtaInSeedCutValueEE = cms.double(0.00984),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.159),
                        dPhiInCutValueEE = cms.double(0.157),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0128),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0445),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0962),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.168),
                        isoCutEBLowPt = cms.double(0.168),
                        isoCutEEHighPt = cms.double(0.185),
                        isoCutEELowPt = cms.double(0.185),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('43be9b381a8d9b0910b7f81a5ad8ff3a'),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("patElectrons")
)


process.elPFIsoDepositChargedAllGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticles")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticles")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoValueCharged03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralGsf"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.eleNewEnergiesProducer = cms.EDProducer("EleNewEnergiesProducer",
    electronCollection = cms.InputTag("patElectrons"),
    photonCollection = cms.InputTag("photons"),
    recHitCollectionEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    recHitCollectionEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    scEnergyCorrectorSemiParm = cms.PSet(
        ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
        ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
        isHLT = cms.bool(False),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    )
)


process.eleSC = cms.EDProducer("ConcreteEcalCandidateProducer",
    particleType = cms.string('gamma'),
    src = cms.InputTag("SCselector")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronMVAVariableHelper = cms.EDProducer("GsfElectronMVAVariableHelper",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    beamSpotMiniAOD = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    vertexCollectionMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons")
)


process.electronRecalibSCAssociator = cms.EDProducer("ElectronRecalibSuperClusterAssociator",
    electronSrc = cms.InputTag("gedGsfElectrons"),
    outputLabel = cms.string('recalibSC'),
    recHitCollectionEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    superClusterCollectionEB = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALBarrel"),
    superClusterCollectionEE = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALEndcapWithPreshower")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    eeReducedRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    esReducedRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaPreshowerHits"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("alCaIsolatedElectrons","alcaPreshowerHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("electronRecalibSCAssociator"),
    useFull5x5 = cms.bool(False)
)


process.fixedGridRhoAll = cms.EDProducer("FixedGridRhoProducer",
    EtaRegion = cms.string('All'),
    pfCandidatesTag = cms.InputTag("particleFlow")
)


process.fixedGridRhoFastjetAll = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(5.0),
    pfCandidatesTag = cms.InputTag("particleFlow")
)


process.fixedGridRhoFastjetCentral = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(2.5),
    pfCandidatesTag = cms.InputTag("particleFlow")
)


process.fixedGridRhoFastjetCentralChargedPileUp = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(2.5),
    pfCandidatesTag = cms.InputTag("pfPileUpAllChargedParticles")
)


process.fixedGridRhoFastjetCentralNeutral = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(2.5),
    pfCandidatesTag = cms.InputTag("pfAllNeutralHadronsAndPhotons")
)


process.hbhecollapse = cms.EDProducer("HBHEPlan1Combiner",
    algorithm = cms.PSet(
        Class = cms.string('SimplePlan1RechitCombiner')
    ),
    hbheInput = cms.InputTag("hbheprereco"),
    ignorePlan1Topology = cms.bool(False),
    usePlan1Mode = cms.bool(True)
)


process.hbhecollapseMB = cms.EDProducer("HBHEPlan1Combiner",
    algorithm = cms.PSet(
        Class = cms.string('SimplePlan1RechitCombiner')
    ),
    hbheInput = cms.InputTag("hbheprerecoMB"),
    ignorePlan1Topology = cms.bool(False),
    usePlan1Mode = cms.bool(True)
)


process.hbheplan1 = cms.EDProducer("HBHEPlan1Combiner",
    algorithm = cms.PSet(
        Class = cms.string('SimplePlan1RechitCombiner')
    ),
    hbheInput = cms.InputTag("hbheprereco"),
    ignorePlan1Topology = cms.bool(False),
    usePlan1Mode = cms.bool(True)
)


process.hbheplan1MB = cms.EDProducer("HBHEPlan1Combiner",
    algorithm = cms.PSet(
        Class = cms.string('SimplePlan1RechitCombiner')
    ),
    hbheInput = cms.InputTag("hbheprerecoMB"),
    ignorePlan1Topology = cms.bool(False),
    usePlan1Mode = cms.bool(True)
)


process.hbheprereco = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        activeBXs = cms.vint32(-1, 0, 1),
        applyPedConstraint = cms.bool(True),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(True),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        chiSqSwitch = cms.double(15.0),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        deltaChiSqThresh = cms.double(0.001),
        dynamicPed = cms.bool(True),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        nMaxItersMin = cms.int32(500),
        nMaxItersNNLS = cms.int32(500),
        nnlsThresh = cms.double(1e-11),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 20000.0, 30000),
        ts4Min = cms.double(0.0),
        ts4Thresh = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(True),
        useMahi = cms.bool(True)
    ),
    digiLabelQIE11 = cms.InputTag("hcalDigis"),
    digiLabelQIE8 = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    0.0, 100.0, -50.0, 0.0, -15.0, 
                    0.15
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0
                )
            )
        )
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(True),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250, 500, 100000),
        LinearCut = cms.vdouble(-3, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20, 100, 100000),
        MinimumChargeThreshold = cms.double(20),
        MinimumTS4TS5Threshold = cms.double(100),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20, 100, 100000),
        RightSlopeCut = cms.vdouble(5, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150, 200, 100000),
        RightSlopeThreshold = cms.vdouble(250, 400, 100000),
        TS3TS4ChargeThreshold = cms.double(70),
        TS3TS4UpperChargeThreshold = cms.double(20),
        TS4TS5ChargeThreshold = cms.double(70),
        TS4TS5LowerCut = cms.vdouble(
            -1, -0.7, -0.5, -0.4, -0.3, 
            0.1
        ),
        TS4TS5LowerThreshold = cms.vdouble(
            100, 120, 160, 200, 300, 
            500
        ),
        TS4TS5UpperCut = cms.vdouble(1, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70, 90, 100, 400),
        TS5TS6ChargeThreshold = cms.double(70),
        TS5TS6UpperChargeThreshold = cms.double(20),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(True),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(True),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(True),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(True),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(True),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    tsFromDB = cms.bool(False)
)


process.hbheprerecoMB = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        activeBXs = cms.vint32(-1, 0, 1),
        applyPedConstraint = cms.bool(True),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(True),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        chiSqSwitch = cms.double(15.0),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        deltaChiSqThresh = cms.double(0.001),
        dynamicPed = cms.bool(True),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        nMaxItersMin = cms.int32(500),
        nMaxItersNNLS = cms.int32(500),
        nnlsThresh = cms.double(1e-11),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 20000.0, 30000),
        ts4Min = cms.double(0.0),
        ts4Thresh = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(False),
        useMahi = cms.bool(False)
    ),
    digiLabelQIE11 = cms.InputTag("hcalDigis"),
    digiLabelQIE8 = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    0.0, 100.0, -50.0, 0.0, -15.0, 
                    0.15
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0
                )
            )
        )
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(True),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250, 500, 100000),
        LinearCut = cms.vdouble(-3, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20, 100, 100000),
        MinimumChargeThreshold = cms.double(20),
        MinimumTS4TS5Threshold = cms.double(100),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20, 100, 100000),
        RightSlopeCut = cms.vdouble(5, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150, 200, 100000),
        RightSlopeThreshold = cms.vdouble(250, 400, 100000),
        TS3TS4ChargeThreshold = cms.double(70),
        TS3TS4UpperChargeThreshold = cms.double(20),
        TS4TS5ChargeThreshold = cms.double(70),
        TS4TS5LowerCut = cms.vdouble(
            -1, -0.7, -0.5, -0.4, -0.3, 
            0.1
        ),
        TS4TS5LowerThreshold = cms.vdouble(
            100, 120, 160, 200, 300, 
            500
        ),
        TS4TS5UpperCut = cms.vdouble(1, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70, 90, 100, 400),
        TS5TS6ChargeThreshold = cms.double(70),
        TS5TS6UpperChargeThreshold = cms.double(20),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(True),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(False),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(False),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(True),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(False),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    tsFromDB = cms.bool(False)
)


process.hbhereco = cms.EDProducer("HBHEIsolatedNoiseReflagger",
    EBThreshold = cms.double(0.07),
    EEThreshold = cms.double(0.3),
    EcalAcceptSeverityLevel = cms.uint32(3),
    HBThreshold = cms.double(0.7),
    HEDThreshold = cms.double(0.8),
    HESThreshold = cms.double(0.8),
    HcalAcceptSeverityLevel = cms.uint32(9),
    LooseDiHitEne = cms.double(50.0),
    LooseEcalIsol = cms.double(0.08),
    LooseHPDEne1 = cms.double(20.0),
    LooseHPDEne2 = cms.double(80.0),
    LooseHPDHits1 = cms.int32(6),
    LooseHPDHits2 = cms.int32(3),
    LooseHcalIsol = cms.double(0.08),
    LooseMonoHitEne = cms.double(35.0),
    LooseRBXEne1 = cms.double(30.0),
    LooseRBXEne2 = cms.double(160.0),
    LooseRBXHits1 = cms.int32(14),
    LooseRBXHits2 = cms.int32(6),
    LooseTrackIsol = cms.double(0.1),
    MinValidTrackNHits = cms.int32(5),
    MinValidTrackPt = cms.double(0.3),
    MinValidTrackPtBarrel = cms.double(0.9),
    RBXEneThreshold = cms.double(500.0),
    TightDiHitEne = cms.double(15.0),
    TightEcalIsol = cms.double(0.04),
    TightHPDEne1 = cms.double(10.0),
    TightHPDEne2 = cms.double(30.0),
    TightHPDHits1 = cms.int32(6),
    TightHPDHits2 = cms.int32(3),
    TightHcalIsol = cms.double(0.04),
    TightMonoHitEne = cms.double(15.0),
    TightRBXEne1 = cms.double(25.0),
    TightRBXEne2 = cms.double(60.0),
    TightRBXHits1 = cms.int32(12),
    TightRBXHits2 = cms.int32(7),
    TightTrackIsol = cms.double(0.05),
    UseAllCombinedRechits = cms.bool(True),
    UseEcalRecoveredHits = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(True),
    debug = cms.untracked.bool(False),
    ebInput = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeInput = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheInput = cms.InputTag("hbheprereco"),
    trackExtrapolationInput = cms.InputTag("trackExtrapolator")
)


process.hbherecoMB = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        activeBXs = cms.vint32(-1, 0, 1),
        applyPedConstraint = cms.bool(True),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(True),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        chiSqSwitch = cms.double(15.0),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        deltaChiSqThresh = cms.double(0.001),
        dynamicPed = cms.bool(True),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        nMaxItersMin = cms.int32(500),
        nMaxItersNNLS = cms.int32(500),
        nnlsThresh = cms.double(1e-11),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 20000.0, 30000),
        ts4Min = cms.double(0.0),
        ts4Thresh = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(False),
        useMahi = cms.bool(False)
    ),
    digiLabelQIE11 = cms.InputTag("hcalDigis"),
    digiLabelQIE8 = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    0.0, 100.0, -50.0, 0.0, -15.0, 
                    0.15
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0
                )
            )
        )
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(True),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250, 500, 100000),
        LinearCut = cms.vdouble(-3, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20, 100, 100000),
        MinimumChargeThreshold = cms.double(20),
        MinimumTS4TS5Threshold = cms.double(100),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20, 100, 100000),
        RightSlopeCut = cms.vdouble(5, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150, 200, 100000),
        RightSlopeThreshold = cms.vdouble(250, 400, 100000),
        TS3TS4ChargeThreshold = cms.double(70),
        TS3TS4UpperChargeThreshold = cms.double(20),
        TS4TS5ChargeThreshold = cms.double(70),
        TS4TS5LowerCut = cms.vdouble(
            -1, -0.7, -0.5, -0.4, -0.3, 
            0.1
        ),
        TS4TS5LowerThreshold = cms.vdouble(
            100, 120, 160, 200, 300, 
            500
        ),
        TS4TS5UpperCut = cms.vdouble(1, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70, 90, 100, 400),
        TS5TS6ChargeThreshold = cms.double(70),
        TS5TS6UpperChargeThreshold = cms.double(20),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(True),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(False),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(False),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(True),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(False),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    tsFromDB = cms.bool(False)
)


process.hfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hfprerecoMB = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hfreco = cms.EDProducer("HFPhase1Reconstructor",
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            2.0, 0.0, 1.0, 0.0, 0.0, 
            1.0, 0.0, 1.0, 0.0, 2.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            1.0
        ),
        minChargeForOvershoot = cms.double(10000000000.0),
        minChargeForUndershoot = cms.double(10000000000.0),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(True),
    inputLabel = cms.InputTag("hfprereco"),
    setNoiseFlags = cms.bool(True),
    useChannelQualityFromDB = cms.bool(True)
)


process.hfrecoMB = cms.EDProducer("HFPhase1Reconstructor",
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFSimpleTimeCheck'),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            2.0, 0.0, 1.0, 0.0, 0.0, 
            1.0, 0.0, 1.0, 0.0, 2.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            1.0
        ),
        minChargeForOvershoot = cms.double(10000000000.0),
        minChargeForUndershoot = cms.double(10000000000.0),
        rejectAllFailures = cms.bool(False),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(True),
    inputLabel = cms.InputTag("hfprerecoMB"),
    setNoiseFlags = cms.bool(False),
    useChannelQualityFromDB = cms.bool(True)
)


process.hgcalLayerClusters = cms.EDProducer("HGCalLayerClusterProducer",
    HGCBHInput = cms.InputTag("HGCalRecHit","HGCHEBRecHits"),
    HGCEEInput = cms.InputTag("HGCalRecHit","HGCEERecHits"),
    HGCFHInput = cms.InputTag("HGCalRecHit","HGCHEFRecHits"),
    dEdXweights = cms.vdouble(
        0.0, 8.603, 8.0675, 8.0675, 8.0675, 
        8.0675, 8.0675, 8.0675, 8.0675, 8.0675, 
        8.9515, 10.135, 10.135, 10.135, 10.135, 
        10.135, 10.135, 10.135, 10.135, 10.135, 
        11.682, 13.654, 13.654, 13.654, 13.654, 
        13.654, 13.654, 13.654, 38.2005, 55.0265, 
        49.871, 49.871, 49.871, 49.871, 49.871, 
        49.871, 49.871, 49.871, 49.871, 49.871, 
        62.005, 83.1675, 92.196, 92.196, 92.196, 
        92.196, 92.196, 92.196, 92.196, 92.196, 
        92.196, 92.196, 46.098
    ),
    deltac = cms.vdouble(2, 2, 5),
    dependSensor = cms.bool(True),
    detector = cms.string('all'),
    doSharing = cms.bool(False),
    ecut = cms.double(3),
    fcPerEle = cms.double(0.00016020506),
    fcPerMip = cms.vdouble(1.25, 2.57, 3.88),
    kappa = cms.double(9),
    noiseMip = cms.PSet(
        refToPSet_ = cms.string('HGCAL_noise_MIP')
    ),
    noises = cms.PSet(
        refToPSet_ = cms.string('HGCAL_noises')
    ),
    thicknessCorrection = cms.vdouble(1.132, 1.092, 1.084),
    verbosity = cms.untracked.uint32(3)
)


process.hgcalMultiClusters = cms.EDProducer("HGCalMultiClusterProducer",
    HGCBHInput = cms.InputTag("HGCalRecHit","HGCHEBRecHits"),
    HGCEEInput = cms.InputTag("HGCalRecHit","HGCEERecHits"),
    HGCFHInput = cms.InputTag("HGCalRecHit","HGCHEFRecHits"),
    HGCLayerClusters = cms.InputTag("hgcalLayerClusters"),
    HGCLayerClustersSharing = cms.InputTag("hgcalLayerClusters","sharing"),
    doSharing = cms.bool(False),
    minClusters = cms.uint32(3),
    multiclusterRadii = cms.vdouble(2, 5, 5),
    verbosity = cms.untracked.uint32(3)
)


process.horeco = cms.EDProducer("HcalHitReconstructor",
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(True),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.horecoMB = cms.EDProducer("HcalSimpleReconstructor",
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctionPhaseNS = cms.double(13),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    firstSample = cms.int32(4),
    samplesToAdd = cms.int32(4),
    tsFromDB = cms.bool(True)
)


process.hybridSuperClusters = cms.EDProducer("UnifiedSCCollectionProducer",
    bcCollection = cms.string('hybridBarrelBasicClusters'),
    bcCollectionUncleanOnly = cms.string('uncleanOnlyHybridBarrelBasicClusters'),
    cleanBcCollection = cms.InputTag("cleanedHybridSuperClusters","hybridBarrelBasicClusters"),
    cleanScCollection = cms.InputTag("cleanedHybridSuperClusters"),
    scCollection = cms.string(''),
    scCollectionUncleanOnly = cms.string('uncleanOnlyHybridSuperClusters'),
    uncleanBcCollection = cms.InputTag("uncleanedHybridSuperClusters","hybridBarrelBasicClusters"),
    uncleanScCollection = cms.InputTag("uncleanedHybridSuperClusters")
)


process.interestingDetIdCollectionProducer = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag(""),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("hybridSuperClusters","hybridBarrelBasicClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdEBU = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridBarrelBasicClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapBasicClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdOOTPFEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterOOTECAL","particleFlowBasicClusterOOTECALBarrel"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdOOTPFEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterOOTECAL","particleFlowBasicClusterOOTECALEndcap"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdOOTPFES = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterOOTECAL","particleFlowBasicClusterOOTECALPreshower"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(False),
    keepNextToDead = cms.bool(False),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    severityLevel = cms.int32(-1)
)


process.interestingEcalDetIdPFEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterECAL","particleFlowBasicClusterECALBarrel"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdPFEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterECAL","particleFlowBasicClusterECALEndcap"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdPFES = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterECAL","particleFlowBasicClusterECALPreshower"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(False),
    keepNextToDead = cms.bool(False),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    severityLevel = cms.int32(-1)
)


process.interestingEcalDetIdRefinedEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowEGamma","EBEEClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdRefinedEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowEGamma","EBEEClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdRefinedES = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowEGamma","ESClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(False),
    keepNextToDead = cms.bool(False),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    severityLevel = cms.int32(-1)
)


process.interestingTrackEcalDetIds = cms.EDProducer("InterestingTrackEcalDetIdProducer",
    MinTrackPt = cms.double(50.0),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useGEM = cms.bool(False),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackCollection = cms.InputTag("generalTracks")
)


process.islandBasicClusters = cms.EDProducer("IslandClusterProducer",
    IslandBarrelSeedThr = cms.double(0.5),
    IslandEndcapSeedThr = cms.double(0.18),
    VerbosityLevel = cms.string('ERROR'),
    barrelClusterCollection = cms.string('islandBarrelBasicClusters'),
    barrelHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    barrelShapeAssociation = cms.string('islandBarrelShapeAssoc'),
    clustershapecollectionEB = cms.string('islandBarrelShape'),
    clustershapecollectionEE = cms.string('islandEndcapShape'),
    endcapClusterCollection = cms.string('islandEndcapBasicClusters'),
    endcapHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    endcapShapeAssociation = cms.string('islandEndcapShapeAssoc'),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    )
)


process.islandSuperClusters = cms.EDProducer("SuperClusterProducer",
    VerbosityLevel = cms.string('ERROR'),
    barrelClusterCollection = cms.string('islandBarrelBasicClusters'),
    barrelClusterProducer = cms.string('islandBasicClusters'),
    barrelEtaSearchRoad = cms.double(0.06),
    barrelPhiSearchRoad = cms.double(0.8),
    barrelSuperclusterCollection = cms.string('islandBarrelSuperClusters'),
    doBarrel = cms.bool(True),
    doEndcaps = cms.bool(True),
    endcapClusterCollection = cms.string('islandEndcapBasicClusters'),
    endcapClusterProducer = cms.string('islandBasicClusters'),
    endcapEtaSearchRoad = cms.double(0.14),
    endcapPhiSearchRoad = cms.double(0.6),
    endcapSuperclusterCollection = cms.string('islandEndcapSuperClusters'),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    seedTransverseEnergyThreshold = cms.double(1.0)
)


process.kt4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.4),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.kt6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.6),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.kt6PFJetsForRhoCorrection = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(2.5),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.6),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.multi5x5BasicClustersCleaned = cms.EDProducer("Multi5x5ClusterProducer",
    IslandBarrelSeedThr = cms.double(0.5),
    IslandEndcapSeedThr = cms.double(0.18),
    RecHitFlagToBeExcluded = cms.vstring(
        'kFaultyHardware', 
        'kNeighboursRecovered', 
        'kTowerRecovered', 
        'kDead', 
        'kWeird'
    ),
    barrelClusterCollection = cms.string('multi5x5BarrelBasicClusters'),
    barrelHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    doBarrel = cms.bool(False),
    doEndcap = cms.bool(True),
    endcapClusterCollection = cms.string('multi5x5EndcapBasicClusters'),
    endcapHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    reassignSeedCrysToClusterItSeeds = cms.bool(True)
)


process.multi5x5BasicClustersUncleaned = cms.EDProducer("Multi5x5ClusterProducer",
    IslandBarrelSeedThr = cms.double(0.5),
    IslandEndcapSeedThr = cms.double(0.18),
    RecHitFlagToBeExcluded = cms.vstring(),
    barrelClusterCollection = cms.string('multi5x5BarrelBasicClusters'),
    barrelHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    doBarrel = cms.bool(False),
    doEndcap = cms.bool(True),
    endcapClusterCollection = cms.string('multi5x5EndcapBasicClusters'),
    endcapHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    reassignSeedCrysToClusterItSeeds = cms.bool(True)
)


process.multi5x5PreshowerClusterShape = cms.EDProducer("PreshowerClusterShapeProducer",
    PreshowerClusterShapeCollectionX = cms.string('multi5x5PreshowerXClustersShape'),
    PreshowerClusterShapeCollectionY = cms.string('multi5x5PreshowerYClustersShape'),
    debugLevel = cms.string('INFO'),
    endcapSClusterProducer = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    preshPi0Nstrip = cms.int32(5),
    preshRecHitProducer = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    preshStripEnergyCut = cms.double(0.0)
)


process.multi5x5SuperClusters = cms.EDProducer("UnifiedSCCollectionProducer",
    bcCollection = cms.string('multi5x5EndcapBasicClusters'),
    bcCollectionUncleanOnly = cms.string('uncleanOnlyMulti5x5EndcapBasicClusters'),
    cleanBcCollection = cms.InputTag("multi5x5BasicClustersCleaned","multi5x5EndcapBasicClusters"),
    cleanScCollection = cms.InputTag("multi5x5SuperClustersCleaned","multi5x5EndcapSuperClusters"),
    scCollection = cms.string('multi5x5EndcapSuperClusters'),
    scCollectionUncleanOnly = cms.string('uncleanOnlyMulti5x5EndcapSuperClusters'),
    uncleanBcCollection = cms.InputTag("multi5x5BasicClustersUncleaned","multi5x5EndcapBasicClusters"),
    uncleanScCollection = cms.InputTag("multi5x5SuperClustersUncleaned","multi5x5EndcapSuperClusters")
)


process.multi5x5SuperClustersCleaned = cms.EDProducer("Multi5x5SuperClusterProducer",
    barrelClusterTag = cms.InputTag("multi5x5BasicClusters","multi5x5BarrelBasicClustersCleaned"),
    barrelEtaSearchRoad = cms.double(0.06),
    barrelPhiSearchRoad = cms.double(0.8),
    barrelSuperclusterCollection = cms.string('multi5x5BarrelSuperClusters'),
    bremRecoveryPset = cms.PSet(
        barrel = cms.PSet(
            cryMin = cms.int32(2),
            cryVec = cms.vint32(
                16, 13, 11, 10, 9, 
                8, 7, 6, 5, 4, 
                3
            ),
            etVec = cms.vdouble(
                5.0, 10.0, 15.0, 20.0, 30.0, 
                40.0, 45.0, 55.0, 135.0, 195.0, 
                225.0
            )
        ),
        endcap = cms.PSet(
            a = cms.double(47.85),
            b = cms.double(108.8),
            c = cms.double(0.1201)
        )
    ),
    doBarrel = cms.bool(False),
    doEndcaps = cms.bool(True),
    dynamicPhiRoad = cms.bool(False),
    endcapClusterTag = cms.InputTag("multi5x5BasicClustersCleaned","multi5x5EndcapBasicClusters"),
    endcapEtaSearchRoad = cms.double(0.14),
    endcapPhiSearchRoad = cms.double(0.6),
    endcapSuperclusterCollection = cms.string('multi5x5EndcapSuperClusters'),
    seedTransverseEnergyThreshold = cms.double(1.0)
)


process.multi5x5SuperClustersUncleaned = cms.EDProducer("Multi5x5SuperClusterProducer",
    barrelClusterTag = cms.InputTag("multi5x5BasicClusters","multi5x5BarrelBasicClustersCleaned"),
    barrelEtaSearchRoad = cms.double(0.06),
    barrelPhiSearchRoad = cms.double(0.8),
    barrelSuperclusterCollection = cms.string('multi5x5BarrelSuperClusters'),
    bremRecoveryPset = cms.PSet(
        barrel = cms.PSet(
            cryMin = cms.int32(2),
            cryVec = cms.vint32(
                16, 13, 11, 10, 9, 
                8, 7, 6, 5, 4, 
                3
            ),
            etVec = cms.vdouble(
                5.0, 10.0, 15.0, 20.0, 30.0, 
                40.0, 45.0, 55.0, 135.0, 195.0, 
                225.0
            )
        ),
        endcap = cms.PSet(
            a = cms.double(47.85),
            b = cms.double(108.8),
            c = cms.double(0.1201)
        )
    ),
    doBarrel = cms.bool(False),
    doEndcaps = cms.bool(True),
    dynamicPhiRoad = cms.bool(False),
    endcapClusterProducer = cms.string('multi5x5BasicClustersUncleaned'),
    endcapClusterTag = cms.InputTag("multi5x5BasicClustersCleaned","multi5x5EndcapBasicClusters"),
    endcapEtaSearchRoad = cms.double(0.14),
    endcapPhiSearchRoad = cms.double(0.6),
    endcapSuperclusterCollection = cms.string('multi5x5EndcapSuperClusters'),
    seedTransverseEnergyThreshold = cms.double(1.0)
)


process.multi5x5SuperClustersWithPreshower = cms.EDProducer("PreshowerPhiClusterProducer",
    assocSClusterCollection = cms.string(''),
    endcapSClusterProducer = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapSuperClusters"),
    esPhiClusterDeltaEta = cms.double(0.15),
    esPhiClusterDeltaPhi = cms.double(0.12),
    esStripEnergyCut = cms.double(0.0),
    etThresh = cms.double(0.0),
    preshClusterCollectionX = cms.string('preshowerXClusters'),
    preshClusterCollectionY = cms.string('preshowerYClusters'),
    preshRecHitProducer = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
)


process.muonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("muons")
)


process.muonSelectionProducers = cms.EDProducer("MuonSelectionProducers",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    chIsoVals = cms.InputTag("elPFIsoValueCharged03PFIdPFIso"),
    conversionCollection = cms.InputTag("allConversions"),
    emIsoVals = cms.InputTag("elPFIsoValueGamma03PFIdPFIso"),
    muonCollection = cms.InputTag("muons"),
    nhIsoVals = cms.InputTag("elPFIsoValueNeutral03PFIdPFIso"),
    rhoFastJet = cms.InputTag("kt6PFJetsForRhoCorrection","rho"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.particleFlowClusterECAL = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        algoName = cms.string('PFClusterEMEnergyCorrector'),
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        autoDetectBunchSpacing = cms.bool(True),
        bunchSpacing = cms.int32(25),
        ebSrFlagLabel = cms.InputTag("ecalDigis"),
        eeSrFlagLabel = cms.InputTag("ecalDigis"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        srfAwareCorrection = cms.bool(True),
        verticesLabel = cms.InputTag("offlinePrimaryVertices")
    ),
    inputECAL = cms.InputTag("particleFlowClusterECALUncorrected"),
    inputPS = cms.InputTag("particleFlowClusterPS"),
    minimumPSEnergy = cms.double(0)
)


process.particleFlowClusterECALUncorrected = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitECAL"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ), 
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                gatheringThreshold = cms.vdouble(0.8, 0.8, 0.8, 0.8),
                gatheringThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ), 
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5, 
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2, 
                    0.2, 0.2
                ),
                gatheringThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0, 
                    0.0, 0.0
                )
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.8, 0.8, 0.8, 0.8)
                ), 
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5, 
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2, 
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.8, 0.8, 0.8, 0.8)
                ), 
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5, 
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2, 
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.8, 0.8, 0.8, 0.8)
            ), 
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5, 
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2, 
                    0.2, 0.2
                )
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHBHE"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                seedingThreshold = cms.vdouble(1.0, 1.0, 1.0, 1.0),
                seedingThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ), 
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5, 
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275, 
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0, 
                    0.0, 0.0
                )
            )
        )
    )
)


process.particleFlowClusterHBHETimeSelected = cms.EDProducer("PFClusterTimeSelector",
    cuts = cms.VPSet(
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(16.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        )
    ),
    src = cms.InputTag("particleFlowClusterHBHE")
)


process.particleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("particleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.8, 0.8, 0.8, 0.8)
                ), 
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5, 
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2, 
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    )
)


process.particleFlowClusterHF = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HF_EM'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('HF_EM'),
                recHitEnergyNorm = cms.double(0.8)
            ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                recHitEnergyNorm = cms.double(0.8)
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHF"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(0),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HF_EM'),
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowClusterHGCal = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('RealisticSimClusterMapper'),
        calibMaxEta = cms.double(3.0),
        calibMinEta = cms.double(1.4),
        egammaCalib = cms.vdouble(
            1.0, 1.0, 1.01, 1.01, 1.02, 
            1.03, 1.04, 1.04
        ),
        exclusiveFraction = cms.double(0.6),
        hadronCalib = cms.vdouble(
            1.24, 1.24, 1.24, 1.23, 1.24, 
            1.25, 1.29, 1.29
        ),
        invisibleFraction = cms.double(0.6),
        maxDforTimingSquared = cms.double(4.0),
        maxDistance = cms.double(10.0),
        maxDistanceFilter = cms.bool(True),
        minNHitsforTiming = cms.uint32(3),
        simClusterSrc = cms.InputTag("mix","MergedCaloTruth"),
        thresholdsByDetector = cms.VPSet(),
        timeOffset = cms.double(5),
        useMCFractionsForExclEnergy = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(

    ),
    positionReCalc = cms.PSet(
        algoName = cms.string('Cluster3DPCACalculator'),
        minFractionInCalc = cms.double(1e-09),
        updateTiming = cms.bool(False)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHGC"),
    seedFinder = cms.PSet(
        algoName = cms.string('PassThruSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet()
    )
)


process.particleFlowClusterHGCalFromMultiCl = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('PFClusterFromHGCalMultiCluster'),
        clusterSrc = cms.InputTag("hgcalMultiClusters"),
        thresholdsByDetector = cms.VPSet()
    ),
    pfClusterBuilder = cms.PSet(

    ),
    positionReCalc = cms.PSet(
        algoName = cms.string('Cluster3DPCACalculator'),
        minFractionInCalc = cms.double(1e-09),
        updateTiming = cms.bool(False)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHGC"),
    seedFinder = cms.PSet(
        algoName = cms.string('PassThruSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet()
    )
)


process.particleFlowClusterHO = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING0'),
                gatheringThreshold = cms.double(0.05),
                gatheringThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                gatheringThreshold = cms.double(0.05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING0'),
                recHitEnergyNorm = cms.double(0.05)
            ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                recHitEnergyNorm = cms.double(0.05)
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHO"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING0'),
                seedingThreshold = cms.double(0.08),
                seedingThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                seedingThreshold = cms.double(0.08),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowClusterPS = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ), 
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitPS"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ), 
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowRecHitECAL = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ), 
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEB")
        ), 
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ), 
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEE")
        )
    )
)


process.particleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitHCALNavigator'),
        sigmaCut = cms.double(4.0),
        timeResolutionCalc = cms.PSet(
            constantTerm = cms.double(1.92),
            constantTermLowE = cms.double(6.0),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(8.64),
            noiseTermLowE = cms.double(0.0),
            threshHighE = cms.double(8.0),
            threshLowE = cms.double(2.0)
        )
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                cuts = cms.VPSet(
                    cms.PSet(
                        depth = cms.vint32(1, 2, 3, 4),
                        detectorEnum = cms.int32(1),
                        threshold = cms.vdouble(0.8, 0.8, 0.8, 0.8)
                    ), 
                    cms.PSet(
                        depth = cms.vint32(
                            1, 2, 3, 4, 5, 
                            6, 7
                        ),
                        detectorEnum = cms.int32(2),
                        threshold = cms.vdouble(
                            0.1, 0.2, 0.2, 0.2, 0.2, 
                            0.2, 0.2
                        )
                    )
                ),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            ), 
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )
        ),
        src = cms.InputTag("hbhereco")
    ))
)


process.particleFlowRecHitHF = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitHCALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        EMDepthCorrection = cms.double(22.0),
        HADDepthCorrection = cms.double(25.0),
        HFCalib29 = cms.double(1.07),
        LongFibre_Cut = cms.double(120.0),
        LongFibre_Fraction = cms.double(0.1),
        ShortFibre_Cut = cms.double(60.0),
        ShortFibre_Fraction = cms.double(0.01),
        name = cms.string('PFHFRecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0, 120.0, 60.0, 30.0),
                flags = cms.vstring(
                    'Standard', 
                    'HFLong', 
                    'HFShort', 
                    'HFDigi'
                ),
                maxSeverities = cms.vint32(11, 9, 9, 9),
                name = cms.string('PFRecHitQTestHCALChannel')
            ), 
            cms.PSet(
                cuts = cms.VPSet(cms.PSet(
                    depth = cms.vint32(1, 2),
                    detectorEnum = cms.int32(4),
                    threshold = cms.vdouble(1.2, 1.8)
                )),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            )
        ),
        src = cms.InputTag("hfreco"),
        thresh_HF = cms.double(0.4)
    ))
)


process.particleFlowRecHitHGC = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        hgcee = cms.PSet(
            name = cms.string('PFRecHitHGCEENavigator'),
            topologySource = cms.string('HGCalEESensitive')
        ),
        hgcheb = cms.PSet(
            name = cms.string('PFRecHitHGCHENavigator'),
            topologySource = cms.string('HGCalHEScintillatorSensitive')
        ),
        hgchef = cms.PSet(
            name = cms.string('PFRecHitHGCHENavigator'),
            topologySource = cms.string('HGCalHESiliconSensitive')
        ),
        name = cms.string('PFRecHitHGCNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            geometryInstance = cms.string('HGCalEESensitive'),
            name = cms.string('PFHGCEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestHGCalThresholdSNR'),
                thresholdSNR = cms.double(5.0)
            )),
            src = cms.InputTag("HGCalRecHit","HGCEERecHits")
        ), 
        cms.PSet(
            geometryInstance = cms.string('HGCalHESiliconSensitive'),
            name = cms.string('PFHGCHEFRecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestHGCalThresholdSNR'),
                thresholdSNR = cms.double(5.0)
            )),
            src = cms.InputTag("HGCalRecHit","HGCHEFRecHits")
        ), 
        cms.PSet(
            geometryInstance = cms.string(''),
            name = cms.string('PFHGCHEBRecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestHGCalThresholdSNR'),
                thresholdSNR = cms.double(5.0)
            )),
            src = cms.InputTag("HGCalRecHit","HGCHEBRecHits")
        )
    )
)


process.particleFlowRecHitHO = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitHCALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHORecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.05)
            ), 
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )
        ),
        src = cms.InputTag("horeco")
    ))
)


process.particleFlowRecHitPS = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.0)
            ), 
            cms.PSet(
                cleaningThreshold = cms.double(0.0),
                name = cms.string('PFRecHitQTestES'),
                topologicalCleaning = cms.bool(True)
            )
        ),
        src = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.particleFlowSuperClusterECAL = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.0),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.0),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterECALBox = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Box'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.28),
    phiwidth_SuperClusterEndcap = cms.double(0.28),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(3.0),
    thresh_PFClusterSeedEndcap = cms.double(5.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(False),
    useRegression = cms.bool(False),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterECALMustache = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.0),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.0),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterHGCal = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.0),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.0),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterHGCalFromMultiCl = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.0),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.0),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowTimeAssignerECAL = cms.EDProducer("PFClusterTimeAssigner",
    src = cms.InputTag("particleFlowClusterECALUncorrected"),
    timeResoSrc = cms.InputTag("ecalBarrelClusterFastTimer","PerfectResolutionModelResolution"),
    timeSrc = cms.InputTag("ecalBarrelClusterFastTimer","PerfectResolutionModel")
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(False),
    addGenMatch = cms.bool(True),
    addMVAVariables = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    computeMiniIso = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        cutBasedElectronHLTPreselection_Summer16_V1 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronHLTPreselection-Summer16-V1"),
        cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
        cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
        cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
        cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
        cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
        cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
        cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
        cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto")
    ),
    electronSource = cms.InputTag("electronRecalibSCAssociator"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(False),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(False),
    genParticleMatch = cms.InputTag("electronMatch"),
    isoDeposits = cms.PSet(

    ),
    miniIsoParamsB = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0
    ),
    miniIsoParamsE = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.015, 
        0.015, 0.08, 0.0, 0.0
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    reducedEndcapRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    usePfCandidateMultiMap = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    addTriggerMatching = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    computeMiniIso = cms.bool(False),
    computeMuonMVA = cms.bool(False),
    computeSoftMuonMVA = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPfEcalEnergy = cms.bool(True),
    embedPickyMuon = cms.bool(True),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(True),
    embedTrack = cms.bool(False),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    hltCollectionFilters = cms.vstring('*'),
    isoDeposits = cms.PSet(

    ),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001, 
        0.01, 0.01, 0.01, 0.0
    ),
    muonSimInfo = cms.InputTag("muonSimClassifier"),
    muonSource = cms.InputTag("muons"),
    mvaDrMax = cms.double(0.4),
    mvaJetTag = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    mvaL1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    mvaL1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    mvaTrainingFile = cms.string('RecoMuon/MuonIdentification/data/mu_BDTG_Run2017.weights.xml'),
    mvaUseJec = cms.bool(True),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    recomputeBasicSelectors = cms.bool(True),
    resolutions = cms.PSet(

    ),
    rho = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
    softMvaTrainingFile = cms.string('RecoMuon/MuonIdentification/data/TMVA-muonid-bmm4-B-25.weights.xml'),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    isoDeposits = cms.PSet(

    ),
    photonIDSources = cms.PSet(
        fiducial = cms.InputTag("phoSelectionProducers","fiducial"),
        loose = cms.InputTag("phoSelectionProducers","loose"),
        loose25nsRun2 = cms.InputTag("phoSelectionProducers","loose25nsRun2"),
        medium = cms.InputTag("phoSelectionProducers","medium"),
        medium25nsRun2 = cms.InputTag("phoSelectionProducers","medium25nsRun2"),
        tight = cms.InputTag("phoSelectionProducers","tight"),
        tight25nsRun2 = cms.InputTag("phoSelectionProducers","tight25nsRun2")
    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    reducedEndcapRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    resolutions = cms.PSet(

    ),
    saveRegressionData = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("PATTriggerProducer",
    ReadPrescalesFromFile = cms.bool(False),
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis"),
    l1GtRecordInputTag = cms.InputTag("gtDigis"),
    l1GtTriggerMenuLiteInputTag = cms.InputTag("gtDigis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
    onlyStandAlone = cms.bool(False),
    packTriggerLabels = cms.bool(False),
    processName = cms.string('HLT')
)


process.patTriggerEvent = cms.EDProducer("PATTriggerEventProducer",
    patTriggerMatches = cms.VInputTag("PatElectronsTriggerMatch"),
    processName = cms.string('HLT')
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME"),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.phoSelectionProducers = cms.EDProducer("PhoSelectionProducers",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    chIsoVals = cms.InputTag("phPFIsoValueCharged03PFIdPFIso"),
    conversionCollection = cms.InputTag("allConversions"),
    emIsoVals = cms.InputTag("phPFIsoValueGamma03PFIdPFIso"),
    nhIsoVals = cms.InputTag("phPFIsoValueNeutral03PFIdPFIso"),
    photonCollection = cms.InputTag("gedPhotons"),
    rhoFastJet = cms.InputTag("kt6PFJetsForRhoCorrection","rho"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.photonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedPhotons")
)


process.puppi = cms.EDProducer("PuppiProducer",
    DeltaZCut = cms.double(0.3),
    MinPuppiWeight = cms.double(0.01),
    PtMaxNeutrals = cms.double(200.0),
    UseDeltaZCut = cms.bool(True),
    algos = cms.VPSet(
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(1.0),
            MinNeutralPt = cms.vdouble(0.2),
            MinNeutralPtSlope = cms.vdouble(0.015),
            RMSEtaSF = cms.vdouble(1.0),
            etaMax = cms.vdouble(2.5),
            etaMin = cms.vdouble(0.0),
            ptMin = cms.vdouble(0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(True),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.1),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(True)
            ))
        ), 
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(0.9, 0.75),
            MinNeutralPt = cms.vdouble(1.7, 2.0),
            MinNeutralPtSlope = cms.vdouble(0.08, 0.08),
            RMSEtaSF = cms.vdouble(1.2, 0.95),
            etaMax = cms.vdouble(3.0, 10.0),
            etaMin = cms.vdouble(2.5, 3.0),
            ptMin = cms.vdouble(0.0, 0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(True),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.5),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(False)
            ))
        )
    ),
    applyCHS = cms.bool(True),
    candName = cms.InputTag("particleFlow"),
    clonePackedCands = cms.bool(False),
    invertPuppi = cms.bool(False),
    puppiDiagnostics = cms.bool(False),
    puppiForLeptons = cms.bool(False),
    useExistingWeights = cms.bool(False),
    useExp = cms.bool(False),
    useWeightsNoLep = cms.bool(False),
    vertexName = cms.InputTag("offlinePrimaryVertices"),
    vtxNdofCut = cms.int32(4),
    vtxZCut = cms.double(24)
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.reducedEcalRecHitsEB = cms.EDProducer("ReducedRecHitCollectionProducer",
    interestingDetIdCollections = cms.VInputTag(
        cms.InputTag("interestingEcalDetIdEB"), cms.InputTag("interestingEcalDetIdEBU"), cms.InputTag("interestingEcalDetIdPFEB"), cms.InputTag("interestingEcalDetIdRefinedEB"), cms.InputTag("interestingEcalDetIdOOTPFEB"), 
        cms.InputTag("interestingGedEleIsoDetIdEB"), cms.InputTag("interestingGedGamIsoDetIdEB"), cms.InputTag("interestingOotGamIsoDetIdEB"), cms.InputTag("interestingGamIsoDetIdEB"), cms.InputTag("muonEcalDetIds"), 
        cms.InputTag("interestingTrackEcalDetIds")
    ),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    reducedHitsCollection = cms.string('')
)


process.reducedEcalRecHitsEE = cms.EDProducer("ReducedRecHitCollectionProducer",
    interestingDetIdCollections = cms.VInputTag(
        cms.InputTag("interestingEcalDetIdEE"), cms.InputTag("interestingEcalDetIdPFEE"), cms.InputTag("interestingEcalDetIdRefinedEE"), cms.InputTag("interestingEcalDetIdOOTPFEE"), cms.InputTag("interestingGedEleIsoDetIdEE"), 
        cms.InputTag("interestingGedGamIsoDetIdEE"), cms.InputTag("interestingOotGamIsoDetIdEE"), cms.InputTag("interestingGamIsoDetIdEE"), cms.InputTag("muonEcalDetIds"), cms.InputTag("interestingTrackEcalDetIds")
    ),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    reducedHitsCollection = cms.string('')
)


process.reducedEcalRecHitsES = cms.EDProducer("ReducedESRecHitCollectionProducer",
    EcalRecHitCollectionES = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    EndcapSuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    OutputLabel_ES = cms.string(''),
    interestingDetIds = cms.VInputTag(cms.InputTag("interestingEcalDetIdPFES"), cms.InputTag("interestingEcalDetIdRefinedES"), cms.InputTag("interestingEcalDetIdOOTPFES")),
    interestingDetIdsNotToClean = cms.VInputTag(cms.InputTag("interestingGedEgammaIsoESDetId"), cms.InputTag("interestingOotEgammaIsoESDetId")),
    scEtThreshold = cms.double(15)
)


process.reducedHcalRecHits = cms.EDProducer("HcalHitSelection",
    hbheTag = cms.InputTag("hbhereco"),
    hfTag = cms.InputTag("hfreco"),
    hoSeverityLevel = cms.int32(13),
    hoTag = cms.InputTag("horeco"),
    interestingDetIds = cms.VInputTag(cms.InputTag("interestingGedEgammaIsoHCALDetId"), cms.InputTag("interestingOotEgammaIsoHCALDetId"))
)


process.selectDigi = cms.EDProducer("EcalDigiSelector",
    EcalEBDigiTag = cms.InputTag("ecalDigis","ebDigis"),
    EcalEBRecHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EcalEEDigiTag = cms.InputTag("ecalDigis","eeDigis"),
    EcalEERecHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    barrelSuperClusterProducer = cms.InputTag("uncleanedHybridSuperClusters"),
    cluster_pt_thresh = cms.double(10.0),
    endcapSuperClusterProducer = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    nclus_sel = cms.int32(2),
    selectedEcalEBDigiCollection = cms.string('selectedEcalEBDigiCollection'),
    selectedEcalEEDigiCollection = cms.string('selectedEcalEEDigiCollection'),
    single_cluster_thresh = cms.double(15.0)
)


process.slimmedECALELFElectrons = cms.EDProducer("PATElectronSlimmer",
    dropBasicClusters = cms.string('0'),
    dropClassifications = cms.string('pt < 5'),
    dropCorrections = cms.string('pt < 5'),
    dropExtrapolations = cms.string('pt < 5'),
    dropIsolations = cms.string('pt < 5'),
    dropPFlowClusters = cms.string('0'),
    dropPreshowerClusters = cms.string('0'),
    dropRecHits = cms.string('0'),
    dropSaturation = cms.string('pt < 5'),
    dropSeedCluster = cms.string('0'),
    dropShapes = cms.string('pt < 5'),
    dropSuperCluster = cms.string('0'),
    linkToPackedPFCandidates = cms.bool(False),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(
            cms.PSet(
                ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
                ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
                electron_config = cms.PSet(
                    electronSrc = cms.InputTag("patElectrons"),
                    energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
                    energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
                    energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
                    energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                photon_config = cms.PSet(

                )
            ), 
            cms.PSet(
                ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
                ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
                electron_config = cms.PSet(
                    electronSrc = cms.InputTag("patElectrons")
                ),
                modifierName = cms.string('EleIDModifierFromValueMaps'),
                photon_config = cms.PSet(

                )
            ), 
            cms.PSet(
                ecalRecHitsEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
                ecalRecHitsEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
                electron_config = cms.PSet(
                    electronSrc = cms.InputTag("patElectrons"),
                    loose25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    loose94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    medium5nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    medium94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    tight25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    tight94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    veto25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    veto94XV1Run2017 = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto")
                ),
                modifierName = cms.string('EleIDModifierFromBoolValueMaps'),
                photon_config = cms.PSet(

                )
            )
        )
    ),
    modifyElectrons = cms.bool(True),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    recoToPFMap = cms.InputTag("reducedEgamma","reducedGsfElectronPfCandMap"),
    reducedBarrelRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    reducedEndcapRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    saveNonZSClusterShapes = cms.string('pt > 5'),
    src = cms.InputTag("patElectrons")
)


process.slimmedElectrons = cms.EDProducer("PATElectronSlimmer",
    dropBasicClusters = cms.string('0'),
    dropClassifications = cms.string('pt < 5'),
    dropCorrections = cms.string('pt < 5'),
    dropExtrapolations = cms.string('pt < 5'),
    dropIsolations = cms.string('pt < 5'),
    dropPFlowClusters = cms.string('0'),
    dropPreshowerClusters = cms.string('0'),
    dropRecHits = cms.string('0'),
    dropSaturation = cms.string('pt < 5'),
    dropSeedCluster = cms.string('0'),
    dropShapes = cms.string('pt < 5'),
    dropSuperCluster = cms.string('0'),
    linkToPackedPFCandidates = cms.bool(True),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    modifyElectrons = cms.bool(True),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    recoToPFMap = cms.InputTag("reducedEgamma","reducedGsfElectronPfCandMap"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    saveNonZSClusterShapes = cms.string('pt > 5'),
    src = cms.InputTag("selectedPatElectrons")
)


process.softKiller = cms.EDProducer("SoftKillerProducer",
    PFCandidates = cms.InputTag("particleFlow"),
    Rho_EtaMax = cms.double(5.0),
    rParam = cms.double(0.4)
)


process.uncleanedHybridSuperClusters = cms.EDProducer("HybridClusterProducer",
    HybridBarrelSeedThr = cms.double(1.0),
    RecHitFlagToBeExcluded = cms.vstring(
        'kFaultyHardware', 
        'kTowerRecovered', 
        'kDead'
    ),
    RecHitSeverityToBeExcluded = cms.vstring(),
    basicclusterCollection = cms.string('hybridBarrelBasicClusters'),
    clustershapecollection = cms.string(''),
    dynamicEThresh = cms.bool(False),
    dynamicPhiRoad = cms.bool(False),
    eThreshA = cms.double(0.003),
    eThreshB = cms.double(0.1),
    eseed = cms.double(0.35),
    ethresh = cms.double(0.1),
    ewing = cms.double(0.0),
    excludeFlagged = cms.bool(False),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    recHitsCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    shapeAssociation = cms.string('hybridShapeAssoc'),
    step = cms.int32(17),
    superclusterCollection = cms.string(''),
    useEtForXi = cms.bool(True),
    xi = cms.double(0.0)
)


process.uncleanedOnlyCorrectedHybridSuperClusters = cms.EDProducer("EgammaSCCorrectionMaker",
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(True),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    hyb_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(8.0),
        brLinearLowThr = cms.double(1.1),
        fBremVec = cms.vdouble(-0.04382, 0.1169, 0.9267, -0.0009413, 1.419),
        fEtEtaVec = cms.vdouble(
            0, 1.00121, -0.63672, 0, 0, 
            0, 0.5655, 6.457, 0.5081, 8.0, 
            1.023, -0.00181
        )
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridSuperClusters"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    sigmaElectronicNoise = cms.double(0.03),
    superClusterAlgo = cms.string('Hybrid')
)


process.uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower = cms.EDProducer("EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string('ERROR'),
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(False),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    fix_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(6.0),
        brLinearLowThr = cms.double(0.9),
        fBremVec = cms.vdouble(-0.05228, 0.08738, 0.9508, 0.002677, 1.221),
        fEtEtaVec = cms.vdouble(
            1, -0.4386, -32.38, 0.6372, 15.67, 
            -0.0928, -2.462, 1.138, 20.93
        )
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("uncleanedOnlyMulti5x5SuperClustersWithPreshower"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    sigmaElectronicNoise = cms.double(0.15),
    superClusterAlgo = cms.string('Multi5x5')
)


process.uncleanedOnlyMulti5x5SuperClustersWithPreshower = cms.EDProducer("PreshowerPhiClusterProducer",
    assocSClusterCollection = cms.string(''),
    endcapSClusterProducer = cms.InputTag("multi5x5SuperClusters","uncleanOnlyMulti5x5EndcapSuperClusters"),
    esPhiClusterDeltaEta = cms.double(0.15),
    esPhiClusterDeltaPhi = cms.double(0.12),
    esStripEnergyCut = cms.double(0.0),
    etThresh = cms.double(0.0),
    preshClusterCollectionX = cms.string('preshowerXClusters'),
    preshClusterCollectionY = cms.string('preshowerYClusters'),
    preshRecHitProducer = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
)


process.zdcreco = cms.EDProducer("ZdcHitReconstructor",
    AuxTSvec = cms.vint32(4, 5, 6, 7),
    Subdetector = cms.string('ZDC'),
    correctForPhaseContainment = cms.bool(False),
    correctForTimeslew = cms.bool(False),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(0.0),
    digiLabelQIE10ZDC = cms.InputTag("hcalDigis","ZDC"),
    digiLabelcastor = cms.InputTag("castorDigis"),
    digiLabelhcal = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    lowGainFrac = cms.double(8.15),
    lowGainOffset = cms.int32(1),
    recoMethod = cms.int32(2),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(True),
    setNoiseFlags = cms.bool(True),
    setSaturationFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(False)
)


process.MinEleNumberFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("gedGsfElectrons")
)


process.MinMuonNumberFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("muons")
)


process.MinPhoNumberFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("gedPhotons")
)


process.MuFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("PassingMuonVeryLooseId")
)


process.NtupleFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring(
        'pathALCARECOEcalUncalZElectron', 
        'pathALCARECOEcalUncalWElectron', 
        'pathALCARECOEcalCalZElectron', 
        'pathALCARECOEcalCalWElectron', 
        'pathALCARECOEcalUncalZSCElectron', 
        'pathALCARECOEcalCalZSCElectron', 
        'pathALCARECOEcalUncalSingleElectron', 
        'pathALCARECOEcalCalSingleElectron'
    ),
    TriggerResultsTag = cms.InputTag("TriggerResults","","RECO"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.PassingMuonVeryLooseId = cms.EDFilter("MuonRefSelector",
    cut = cms.string('(isPFMuon) && (isGlobalMuon || isTrackerMuon)'),
    src = cms.InputTag("muons")
)


process.PassingPhotonVeryLooseId = cms.EDFilter("PhotonRefSelector",
    cut = cms.string('(abs(superCluster.eta)<3) && (pt > 10)&& ( (eta<1.479 && sigmaIetaIeta<0.02 && hadronicOverEm<0.06 )||( eta>=1.479 && sigmaIetaIeta<0.04 && hadronicOverEm<0.06 ) )'),
    src = cms.InputTag("gedPhotons")
)


process.PassingVetoId = cms.EDFilter("GsfElectronRefSelector",
    cut = cms.string("(abs(superCluster.eta)<3) && (energy*sin(superClusterPosition.theta)> 15) && (gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\')<=2) && ((isEB && ( ((pfIsolationVariables().sumChargedHadronPt + max(0.0,pfIsolationVariables().sumNeutralHadronEt + pfIsolationVariables().sumPhotonEt - 0.5 * pfIsolationVariables().sumPUPt))/p4.pt)<0.164369) && (full5x5_sigmaIetaIeta<0.011100) && ( - \t0.252044<deltaPhiSuperClusterTrackAtVtx< \t0.252044 ) && ( -0.016315<deltaEtaSuperClusterTrackAtVtx<0.016315 ) && (hadronicOverEm<0.345843)) || (isEE && (gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\')<=3) && ( ((pfIsolationVariables().sumChargedHadronPt + max(0.0,pfIsolationVariables().sumNeutralHadronEt + pfIsolationVariables().sumPhotonEt - 0.5 * pfIsolationVariables().sumPUPt))/p4.pt)<0.212604 ) && (full5x5_sigmaIetaIeta<0.033987) && ( -0.245263<deltaPhiSuperClusterTrackAtVtx<0.245263 ) && ( -0.010671<deltaEtaSuperClusterTrackAtVtx<0.010671 ) && (hadronicOverEm<0.134691) ))"),
    src = cms.InputTag("electronRecalibSCAssociator")
)


process.PhoFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("PassingPhotonVeryLooseId")
)


process.SCselector = cms.EDFilter("SuperClusterSelector",
    cut = cms.string('(eta>2.4 || eta<-2.4) && (energy*sin(position.theta)> 15)'),
    src = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower")
)


process.WFilterMC = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("combW")
)


process.WZFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("WZSelector")
)


process.WenuFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("WenuSelector")
)


process.ZFilterMC = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("combZ")
)


process.ZSCFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("EleSCSelector")
)


process.ZSCHltFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.ZeeFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("ZeeSelector")
)


process.ZmmgDimuonFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("ZmmgDimuons")
)


process.ZmmgFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("ZmmgCandidates")
)


process.ZmmgHLTFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring(
        'HLT_Mu*', 
        'HLT_IsoMu*', 
        'HLT_DoubleMu*'
    ),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.ZmmgLeadingMuons = cms.EDFilter("MuonSelector",
    cut = cms.string('pt > 20'),
    filter = cms.bool(True),
    src = cms.InputTag("ZmmgTrailingMuons")
)


process.ZmmgPhotons = cms.EDFilter("CandViewSelector",
    cut = cms.string('et > 5'),
    filter = cms.bool(True),
    src = cms.InputTag("ZmmgPhotonCandidates")
)


process.ZmmgTrailingMuons = cms.EDFilter("MuonSelector",
    cut = cms.string('pt > 10 && \n                        abs(eta) < 2.4 && \n                        isGlobalMuon = 1 && \n                        isTrackerMuon = 1 && \n                        abs(innerTrack().dxy)<2.0'),
    filter = cms.bool(True),
    src = cms.InputTag("muons")
)


process.genEleFromW = cms.EDFilter("CandViewSelector",
    cut = cms.string('(pdgId == 11 || pdgId == -11) && eta <2.5 && eta>-2.5 && pt > 25 && (mother(0).pdgId == 24 || mother(0).pdgId == -24)'),
    src = cms.InputTag("genParticles")
)


process.genEleFromZ = cms.EDFilter("CandViewSelector",
    cut = cms.string('(pdgId == 11 || pdgId == -11) && eta <2.5 && eta>-2.5 && pt > 15 && mother(0).pdgId == 23'),
    src = cms.InputTag("genParticles")
)


process.genNuFromW = cms.EDFilter("CandViewSelector",
    cut = cms.string('(pdgId == 12 || pdgId == -12) && (mother(0).pdgId == 24 || mother(0).pdgId == -24)'),
    src = cms.InputTag("genParticles")
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.hltHighLevel = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring(),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(True)
)


process.jsonFilter = cms.EDFilter("JsonFilter",
    jsonFileName = cms.string('')
)


process.selectedECALElectrons = cms.EDFilter("GsfElectronRefSelector",
    cut = cms.string('(abs(superCluster.eta)<3) && (energy*sin(superClusterPosition.theta)> 15)'),
    src = cms.InputTag("electronRecalibSCAssociator")
)


process.selectedECALMuons = cms.EDFilter("MuonRefSelector",
    cut = cms.string(''),
    src = cms.InputTag("muons")
)


process.selectedECALPhotons = cms.EDFilter("PhotonRefSelector",
    cut = cms.string('(abs(superCluster.eta)<3) && (pt > 10)'),
    src = cms.InputTag("gedPhotons")
)


process.PUDumper = cms.EDAnalyzer("PUDumper",
    pileupSummary = cms.InputTag("addPileupInfo")
)


process.zNtupleDumper = cms.EDAnalyzer("ZNtupleDumper",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    EESuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    SelectEvents = cms.vstring(
        'pathALCARECOEcalUncalZElectron', 
        'pathALCARECOEcalUncalWElectron', 
        'pathALCARECOEcalCalZElectron', 
        'pathALCARECOEcalCalWElectron', 
        'pathALCARECOEcalUncalZSCElectron', 
        'pathALCARECOEcalCalZSCElectron', 
        'pathALCARECOEcalUncalSingleElectron', 
        'pathALCARECOEcalCalSingleElectron'
    ),
    WZSkimResultsCollection = cms.InputTag("TriggerResults","","RECO"),
    conversionCollection = cms.InputTag("allConversions"),
    doEleIDTree = cms.bool(False),
    doExtraCalibTree = cms.bool(False),
    doExtraStudyTree = cms.bool(False),
    doHighEta_LowerEtaCut = cms.double(2.4),
    doStandardTree = cms.bool(False),
    doTrackTree = cms.bool(False),
    eleID_loose = cms.string('loose94XV1Run2017'),
    eleID_medium = cms.string('medium94XV1Run2017'),
    eleID_tight = cms.string('tight94XV1Run2017'),
    electronCollection = cms.InputTag("slimmedECALELFElectrons"),
    foutName = cms.string('ntuple_numEvent200.root'),
    fsrWeightCollection = cms.InputTag("fsrWeight"),
    genParticleCollection = cms.InputTag("prunedGenParticles"),
    hltPaths = cms.vstring(),
    isPartGun = cms.bool(False),
    jsonFileName = cms.string(''),
    metCollection = cms.InputTag("pfMet"),
    muonCollection = cms.InputTag("patMuons"),
    pdfWeightCollections = cms.VInputTag(),
    photonCollection = cms.InputTag("patPhotons"),
    pileupInfo = cms.InputTag("addPileupInfo"),
    recHitCollectionEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    recHitCollectionEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    recHitCollectionES = cms.InputTag("alCaIsolatedElectrons","alcaPreshowerHits"),
    rhoFastJet = cms.InputTag("fixedGridRhoFastjetAll"),
    triggerResultsCollection = cms.InputTag("TriggerResults","","HLT"),
    uncalibRecHitCollectionEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelUncalibHits"),
    uncalibRecHitCollectionEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapUncalibHits"),
    useIDforPresel = cms.bool(True),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    weakWeightCollection = cms.InputTag("weakWeight")
)


process.outputALCARAW = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalSingleElectron')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('alcaraw.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)


process.outputALCARECO = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalSingleElectron')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('EcalRecalElectron.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*', 
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'drop *_alCaIsolatedElectrons_*_RECO', 
        'keep *_alCaIsolatedElectrons_*_ALCARERECO', 
        'drop *_gedGsfElectrons__RECO', 
        'drop *_gedGsfElectronCores__RECO', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*'
    )
)


process.outputALCARERECO = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARERECOEcalCalElectron')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('EcalRecalElectron.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*', 
        'drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'drop *_alCaIsolatedElectrons_*_RECO', 
        'keep *_alCaIsolatedElectrons_*_ALCARERECO', 
        'drop *_gedGsfElectrons__RECO', 
        'drop *_gedGsfElectronCores__RECO', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*'
    )
)


process.outputRECO = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('RECO.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring('keep *')
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(100)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring('particleFlowDisplacedVertexCandidate'),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonGEMDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    useDDD = cms.bool(False)
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ecalNextToDeadChannelESProducer = cms.ESProducer("EcalNextToDeadChannelESProducer",
    channelStatusThresholdForDead = cms.int32(12)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated', 
            'kDeadVFE', 
            'kDeadFE', 
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC', 
            'kNoLaser', 
            'kNoisy', 
            'kNNoisy', 
            'kNNNoisy', 
            'kNNNNoisy', 
            'kNNNNNoisy', 
            'kFixedG6', 
            'kFixedG1', 
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware', 
            'kDead', 
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered', 
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird', 
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalOOTPileupESProducer = cms.ESProducer("OOTPileupDBCompatibilityESProducer")


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(''),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring('HBHEIsolatedNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity', 
                'HBHESpikeNoise', 
                'HBHETS4TS5Noise', 
                'HBHEOOTPU'
            )
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort', 
                'HFS8S1Ratio', 
                'HFPET', 
                'HFSignalAsymmetry', 
                'HFDigiTime'
            )
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring(
                'HBHEFlatNoise', 
                'HBHENegativeNoise'
            )
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff', 
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring('')
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    )
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('102X_dataRun2_Prompt_v1')
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(100.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(True),
    useHFUpgrade = cms.bool(True),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(False),
    useLayer0Weight = cms.bool(True)
)


process.essourceEcalNextToDead = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalNextToDeadChannelRcd')
)


process.essourceEcalSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.essourceSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.tpparams12 = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalTPGPhysicsConstRcd')
)


process.prefer("es_hardcode")

process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer, process.electronMVAVariableHelper, process.electronRegressionValueMapProducer)


process.pfClusteringHBHEHFTask = cms.Task(process.particleFlowClusterHBHE, process.particleFlowClusterHCAL, process.particleFlowClusterHF, process.particleFlowRecHitHBHE, process.particleFlowRecHitHF)


process.pfClusteringPSTask = cms.Task(process.particleFlowClusterPS, process.particleFlowRecHitPS)


process.multi5x5ClusteringTask = cms.Task(process.multi5x5BasicClustersCleaned, process.multi5x5BasicClustersUncleaned, process.multi5x5SuperClusters, process.multi5x5SuperClustersCleaned, process.multi5x5SuperClustersUncleaned, process.multi5x5SuperClustersWithPreshower)


process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.hybridClusteringTask = cms.Task(process.cleanedHybridSuperClusters, process.correctedHybridSuperClusters, process.hybridSuperClusters, process.uncleanedHybridSuperClusters, process.uncleanedOnlyCorrectedHybridSuperClusters)


process.recoAllPFJetsTask = cms.Task(process.ak4PFJets, process.ak4PFJetsCHS, process.ak8PFJets, process.ak8PFJetsCHS, process.ak8PFJetsCHSFiltered, process.ak8PFJetsCHSFilteredMass, process.ak8PFJetsCHSPruned, process.ak8PFJetsCHSPrunedMass, process.ak8PFJetsCHSSoftDrop, process.ak8PFJetsCHSSoftDropMass, process.ak8PFJetsCHSTrimmed, process.ak8PFJetsCHSTrimmedMass, process.ca15PFJetsCHSFiltered, process.ca15PFJetsCHSMassDropFiltered, process.fixedGridRhoAll, process.fixedGridRhoFastjetAll, process.fixedGridRhoFastjetCentral, process.fixedGridRhoFastjetCentralChargedPileUp, process.fixedGridRhoFastjetCentralNeutral, process.pfNoPileUpJMETask)


process.pfClusteringHOTask = cms.Task(process.particleFlowClusterHO, process.particleFlowRecHitHO)


process.particleFlowClusterECALTask = cms.Task(process.particleFlowClusterECAL)


process.multi5x5PreshowerClusteringTask = cms.Task(process.correctedMulti5x5SuperClustersWithPreshower, process.multi5x5PreshowerClusterShape, process.uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower, process.uncleanedOnlyMulti5x5SuperClustersWithPreshower)


process.seldigisTask = cms.Task(process.selectDigi)


process.recoPFJetsWithSubstructureTask = cms.Task(process.ak4PFJets, process.ak4PFJetsCHS, process.ak4PFJetsPuppi, process.ak4PFJetsSK, process.ak8PFJets, process.ak8PFJetsCHS, process.ak8PFJetsCHSConstituents, process.ak8PFJetsCHSFiltered, process.ak8PFJetsCHSFilteredMass, process.ak8PFJetsCHSPruned, process.ak8PFJetsCHSPrunedMass, process.ak8PFJetsCHSSoftDrop, process.ak8PFJetsCHSSoftDropMass, process.ak8PFJetsCHSTrimmed, process.ak8PFJetsCHSTrimmedMass, process.ak8PFJetsCS, process.ak8PFJetsCSConstituents, process.ca15PFJetsCHSFiltered, process.ca15PFJetsCHSMassDropFiltered, process.fixedGridRhoAll, process.fixedGridRhoFastjetAll, process.fixedGridRhoFastjetCentral, process.fixedGridRhoFastjetCentralChargedPileUp, process.fixedGridRhoFastjetCentralNeutral, process.pfNoPileUpJMETask, process.puppi, process.softKiller)


process.reducedEcalRecHitsSequenceEcalOnlyTask = cms.Task(process.interestingEcalDetIdEB, process.interestingEcalDetIdEBU, process.interestingEcalDetIdEE, process.reducedEcalRecHitsEB, process.reducedEcalRecHitsEE, process.seldigisTask)


process.recoPFJetsTask = cms.Task(process.ak4PFJets, process.ak4PFJetsCHS, process.ak8PFJetsCHS, process.ak8PFJetsCHSConstituents, process.ak8PFJetsCHSSoftDrop, process.ak8PFJetsCHSSoftDropMass, process.cmsTopTagPFJetsCHS, process.fixedGridRhoAll, process.fixedGridRhoFastjetAll, process.fixedGridRhoFastjetCentral, process.fixedGridRhoFastjetCentralChargedPileUp, process.fixedGridRhoFastjetCentralNeutral, process.pfNoPileUpJMETask)


process.pfClusteringECALTask = cms.Task(process.particleFlowClusterECALTask, process.particleFlowClusterECALUncorrected, process.particleFlowRecHitECAL)


process.reducedEcalRecHitsTask = cms.Task(process.interestingEcalDetIdEB, process.interestingEcalDetIdEBU, process.interestingEcalDetIdEE, process.interestingEcalDetIdOOTPFEB, process.interestingEcalDetIdOOTPFEE, process.interestingEcalDetIdOOTPFES, process.interestingEcalDetIdPFEB, process.interestingEcalDetIdPFEE, process.interestingEcalDetIdPFES, process.interestingEcalDetIdRefinedEB, process.interestingEcalDetIdRefinedEE, process.interestingEcalDetIdRefinedES, process.interestingTrackEcalDetIds, process.reducedEcalRecHitsEB, process.reducedEcalRecHitsEE, process.reducedEcalRecHitsES, process.seldigisTask)


process.particleFlowClusterTask = cms.Task(process.pfClusteringECALTask, process.pfClusteringHBHEHFTask, process.pfClusteringHOTask, process.pfClusteringPSTask)


process.particleFlowRecHitHGCSeq = cms.Sequence(process.particleFlowRecHitHGC)


process.postPatSequence = cms.Sequence(process.eleNewEnergiesProducer+process.slimmedECALELFElectrons)


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.ZmmgDimuonSequence = cms.Sequence(process.ZmmgTrailingMuons+process.ZmmgLeadingMuons+process.ZmmgDimuons+process.ZmmgDimuonFilter)


process.NtupleFilterSeq = cms.Sequence()


process.hcalLocalRecoSequence = cms.Sequence(process.hfprereco+process.hbheprereco+process.hfreco+process.horeco+process.zdcreco)


process.preFilterSeq = cms.Sequence(process.MinEleNumberFilter)


process.filterSeq = cms.Sequence()


process.hcalLocalRecoSequenceNZS = cms.Sequence(process.hfprerecoMB+process.hbherecoMB+process.hfrecoMB+process.horecoMB)


process.islandClusteringSequence = cms.Sequence(process.islandBasicClusters+process.islandSuperClusters+process.correctedIslandBarrelSuperClusters+process.correctedIslandEndcapSuperClusters)


process.pfClusteringPS = cms.Sequence(process.pfClusteringPSTask)


process.PUDumperSeq = cms.Sequence()


process.alcarecoElectronTracksReducerSeq = cms.Sequence(process.alcaElectronTracksReducer)


process.checkMCWSeq = cms.Sequence(process.genEleFromW+process.genNuFromW+process.combW+process.WFilterMC)


process.ZmmgPhotonSequence = cms.Sequence(process.ZmmgMergedSuperClusters+process.ZmmgPhotonCandidates+process.ZmmgPhotons)


process.ecalUncalibRecHitSequence = cms.Sequence(process.ecalMultiFitUncalibRecHit+process.ecalDetIdToBeRecovered)


process.hgcalLocalRecoSequence = cms.Sequence(process.HGCalUncalibRecHit+process.HGCalRecHit+process.hgcalLayerClusters+process.hgcalMultiClusters+process.particleFlowRecHitHGCSeq+process.particleFlowClusterHGCal+process.particleFlowClusterHGCalFromMultiCl)


process.pfClusteringECAL = cms.Sequence(process.pfClusteringECALTask)


process.uncalibRecHitSeq = cms.Sequence(process.ecalDigis+process.ecalPreshowerDigis)


process.prePatSequence = cms.Sequence()


process.recoPFJets = cms.Sequence(process.recoPFJetsTask)


process.checkMCZSeq = cms.Sequence(process.genEleFromZ+process.combZ+process.ZFilterMC)


process.eleIsoSequence = cms.Sequence(process.elPFIsoDepositChargedGsf+process.elPFIsoDepositChargedAllGsf+process.elPFIsoDepositNeutralGsf+process.elPFIsoDepositGammaGsf+process.elPFIsoDepositPUGsf+(process.elPFIsoValueCharged03PFIdGsf+process.elPFIsoValueChargedAll03PFIdGsf+process.elPFIsoValueGamma03PFIdGsf+process.elPFIsoValueNeutral03PFIdGsf+process.elPFIsoValuePU03PFIdGsf))


process.ecalUncalibRecHitSequence53X = cms.Sequence(process.ecalGlobalUncalibRecHit+process.ecalDetIdToBeRecovered)


process.seqALCARECOEcalCalPhoton = cms.Sequence(process.alCaIsolatedElectrons+process.fixedGridRhoFastjetAll)


process.muSelSeq = cms.Sequence(process.selectedECALMuons+process.selectedECALPhotons+process.PassingMuonVeryLooseId+process.PassingPhotonVeryLooseId+process.MuFilter+process.PhoFilter+process.SCselector+process.eleSC)


process.rerecoPFClusteringSeq = cms.Sequence(process.pfClusteringPS+process.pfClusteringECAL)


process.pfClusteringHGCal = cms.Sequence(process.particleFlowRecHitHGC)


process.pfIsoEgamma = cms.Sequence()


process.pfClusteringHBHEHF = cms.Sequence(process.pfClusteringHBHEHFTask)


process.multi5x5ClusteringSequence = cms.Sequence(process.multi5x5ClusteringTask)


process.multi5x5PreshowerClusteringSequence = cms.Sequence(process.multi5x5PreshowerClusteringTask)


process.ALCARECOEcalUncalElectronECALSeq = cms.Sequence(process.uncalibRecHitSeq)


process.ZmmgSequence = cms.Sequence(process.ZmmgCandidates+process.ZmmgFilter)


process.particleFlowClusterWithoutHOTask = cms.Sequence(process.pfClusteringECALTask, process.pfClusteringHBHEHFTask, process.pfClusteringPSTask)


process.reducedEcalRecHitsSequenceEcalOnly = cms.Sequence(process.reducedEcalRecHitsSequenceEcalOnlyTask)


process.particleFlowCluster = cms.Sequence(process.particleFlowClusterTask)


process.ALCARECOEcalCalElectronNonECALSeq = cms.Sequence(process.fixedGridRhoFastjetAll+process.alcaElectronTracksReducer)


process.particleFlowClusterECALSequence = cms.Sequence(process.particleFlowClusterECALTask)


process.eleSelSeq = cms.Sequence(process.selectedECALElectrons+process.PassingVetoId+process.SCselector+process.eleSC)


process.hcalGlobalRecoSequence = cms.Sequence(process.hbhereco)


process.rhoFastJetSeq = cms.Sequence()


process.recoPFJetsWithSubstructure = cms.Sequence(process.recoPFJetsWithSubstructureTask)


process.trivialCond = cms.Sequence()


process.reducedHcalRecHitsSequence = cms.Sequence(process.reducedHcalRecHits)


process.reducedEcalRecHitsSequence = cms.Sequence(process.reducedEcalRecHitsTask)


process.egmGsfElectronIDSequence = cms.Sequence(process.egmGsfElectronIDTask)


process.seldigis = cms.Sequence(process.seldigisTask)


process.alcarecoEcalRecHitReducerSeq = cms.Sequence(process.alCaIsolatedElectrons)


process.hybridClusteringSequence = cms.Sequence(process.hybridClusteringTask)


process.recoAllPFJets = cms.Sequence(process.recoAllPFJetsTask)


process.ecalRecHitSequence = cms.Sequence(process.ecalRecHit+process.ecalCompactTrigPrim+process.ecalTPSkim+process.ecalPreshowerRecHit)


process.patTriggerMatchSeq = cms.Sequence(process.patTrigger+process.PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7+process.PatElectronsTriggerMatch+process.patTriggerEvent)


process.pfClusteringHO = cms.Sequence(process.pfClusteringHOTask)


process.ALCARECOEcalCalElectronECALSeq = cms.Sequence(process.alCaIsolatedElectrons)


process.particleFlowSuperClusteringSequence = cms.Sequence(process.particleFlowSuperClusterECAL)


process.particleFlowClusterWithoutHO = cms.Sequence(process.particleFlowClusterWithoutHOTask)


process.ecalLocalRecoSequence = cms.Sequence(process.ecalUncalibRecHitSequence+process.ecalRecHitSequence)


process.ZmmgSkimSeq = cms.Sequence(process.ZmmgHLTFilter+process.ZmmgDimuonSequence+process.ZmmgPhotonSequence+process.ZmmgSequence)


process.EIsequence = cms.Sequence(process.egmGsfElectronIDSequence)


process.ALCARECOEcalCalElectronSeq = cms.Sequence(process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalCalElectronECALSeq)


process.calolocalreco = cms.Sequence(process.ecalLocalRecoSequence+process.hcalLocalRecoSequence)


process.calolocalrecoNZS = cms.Sequence(process.ecalLocalRecoSequence+process.hcalLocalRecoSequence+process.hcalLocalRecoSequenceNZS)


process.seqALCARECOEcalUncalElectron = cms.Sequence(process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.caloglobalreco = cms.Sequence(process.hcalGlobalRecoSequence)


process.FilterMuSeq = cms.Sequence(process.muSelSeq+process.ZeeSelector+process.WenuSelector+process.EleSCSelector+process.WZSelector)


process.selectorProducerSeq = cms.Sequence(process.eleSelSeq+process.ZeeSelector+process.WenuSelector+process.EleSCSelector+process.WZSelector)


process.recoECALSeq = cms.Sequence(process.ecalLocalRecoSequence)


process.ecalClustersNoPFBox = cms.Sequence(process.hybridClusteringSequence+process.multi5x5ClusteringSequence+process.multi5x5PreshowerClusteringSequence)


process.patSequence = cms.Sequence(process.prePatSequence+process.patElectrons+process.EIsequence+process.postPatSequence)


process.pfisoALCARECO = cms.Sequence(process.eleIsoSequence)


process.ZeeSkimFilterSeq = cms.Sequence(process.preFilterSeq+process.selectorProducerSeq+process.ZeeFilter)


process.ntupleSeq = cms.Sequence(process.jsonFilter+process.patSequence)


process.ecalClusters = cms.Sequence(process.ecalClustersNoPFBox+process.particleFlowSuperClusteringSequence)


process.seqALCARECOEcalCalZElectron = cms.Sequence(process.ZeeSkimFilterSeq+process.ALCARECOEcalCalElectronSeq)


process.ZSCSkimFilterSeq = cms.Sequence(process.preFilterSeq+process.selectorProducerSeq+~process.ZeeFilter+process.ZSCFilter)


process.seqALCARECOEcalUncalZElectron = cms.Sequence(process.ZeeSkimFilterSeq+process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.WenuSkimFilterSeq = cms.Sequence(process.preFilterSeq+process.selectorProducerSeq+~process.ZeeFilter+~process.ZSCFilter+process.WenuFilter)


process.seqALCARECOEcalUncalZSCElectron = cms.Sequence(process.ZSCSkimFilterSeq+process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.seqALCARECOEcalCalZSCElectron = cms.Sequence(process.ZSCSkimFilterSeq+process.ALCARECOEcalCalElectronSeq)


process.seqALCARECOEcalCalWElectron = cms.Sequence(process.WenuSkimFilterSeq+process.ALCARECOEcalCalElectronSeq)


process.ecalClusteringSeq = cms.Sequence(process.ecalClusters+process.electronRecalibSCAssociator)


process.rerecoECALSeq = cms.Sequence(process.recoECALSeq+process.rerecoPFClusteringSeq+process.ecalClusteringSeq)


process.seqALCARECOEcalUncalWElectron = cms.Sequence(process.WenuSkimFilterSeq+process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.seqALCARECOEcalRecalElectron = cms.Sequence(process.bunchSpacingProducer+process.rerecoECALSeq+process.selectorProducerSeq+process.ALCARECOEcalCalElectronECALSeq)


process.alcarerecoSeq = cms.Sequence(process.trivialCond+process.seqALCARECOEcalRecalElectron)


process.pathALCARECOEcalUncalSingleElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.seqALCARECOEcalUncalElectron)


process.pathALCARECOEcalUncalZElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.preFilterSeq+process.seqALCARECOEcalUncalZElectron)


process.pathALCARECOEcalUncalZSCElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.preFilterSeq+~process.ZeeFilter+process.ZSCFilter+process.seqALCARECOEcalUncalZSCElectron)


process.pathALCARECOEcalUncalWElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.preFilterSeq+~process.ZeeFilter+~process.ZSCFilter+process.WenuFilter+process.seqALCARECOEcalUncalWElectron)


process.pathALCARECOEcalUncalZmmgPhoton = cms.Path(process.PUDumperSeq+process.filterSeq+process.FilterMuSeq+process.ZmmgSkimSeq+~process.ZeeFilter+~process.ZSCFilter+~process.WenuFilter+process.seqALCARECOEcalUncalElectron)


process.pathALCARERECOEcalCalElectron = cms.Path(process.alcarerecoSeq)


process.pathALCARECOEcalCalSingleElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalZElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.ZeeSkimFilterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalWElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.WenuSkimFilterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalZSCElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.ZSCSkimFilterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalZmmgPhoton = cms.Path(process.PUDumperSeq+process.filterSeq+process.FilterMuSeq+process.ZmmgSkimSeq+~process.ZeeFilter+~process.ZSCFilter+~process.WenuFilter+process.pfIsoEgamma+process.seqALCARECOEcalCalPhoton)


process.NtuplePath = cms.Path(process.filterSeq+process.preFilterSeq+process.NtupleFilterSeq+process.ntupleSeq)


process.NtupleEndPath = cms.EndPath(process.zNtupleDumper)


process.ALCARECOoutput_step = cms.EndPath(process.outputALCARECO)


process.ALCARERECOoutput_step = cms.EndPath(process.outputALCARERECO)


process.schedule = cms.Schedule(*[ process.pathALCARERECOEcalCalElectron, process.ALCARERECOoutput_step ])

