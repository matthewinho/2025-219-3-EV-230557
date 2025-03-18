import firebase_admin
 
from firebase_admin import credentials
 
from firebase_admin import db
 
import matplotlib.pyplot as plt
 
import matplotlib.animation as animation
 
cred = credentials.Certificate("lcacc2024-firebase-adminsdk-8bnwo-9b308a3274.json")
 
firebase_admin.initialize_app(cred, {'databaseURL':'https://lcacc2024-default-rtdb.europe-west1.firebasedatabase.app//'})
 
ref = db.reference('/')
 
data = ref.get()
mon = ['months','January','February','March','April','May','June','July','August','September','October','November','December']
xd = 0
 
def get_streams():
 
    ref = db.reference('streams')
 
    streamsdata = ref.get()
 
    return streamsdata
 
streamedhitsongs=get_streams()
 
originalstreams = get_streams()
 
streamedhitsongs.sort()
 
del streamedhitsongs[-1]  #due to excel sheet layout it recieved text for the last item in list , so im just removing it to get the highest value
 
MOSTstreamedhitsong = []
 
MOSTstreamedhitsong.append(streamedhitsongs[-1])
 
 
def get_songnames():
 
    ref = db.reference('track_name')
 
    names = ref.get()
 
    return names
 
allnames = get_songnames()
 
def get_monthrelease():
 
    ref = db.reference('released_month')
 
    monthdata = ref.get()
 
    return monthdata
 
#getting all the months
 
months = ()   
 
allmonth = get_monthrelease()
 
#print(allmonth)
 
countlist =  []
 
inmonthsorted = []
 
 
xy = 0    
 
monthcheck = []
 
checker2 = []
 
songsinmonth = []
 
monthsd = {}
 
for x in range(len(allmonth)):
 

 
    inmonth = allmonth[x]
 
    inmonthsorted.append(inmonth)
 
    inmonthsorted.sort()
 
 
monthlyreleases = {}
 
print(songsinmonth)
 
for v in range(13):
 
    print(mon[v])
 
    myValues = inmonthsorted.count(v)
 
    monthlyreleases[mon[v]] = myValues
 
removed_value = monthlyreleases.pop('months')   # i had it initially due to '0' being the first index
 
print(monthlyreleases)
 
categories = list(monthlyreleases.keys()) #insert year to get data on year
 
values = list(monthlyreleases.values())
 
# Data
 
# Creating bar chart
 
plt.bar(categories, values)
 
# Adding labels and title
 
plt.xlabel('months of year')
 
plt.ylabel('Values')
 
plt.title('Basic Bar Chart')
 
# Displaying chart
 
plt.show()
 
 
#  
 
#     
 
# print('months released for music')
 
# a=  sorted(top3)
 
# a.reverse()
 
# print(a[:3])
 
# #
 
def get_bpm():
 
    ref = db.reference('bpm')
 
    bpmdata = ref.get()
 
    return bpmdata
 
allbpm =  get_bpm()
 
#print(allbpm)
 
totalBPM = sum(allbpm)
 
listedBPM = list(allbpm)
 
lengthBPM = len(listedBPM)
 
AVGbpm = totalBPM/lengthBPM
 
#print(AVGbpm) not rounded
 
roundedBPM = round(AVGbpm,1)
 
print(roundedBPM,"average BPM")
 
 
# Information to use to make a HIT SONG!
 
def get_deezerchart():
 
    ref = db.reference('in_deezer_charts')
 
    deezerCdata = ref.get()
 
    return deezerCdata
 
deezerchart =  get_deezerchart()
 
def get_applechart():
 
    ref = db.reference('in_apple_charts')
 
    appleCdata = ref.get()
 
    return appleCdata
 
applechart=  get_applechart()
 
totalsongsinapplechart = sum(applechart)
 
#print(totalsongsinapplechart)
 
print(len(applechart)) #953 for all
 
def get_spotifychart():
 
    ref = db.reference('in_spotify_charts')
 
    spotCdata = ref.get()
 
    return spotCdata
 
spotifychart=  get_spotifychart()
 
#print(spotifychart)
 
totalsongsinspotchart = sum(spotifychart)
 
#print(totalsongsinspotchart)
 
totaldeezerchart =sum(deezerchart)
 

 
# bing = totalsongsinspotchart+totalsongsinapplechart
#  
# bong = totalsongsinspotchart/bing*100/1
#  
# cong = totalsongsinapplechart/bing*100/1
#  
# zong =totaldeezerchart/bing*100
#  
# #print(bong,"%")
#  
# rounded2 = round(bong,2)
#  
# print(rounded2, "% people that use spotify  in all years mentioned")
#  
# #print(bing,"%")
#  
# rounded3 = round(cong,2)
#  
# print(rounded3,"% that use apple music  in all years mentioned")
#  
# rounded4 = round(zong,2)
#  ENDED UP NOT USING THIS INFORMATION
# print(rounded4,"% that use deezer in all years mentioned")
def get_years():
 
    ref = db.reference('released_year')
 
    yeardata = ref.get()
 
    #print('Year data is:')
 
    #print(yeardata)
 
    return yeardata
 
