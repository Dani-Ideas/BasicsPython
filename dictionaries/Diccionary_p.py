alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
print(f"alien_0 Data:{alien_0}")
alien_0['positionX']=0
alien_0['planet']="mars"
print(f"alien_0 Data:{alien_0}")
alien_1 = {}
print(f"alien_1 start empty:{alien_1}")
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['planet'] ='jupiter'
print(f"alien_1:{alien_1}")
print("Modifying Values in a Dictionary")
print(f"alien_0 is {alien_0['color']}, but now", end=' ')
alien_0['color']="red"
print(f"it's {alien_0['color']}.")
print(f"*-*-*-*-*-*-*-*-*-*-*\nalien 1 now be in {alien_1['planet']}, ", end=' ')
if alien_1['planet']== 'terra' and alien_0['planet']== 'terra':
    alien_1['planet']='mars'
elif alien_1['planet']== 'mars' and alien_0['planet']== 'mars':
    alien_1['planet']='jupiter'
elif alien_1['planet']== 'jupiter' and alien_0['planet']== 'jupiter':
    alien_1['planet']='terra'
else :
    alien_1['planet']='saturn'
print(f" them choose go to {alien_1['planet']}")
print("oh but it's a trap he lost all points,", end=' ')
del alien_1['points']
print(alien_1)
print("/-/-/-/-/-/-/-/-/-\n/-/-/-/-/-/-/-/-/-/-/-/-/\n/-/-/-/-/-/-/-/-/-/-/-/")
#dictionary like a Object
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends =['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")