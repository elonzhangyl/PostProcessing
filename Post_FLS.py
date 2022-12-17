import OrcFxAPI
import numpy as np
import pandas as pd
import time as timecounter
import multiprocessing as mp
import matplotlib.pyplot as plt

# Modify the following parameters
DLC_desciption = "DLC1.2"
workDir = r"D:\Projects\10097 Huadong floating\20221207 4thLoop"
varN = 7 # number of extracted variables
bin_size = 10
workDir_DLC12 = workDir + r"\4. DLC1.2 - RigidBlade - A16 - 0deg"
dlcN_DLC12 = 1656
stageN_DLC12 = 1
m = 5

labels = [
    'Tower bottom Mxy - max [kNm]',
    'Fairlead tension 1a [kN]',
    'Fairlead tension 1b [kN]',
    'Fairlead tension 2a [kN]',
    'Fairlead tension 2b [kN]',
    'Fairlead tension 3a [kN]',
    'Fairlead tension 3b [kN]',]

period = 2
def dlcResultsExtracting(workDir, DLCIndex, period):
    try:
        model = OrcFxAPI.Model(workDir + r'/'+ DLCIndex +'.sim') # load the data from a simulation file

        timeModule = model['General']
        time = timeModule.TimeHistory('Time', period)
        floater = model['OrcaWave A16_EOL']
        turbine = model['15MW RWT']
        nacelle = model['Nacelle']
        environment = model['Environment']
        tower = model['Tower']
        mooring1a = model['Mooring1a']
        mooring1b = model['Mooring1b']
        mooring2a = model['Mooring2a']
        mooring2b = model['Mooring2b']
        mooring3a = model['Mooring3a']
        mooring3b = model['Mooring3b']

        ################### Extracting results #####################################
        # Tower bottom
        TowerFx = tower.CycleHistogramBins("x shear force", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerFy = tower.CycleHistogramBins("y shear force", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerFxy = tower.CycleHistogramBins("shear force", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerFz = tower.CycleHistogramBins("Effective tension", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerMx = tower.CycleHistogramBins("x bend moment", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerMy = tower.CycleHistogramBins("y bend moment", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerMxy = tower.CycleHistogramBins("Bend moment", period, OrcFxAPI.oeEndB, binSize=bin_size)
        TowerMz = tower.CycleHistogramBins("Torque", period, OrcFxAPI.oeEndB, binSize=bin_size)
        # Fairleads
        MooringFairleadRainflow1a = mooring1a.CycleHistogramBins('Effective tension', period, OrcFxAPI.oeEndA, binSize=bin_size)
        MooringFairleadRainflow1b = mooring1b.CycleHistogramBins('Effective tension', period, OrcFxAPI.oeEndA, binSize=bin_size)
        MooringFairleadRainflow2a = mooring2a.CycleHistogramBins('Effective tension', period, OrcFxAPI.oeEndA, binSize=bin_size)
        MooringFairleadRainflow2b = mooring2b.CycleHistogramBins('Effective tension', period, OrcFxAPI.oeEndA, binSize=bin_size)
        MooringFairleadRainflow3a = mooring3a.CycleHistogramBins('Effective tension', period, OrcFxAPI.oeEndA, binSize=bin_size)
        MooringFairleadRainflow3b = mooring3b.CycleHistogramBins('Effective tension', period, OrcFxAPI.oeEndA, binSize=bin_size)

        results = [
            TowerFx, TowerFy, TowerFxy, TowerFz, TowerMx, TowerMy, TowerMxy, TowerMz,
            MooringFairleadRainflow1a, MooringFairleadRainflow1b,
            MooringFairleadRainflow2a, MooringFairleadRainflow2b,
            MooringFairleadRainflow3a, MooringFairleadRainflow3b]

        equiv_fatigue = np.zeros(varN)
        for i in range(len(results)):
            res = results[i]
            for obj in res:
                equiv_fatigue[i] += pow(obj.Value, m) * obj.Count
        print(DLCIndex+" - YES")
        return equiv_fatigue
    
    except OrcFxAPI.DLLError:
        equiv_fatigue = np.zeros(varN)
        print(DLCIndex+" - None")
        return equiv_fatigue


def extact(DLC_desciption, workDir_DLC12, dlcN_DLC12, stageN_DLC12):
    pool = mp.Pool(num_cores)
    match DLC_desciption:
        case "DLC1.2":
            Results = np.array(pool.starmap(
                        dlcResultsExtracting, 
                        [(workDir_DLC12, 
                        "DLC1.6" + '-' + str(j+1), 
                        (i+1)+1)
                        for i in range(stageN_DLC12) for j in range(dlcN_DLC12)]
                        ))
            return Results, workDir_DLC12

        case _:
            return "Please provide correct a DLC name"

if __name__ == '__main__':
    timeElapsedStart = timecounter.time()
    num_cores = int(mp.cpu_count())
    print("There are " + str(num_cores) + " cores")
    
    results, workDir_slt = extact(DLC_desciption, workDir_DLC12, dlcN_DLC12, stageN_DLC12)
    df = pd.DataFrame(results, columns=labels)
    df.to_excel(workDir_slt+'\\Results-python.xlsx', index=False)

    timeElapsedEnd = timecounter.time()
    timeElapased = round((timeElapsedEnd - timeElapsedStart)/60, 2)
    print(f'The elapsed time is {timeElapased} min')
