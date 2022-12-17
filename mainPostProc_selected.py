import OrcFxAPI
import numpy as np
import pandas as pd
import time as timecounter
import multiprocessing as mp

# Modify the following parameters
DLC_desciption = "DLC1.6"
workDir = r"D:\Projects\10097 Huadong floating\20221207 4thLoop"
workDir_DLC62_1h = workDir + r"\2. DLC6.2 - RigidBlade - A16"
workDir_DLC62_10min = workDir + r"\1. DLC6.2 - RigidBlade - Restart - A16"
workDir_DLC16 = workDir + r"\3. DLC1.6 - RigidBlade - A16"
dlcN_DLC62 = 204 # number of DLC
dlcN_DLC16 = 126
stageN_DLC62_1h = 1 # number of stages; 3 for DLC6.2-Restart, 1 for the others
stageN_DLC62_10min = 3
stageN_DLC16 = 1
labels = [
    'RNAAcc[ms2]', 'RNAPitch[deg]', 'RNARoll[deg]',
    'TDP1a[m]', 'TDP1b[m]', 'TDP2a[m]', 'TDP2b[m]', 'TDP3a[m]', 'TDP3b[m]',
    'FloaterPitchMax[deg]', 'FloaterRollMax[deg]', 'FloaterTiltMax[deg]',
    'ExcursionColumn1DistMax[m]', 'ExcursionColumn2DistMax[m]', 'ExcursionColumn3DistMax[m]',
    'airGapBladeTipMin[m]',
    'airGapColumn1Min[m]', 'airGapColumn2Min[m]', 'airGapColumn3Min[m]',
    'TwrFxMax[kN]', 'TwrFyMax[kN]', 'TwrFxyMax[kN]', 'TwrFzMax[kN]', 'TwrMxMax[kNm]', 'TwrMyMax[kNm]', 'TwrMxyMax[kNm]', 'TwrMzMax[kNm]',
    'TwrFxMin[kN]', 'TwrFyMin[kN]', 'TwrFxyMin[kN]', 'TwrFzMin[kN]', 'TwrMxMin[kNm]', 'TwrMyMin[kNm]', 'TwrMxyMin[kNm]', 'TwrMzMin[kNm]',
    'Fairlead1aFxMax[kN]', 'Fairlead1aFyMax[kN]', 'Fairlead1aFzMax[kN]',
    'Fairlead1bFxMax[kN]', 'Fairlead1bFyMax[kN]', 'Fairlead1bFzMax[kN]',
    'Fairlead2aFxMax[kN]', 'Fairlead2aFyMax[kN]', 'Fairlead2aFzMax[kN]',
    'Fairlead2bFxMax[kN]', 'Fairlead2bFyMax[kN]', 'Fairlead2bFzMax[kN]',
    'Fairlead3aFxMax[kN]', 'Fairlead3aFyMax[kN]', 'Fairlead3aFzMax[kN]',
    'Fairlead3bFxMax[kN]', 'Fairlead3bFyMax[kN]', 'Fairlead3bFzMax[kN]',
    'Fairlead1aFxMin[kN]', 'Fairlead1aFyMin[kN]', 'Fairlead1aFzMin[kN]',
    'Fairlead1bFxMin[kN]', 'Fairlead1bFyMin[kN]', 'Fairlead1bFzMin[kN]',
    'Fairlead2aFxMin[kN]', 'Fairlead2aFyMin[kN]', 'Fairlead2aFzMin[kN]',
    'Fairlead2bFxMin[kN]', 'Fairlead2bFyMin[kN]', 'Fairlead2bFzMin[kN]',
    'Fairlead3aFxMin[kN]', 'Fairlead3aFyMin[kN]', 'Fairlead3aFzMin[kN]',
    'Fairlead3bFxMin[kN]', 'Fairlead3bFyMin[kN]', 'Fairlead3bFzMin[kN]',
    'FairleadT1a[kN]', 'FairleadT1b[kN]', 'FairleadT2a[kN]', 'FairleadT2b[kN]', 'FairleadT3a[kN]', 'FairleadT3b[kN]',
    'AnchorT1a[kN]', 'AnchorT1b[kN]', 'AnchorT2a[kN]', 'AnchorT2b[kN]', 'AnchorT3a[kN]', 'AnchorT3b[kN]',]
