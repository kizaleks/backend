from django.contrib import admin
from .models import Counterparty, Profile

# class AdvertisementAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Advertisement
#         fields = '__all__'
# class AdvertisementAdmin(admin.ModelAdmin):
#     form = AdvertisementAdminForm

class UserAdmin(admin.ModelAdmin):

    list_display = ('user','сategory','company')
    list_filter = ('user','сategory','company')
    search_fields = ('user','сategory','company')




admin.site.register(Counterparty,)
admin.site.register(Profile,UserAdmin)

