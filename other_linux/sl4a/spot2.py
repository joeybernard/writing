import android, time

droid = android.Android()
droid.startLocating()
loc = {}
while loc == {}:
   time.sleep(15)
   loc = droid.readLocation().result
   try:
      locgps = loc['gps']
   except:
      loc = {}
lat = locgps['latitude']
long = locgps['longitude']
droid.stopLocating()

droid.smsSend('506-555-1234', 'lat: ' + str(lat) + '\n long: ' + str(long))
