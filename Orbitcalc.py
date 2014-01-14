import ephem
import math
import datetime
import unittest

ENCODING='utf-8'

degreeconv=180/math.pi
#
home = ephem.Observer()
home.lat='43.134694'
home.lon='141.248194'
home.elev=50
#home.lat='43.066438'
#home.lon='141.300925'

#home.lat='43.579953888889'
#home.lon='141.998324722222'
#1 25544U 98067A   12366.89848378  .00006715  00000-0  11734-3 0  9373
#2 25544  51.6460 219.3718 0016515 109.6991  15.4155 15.51833175808723
#calctime_utc=datetime.datetime(2013,11,23,0,0)
calctime_utc=datetime.datetime.now()
satresult=[]

class Orbitcalc(object):
    _gslat = ''
    _gslon = ''
    _gselev = ''
    _satname = ''
    _tle1 = ''
    _tle2 = ''
    _frequency = ''
    _mode = ''
    def __init__(self,gslat,gslon,gselev):
        self._gslat = str(gslat)
        self._gslon = str(gslon)
        self._gselev = str(gselev)

    def SatInfo(self,satname,tle1,tle2,frequency,mode):
        self._satname=str(satname)
        self._tle1=str(tle1)
        self._tle2=str(tle2)
        self._frequency=str(frequency)
        self._mode=str(mode)

    def dopplershift(self, c, rangerate):
        #return math.sqrt(1-(V/c)**2)/(1-(V/c)*math.cos(theta))
        #http://stackoverflow.com/questions/18763484/wrong-range-rate-with-pyephem
        return (c/(c + rangerate))

    def CalcObserve(self):
        home = ephem.Observer()
        home.lat = self._gslat
        home.lon = self._gslon
        home.elev = int(self._gselev)
        sat = ephem.readtle(self._satname, self._tle1, self._tle2)
        sat.compute(home)
        sataz = math.degrees(sat.az)
        satalt = math.degrees(sat.alt)
        c = 299792458
        satfreq = float(self._frequency) * self.dopplershift(c,sat.range_velocity/1000)
        return sataz, satalt, satfreq



#def CalcPass(sat_num,tle1,tle2,epoch_utc):
#    home=ephem.Observer()
#    home.lat='43.131'
#    home.lon='141.253'
#    home.elev=69
#    home.date=epoch_utc
#    sattle=ephem.readtle('sat',tle1,tle2)
#    sattle.compute(home)
#    risetime=ephem.localtime(sattle.rise_time)
#    settime=ephem.localtime(sattle.set_time)
#    return sat_num,risetime,settime,math.degrees(sattle.transit_alt)
#
#def CalcPasses(sat_num,tle1,tle2,epoch_utc,delta):
#    resultlist=[]
#    inputtime_utc=epoch_utc
#    end_jst=epoch_utc+timedelta(minutes=delta)+timedelta(hours=9)
#    result=CalcPass(sat_num,tle1,tle2,inputtime_utc)
#    if(result[1]>result[2]):
#        inputtime_utc=result[2]
#    while(True):
#        result=CalcPass(sat_num,tle1,tle2,inputtime_utc)
#	print result[1],result[3],result[2]
#        if(result[1]<end_jst):
#            resultlist.append(result)
#            inputtime_utc=result[2]+timedelta(seconds=5)-timedelta(hours=9)
#        else:
#	    print "----------------------------------------------------"
#            break
#    return resultlist
class testOrbitCalc(unittest.TestCase):

    def testOrbitcalc(self):
        orbitinfo = Orbitcalc(gslat='43',gslon='141',gselev='50')
        orbitinfo.SatInfo('iss',
                      '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
                      '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
                      '437.234','FM')
        satlat,satlon,satfreq = orbitinfo.CalcObserve()
        print satlat
        print satlon
        print satfreq

    def testinputparamcheck(self):
        orbitinfo = Orbitcalc(gslat=43,gslon=141,gselev=50)
        orbitinfo.SatInfo('iss',
                      '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
                      '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
                      437.234,'FM')
        satlat,satlon,satfreq = orbitinfo.CalcObserve()
        print satlat
        print satlon
        print satfreq

if __name__=="__main__":
    print calctime_utc
    unittest.main()

    #CalcPasses('',
    #            '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
    #            '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
    #            calctime_utc,1300)
    #if(sys.argv[1].split('.')[1]=='txt'):
    #    f = open(sys.argv[1],'r')
    #    tle1 = ''
    #    tle2 = ''
    #    raw = ''
    #    for raw in f:
    #        if(raw.startswith('1 ') ==True):
    #            tle1 = raw
    #        if(raw.startswith('2 ') ==True):
    #            tle2 = raw
    #    CalcPasses('',tle1,tle2,calctime_utc,1000)
    #else:
    #   CalcPasses('',
    #               '1 99999U          13323.51230604  .00000000  00000-0  00000-0 0 00001',
    #               '2 99999 051.5826 058.9447 0003029 020.0291 190.6000 15.51011028000098',
    #               calctime_utc,1300)
