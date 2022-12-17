import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

workDir1 = r"D:\Projects\10097 Huadong floating\20221207 4thLoop\2. DLC6.2 - RigidBlade - A16"
workDir2 = r"D:\Projects\10097 Huadong floating\20221207 4thLoop\3. DLC1.6 - RigidBlade - A16"
fileName = r'\Results_globalCS.xlsx'
results_1h1 = round(pd.read_excel(workDir1 + fileName, sheet_name='Sheet1'), 1)
results_1h2 = round(pd.read_excel(workDir2 + fileName, sheet_name='Sheet1'), 1)
results_1h = pd.concat([results_1h1,results_1h2])

workDir0 = r'D:\Projects\10097 Huadong floating\pythonScripts\PostProcessing'
fileName01 = r'\DLC6.2Labels.xlsx'
results01 = pd.read_excel(workDir0 + fileName01, sheet_name='labels')
DLCLabels1 = results01.iloc[15:219,35]
fileName02 = r'\DLC1.6Labels.xlsx'
results02 = pd.read_excel(workDir0 + fileName02, sheet_name='labels')
DLCLabels2 = results02.iloc[8:134,21]
DLCLabels = pd.concat([DLCLabels1,DLCLabels2])
DLCLabels.reset_index(drop=True, inplace=True)


labels = [
    'TwrFxMax[kN]', 'TwrFxMin[kN]', 'TwrFyMax[kN]', 'TwrFyMin[kN]','TwrFxyMax[kN]',  'TwrFxyMin[kN]','TwrFzMax[kN]', 'TwrFzMin[kN]', 
	'TwrMxMax[kNm]','TwrMxMin[kNm]', 'TwrMyMax[kNm]','TwrMyMin[kNm]', 'TwrMxyMax[kNm]','TwrMxyMin[kNm]', 'TwrMzMax[kNm]', 'TwrMzMin[kNm]',
    'Fairlead1aFxMax[kN]', 'Fairlead1aFxMin[kN]', 'Fairlead1aFyMax[kN]', 'Fairlead1aFyMin[kN]', 'Fairlead1aFzMax[kN]', 'Fairlead1aFzMin[kN]',
    'Fairlead1bFxMax[kN]', 'Fairlead1bFxMin[kN]', 'Fairlead1bFyMax[kN]', 'Fairlead1bFyMin[kN]', 'Fairlead1bFzMax[kN]', 'Fairlead1bFzMin[kN]',
    'Fairlead2aFxMax[kN]', 'Fairlead2aFxMin[kN]', 'Fairlead2aFyMax[kN]', 'Fairlead2aFyMin[kN]', 'Fairlead2aFzMax[kN]', 'Fairlead2aFzMin[kN]',
    'Fairlead2bFxMax[kN]', 'Fairlead2bFxMin[kN]', 'Fairlead2bFyMax[kN]', 'Fairlead2bFyMin[kN]', 'Fairlead2bFzMax[kN]', 'Fairlead2bFzMin[kN]',
    'Fairlead3aFxMax[kN]', 'Fairlead3aFxMin[kN]', 'Fairlead3aFyMax[kN]', 'Fairlead3aFyMin[kN]', 'Fairlead3aFzMax[kN]', 'Fairlead3aFzMin[kN]',
    'Fairlead3bFxMax[kN]', 'Fairlead3bFxMin[kN]', 'Fairlead3bFyMax[kN]', 'Fairlead3bFyMin[kN]', 'Fairlead3bFzMax[kN]', 'Fairlead3bFzMin[kN]',
    ]

results_slt = results_1h[labels]
results_slt.insert(0, "DLC", DLCLabels)
results_slt = results_slt.set_index('DLC')
Interface_ULS = results_slt[0:0]

for label in labels:
    if label in [
    'TwrFxMin[kN]', 'TwrFyMin[kN]', 'TwrFxyMin[kN]', 'TwrFzMin[kN]', 'TwrMxMin[kNm]', 'TwrMyMin[kNm]', 'TwrMxyMin[kNm]', 'TwrMzMin[kNm]',
    'Fairlead1aFxMin[kN]', 'Fairlead1aFyMin[kN]', 'Fairlead1aFzMin[kN]',
    'Fairlead1bFxMin[kN]', 'Fairlead1bFyMin[kN]', 'Fairlead1bFzMin[kN]',
    'Fairlead2aFxMin[kN]', 'Fairlead2aFyMin[kN]', 'Fairlead2aFzMin[kN]',
    'Fairlead2bFxMin[kN]', 'Fairlead2bFyMin[kN]', 'Fairlead2bFzMin[kN]',
    'Fairlead3aFxMin[kN]', 'Fairlead3aFyMin[kN]', 'Fairlead3aFzMin[kN]',
    'Fairlead3bFxMin[kN]', 'Fairlead3bFyMin[kN]', 'Fairlead3bFzMin[kN]',]:
        results_sorted = results_slt.sort_values(by=[label], ascending=True)
    else:
        results_sorted = results_slt.sort_values(by=[label], ascending=False)

    Interface_ULS = Interface_ULS.append(results_sorted.iloc[0,:])
    # pd.concat([Interface_ULS,results_sorted.iloc[0,:]],axis=1)
Interface_ULS.insert(0, 'Label', labels)

Interface_ULS.to_excel(workDir1+'\\Results_Interface_ULS.xlsx')







