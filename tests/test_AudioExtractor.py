# test_AudioExtractor.py
#----------------------------------------------------------------------------------------------------
import re
import sys
sys.path.append("..")

from audioExtractor import *
#----------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()
    test_determineStartAndEndTimes()
    test_extract_harryMosesDaylight()
    #test_extract_monkeyAndThunder()
    #test_extract_prayer()

def test_constructor():

    print("--- test_constructor")

    ea = AudioExtractor("../testData/harryMosesDaylight/daylight_1_4.wav",
                        "../testData/harryMosesDaylight/daylight_1_4.eaf",
                        "../testData/harryMosesDaylight/audioPhrases")
    assert(ea.validInputs)

def test_determineStartAndEndTimes():

    print("--- test_determineStartAndEndTimes")
    ea = AudioExtractor("../testData/harryMosesDaylight/daylight_1_4.wav",
                        "../testData/harryMosesDaylight/daylight_1_4.eaf",
                        "../testData/harryMosesDaylight/audioPhrases")
    tbl = ea.determineStartAndEndTimes()
    # print(tbl)
    assert(tbl.shape == (4, 5))
    assert(list(tbl.columns) == ["lineID", "start", "end", "t1", "t2"])
    (a4_start, a4_end) = tbl.loc[tbl['lineID'] == 'a4'][['start', 'end']].iloc[0].tolist()
    assert(a4_start == 17800)
    assert(a4_end == 22938)

def test_extract_harryMosesDaylight():

    print("--- test_extract_harryMosesDaylight")

    ea = AudioExtractor("../testData/harryMosesDaylight/daylight_1_4.wav",
                        "../testData/harryMosesDaylight/daylight_1_4.eaf",
                        "../testData/harryMosesDaylight/audioPhrases")
    ea.extract(quiet=True)
    assert(len(os.listdir("../testData/harryMosesDaylight/audioPhrases")) == 4)


def test_extract_monkeyAndThunder():
    print("--- test_extract_monkeyAndThunder")
    ea = AudioExtractor("../testData/monkeyAndThunder/AYA1_MonkeyandThunder-32bit.wav",
                        "../testData/monkeyAndThunder/AYA1_MonkeyandThunder.eaf",
                        "../testData/monkeyAndThunder/audioPhrases")
    ea.extract(quiet=True)
    assert(len(os.listdir("../testData/monkeyAndThunder/audioPhrases")) == 41)


def test_extract_prayer():
    print("--- test_extract_prayer")
    ea = AudioExtractor("../testData/prayer/SJQ-2009_Cruz.wav",
                        "../testData/prayer/20150717_Prayer_community_one.eaf",
                        "../testData/prayer/audioPhrases")
    ea.extract(quiet=False)
    assert(len(os.listdir("../testData/prayer/audioPhrases")) == 9)

def test_extract_aktzini():
    print("--- test_extract_aktzini")
    ea = AudioExtractor("../testData/aktzini/18-06-03Aktzini-GA.wav",
                        "../testData/aktzini/18-06-03Aktzini-GA.eaf",
                        "../testData/aktzini/audioPhrases")
    ea.extract(quiet=False)
    assert(len(os.listdir("../testData/aktzini/audioPhrases")) == 16)

def test_extract_plumedSerpent():
    print("--- test_extract_plumedSerpent")
    ea = AudioExtractor("../testData/plumedSerpent/Chicahuaxtla Triqui - La serpiente emplumada 04-28-2016.wav",
                        "../testData/plumedSerpent/TRS Plumed Serpent Legend 05-15-2017.eaf",
                        "../testData/plumedSerpent/audioPhrases")
    ea.extract(quiet=False)
    assert(len(os.listdir("../testData/plumedSerpent/audioPhrases")) == 15)


if __name__ == '__main__':
    runTests()

