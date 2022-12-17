import pandas as pd
import matplotlib.pyplot as plt

topN = 10


workDir = r"D:\Projects\10097 Huadong floating\20221207 4thLoop\2. DLC6.2 - RigidBlade - A16"
fileName = r'\Results-python.xlsx'
results_1h = round(pd.read_excel(workDir + fileName, sheet_name='Sheet1'), 1)
workDir0 = r'D:\Projects\10097 Huadong floating\pythonScripts\PostProcessing'
fileName0 = r'\DLC6.2Labels.xlsx'
results0 = pd.read_excel(workDir0 + fileName0, sheet_name='labels')
DLCLabels = results0.iloc[15:219,35]
DLCLabels.reset_index(drop=True, inplace=True)

# workDir = r"D:\Projects\10097 Huadong floating\20221207 4thLoop\3. DLC1.6 - RigidBlade - A16"
# fileName = r'\Results-python.xlsx'
# results_1h = round(pd.read_excel(workDir + fileName, sheet_name='Sheet1'), 1)
# workDir0 = r'D:\Projects\10097 Huadong floating\pythonScripts\PostProcessing'
# fileName0 = r'\DLC1.6Labels.xlsx'
# results0 = pd.read_excel(workDir0 + fileName0, sheet_name='labels')
# DLCLabels = results0.iloc[8:134,21]
# DLCLabels.reset_index(drop=True, inplace=True)

results_1h.insert(0, "DLC", DLCLabels)

# workDir2 = r'C:\0.OrcaflexBox\6. DLC6.2 - RigidBlade - Restart - HSWL - 1periodSameSeeds'
# fileName2 = r'\0. DLC6.2 - RigidBlade - Restart - HSWL - 1periodSameSeeds.xlsx'
# results2 = pd.read_excel(workDir2 + fileName2, sheet_name='Result123')
# results_10min= results2.iloc[0:204,2:]

labels = [
    'RNA acceleration - max [ms2]',
    'RNA pitch angle - max [deg]',
    'RNA roll angle - max [deg]',
    # 'Tower bottom Fx - max [kN]',
    # 'Tower bottom Fy - max [kN]',
    # 'Tower bottom Fxy - max [kN]',
    # 'Tower bottom Fz - max [kN]',
    # 'Tower bottom Mx - max [kNm]',
    # 'Tower bottom My - max [kNm]',
    # 'Tower bottom Mxy - max [kNm]',
    # 'Tower bottom Mz - max [kNm]',
    # 'Fairlead tension 1 [kN]',
    # 'Fairlead tension 2 [kN]',
    # 'Fairlead tension 3 [kN]',
    'Touchdown point 1a [m]',
    'Touchdown point 2a [m]',
    'Touchdown point 3a [m]',
    'Touchdown point 1b [m]',
    'Touchdown point 2b [m]',
    'Touchdown point 3b [m]',
    # 'Anchor force 1 [kN]',
    # 'Anchor force 2 [kN]',
    # 'Anchor force 3 [kN]',
    # 'Floater pitch angle - max [deg]',
    # 'Floater roll angle - max [deg]',
    # 'Floater Tilt - Max [deg]',
    'ExcursionColumn1DistMax [m]', 
    'ExcursionColumn2DistMax [m]', 
    'ExcursionColumn3DistMax [m]',
    'Air Gap Blade Tip - Min [m]',
    'Air Gap Column1 - Min [m]', 
    'Air Gap Column2 - Min [m]', 
    'Air Gap Column3 - Min [m]'
    ]

for label in labels:
    if label in [
        # 'ExcursionColumn1DistMax [m]', 
        #         # 'ExcursionColumn2DistMax [m]', 
        #         'ExcursionColumn3DistMax [m]',
                'Air Gap Blade Tip - Min [m]',
                'Air Gap Column1 - Min [m]', 
                'Air Gap Column2 - Min [m]', 
                'Air Gap Column3 - Min [m]'
                ]:
        results_1h_tdp1 = results_1h.sort_values(by=[label], ascending=True)
        results_1h_tdp1 = results_1h_tdp1.iloc[0:topN,:]
    else:
        results_1h_tdp1 = results_1h.sort_values(by=[label], ascending=False)
        results_1h_tdp1 = results_1h_tdp1.iloc[0:topN,:]

    fig, axs = plt.subplots(1,1,figsize = (12,4), sharex=True,num=label)
    axs.invert_yaxis()
    bars_1h = axs.barh(results_1h_tdp1["DLC"], results_1h_tdp1[label], align="center", height=0.4)
    axs.set_title("DLC6.2 - 1h - "+label)
    axs.bar_label(bars_1h)
    plt.subplots_adjust(left=0.5)
    plt.yticks
    plt.savefig(workDir+"/DLC62-"+label)

# yax = axs.get_yaxis()
# pad = max(T.label)
# plt.show()




