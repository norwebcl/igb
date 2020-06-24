from instapy import InstaPy

session = InstaPy(username=".cl", password="")
session.login()
session.like_by_tags(["arica", "iquique", "calama"], amount=50)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Excelente!", "Muy bien!", "Saludos :heart_eyes:"])
session.end()
