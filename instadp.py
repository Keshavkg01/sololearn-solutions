import instaloader
i=instaloader.Instaloader()
dp=input('enter insta username:  ')
i.download_profile(dp,profile_pic_only=True)