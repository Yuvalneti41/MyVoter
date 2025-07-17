from django.db import models
from django.contrib.auth.models import User




class Politikai(models.Model):
    profile_picture = models.ImageField(upload_to='govener_profile_pics/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    country_of_origin = models.CharField(max_length=50)
    biography = models.TextField(max_length=1000)
    
    political_party = models.CharField(max_length=100)
    political_past = models.TextField(max_length=1000)
    political_opinion = models.TextField(max_length=1000)
    
    millitery_rank = models.CharField(max_length=100)
    millitery_past = models.TextField(max_length=500)

    education = models.TextField(max_length=500)
    career = models.CharField(max_length=100)

    def __str__(self):
        return f"politikai: {self.first_name + ' ' + self.last_name}"
    



class Goverment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    party_leader = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_leader')
    party_ceo_or_secretary_general = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_ceo_or_secretary_general')
    party_spokesperson = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_spokesperson')
    treasurer_or_finance_manager = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='treasurer_or_finance_manager')
    strategic_advisor_or_campaign_manager = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='strategic_advisor_or_campaign_manager')
    regional_activists_or_branch_leaders = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='regional_activists_or_branch_leaders')
    party_member_one = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_one', null=True, blank=True)
    party_member_two = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_two', null=True, blank=True)
    party_member_three = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_three', null=True, blank=True)
    party_member_four = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_four', null=True, blank=True)
    party_member_five = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_five', null=True, blank=True)
    party_member_six = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_six', null=True, blank=True)
    party_member_seven = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_seven', null=True, blank=True)
    party_member_eight = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_eight', null=True, blank=True)
    party_member_nine = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_nine', null=True, blank=True)
    party_member_ten = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_ten', null=True, blank=True)
    party_member_eleven = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_eleven', null=True, blank=True)
    party_member_twelve = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_twelve', null=True, blank=True)
    party_member_thirteen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_thirteen', null=True, blank=True)
    party_member_fourteen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_fourteen', null=True, blank=True)
    party_member_fifteen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_fifteen', null=True, blank=True)
    party_member_sixteen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_sixteen', null=True, blank=True)
    party_member_seventeen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_seventeen', null=True, blank=True)
    party_member_eighteen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_eighteen', null=True, blank=True)
    party_member_nineteen = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_nineteen', null=True, blank=True)
    party_member_twenty = models.ForeignKey(Politikai, on_delete=models.CASCADE, related_name='party_member_twenty', null=True, blank=True)

    def __str__(self):
        return f"Custom Goverment by: {self.user.first_name} {self.user.last_name}"
