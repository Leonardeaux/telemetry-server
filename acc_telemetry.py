import mmap
from ctypes import Structure, sizeof, c_float, c_int32, c_wchar, c_int


class SPageFileStatic(Structure):
    _fields_ = [
        ("smVersion", c_wchar * 15),
        ("acVersion", c_wchar * 15),
        ("numberOfSessions", c_int),
        ("numCars", c_int),
        ("carModel", c_wchar * 33),
        ("track", c_wchar * 33),
        ("playerName", c_wchar * 33),
        ("playerSurname", c_wchar * 33),
        ("playerNick", c_wchar * 33),
        ("sectorCount", c_int),
        ("maxTorque", c_float),
        ("maxPower", c_float),
        ("maxRpm", c_int),
        ("maxFuel", c_float),
        ("suspensionMaxTravel", c_float * 4),
        ("tyreRadius", c_float * 4),
        ("maxTurboBoost", c_float * 4),
        ("deprecated_1", c_float),
        ("deprecated_2", c_float),
        ("penaltiesEnabled", c_int),
        ("aidFuelRate", c_float),
        ("aidTireRate", c_float),
        ("aidMechanicalDamage", c_float),
        ("aidAllowTyreBlankets", c_int),
        ("aidStability", c_float),
        ("aidAutoClutch", c_int),
        ("aidAutoBlip", c_int),
        ("hasDRS", c_int),
        ("hasERS", c_int),
        ("hasKERS", c_int),
        ("kersMaxJ", c_float),
        ("engineBrakeSettingsCount", c_int),
        ("ersPowerControllerCount", c_int),
        ("trackSPlineLength", c_float),
        ("trackConfiguration", c_wchar * 33),
        ("ersMaxJ", c_float),
        ("isTimedRace", c_int),
        ("hasExtraLap", c_int),
        ("carSkin", c_wchar * 33),
        ("reversedGridPositions", c_int),
        ("PitWindowStart", c_int),
        ("PitWindowEnd", c_int),
        ("isOnline", c_int),
    ]

    def toDict(self):
        return {
            "PitWindowStart": self.PitWindowStart,
            "PitWindowEnd": self.PitWindowEnd,
        }


class SPageFileGraphic(Structure):
    _fields_ = [
        ("packetId", c_int),
        ("AC_STATUS", c_int),
        ("AC_SESSION_TYPE", c_int),
        ("currentTime", c_wchar * 15),
        ("lastTime", c_wchar * 15),
        ("bestTime", c_wchar * 15),
        ("split", c_wchar * 15),
        ("completedLaps", c_int),
        ("position", c_int),
        ("iCurrentTime", c_int),
        ("iLastTime", c_int),
        ("iBestTime", c_int),
        ("sessionTimeLeft", c_float),
        ("distanceTraveled", c_float),
        ("isInPit", c_int),
        ("currentSectorIndex", c_int),
        ("lastSectorTime", c_int),
        ("numberOfLaps", c_int),
        ("tyreCompound", c_wchar * 33),
        ("replayTimeMultiplier", c_float),
        ("normalizedCarPosition", c_float),

        ("activeCars", c_int),
        ("carCoordinates", c_float * 60 * 3),
        ("carID", c_int * 60),
        ("playerCarID", c_int),
        ("penaltyTime", c_float),
        ("flag", c_int),
        ("penalty", c_int),
        ("idealLineOn", c_int),
        ("isInPitLane", c_int),

        ("surfaceGrip", c_float),
        ("mandatoryPitDone", c_int),

        ("windSpeed", c_float),
        ("windDirection", c_float),

        ("isSetupMenuVisible", c_int),

        ("mainDisplayIndex", c_int),
        ("secondaryDisplayIndex", c_int),
        ("TC", c_int),
        ("TCCut", c_int),
        ("EngineMap", c_int),
        ("ABS", c_int),
        ("fuelXLap", c_int),
        ("rainLights", c_int),
        ("flashingLights", c_int),
        ("lightsStage", c_int),
        ("exhaustTemperature", c_float),
        ("wiperLV", c_int),
        ("DriverStintTotalTimeLeft", c_int),
        ("DriverStintTimeLeft", c_int),
        ("rainTypes", c_int),
    ]

    def toDict(self):
        return {
            "bestTime": self.bestTime,
            "completedLaps": self.completedLaps,
            "distanceTraveled": self.distanceTraveled,
        }