testing = []
 
allyears =  get_years()
 
#print(allyears)
 
count  = allyears[0]
 
x= 0
 
z = 0
 
#streamedhitsongs
 
checker= []
 
songsinyear = []
 
deezercount = []
 

 
storage  = dict({})
 
while x < len(allyears):
 
     cc = allyears[x]
 
     dd =originalstreams[x]
     storage[dd] = cc
 
 
 
     specificyear = allyears.count(cc)
 
     # i did not want the numbers to repeat, so i did adjustments.
 
     if specificyear not in songsinyear:
 
         songsinyear.append(specificyear)
 
     if cc not in checker:
 
         checker.append(cc)
 
     deezercount = deezerchart[x]
 
     #namescount = allnames[x]
 
     spotcount = spotifychart[x]
 
 
     x = x + 1
 
 
 
accelerator =0
 
total_sum = dict({})
 
for i in range (len(checker)):
     yearstreams = []
     for j in range(953):
         a= checker[i]
         if allyears[j] == a:
            try:yearstreams.append(int(originalstreams[j]))
            except:pass
     
     total_sum[a]  = sum(yearstreams)
#print(total_sum)
 
 
y = 0
 
mYearRELEASE = dict({})
 
while y < len(checker):
 
    count2 = checker[y]
 
    Mreleasedinyears = allyears.count(count2)
 
    y = y +1
 
    infoyears = count2,Mreleasedinyears
 
    #print(count2,Mreleasedinyears)
 
    mYearRELEASE[count2] = Mreleasedinyears
 
print(mYearRELEASE)
 
print(len(checker))

 
# THE MODE OF THE AMOUNT OF MUSIC RELEASED IN A YEAR
 
months = list(mYearRELEASE.keys())
 
#change month labels to year
 
values = list(mYearRELEASE.values())
 
months_str =[]
 
for i in months:
 
    months_str.append(str(i))
 
print(months_str)
 
fig, ax = plt.subplots()
 
ax.plot(months_str, values)
 
ax.set(xlabel='Years (s)', ylabel='music released', title = "songs released in year [frequency]")
 
ax.tick_params(axis='x', labelrotation=45)
 
plt.show()
 
# Creating the plot
#d = 0
 
#piechart
 
spotify = dict({})
 
applep = dict({})
 
deezerp = dict({})
 
for d in range(len(allyears)):
 
    A = allyears[d]
 
    spotinfo = spotifychart[d]
 
    deezercount = deezerchart[d]
 
    applecount = applechart[d]
 
             #print(A,spotinfo)
 
    if A not in spotify:
 
        spotify[A] = spotinfo
 
    else:
 
        spotify[A] = spotify[A]+ spotinfo
 
       #deezer          
 
    if A not in deezerp:
 
        deezerp[A] = deezercount
 
    else:
 
        deezerp[A] = deezerp[A]+ deezercount
 
    if A not in applep:
 
        applep[A] = applecount
 
    else:
 
        applep[A] = applep[A]+ applecount
 
#print(applep)
 
#print(deezerp)     
 
#print(spotify)
 
#print(spotify[2023])
 
averagesByYear = {}
 
for d in range(len(allyears)):
 
    A = allyears[d]
 
    totalForYear = spotify[A] +deezerp[A] +applep[A]
 
    if totalForYear>0.0:
 
        roundeddeezer = round(deezerp[A]/totalForYear*100/1,2)
 
        roundedspotify = round(spotify[A]/totalForYear*100/1,2)
 
        roundedapple = round(applep[A]/totalForYear*100/1,2)
 
        averagesByYear[A] ={'spotify':roundedspotify,'deezer':roundeddeezer,'apple':roundedapple,}
 
        #answer = averageByYear * 100/1
 
#print(averagesByYear)
#roundedBPM = round(AVGbpm,1)
 
# Extract labels and values
 
labels = list(averagesByYear[2016].keys()) #insert year to get data on year
 
sizes = list(averagesByYear[2016].values())
ax.set(xlabel='music platforms', ylabel='music released', title = "songgs released in year [frequency]") 
print(labels)
 
# Plot the pie chart
plt.title('Pie Chart showing , which music apps positively affect hitsongs from certain years [2016]')
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
 
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

 

plt.show()
 
print('sending to firebase')
 
ref = db.reference('/music_app_interaction')
 
ref.set(averagesByYear)
 
ref = db.reference('/music_yearly_release')
 
ref.set(mYearRELEASE)
 
ref = db.reference("/monthly_hitsong_release")
 
ref.set(monthlyreleases)
 
ref = db.reference('/averageBPM')
 
ref.set(roundedBPM)
 
ref = db.reference('/higheststreamsong')
 
ref.set(MOSTstreamedhitsong)
 
ref = db.reference('streamsperyeartotal')
ref.set(total_sum)
 
