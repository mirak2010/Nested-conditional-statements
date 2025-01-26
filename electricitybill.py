ec=int(input("Please enter the units spend: "))
if ec<50:
    print((ec*2.6)+25)
elif 50<ec<100:
    print((ec*3.25)+35)
elif 100<ec<200:
    print((ec*5.26)+45)
elif ec>200:
    print((ec*8.45)+75)