from django.contrib import admin
from .models import Profile, Post, LikePost, FollowUnFollow, Comment, Message, EmailVerification

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowUnFollow)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(EmailVerification)