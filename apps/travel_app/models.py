from django.db import models
from ..user_app.models import User
from datetime import date




class TravelManager(models.Manager):
    def add_trip(self, trips, userID):
        response={}
        errors=[]
        if Travel.objects.filter(destination  = trips['destination']):
            errors.append("Sorry that destination already exists please add from other user's table")
        if trips['destination'] =="" or  trips['description']=="" or trips['travel_date_from'] =="" or trips['travel_date_to'] =="" :
            errors.append("One or the more fields are empty! All fields should be filled out!")
        if trips['travel_date_from'] <= str(date.today()):
            errors.append("Travel date cannot be from past")
        if trips['travel_date_from'] > trips['travel_date_to']:
            errors.append(" 'Travel Date To' should not be before the 'Travel Date From'!")
        if errors:
            response['status'] = False
            response['errors'] = errors
        else:
            response['status']=True
            response['travels'] = Travel.objects.create(destination=trips['destination'], my_plan=User.objects.get(id = userID), description = trips['description'], start_date = trips['travel_date_from'], end_date = trips['travel_date_to'])
            response['travels'].your_plan.add(User.objects.get(id = userID))
        return response

    def trip_detail(self, UserID):
        return self.get(id = UserID)


class Travel(models.Model):
    destination= models.CharField(max_length =225)
    my_plan= models.ForeignKey(User, related_name="my")
    your_plan=models.ManyToManyField(User, related_name="yours")
    description = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = TravelManager()