varN = len(labels) # number of extracted variables



def dlcResultsExtracting(workDir, DLCIndex, period):
    # Loading data
    # print(DLCIndex)
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
        # RNA
        RNAAcc = np.max(np.abs(nacelle.TimeHistory('Acceleration', period, OrcFxAPI.oeBuoy(-3.945,0,3.352))))
        RNAPitch = np.max(np.abs(nacelle.TimeHistory('Rotation 2', period)))
        RNARoll = np.max(np.abs(nacelle.TimeHistory('Rotation 1', period)))

        # Tower
        # local
        # TwrFx = tower.TimeHistory("x shear force", period, OrcFxAPI.oeEndB)
        # TwrFy = tower.TimeHistory("y shear force", period, OrcFxAPI.oeEndB)
        # TwrFxy = tower.TimeHistory("shear force", period, OrcFxAPI.oeEndB)
        # TwrFz = tower.TimeHistory("Effective tension", period, OrcFxAPI.oeEndB)
        # TwrMx = tower.TimeHistory("x bend moment", period, OrcFxAPI.oeEndB)
        # TwrMy = tower.TimeHistory("y bend moment", period, OrcFxAPI.oeEndB)
        # TwrMxy = tower.TimeHistory("Bend moment", period, OrcFxAPI.oeEndB)
        # TwrMz = tower.TimeHistory("Torque", period, OrcFxAPI.oeEndB)

        # global
        TwrFx = tower.TimeHistory("End GX force", period, OrcFxAPI.oeEndB)
        TwrFy = tower.TimeHistory("End GY force", period, OrcFxAPI.oeEndB)
        TwrFxy = np.sqrt(np.square(TwrFx) + np.square(TwrFy))
        TwrFz = tower.TimeHistory("End GZ force", period, OrcFxAPI.oeEndB)
        TwrMx = tower.TimeHistory("End GX moment", period, OrcFxAPI.oeEndB)
        TwrMy = tower.TimeHistory("End GY moment", period, OrcFxAPI.oeEndB)
        TwrMxy = np.sqrt(np.square(TwrMx) + np.square(TwrMy))
        TwrMz = tower.TimeHistory("End GZ moment", period, OrcFxAPI.oeEndB)

        TwrFxMax = np.max(TwrFx)
        TwrFyMax = np.max(TwrFy)
        TwrFxyMax = np.max(TwrFxy)
        TwrFzMax = np.max(TwrFz)
        TwrMxMax = np.max(TwrMx)
        TwrMyMax = np.max(TwrMy)
        TwrMxyMax = np.max(TwrMxy)
        TwrMzMax = np.max(TwrMz)

        TwrFxMin = np.min(TwrFx)
        TwrFyMin = np.min(TwrFy)
        TwrFxyMin = np.min(TwrFxy)
        TwrFzMin = np.min(TwrFz)
        TwrMxMin = np.min(TwrMx)
        TwrMyMin = np.min(TwrMy)
        TwrMxyMin = np.min(TwrMxy)
        TwrMzMin = np.min(TwrMz)

        # Mooring line 
        # global
        Fairlead1aFx = mooring1a.TimeHistory("End GX force", period, OrcFxAPI.oeEndA)
        Fairlead1aFy = mooring1a.TimeHistory("End GY force", period, OrcFxAPI.oeEndA)
        Fairlead1aFz = mooring1a.TimeHistory("End GZ force", period, OrcFxAPI.oeEndA)
        Fairlead1bFx = mooring1b.TimeHistory("End GX force", period, OrcFxAPI.oeEndA)
        Fairlead1bFy = mooring1b.TimeHistory("End GY force", period, OrcFxAPI.oeEndA)
        Fairlead1bFz = mooring1b.TimeHistory("End GZ force", period, OrcFxAPI.oeEndA)
        Fairlead2aFx = mooring2a.TimeHistory("End GX force", period, OrcFxAPI.oeEndA)
        Fairlead2aFy = mooring2a.TimeHistory("End GY force", period, OrcFxAPI.oeEndA)
        Fairlead2aFz = mooring2a.TimeHistory("End GZ force", period, OrcFxAPI.oeEndA)
        Fairlead2bFx = mooring2b.TimeHistory("End GX force", period, OrcFxAPI.oeEndA)
        Fairlead2bFy = mooring2b.TimeHistory("End GY force", period, OrcFxAPI.oeEndA)
        Fairlead2bFz = mooring2b.TimeHistory("End GZ force", period, OrcFxAPI.oeEndA)
        Fairlead3aFx = mooring3a.TimeHistory("End GX force", period, OrcFxAPI.oeEndA)
        Fairlead3aFy = mooring3a.TimeHistory("End GY force", period, OrcFxAPI.oeEndA)
        Fairlead3aFz = mooring3a.TimeHistory("End GZ force", period, OrcFxAPI.oeEndA)
        Fairlead3bFx = mooring3b.TimeHistory("End GX force", period, OrcFxAPI.oeEndA)
        Fairlead3bFy = mooring3b.TimeHistory("End GY force", period, OrcFxAPI.oeEndA)
        Fairlead3bFz = mooring3b.TimeHistory("End GZ force", period, OrcFxAPI.oeEndA)

        Fairlead1aFxMax = np.max(Fairlead1aFx)
        Fairlead1aFyMax = np.max(Fairlead1aFy)
        Fairlead1aFzMax = np.max(Fairlead1aFz) 
        Fairlead1bFxMax = np.max(Fairlead1bFx) 
        Fairlead1bFyMax = np.max(Fairlead1bFy) 
        Fairlead1bFzMax = np.max(Fairlead1bFz) 
        Fairlead2aFxMax = np.max(Fairlead2aFx) 
        Fairlead2aFyMax = np.max(Fairlead2aFy) 
        Fairlead2aFzMax = np.max(Fairlead2aFz) 
        Fairlead2bFxMax = np.max(Fairlead2bFx) 
        Fairlead2bFyMax = np.max(Fairlead2bFy) 
        Fairlead2bFzMax = np.max(Fairlead2bFz) 
        Fairlead3aFxMax = np.max(Fairlead3aFx) 
        Fairlead3aFyMax = np.max(Fairlead3aFy) 
        Fairlead3aFzMax = np.max(Fairlead3aFz) 
        Fairlead3bFxMax = np.max(Fairlead3bFx) 
        Fairlead3bFyMax = np.max(Fairlead3bFy) 
        Fairlead3bFzMax = np.max(Fairlead3bFz) 


        Fairlead1aFxMin = np.min(Fairlead1aFx)
        Fairlead1aFyMin = np.min(Fairlead1aFy)
        Fairlead1aFzMin = np.min(Fairlead1aFz)
        Fairlead1bFxMin = np.min(Fairlead1bFx)
        Fairlead1bFyMin = np.min(Fairlead1bFy)
        Fairlead1bFzMin = np.min(Fairlead1bFz)
        Fairlead2aFxMin = np.min(Fairlead2aFx)
        Fairlead2aFyMin = np.min(Fairlead2aFy)
        Fairlead2aFzMin = np.min(Fairlead2aFz)
        Fairlead2bFxMin = np.min(Fairlead2bFx)
        Fairlead2bFyMin = np.min(Fairlead2bFy)
        Fairlead2bFzMin = np.min(Fairlead2bFz)
        Fairlead3aFxMin = np.min(Fairlead3aFx)
        Fairlead3aFyMin = np.min(Fairlead3aFy)
        Fairlead3aFzMin = np.min(Fairlead3aFz)
        Fairlead3bFxMin = np.min(Fairlead3bFx)
        Fairlead3bFyMin = np.min(Fairlead3bFy)
        Fairlead3bFzMin = np.min(Fairlead3bFz)

        TDP1a = np.max(mooring1a.TimeHistory('Arc length', period, OrcFxAPI.oeTouchdown))
        TDP1b = np.max(mooring1b.TimeHistory('Arc length', period, OrcFxAPI.oeTouchdown))
        TDP2a = np.max(mooring2a.TimeHistory('Arc length', period, OrcFxAPI.oeTouchdown))
        TDP2b = np.max(mooring2b.TimeHistory('Arc length', period, OrcFxAPI.oeTouchdown))
        TDP3a = np.max(mooring3a.TimeHistory('Arc length', period, OrcFxAPI.oeTouchdown))
        TDP3b = np.max(mooring3b.TimeHistory('Arc length', period, OrcFxAPI.oeTouchdown))
        FairleadT1a = np.max(mooring1a.TimeHistory('Effective tension', period, OrcFxAPI.oeEndA))
        FairleadT1b = np.max(mooring1b.TimeHistory('Effective tension', period, OrcFxAPI.oeEndA))
        FairleadT2a = np.max(mooring2a.TimeHistory('Effective tension', period, OrcFxAPI.oeEndA))
        FairleadT2b = np.max(mooring2b.TimeHistory('Effective tension', period, OrcFxAPI.oeEndA))
        FairleadT3a = np.max(mooring3a.TimeHistory('Effective tension', period, OrcFxAPI.oeEndA))
        FairleadT3b = np.max(mooring3b.TimeHistory('Effective tension', period, OrcFxAPI.oeEndA))
        AnchorT1a = np.max(mooring1a.TimeHistory('Effective tension', period, OrcFxAPI.oeEndB))
        AnchorT1b = np.max(mooring1b.TimeHistory('Effective tension', period, OrcFxAPI.oeEndB))
        AnchorT2a = np.max(mooring2a.TimeHistory('Effective tension', period, OrcFxAPI.oeEndB))
        AnchorT2b = np.max(mooring2b.TimeHistory('Effective tension', period, OrcFxAPI.oeEndB))
        AnchorT3a = np.max(mooring3a.TimeHistory('Effective tension', period, OrcFxAPI.oeEndB))
        AnchorT3b = np.max(mooring3b.TimeHistory('Effective tension', period, OrcFxAPI.oeEndB))


        # Excursion
        C2C = 110
        C2Cx = 110*np.sqrt(3)/2
        C2Cy = 110/2
        ExcursionColumn1X = floater.TimeHistory('X', period, OrcFxAPI.oeVessel(0.0, 0.0, 0))
        ExcursionColumn1Y = floater.TimeHistory('Y', period, OrcFxAPI.oeVessel(0.0, 0.0, 0))
        ExcursionColumn2X = floater.TimeHistory('X', period, OrcFxAPI.oeVessel(C2Cx, -C2Cy, 0))
        ExcursionColumn2Y = floater.TimeHistory('Y', period, OrcFxAPI.oeVessel(C2Cx, -C2Cy, 0))
        ExcursionColumn3X = floater.TimeHistory('X', period, OrcFxAPI.oeVessel(C2Cx, C2Cy, 0))
        ExcursionColumn3Y = floater.TimeHistory('Y', period, OrcFxAPI.oeVessel(C2Cx, C2Cy, 0))
        ExcursionColumn1DistMax = max(np.sqrt(np.square(ExcursionColumn1X) + np.square(ExcursionColumn1Y))) 
        ExcursionColumn2DistMax = max(np.sqrt(np.square(ExcursionColumn2X - C2Cx) + np.square(ExcursionColumn2Y + C2Cy)))
        ExcursionColumn3DistMax = max(np.sqrt(np.square(ExcursionColumn3X - C2Cx) + np.square(ExcursionColumn3Y - C2Cy)))
        # Tilt
        FloaterPitch = floater.TimeHistory('Rotation 2', period)
        FloaterRoll = floater.TimeHistory('Rotation 1', period)
        FloaterPitchMax = np.max(np.abs(FloaterPitch))
        FloaterRollMax = np.max(np.abs(FloaterRoll))
        FloaterTiltMax = max(np.sqrt(np.square(FloaterRoll) + np.square(FloaterPitch)))
        # # Air gap - Blade tip
        bladeTip1 = turbine.TimeHistory('Node Z', period, OrcFxAPI.oeTurbineEndB(BladeIndex=1))
        bladeTip2 = turbine.TimeHistory('Node Z', period, OrcFxAPI.oeTurbineEndB(BladeIndex=2))
        bladeTip3 = turbine.TimeHistory('Node Z', period, OrcFxAPI.oeTurbineEndB(BladeIndex=3))
        waveElevationColumn1 = environment.TimeHistory('Elevation', period, OrcFxAPI.oeEnvironment(0, 0, 0))
        airGapBladeTipMin1 = min(bladeTip1 - waveElevationColumn1)
        airGapBladeTipMin2 = min(bladeTip2 - waveElevationColumn1)
        airGapBladeTipMin3 = min(bladeTip3 - waveElevationColumn1)
        airGapBladeTipMin = min(airGapBladeTipMin1, airGapBladeTipMin2, airGapBladeTipMin3)

        # Air gap - Platform
        column1Elevation = floater.TimeHistory('Z', period, OrcFxAPI.oeVessel(0.0, 0.0, 21.0))
        column2Elevation = floater.TimeHistory('Z', period, OrcFxAPI.oeVessel(C2Cx, -C2Cy, 21))
        column3Elevation = floater.TimeHistory('Z', period, OrcFxAPI.oeVessel(C2Cx, C2Cy, 21))
        waveElevationColumn1 = environment.TimeHistory('Elevation', period, OrcFxAPI.oeEnvironment(0, 0, 0))
        waveElevationColumn2 = environment.TimeHistory('Elevation', period, OrcFxAPI.oeEnvironment(C2Cx, -C2Cy, 21))
        waveElevationColumn3 = environment.TimeHistory('Elevation', period, OrcFxAPI.oeEnvironment(C2Cx, C2Cy, 21))
        airGapColumn1Min = min(column1Elevation - waveElevationColumn1)
        airGapColumn2Min = min(column2Elevation - waveElevationColumn2)
        airGapColumn3Min = min(column3Elevation - waveElevationColumn3)

        result = np.array([
            RNAAcc, RNAPitch, RNARoll,
            TDP1a, TDP1b, TDP2a, TDP2b, TDP3a, TDP3b,
            FloaterPitchMax, FloaterRollMax, FloaterTiltMax,
            ExcursionColumn1DistMax, ExcursionColumn2DistMax, ExcursionColumn3DistMax,
            airGapBladeTipMin,
            airGapColumn1Min, airGapColumn2Min, airGapColumn3Min,
            TwrFxMax, TwrFyMax, TwrFxyMax, TwrFzMax, TwrMxMax, TwrMyMax, TwrMxyMax, TwrMzMax,
            TwrFxMin, TwrFyMin, TwrFxyMin, TwrFzMin, TwrMxMin, TwrMyMin, TwrMxyMin, TwrMzMin,
            Fairlead1aFxMax, Fairlead1aFyMax, Fairlead1aFzMax,
            Fairlead1bFxMax, Fairlead1bFyMax, Fairlead1bFzMax,
            Fairlead2aFxMax, Fairlead2aFyMax, Fairlead2aFzMax,
            Fairlead2bFxMax, Fairlead2bFyMax, Fairlead2bFzMax,
            Fairlead3aFxMax, Fairlead3aFyMax, Fairlead3aFzMax,
            Fairlead3bFxMax, Fairlead3bFyMax, Fairlead3bFzMax,
            Fairlead1aFxMin, Fairlead1aFyMin, Fairlead1aFzMin,
            Fairlead1bFxMin, Fairlead1bFyMin, Fairlead1bFzMin,
            Fairlead2aFxMin, Fairlead2aFyMin, Fairlead2aFzMin,
            Fairlead2bFxMin, Fairlead2bFyMin, Fairlead2bFzMin,
            Fairlead3aFxMin, Fairlead3aFyMin, Fairlead3aFzMin,
            Fairlead3bFxMin, Fairlead3bFyMin, Fairlead3bFzMin,
            FairleadT1a, FairleadT1b, FairleadT2a, FairleadT2b, FairleadT3a, FairleadT3b,
            AnchorT1a, AnchorT1b, AnchorT2a, AnchorT2b, AnchorT3a, AnchorT3b,])
        print(DLCIndex+" - YES")
        return result

    except OrcFxAPI.DLLError:
        result = np.zeros(varN)
        print(DLCIndex+" - None")
        return result

