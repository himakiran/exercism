from datetime import timedelta, datetime
def add(moment):
    OneGigaSec = timedelta(seconds=10**9)
    print(moment)
    return moment + OneGigaSec
