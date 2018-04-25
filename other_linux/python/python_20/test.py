import twitter

# The first step is to connect to Twitter
api1 = twitter.Api(consumer_key='oyNhFvOosuzvwP0ssfZHayiht',
                   consumer_secret='9Tj4EJ9SZcwgU2ZbkONBiW4hCRwZk3G1ZQ1zl3FROxVjf7OhrX',
                   access_token_key='10035252-RnJ22SWKp4kZwm1TR2HZ3kkW2D9Gv53l68YYifY7S',
                   access_token_secret='bTXQtzNH4L1fY605xsx9lABHdtgHmpJMCj3MMTwBlPux6')

# You can post status updates
update_status = api1.PostUpdate('I am now connected!')

# You can geotag updates with lat/long
update_status = api1.PostUpdate('I am here...', latitude=45.949874, longitude=-66.642347)

