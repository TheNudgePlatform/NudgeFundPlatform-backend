from django.contrib import admin
from microfinance.models import *

# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Student)
admin.site.register(Gurukul)
admin.site.register(SponsorTransactionHistory)
admin.site.register(SponsorFundHistory)
admin.site.register(SponsorWallet)
