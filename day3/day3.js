function main(input) {
    input = input.split("\n");
    var sum = 0;
    // for (var i = 0; i < input.length; i++) {
    //     l = findCommon(input[i]);
    //     l = l.charCodeAt(0);
    //     if(l > 96) {
    //         l -= 96;
    //     } else if(l > 64) {
    //         l -= 38;
    //     }
    //     sum += l;
    // }
    for (var i = 0; i < input.length; i+=3) {
        l = findCommon3(input[i],input[i+1],input[i+2]);
        l = l.charCodeAt(0);
        if(l > 96) {
            l -= 96;
        } else if(l > 64) {
            l -= 38;
        }
        sum += l;
    }

    return sum;
}

function findCommon(s) {
    secondHalf = s.slice(s.length / 2);
    for(var i = 0; i < s.length/2; i++) {
        var c = s.charAt(i);
        if(secondHalf.indexOf(c) > -1) {
            return c;
        }
    }
}

function findCommon3(a,b,c) {
    for(var i = 0; i < a.length; i++) {
        var cc = a.charAt(i);
        if(b.indexOf(cc) > -1 && c.indexOf(cc) > -1) {
            return cc;
        }
    }
}


main(`rNZNWvMZZmDDmwqNdZrWTqhJMhhgzggBhzBJBchQzzJJ
pHlSVbVbFHgHBzzhQHqg
nVsqGpbbtDtTNmrmfZ
zrBMnbzBchshsttfbMRBgmJggmmCHGgDhDgNDGHL
VddZqQqdvSQMJHJGdCDCDDmH
pZWWllPQlPZQvZvwpSVlqlvtfswMRzBbntzRbzbfstsRzF
NnjjRlnWNSWWbGwccbcchfPfTvfjfTBBpvmdMjTfvB
FVzJtDDJDqTMlmlM
gVQZlFLlzHhLGShGww
rPZtvtFrFPgWjQvCBlcqMzlqQC
QGVDJJnLnVTCJBczqqTM
fNSSnmLDSVLhhhSNSLhGSGfVPjrFHwmQwtwWFRWRjWPHrwgt
SvmlrVrCvmNhSSVZVCrsgqPfbwGFwwwsflbbGb
QHffdnHDDQdMGbgqPwztdPds
DjBjWHfQDfTQWTBfpMBQLVmmmcCCcVhCBBBhhCmC
trLHFFQHTLHJQrflfCnLLHrRfRRPqSRPbPbbsRGqqGqhjj
mcMpNWVVNmNVsSbSJPcGhPRR
NpzNgwzZDVNZVWNpHJQLQHtQrZQHrBCl
JVCMfgJVrJtMBhhrfVVfhVsjvpFGFgjSSgFdSGGqjvjvqF
mHllHlHpmWlDSFqbdSTS
nmZRLzQnWVpctMVpQs
BrvRzWBPWbRwGRjbbRGrtrfqjCJCjCJgJsZJscFCZcJC
MnnnVMVhTMQhsccVfwqFJgqf
mMShHHppQmHrrBzwtSbWwR
pWWGJMJJwlnZSqjWmvSWZC
gtHrLttDtgFjjqRZZCrjpp
bFtbTpHFHLbfLFbHVttccttddJGQdJzTwdTzJlMnMBwwJJ
JhqHFhVMzJPQcdcVncdc
NhgfwSjwCWwltSfnrnRWZdpcPrrRnp
NNhlltBjssNBgwLFFvDmDqLzHqBB
LnFrnddfrLnMFjWzpFhcWpjpFc
ntCwgtNggCqCgCqqPPltvcjjhvmWhmvDzTzDzD
lqlVQgVCSPVllVQSNGMHHrdQsHrJJBnMHHJf
ZGZcRZNWpcHZhJfbbNblrfrgllNr
stBMtzCCsHMfFQjfSSPgtt
qmszdsCzMncdGwdWZGvH
PccqPqbhvSvvvtWNjTtWsWcscp
gRwdDzHJQgHzfdRhgHRffzwsTTjTTCjNjssCpmWWDjtCLW
zdRMwdRHhGJwgHlnGGSFvvSrnSrr
rRpMJtPwrcCTNNQNMZQm
mDWdWVddbbbmBflFhvTHjjQjfZTgZgLLfH
bhBbFFnDVhdddFBhdmpJRrzStJmwnPzcsJ
RjlpRRWzzRGRmGzlCRRlQjCgtvTJTtJrTPttrWTwhFvvVJFT
bSBdLLqbcqcLndLHZNqcZdBDPrVTDDTJSFrJJvVthTwwDS
cqVsnBfHffVdqnZccGMmCsGzQmjsjlljgz
wMzJhLtwbnMWtHcFCCFqFNNbgq
fMlMfjrRRmdmGCGVVCHcVqcVTC
MmRRRlvmQWzpvnZpwJ
gRmgMRMmRwzzmwHbwcTNqPDVBbPTZVqPNZ
fWHphpGFpfJrrhPsNTNZVsNVhT
WGfJdvltJJfHrJpRgvMRMSwRznwMmw
htJFGsGspCppCFCGthCdpmJmgmWZfqqzWzlWcfgZHgzHlg
nwVMjVcVcWlbnBlfWB
wcNDTvPPDMFJLLppDGDD
hjCBgPbvMvmQDzlWnWjm
HrHtgZRRRNwczDWwwDzsQQWW
LpTqNtFtLFqHLHRrqgFHffVVBChvhhVPBCPhbPbp
CwpbCwjGqSjVllpGCllBfhZZRDPNcPPNvLLLDSDN
WshFFWsgTHsdMzQvPczLfLZDZRcLfR
rWsJQTMhWWHdsQTgsFJgllClVpqVbqnGblCppCVr
gRBSGcBDBSJSvPQwrTFLjggQTQ
HMMnHHHZfFVFrrMT
HhlhppCNcJzCTtBT
CCffCCmRLTsQRPHQQMPF
dWdbgcDSNclbbdwdSqHsvHPQPTPJplPMFMGJ
DWbDNcqZDSWSccNTVBCzVVfmBVZnVz
BnsrrvZwBsBSJrrrqSTgJQjCbCjgbCHDJgJFjQ
hLmGlnLmGWcjGDgfFFjQdF
hhWPmhPtczWpNRmppzRhLchMsnwZvTMZvVSwwrsNwSsBvr
tDCCltNVttJhNGlMPSWdqBqSjM
RFQcpcRTpFcnFzdLmLSWjMSSBLSQ
jwzzczpFbwnHcDCsthDJJsNbst
dLRWTHSwTmTwTcTWvQNVVQCvVvNFps
GnBPtBMJBPrjGGJMjrlqChNpNlsnhVFhQsVQ
JtMtGJfrJgDJjPjRTZLdFcRZRmwSDH
VSccPJSBLgZPDLDQ
zfpLMmLsHQGqgQHnDD
zdLLMssmrdfhddcVdJtScB
VvpTVQHSqSHSHqqHJVmRJVHpgDBwDgjcDDDgZjBZBjwBZbRw
PCdssGlstdWslFPfNPrtClGjwBgBJgJNwcjBjBgZwwMBJD
tlJldhdhdsdhTqSTqVQqQq
VGqTcTqbpPwrjfbl
BvntnZNNsLZvLszSnCsvJthlfjTrZwlrjrpPlwlhfwrl
QBtNtJLvTsFdQcqWmQRR
fjcjhmjBvcvcSvcZ
HMwZtRQQpGGRgzMvLnWWnbLlSntlbv
JQPzzJHqQRqGMMQwHwzDZZhmmPfjDjmjsCZhPj
cBlZZMfBrCBMwBMCvQzTwFbQzPnbwjTbTg
WtzpVDzmtthzGFQTbTThnnTQQg
sGWstpHdpGDmdHdmGmmmJNstRMrCcBSfBSzNBNRrSRNMcMMv
mMPDVBZZLSmRdcFpjr
fggGGfbfgQStjjsdbtdt
gNqQgCQlNCCJgJHvnvnHMjPHjv
bLsRQrQsGQbLrbRZMGgbJJBJFtlFFngJphhcfBBq
jjdHCCjfVNmmmNDFcBcpBthcplFDFq
jmvvmWVjjHTCVvNjSbQGLrRzwMWsMRwfGG
sJNCsCFFCNPhCzlrSvRrvwhRjj
MMGMTwpMHGzrGczzlG
qVmwgHtDtmCdWCsNFmNJ
fmhWhjVjNpqRRJjwRw
gnGQGDDCgSsCvPlvPgnPgnPtwqbpHRHqHdJpzpQJJJRJRF
wgPGsDGPsZgGgBmBWNZNfLWWrZ
WdsCVtjWWWHRRqLLHncC
fbSpMSPSZHRRcqlpRc
cGMmJmfMPPPccZMNQPWvjTtdTjvgmdtTsggw
tPBQhHWBtQHgWQCtLwddcGnfpGpwwnbhVb
vqQzTNJJJTvRrTNFJsZrrzFlbbfcnVbbcwmGGGpVzmddcdfd
NSSqJvFFFFFQjQCjQDSDPD
rQZnVVrZmZmgSWqHrSzHPC
LGFLwcMBcllBjFNwGjltggSqSWCCzvNgSqSHtt
wdhqqGBwwqGMcDhcwdFFbbJppZbssbfZQsQsdVQm
lqBZlsjVTbVqmFrSnTFSvwncPP
zQztHfZQtWLJzPFnnQScFcFrvS
ftHJWHhfttHWffhtgLNfZDWbdqBqjbVssBDCqCdCsmClGG
MlbWFTJQFbFFzRdNjNtjdtBT
srwnrsLVHzQPQsjjSQ
gLpnwgnwnHCvcHHcvwgCvGFFhWGmFmqMMbQFQFFhlGmJ
qqNcJgJccdqhsqgsggdgqgcrtfNWNZzVbvVFzttMfzbVMZ
GLlpPpCpwPLDGvrFVWrWWbZt
DlRCDDLSjTjDjSRSjPClwnwSHHHQmmQvTJcQgvddHsqdcgmB
jmRjRbRQLLZbPnbrcTTHHHNn
MfhhmmwtvStrpnJJHc
fgqlvfhvFzMwqfvMfFWlmMvLZsdQsZVdCdLZdGQjRzdQjD
lTPcDlVdTlVVMSDfTJccVzdlmMgGBmppgBmnHGHqHqQqqQMH
ZRjWFPsLNLLrPhWNtnBBvnpGpHGpQmHnmR
CtwssCNLrsZWjrjcbfPzwJJJffDbTl
cjMvvqpJFqhShNCRQR
ldtDgQZDPdzztLZgPTtfbnStfBSbNNSbnbhhSS
TDsrzsZZZTFHmVHjcsQW
BQmQchrmBddcmZZdpSgrpswWWswVsnnnDJVnnZFnGN
TfStMPLTHvbvRVGnHGsNnJWFNV
qtvMRMMPbbPMLqRPvRTRzMjSSmprpQdBchlmmgldgjzm
nRRnvNPhrbZDLjvS
HCszMwcHHcLDrbQDWr
ptszqwdMbnnhPBqN
QbzhhfbFhBbpbzwwLjLJjSjltL
mNndGrSStHJTJLln
rDMMNVWdVpCbSbSp
tDTSTSTTTTJDwqjWqBWttdjg
nNPmVfnGfPNVLmNzfnzPVFMjdpBwWZwZHwBLBqgjqpWH
dfGPfVQGVPhGzlmnzSvsSTDJhTbTTrrSRD
ZfgtZBptBfRQNQggjjrjjwmwsQJPzrwm
TwTGGwTwzzsJzTsH
lFvwqFLhFMnqcLlVLMLfptNWppppDBDbDfbFgW
mjftBfVPjttmjcSjcPttzJlvnrwvTRrTnvwvlRrHHTHRTR
WZDWDNLFWbZbcMDWGZDbNdMCRsnTdTvdnqrHCTrvsRRvwC
DQFZLNNgtBJQcBzJ
HbZQZFVbQVpQplQZGbGchDffltfLtmdgDjggTmtm
zWzRCdnCRBRdJrzDjLhDthjLJTTtjq
CPPnwSrRdRSzCGMcZZZMwFwMZF
WBQqNQnQllwnWQlvBBMlljHTqqFdGfmTdFfcFTFFcqmP
rsRRVrZhrzbtpZRRhFDmPvfFFrfTdFHGvc
VtSCtSLbtsZVtttthCbJSWSlJlwJQggWWglvwW
QfFLWCvRfSLFCtvtFhNcqDDcGVbhGcqh
ZVgrdZZPPZZzPwdjzZhmccsqJGqDdsDDNddD
pzzwpgZzZZTznZnjZZzPVRLQLlvfSlQRSpWlCvtSQv
RtcHhRMcrHhBrrTNDVBNLqLqQqfBPm
wCbWzWbvdWCjbWppmtmNmqmLLsfsNV
lwjWdbztgHTgggnnnR
flBbzbMfbrTlrMvBCcwPggdmcdmg
VDVVRFZRZSFFhQLSGFQhjSVZCgpvPwLCzpdWWzccwdvvvwcC
hDHRGQVHHQVRZSQGbqqfNTlbHzrbbsqb
MTFdTsZpPTcMpFCPdCBmMBmRfRGBmQgQRRgt
vbDSwvhzznnbbhDWnvSzRBgQQLgLQltqtqlmwfGB
jVjhfSnNDNbzzWzjWSjrCFNpcHdpTTJddJFpsJcc
ZrrZPHfChPdDPVVdDq
vFmsbTsmSbbBJssmSBvTmmnTrnrwlWqwVlLrVTLLTWqL
JrFbpsvFBMBmzBzFStcRhjZjfCCpZNCtct
TGgRrTggwwtvtQtdCdQNqN
sJHZJVZHDBpFBZBBNzNdhzdpSzddvqhN
VZcvFsJVFvsmvssbcnrwbrnGMbMlRn
SdcdWzMJdSMWMddZJdVcmBmwrwqrrnVnVNtr
mlQHCfgbjsfQTbfCBNtVhVnntVBnVh
HLDslDDmblgHfvLHPJFSZPpDFpFFpdPS
qNqPNJvcSzGGPQnGQp
bWhbgsshZWBhltthhbWtCsZNjrzpnQnnznnjtQFrjGjVFGnn
bRDNddhNdDsZdNChmvDmmwqqvLqwSJDq
TnSfPnCSmnSgpSTmfLzfMFLWFJJLWWsBsr
jdQjcdqDVVwDcPsPzMRJMLqPqR
PGhGchjhtZlTGTHCCb
ZZRrJJqSqJwNFFphsGsLPJ
blcMCflvTTPFFNpVvsFv
CcTlltTmtmMdmCmnlllBDDSDQSwSjRDQSdswjR
MCCPNsnQFWbvvTPF
CcCVJJhjVJZRtcCclDDlbcbTcGFFDz
HpjtVwVZfpjJVhZgCVtLmrBwdMrLsNNsMmdLqB
TJTDTnrFzzdWgWGJSSMJwg
LhPVttjtLmsPqqqVsVpsjLlgWlwHvGnlHWlgHlGgwvlP
mQshLhmsnsqZcqhZqpshsLVpNTNbBfzTRBQdFRzNNFBTdbzR
ZGqMLGqvJsJsMJmd
PDVQPfPcrrcFrrzrTdgCjSSCzgszmlJjBj
PfRtVfttVcWtVJrfbGqvwqLpRRwvpppH
HmLmMSnnWnrTrnvpqFCHVGfzVFVHQj
ttsstRhhcNwbswNtdwsdNPFfjzQppQPjfGGfQVPCpR
bbsDNtDcbhstsSZLDmSSgCmnSS
tfwBBLcJVrDnqvLv
zmWWJRZhWRRRGRNdgSZGgWTvpnjvrDqvpHjjzrpnrPDnHj
NdJmSGZWRhRNsghWTJmdGfQCtllCcFMwffBftsfMQc
lTLgTghpGZJDBrnGWnnm
VlRwlHttwqmHHbDWHJ
twldzCvsRdsFFtRtSczTjSgMcfSpSzTM
pBpMBTcSlNtMcTfFCmbPDzCDLb
JgrjjJqhGZQrQrZhnJGDDCZfvPDdDzFFdzfmZL
QHhqqnrVJJPhHrnGQgwMNwMMctcWRWSBMNtNsW
FJrlhpcfDCcFWpNpwWwjNQwz
RTTvPdbjWzMbnNNM
GRZTGggGgtvjGcqrBcttcDlFhr
pMRVdVbbMMMSdWWqHpCTvTjnBBBFFGGB
smNfZgcsNrcmzggZszsgRnPGFHjBPTBTjGjPTBNj
RmwgsmgfrzzsZtfgZLQQSVWlwbdMhlwdqQ
mRRjPmLrrSmzSczSzPgVZFpTCpZCMWrZQMQrZJZT
BvdbHNdnJtvBDbqqdBlvwvqpDQMpZQFMCsQCspZTMMCZCF
nBlfbfbndJBHPfLRfmhhhhPL
ScJDFBNLLbVRqVfZ
rWrgmdMgnnBhBtnntf
CwBWWMgCwddCgwsQjsrvNvlTJzSNHwNTHFJHzS
vnddCrNpCgtjLdSdgCgCCvLnWqDhWBQhHqQHDqBhQHDHNNDl
wPTVfVTJmZGJVJGffZBwHMWlWlHlWtbQDqbl
mGsJVVJsTVTTmtJVzzTJjdSjjprzCvpSLSCjdnLg
zLNggsVHmNNsssLmwzLQZLwDRvGQBqGGDDBBvvDBDqPhRG
WrCjbtJdbFhBRglGgjqv
JWCJcWcSdWcctnJCcJJJbcbmzwwznmgLzNzmLHmHZMwsZL
JRRDNNhhszMTzNMwCG
MnHPqmgmHjPnnvjqdmjFLQwLwTLwzTwTdGLCzS
BnPPZqmcfqgqnnZmBmqjqhfWVJlRMlhWlRDlVsssbh
nmTLTqsvqnwqsvwDPnLHdNVrMMHHCBlmVdmGNV
RgRpcJhQRfQZcJbWhQpBHCjVCdjCVGdddMllHp
fczbZhzbtcZfgRRBcWSPPwFsLSDswSwTsSzw
rbFpzFCVBrrBZCjbCzHHBVdJllGDLsLrDtsswswstGJs
QNhNNnNnnQhNWSnRhnJtdpJpJtMDGsGLLtsQ
ScmRvNRNnWWvNvNvfpTccjVZbqgZgVzqHjCjTVTVVq
BTppwCwBpwwBqnjlHcLBTHnbbSbDthsSSJgsnDDRgJRD
FVGzzvrdMGSSsdtZtZgd
QvQtvtGFlBLLjLQL
gsWWsNMjwgPMPWnMjShHHZSZbmZbbmTSnb
rlCvVQrCfqffpVjQRqCCvDDTTTmmZhZTmZhThFmhhZZhqb
CDDVJpVfrJJVJLMNzMwWwLwj
nHrcsZrssPcBPtQJLJtQQCZQpV
GFWzNzNFdNbTMMqbGTqTqzqqdLCpfDQCtRVVCLtdCfQsdCCt
TlNqGTWFNmMMszhGsmFTWGFzwHnvSjgPgvgSjllBvBnvwPBB
mpMggjgMlmtjtGMwZpcSscBlcsSblhsfSdfs
zzPVDRrLrCTQNCzNRTVFNLhBhBSqdQbcfSsJBJdbjJfB
RPTRPTVNTFzVrHVDCrTHmHtwMvwWMmtwmGjWgvGv
rLMcvfHVfMgLFvfNnBBzwRbBwnrGNs
dttJjJCtdjmwzwBCRRCqcs
TddDQDJDtQJtcJFpPQHPQMvfQlFL
LQSqqpqTCSJcsDcqQMMhnnjMjppZhwHZbZ
NRtvtmgmvdBffgtVCBWVRgFbPzHbMHbnwwjMPZfHbPjzPP
RNtvCvNdgtNNmldgvCFRNVLsQLqJcQGJJrccGSlDLDLr
GdwwqqqwGVtjdPvTCplbHTPbPzPTpp
RpLmLLpFfNsgTzclhzClThgH
ZFsWZLFZJsNsnWsnRsRfnfJQGBttjdGJjBvvwjdpjjttvj
tfPzzLrrdrQlTlvn
qJRBhNhNGVRBFRTlnJvCmvmJPCCl
VVPDNchNMVFGRMFcRVBjsZZcttSLSZzzStcWtZ
pTrwTrnjtttjprTSTNTQfcjcgPsPZfPgjdgdsQ
mCmCzvzhmJDHzJDbhFCDPsgddcsfcdsbdgVRpdVs
zqJzFCDhmqvGhMmCvmGhMCGJnSlnllSBLllLMtNpWtpNBnlt
JBhJrFLhGrnJZrlcbffndnggfggf
jqmWMGGSsqCsmpjmsDQzlcHgbtdzjjlVfctjHV
GWSmSCspCsMSpRmSmqMMCBvFLJLhTTwFhRFLLBTwrv
BCdWccqcqpQqrsNgGsWMgfNW
lFttLzzLwnfsLrsNsNLG
zjNlznlwvRPZnltwvPFnZRCbmjCcqjpcpQcqVVdbdVBm
CwTbbCGNFHtHwwjSjJpzjLMdMMzT
rscqqVvWgWrZMjrlmSzzmLrM
WPqqZnPqgncnBQQVRbCDwRHGSFHPwRNw
ZQnZwWjFvdsHwBJltfmfSlsqlJ
gPprhMDTpMpPMVNqNRqNlJhltJdJ
pLGCcCrgppCrVcMpdzjvzvjLwQQzFjwzHF
NmmmvfqcvmLSQhCLvtvL
TVlWTZVJZJsFbwWbQQhtQgLFCnSgghLt
hZJTJZhwZlRJrJWHVlblMBffmqfdNMjdGdBBqqcH
GJJfLfptGqqqnsVqVVjjDnNc
mZPSvPmBCdmwdCLDshSbRnnDDhRL
gvBrBvPBPPZCTLZmwmrgQdwfTJMHGzHfWffJzFzttHWFzW
sBMvmzWzmFmNWJfffZNLfbqZbtZq
jRQVRnhhppnVhjgnDLttLqbLqLQfDLss
jRRgpGVGhwhnspgpRppwSnBvMMcWvGczGJJHdmHJmJFF
VCLHFwHMhLghHHWhFFgWNMMVzmdmbvWdJqBPJPPBppqmBdzm
SRTsjGZTsZZnSnGZGqdBmrqPvmqqqsPpmv
GvQSGtZSQllVhtLMcLLNMH
GsNdWpdVWGSHjFCWCqFFgqngvW
mRQTcrLRmZTPRLPZfqqqHbDDDgFvFnvqzQ
hfZHrwwmcZRwlLfwlmrRjMJJsVjslVNBGNjpVBBG
pllpztRqBBvvGPpG
QQhhZQbVcZQTPMWWGbvvbMHM
cwgCQCLZChQwwLZVzCrzzqNCzrDqdFPF
bgcLPvvpcbdsbpSsHRTCqsRfWfsHRm
lZlQtthrnlVMmTHqqqqHSChB
rDtlzttnlSNrMtQjZVrcgGDLLddcdcpPgPGJJd
jvGbvLLQDSGlRmmSLjlDmRQggFBrMCwWdsBFWBFjdrrWrr
PpTfcPZpNTVNpHzTzzzpPJhBcwrrhFsrMdFcMCBFhgMF
JTTqdtfzfzJpqffNdTTHGtQRnmDQGGLQQlQRbblD
CQQCshCMwgQhMdjWJFBPpbjgmmWj
SNNvcGNSZSTDtGDcczJJBmzbjBJjmppbppms
cDtfDVNTGGGNNrwLLwHdqLhfLs
ngghZCChzhNjjNbbJfdh
slPPRLlBBlVRMvRllLLHvcpcdFfJjvdFpfHfcZ
RDZPZBLmPVWDVrQtnzSTmgTwmTSg`);