def extact(DLC_desciption, workDir_DLC62_1h, workDir_DLC62_10min, workDir_DLC16, dlcN_DLC62, dlcN_DLC16, stageN_DLC62_1h, stageN_DLC62_10min, stageN_DLC16):
    pool = mp.Pool(num_cores)
    match DLC_desciption:
        case "DLC6.2-1h":
            Results = np.array(pool.starmap(
                        dlcResultsExtracting, 
                        [(workDir_DLC62_1h, 
                        "DLC6.2" + '-' + str(j+1), 
                        (i+1)+1)
                        for i in range(stageN_DLC62_1h) for j in range(dlcN_DLC62)]
                        ))
            return np.reshape(Results, (stageN_DLC62_1h, dlcN_DLC62, varN)), workDir_DLC62_1h

        case "DLC6.2-10min":
            Results = np.array(pool.starmap(
                        dlcResultsExtracting, 
                        [(workDir_DLC62_10min, 
                        "DLC6.2" + '-' + str(i+1) + '-' + str(j+1), 
                        (i+1)+1)
                        for i in range(stageN_DLC62_10min) for j in range(dlcN_DLC62)]
                        ))
            return np.reshape(Results, (stageN_DLC62_10min, dlcN_DLC62, varN)), workDir_DLC62_10min

        case "DLC1.6":
            Results = np.array(pool.starmap(
                        dlcResultsExtracting, 
                        [(workDir_DLC16, 
                        "DLC1.6" + '-' + str(j+1), 
                        (i+1)+1)
                        for i in range(stageN_DLC16) for j in range(dlcN_DLC16)]
                        ))
            return np.reshape(Results, (stageN_DLC16, dlcN_DLC16, varN)), workDir_DLC16

        case _:
            return "Please provide correct a DLC name"