class SPageFilePhysics(Structure):
    _fields_ = [
        ("packetId", c_int),
        ("gas", c_float),
        ("brake", c_float),
        ("fuel", c_float),
        ("gear", c_int),
        ("rpms", c_int),
        ("steerAngle", c_float),
        ("speedKmh", c_float),
        ("velocity", c_float * 3),
        ("accG", c_float * 3),
        ("wheelSlip", c_float * 4),
        ("wheelLoad", c_float * 4),
        ("wheelsPressure", c_float * 4),
        ("wheelAngularSpeed", c_float * 4),
        ("tyreWear", c_float * 4),
        ("tyreDirtyLevel", c_float * 4),
        ("tyreCoreTemperature", c_float * 4),
        ("camberRAD", c_float * 4),
        ("suspensionTravel", c_float * 4),
        ("drs", c_float),
        ("tc", c_float),
        ("heading", c_float),
        ("pitch", c_float),
        ("roll", c_float),
        ("cgHeight", c_float),
        ("carDamage", c_float * 5),
        ("numberOfTyresOut", c_int),
        ("pitLimiterOn", c_int),
        ("abs", c_float),
        ("kersCharge", c_float),
        ("kersInput", c_float),
        ("autoShifterOn", c_int),
        ("rideHeight", c_float * 2),
        ("turboBoost", c_float),
        ("ballast", c_float),
        ("airDensity", c_float),
        ("airTemp", c_float),
        ("roadTemp", c_float),
        ("localAngularVel", c_float * 3),
        ("finalFF", c_float),
        ("performanceMeter", c_float),

        ("engineBrake", c_int),
        ("ersRecoveryLevel", c_int),
        ("ersPowerLevel", c_int),
        ("ersHeatCharging", c_int),
        ("ersIsCharging", c_int),
        ("kersCurrentKJ", c_float),

        ("drsAvailable", c_int),
        ("drsEnabled", c_int),

        ("brakeTemp", c_float * 4),
        ("clutch", c_float),

        ("tyreTempI", c_float * 4),
        ("tyreTempM", c_float * 4),
        ("tyreTempO", c_float * 4),

        ("isAIControlled", c_int),

        ("tyreContactPoint", c_float * 4 * 3),
        ("tyreContactNormal", c_float * 4 * 3),
        ("tyreContactHeading", c_float * 4 * 3),

        ("brakeBias", c_float),

        ("localVelocity", c_float * 3),

        ("P2PActivations", c_int),
        ("P2PStatus", c_int),

        ("currentMaxRpm", c_int),

        ("mz", c_float * 4),
        ("fx", c_float * 4),
        ("fy", c_float * 4),
        ("slipRatio", c_float * 4),
        ("slipAngle", c_float * 4),

        ("tcinAction", c_int),
        ("absInAction", c_int),
        ("suspensionDamage", c_float * 4),
        ("tyreTemp", c_float * 4),
    ]

    def toDict(self):
        return {
            "gas": self.gas,
            "brake": self.brake,
            # "fuel": self.fuel,
            # "gear": self.gear,
            # "rpms": self.rpms,
            "steerAngle": self.steerAngle,
            "speedKmh": self.speedKmh,
            # "velocity": "{} {} {}".format(self.velocity[0], self.velocity[1], self.velocity[2]),
            # "accG": self.accG,
            # "wheelSlip": self.wheelSlip,
            # "wheelLoad": self.wheelLoad,
            # "wheelsPressure": self.wheelsPressure,
            # "wheelAngularSpeed": self.wheelAngularSpeed,
            # "tyreWear": self.tyreWear,
            # "tyreDirtyLevel": self.tyreDirtyLevel,
            # "tyreCoreTemperature": self.tyreCoreTemperature,
            # "camberRAD": self.camberRAD,
            # "suspensionTravel": self.suspensionTravel,
            # "drs": self.drs,
            # "tc": self.tc,
            # "heading": self.heading,
            # "pitch": self.pitch,
            # "roll": self.roll,
            # "cgHeight": self.cgHeight,
            # "carDamage": self.carDamage,
            # "numberOfTyresOut": self.numberOfTyresOut,
            # "pitLimiterOn": self.pitLimiterOn,
            "abs": self.abs,
            # "kersCharge": self.kersCharge,
            # "kersInput": self.kersInput,
            # "autoShifterOn": self.autoShifterOn,
            # "rideHeight": self.rideHeight,
            # "turboBoost": self.turboBoost,
            # "ballast": self.ballast,
            # "airDensity": self.airDensity,
            # "airTemp": self.airTemp,
            # "roadTemp": self.roadTemp,
            # "localAngularVel": self.localAngularVel,
            # "finalFF": self.finalFF,
            # "performanceMeter": self.performanceMeter,
            # "engineBrake": self.engineBrake,
            # "ersRecoveryLevel": self.ersRecoveryLevel,
            # "ersPowerLevel": self.ersPowerLevel,
            # "ersHeatCharging": self.ersHeatCharging,
            # "ersIsCharging": self.ersIsCharging,
            # "kersCurrentKJ": self.kersCurrentKJ,
            # "drsAvailable": self.drsAvailable,
            # "drsEnabled": self.drsEnabled,
            # "brakeTemp": self.brakeTemp,
            # "clutch": self.clutch,
            # "tyreTempI": self.tyreTempI,
            # "tyreTempM": self.tyreTempM,
            # "tyreTempO": self.tyreTempO,
            # "isAIControlled": self.isAIControlled,
            # "tyreContactPoint": self.tyreContactPoint,
            # "tyreContactNormal": self.tyreContactNormal,
            # "tyreContactHeading": self.tyreContactHeading,
            # "brakeBias": self.brakeBias,
            # "localVelocity": self.localVelocity,
            # "P2PActivations": self.P2PActivations,
            # "P2PStatus": self.P2PStatus,
            # "currentMaxRpm": self.currentMaxRpm,
            # "mz": self.mz,
            # "fx": self.fx,
            # "fy": self.fy,
            # "slipRatio": self.slipRatio,
            # "slipAngle": self.slipAngle,
            # "tcinAction": self.tcinAction,
            # "absInAction": self.absInAction,
            # "suspensionDamage": self.suspensionDamage,
            # "tyreTemp": self.tyreTemp,
        }

    def toDict(self):
        return {
            "gas": self.gas,
            "brake": self.brake,
            # "fuel": self.fuel,
            # "gear": self.gear,
            # "rpms": self.rpms,
            "steerAngle": self.steerAngle,
            "speedKmh": self.speedKmh,
            # "velocity": "{} {} {}".format(self.velocity[0], self.velocity[1], self.velocity[2]),
            # "accG": self.accG,
            # "wheelSlip": self.wheelSlip,
            # "wheelLoad": self.wheelLoad,
            # "wheelsPressure": self.wheelsPressure,
            # "wheelAngularSpeed": self.wheelAngularSpeed,
            # "tyreWear": self.tyreWear,
            # "tyreDirtyLevel": self.tyreDirtyLevel,
            # "tyreCoreTemperature": self.tyreCoreTemperature,
            # "camberRAD": self.camberRAD,
            # "suspensionTravel": self.suspensionTravel,
            # "drs": self.drs,
            # "tc": self.tc,
            # "heading": self.heading,
            # "pitch": self.pitch,
            # "roll": self.roll,
            # "cgHeight": self.cgHeight,
            # "carDamage": self.carDamage,
            # "numberOfTyresOut": self.numberOfTyresOut,
            # "pitLimiterOn": self.pitLimiterOn,
            "abs": self.abs,
            # "kersCharge": self.kersCharge,
            # "kersInput": self.kersInput,
            # "autoShifterOn": self.autoShifterOn,
            # "rideHeight": self.rideHeight,
            # "turboBoost": self.turboBoost,
            # "ballast": self.ballast,
            # "airDensity": self.airDensity,
            # "airTemp": self.airTemp,
            # "roadTemp": self.roadTemp,
            # "localAngularVel": self.localAngularVel,
            # "finalFF": self.finalFF,
            # "performanceMeter": self.performanceMeter,
            # "engineBrake": self.engineBrake,
            # "ersRecoveryLevel": self.ersRecoveryLevel,
            # "ersPowerLevel": self.ersPowerLevel,
            # "ersHeatCharging": self.ersHeatCharging,
            # "ersIsCharging": self.ersIsCharging,
            # "kersCurrentKJ": self.kersCurrentKJ,
            # "drsAvailable": self.drsAvailable,
            # "drsEnabled": self.drsEnabled,
            # "brakeTemp": self.brakeTemp,
            # "clutch": self.clutch,
            # "tyreTempI": self.tyreTempI,
            # "tyreTempM": self.tyreTempM,
            # "tyreTempO": self.tyreTempO,
            # "isAIControlled": self.isAIControlled,
            # "tyreContactPoint": self.tyreContactPoint,
            # "tyreContactNormal": self.tyreContactNormal,
            # "tyreContactHeading": self.tyreContactHeading,
            # "brakeBias": self.brakeBias,
            # "localVelocity": self.localVelocity,
            # "P2PActivations": self.P2PActivations,
            # "P2PStatus": self.P2PStatus,
            # "currentMaxRpm": self.currentMaxRpm,
            # "mz": self.mz,
            # "fx": self.fx,
            # "fy": self.fy,
            # "slipRatio": self.slipRatio,
            # "slipAngle": self.slipAngle,
            # "tcinAction": self.tcinAction,
            # "absInAction": self.absInAction,
            # "suspensionDamage": self.suspensionDamage,
            # "tyreTemp": self.tyreTemp,
        }

    def transformation_factory(self, transformation: str):
        return {
            "speed_influence_per_gas_per_frames": self.speed_influence_per_gas_per_frames_transformation,
            "speed_influence_per_brake_per_frames": self.speed_influence_per_brake_per_frames_transformation,
            "mean_speed_by_laps_transformation": self.mean_speed_by_laps_transformation
        }[transformation]()

    def speed_influence_per_gas_per_frames_transformation(self):
        pass

    def speed_influence_per_brake_per_frames_transformation(self):
        pass

    def mean_speed_by_laps_transformation(self):
        pass


def read_physics():
    buf = mmap.mmap(-1, sizeof(SPageFilePhysics), u"Local\\acpmf_physics")
    data = SPageFilePhysics.from_buffer(buf)
    return data.toDict()


def read_static():
    buf = mmap.mmap(-1, sizeof(SPageFileStatic), u"Local\\acpmf_static")
    data = SPageFileStatic.from_buffer(buf)
    return data.toDict()


def read_graphics():
    buf = mmap.mmap(-1, sizeof(SPageFileGraphic), u"Local\\acpmf_graphics")
    data = SPageFileGraphic.from_buffer(buf)
    return data.toDict()
