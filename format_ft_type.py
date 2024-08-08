#the current unix time

timestamp= time.time()

#Format the current data in the desired format
current_time=time.strftime(%b %d %Y, time.localtime(timestamp))
#print the results
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or", f"{timestamp:.2e} in scientific notation")
print(current_time)
