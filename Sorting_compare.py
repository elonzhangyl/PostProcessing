import pandas as pd
import matplotlib.pyplot as plt

workDir = r"D:\Projects\10097 Huadong floating\20221207 4thLoop\1. DLC6.2 - RigidBlade - Restart - A16"
fileName = r'\Results_All.xlsx'
results_10min = round(pd.read_excel(workDir + fileName, sheet_name='Sheet1'), 2)

workDir1 = r"D:\Projects\10097 Huadong floating\20221207 4thLoop\2. DLC6.2 - RigidBlade - A16"
fileName = r'\Results_All.xlsx'
results_1h = round(pd.read_excel(workDir1 + fileName, sheet_name='Sheet1'), 2)

workDir0 = r'D:\Projects\10097 Huadong floating\pythonScripts\PostProcessing'
fileName0 = r'\DLC6.2Labels.xlsx'
results0 = pd.read_excel(workDir0 + fileName0, sheet_name='labels')
DLCLabels = results0.iloc[15:219,35]
DLCLabels.reset_index(drop=True, inplace=True)

results_1h.insert(0, "DLC", DLCLabels)
results_10min.insert(0, "DLC", DLCLabels)

labels = [
    'RNAAcc[ms2]', 'RNAPitch[deg]', 'RNARoll[deg]',
    'TDP1a[m]', 'TDP1b[m]', 'TDP2a[m]', 'TDP2b[m]', 'TDP3a[m]', 'TDP3b[m]',
    # 'FloaterPitchMax[deg]', 'FloaterRollMax[deg]', 'FloaterTiltMax[deg]',
    'ExcursionColumn1DistMax[m]', 'ExcursionColumn2DistMax[m]', 'ExcursionColumn3DistMax[m]',
    'airGapBladeTipMin[m]',
    'airGapColumn1Min[m]', 'airGapColumn2Min[m]', 'airGapColumn3Min[m]',
    # 'TwrFxMax[kN]', 'TwrFyMax[kN]', 'TwrFxyMax[kN]', 'TwrFzMax[kN]', 'TwrMxMax[kNm]', 'TwrMyMax[kNm]', 'TwrMxyMax[kNm]', 'TwrMzMax[kNm]',
    # 'TwrFxMin[kN]', 'TwrFyMin[kN]', 'TwrFxyMin[kN]', 'TwrFzMin[kN]', 'TwrMxMin[kNm]', 'TwrMyMin[kNm]', 'TwrMxyMin[kNm]', 'TwrMzMin[kNm]',
    # 'Fairlead1aFxMax[kN]', 'Fairlead1aFyMax[kN]', 'Fairlead1aFzMax[kN]',
    # 'Fairlead1bFxMax[kN]', 'Fairlead1bFyMax[kN]', 'Fairlead1bFzMax[kN]',
    # 'Fairlead2aFxMax[kN]', 'Fairlead2aFyMax[kN]', 'Fairlead2aFzMax[kN]',
    # 'Fairlead2bFxMax[kN]', 'Fairlead2bFyMax[kN]', 'Fairlead2bFzMax[kN]',
    # 'Fairlead3aFxMax[kN]', 'Fairlead3aFyMax[kN]', 'Fairlead3aFzMax[kN]',
    # 'Fairlead3bFxMax[kN]', 'Fairlead3bFyMax[kN]', 'Fairlead3bFzMax[kN]',
    # 'Fairlead1aFxMin[kN]', 'Fairlead1aFyMin[kN]', 'Fairlead1aFzMin[kN]',
    # 'Fairlead1bFxMin[kN]', 'Fairlead1bFyMin[kN]', 'Fairlead1bFzMin[kN]',
    # 'Fairlead2aFxMin[kN]', 'Fairlead2aFyMin[kN]', 'Fairlead2aFzMin[kN]',
    # 'Fairlead2bFxMin[kN]', 'Fairlead2bFyMin[kN]', 'Fairlead2bFzMin[kN]',
    # 'Fairlead3aFxMin[kN]', 'Fairlead3aFyMin[kN]', 'Fairlead3aFzMin[kN]',
    # 'Fairlead3bFxMin[kN]', 'Fairlead3bFyMin[kN]', 'Fairlead3bFzMin[kN]',
    # 'FairleadT1a[kN]', 'FairleadT1b[kN]', 'FairleadT2a[kN]', 'FairleadT2b[kN]', 'FairleadT3a[kN]', 'FairleadT3b[kN]',
    # 'AnchorT1a[kN]', 'AnchorT1b[kN]', 'AnchorT2a[kN]', 'AnchorT2b[kN]', 'AnchorT3a[kN]', 'AnchorT3b[kN]',
    ]

    # testhh

topN = 10
for label in labels:
    if label in [
        'airGapBladeTipMin[m]',
        'airGapColumn1Min[m]', 'airGapColumn2Min[m]', 'airGapColumn3Min[m]',
            ]:
        results_10min_tdp1 = results_10min.sort_values(by=[label], ascending=True)
        results_10min_tdp1 = results_10min_tdp1.iloc[0:topN,:]
        results_1h_tdp1 = results_1h.sort_values(by=[label], ascending=True)
        results_1h_tdp1 = results_1h_tdp1.iloc[0:topN,:]
    else:
        results_10min_tdp1 = results_10min.sort_values(by=[label], ascending=False)
        results_10min_tdp1 = results_10min_tdp1.iloc[0:topN,:]
        results_1h_tdp1 = results_1h.sort_values(by=[label], ascending=False)
        results_1h_tdp1 = results_1h_tdp1.iloc[0:topN,:]

    

    fig, axs = plt.subplots(2,1,figsize = (12,8), sharex=True,num=label)
    axs[0].invert_yaxis()
    bars_10min = axs[0].barh(results_10min_tdp1["DLC"],results_10min_tdp1[label])
    axs[0].set_title("10min - "+label) # "10min - "+label
    axs[0].bar_label(bars_10min)
    # plt.savefig("10min-"+label)
    plt.subplots_adjust(left=0.5)
    bars_1h = axs[1].barh(results_1h_tdp1["DLC"],results_1h_tdp1[label])
    # axs[1].tick_params(labelrotation=0,labelsize=8)
    axs[1].set_title("1h - "+label) # "1h - "+label
    axs[1].bar_label(bars_1h)
    axs[1].invert_yaxis()
    plt.subplots_adjust(left=0.5)
    plt.yticks
    # plt.savefig("./Pics/DLC62-"+label)
    plt.savefig(workDir1+"/DLC62-"+label)
# plt.show()




