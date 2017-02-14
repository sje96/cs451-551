import arrow

n = arrow.utcnow()
expected = arrow.get("9/8/2017 4:00", "D/M/YYYY H:m")

if n > expected:
    print("Date Missed and you in some trouble.")
else:
    print("Date not missed looking good.")