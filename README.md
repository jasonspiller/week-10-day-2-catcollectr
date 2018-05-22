# week-10-day-2-catcollectr

Typo:

5. Now we will map this particular view to a url. We want to use the route /index for now as an example. Lets add a url for our view in the url dispatcher file in CatCollector/CatCollectr/urls.py:

urlpatterns = [
	path('admin/', admin.site.urls),
	# add the line below to your urlpatterns array
	path('**index/**', views.index)
]
