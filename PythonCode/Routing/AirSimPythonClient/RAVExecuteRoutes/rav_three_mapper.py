
from AirSimClient import *
import time

# connect to the AirSim simulator
client = MultirotorClient(port=41454)
#client1 = MultirotorClient(port=41452)
client.confirmConnection()
print('Seem to be connected...')
client.enableApiControl(True)
#client.armDisarm(True)
#client1.enableApiControl(True)
#client1.armDisarm(True)

state = client.getGpsLocation()
#s = pprint.pformat(state)
print("state: %s" % state)

print('Taking off...')
client.takeoff()
print('moving to first location')
i = ''
while i!='m':
	i = input("Type 'm' to begin mapping the environment")
print('Moving clear of tree line')
client.moveToPosition(client.getPosition().x_val, client.getPosition().y_val, client.getPosition().z_val-30, 3)
print('Client position: {}'.format(client.getPosition()))


client.moveToGPSPosition(GPSCoordinate(53.282, -9.052, 50), 6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28021443763637, -9.057533053890909, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28006243978182,  -9.057393670804545, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27996362880909,  -9.057695074313637, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27981163095455,  -9.057555691227273, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.2796596331,  -9.05741630814091, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27950763524546,  -9.057276925054547, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27935563739091,  -9.057137541968181, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27920363953636,  -9.056998158881818, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27905164168182,  -9.056858775795455, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.278952830709095,  -9.057160179304544, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27910482856364,  -9.057299562390908, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.279256826418184,  -9.057438945477271, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.279408824272736,  -9.057578328563636, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27956082212728,  -9.05771771165, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.279712819981825,  -9.057857094736363, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.27986481783637,  -9.057996477822726, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280016815690914,  -9.05813586090909, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28016881354546,  -9.058275243995453, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.2803208114,  -9.058414627081817, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280472809254555,  -9.05855401016818, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.2806248071091,  -9.058693393254545, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280776804963644,  -9.058832776340909, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28092880281819,  -9.058972159427272, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28108080067273,  -9.059111542513635, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28123279852728,  -9.059250925599999, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28138479638182,  -9.059390308686362, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28153679423637,  -9.059529691772726, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28168879209092,  -9.059669074859091, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28184078994546,  -9.059808457945454, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28199278780001,  -9.059947841031818, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28214478565455,  -9.060087224118181, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.282243596627275,  -9.059785820609092, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28209159877273,  -9.059646437522728, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.281939600918186,  -9.059507054436365, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28178760306364,  -9.059367671350001, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28163560520909,  -9.059228288263636, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.281483607354545,  -9.059088905177273, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.2813316095,  -9.05894952209091, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.281179611645456,  -9.058810139004546, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28102761379091,  -9.058670755918182, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28087561593637,  -9.058531372831819, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28072361808182,  -9.058391989745456, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28057162022728,  -9.05825260665909, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280419622372726,  -9.058113223572727, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28026762451818,  -9.057973840486364, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28011562666364,  -9.0578344574, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28036643549091,  -9.057672436977272, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280518433345456,  -9.057811820063636, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28067043120001,  -9.05795120315, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28082242905455,  -9.058090586236364, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.2809744269091,  -9.058229969322728, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28112642476364,  -9.058369352409091, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.281278422618186,  -9.058508735495455, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28143042047273,  -9.058648118581818, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.281582418327275,  -9.058787501668181, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28173441618182,  -9.058926884754545, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28188641403637,  -9.05906626784091, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.282038411890916,  -9.059205650927273, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28219040974546,  -9.059345034013637, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.282342407600005,  -9.0594844171, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28135429787273,  -9.062498452190908, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28120230001819,  -9.062359069104545, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28105030216364,  -9.062219686018182, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.2808983043091,  -9.062080302931818, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280746306454546,  -9.061940919845453, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.280647495481816,  -9.062242323354544, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28079949333637,  -9.06238170644091, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28095149119091,  -9.062521089527273, 50),6)
time.sleep(1)
client.moveToGPSPosition(GPSCoordinate(53.28110348904546,  -9.062660472613636, 50),6)
time.sleep(1)