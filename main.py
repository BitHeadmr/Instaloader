#To install instaloader
pip3 install instaloader

instaloader [--comments] [--geotags]
            [--stories] [--highlights] [--tagged] [--igtv]
            [--login YOUR-USERNAME] [--fast-update]
            profile | "#hashtag" | :stories | :feed | :saved


#To download all pictures and videos of a profile, as well as the profile picture, do
instaloader profile [profile ...]

#To later update your local copy of that profiles, you may run
instaloader --fast-update profile [profile ...]

#Instaloader can also be used to download private profiles. To do so, invoke it with
instaloader --login=your_username profile [profile ...]