from rest_framework import throttling

class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        'anon':'10000/day'
    }

class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        'user':'10000/day'
    }