if __name__ == '__main__':
    timeElapsedStart = timecounter.time()
    num_cores = int(mp.cpu_count())
    print("There are " + str(num_cores) + " cores")
    
    results, workDir_slt = extact(DLC_desciption, workDir_DLC62_1h, workDir_DLC62_10min, workDir_DLC16, dlcN_DLC62, dlcN_DLC16, stageN_DLC62_1h, stageN_DLC62_10min, stageN_DLC16)
    resultsMax1 = np.max(results[:,:,0:15], axis=0)
    resultsMin1 = np.min(results[:,:,15:19], axis=0)
    resultsMax2 = np.max(results[:,:,19:27], axis=0)
    resultsMin2 = np.min(results[:,:,27:35], axis=0)
    resultsMax3 = np.max(results[:,:,35:53], axis=0)
    resultsMin3 = np.min(results[:,:,53:71], axis=0)
    resultsMax4 = np.max(results[:,:,71:], axis=0)
    results = np.concatenate((resultsMax1,resultsMin1,resultsMax2,resultsMin2,resultsMax3,resultsMin3,resultsMax4), axis=1)
    df = pd.DataFrame(results, columns=labels)
    df.to_excel(workDir_slt+'\\Results_All.xlsx', index=False)

    timeElapsedEnd = timecounter.time()
    timeElapased = round((timeElapsedEnd - timeElapsedStart)/60, 2)
    print(f'The elapsed time is {timeElapased} min')
