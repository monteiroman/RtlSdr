

class DataStructure (object):
    def __init__(self, *args, **kwargs):
        self.samples = []
        self.sdr = 0
        self.sample_rate = 0
        self.center_freq = 0
        self.gain = 0
        self.quitFlag = False

    def setSamples (self, samples):
        self.samples = samples

    def getSamples (self):
        return self.samples

    def setParameters (self, sample_rate, center_freq, gain):
        self.sample_rate = sample_rate
        self.center_freq = center_freq
        self.gain = gain

    def getParameters (self):
        return (self.sample_rate, self.center_freq, self.gain)

    def setQuitState (self):
        self.quitFlag = True

    def getQuitState (self):
        return self.quitFlag
