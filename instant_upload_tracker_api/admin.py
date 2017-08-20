from django.contrib import admin

# Register your models here.

from .models import IuBugTracker, IuDeviceInfoTracker, IuPerfTracker

class IuPerfTrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'vender_id', 'device_id', 'serial', 'android_user_unique_id', 'lib_version', 'filesize', 'cost_ts')
    search_fields = ('id', 'vender_id', 'device_id', 'serial', 'android_user_unique_id', 'lib_version',)
    list_filter = ('device_id', 'serial', 'android_user_unique_id', 'lib_version')

class IuBugTrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'vender_id', 'device_id', 'serial', 'android_user_unique_id', 'lib_version', 'exception')
    search_fields = ('id', 'vender_id', 'device_id', 'serial', 'android_user_unique_id', 'lib_version', )
    list_filter = ('device_id', 'serial', 'android_user_unique_id', 'lib_version')

class IuDeviceInfoTrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'vender_id', 'device_id', 'serial', 'android_user_unique_id' )
    search_fields = ('id', 'vender_id', 'device_id', 'serial', 'android_user_unique_id' )
    list_filter = ('device_id', 'serial', 'android_user_unique_id', 'lib_version')



admin.site.register(IuPerfTracker, IuPerfTrackerAdmin)
admin.site.register(IuBugTracker, IuBugTrackerAdmin)
admin.site.register(IuDeviceInfoTracker, IuDeviceInfoTrackerAdmin)