# ---  ads data ---
tracking_stats = {
  "Christian church Ad": {
    "data": [],
    "average_visioning_time": 0, 
  }, 
  "Honda Car Ad": {
    "data": [],
    "average_visioning_time": 0, 
  },
  "Kinder Bueno Ad": {
    "data": [], 
    "average_visioning_time": 0, 
  } 
}

# --- user data ---
user_samples = [
  {"user1": { "watchtime": { 
      "Christian church": 12,  
      "Honda Car": 6,  
      "Kinder Bueno": 9,
  }}}, 
  {"user2": { "watchtime": {
      "Christian church": 1, 
      "Honda Car": 2, 
      "Kinder Bueno": 3,
  }}},
  {"user3": { "watchtime": {
      "Christian church": 4, 
      "Honda Car": 20, 
      "Kinder Bueno": 1,
  }}},
]

# --- returns the sum of all elements in an array """
def array_sum(array):
    total = 0
    for item in array:
        total += item
    return total 

# --- fills ads data objects with each user's average watching time"""
def watch_time(ad, user):
    if ad in tracking_stats:
        tracking_stats[ad]["data"].append(user["watchtime"][ad])
    return tracking_stats

# --- computes the average watching time for each add using user's respective data """
def average_calc():
    for key, value in tracking_stats.items():
        if len(tracking_stats[key]["data"]) > 0:
            average_time = array_sum(tracking_stats[key]["data"]) / len(tracking_stats[key]["data"])
            tracking_stats[key]["average_visioning_time"] = average_time

# --- goes through every data object average time and returns the ad with the most average watched time """
def find_most_popular_ad():
    most_popular_ad = None
    highest_avg = -1
    for key, value in tracking_stats.items(): 
        if tracking_stats[key]["average_visioning_time"] > highest_avg:
            highest_avg = tracking_stats[key]["average_visioning_time"]
            most_popular_ad = key
    return most_popular_ad, highest_avg

# --- Remplissage des données ---
for user in user_samples:
    for username, userdata in user.items():
        for ad in userdata["watchtime"]:
            watch_time(ad, userdata)

# --- result ---
average_calc()
print("Most popular ad:", find_most_popular_ad())
