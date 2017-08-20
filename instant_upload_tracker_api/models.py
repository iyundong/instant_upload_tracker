from django.db import models

# Create your models here.


class IuPerfTracker(models.Model):

    id = models.IntegerField(primary_key=True),
    vender_id = models.IntegerField(verbose_name="厂商id")
    device_id = models.IntegerField(verbose_name="设备id")
    serial = models.CharField(max_length=255, verbose_name="设备串号")
    android_device_unique_id = models.CharField(max_length=255, verbose_name="安卓设备唯一编号")
    android_user_unique_id = models.IntegerField(verbose_name="使用用户的唯一id编号")
    android_device_info = models.CharField(max_length=255, verbose_name="Build.BRAND + Build.DEVICE + Build.MODEL")
    android_os_ver = models.IntegerField(verbose_name="操作系统版本")
    lib_version = models.IntegerField(verbose_name="所使用的库的版本")
    sync_trigger_mode = models.IntegerField(verbose_name="所使用的同步触发模式")
    sync_mode = models.IntegerField(verbose_name="同步模式")
    sync_record_mode = models.IntegerField(verbose_name="同步记录模式")
    filesize = models.IntegerField(verbose_name="传输文件尺寸")
    start_ts = models.FloatField(verbose_name="开始时间")
    end_ts = models.FloatField(verbose_name="结束时间")
    cost_ts = models.FloatField(verbose_name="消耗时间")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


class IuBugTracker(models.Model):

    id = models.IntegerField(primary_key=True)
    vender_id = models.IntegerField(verbose_name="厂商id")
    device_id = models.IntegerField(verbose_name="设备id")
    serial = models.CharField(max_length=255, verbose_name="设备串号")
    android_device_unique_id = models.CharField(max_length=255, verbose_name="安卓设备唯一编号")
    android_user_unique_id = models.IntegerField(verbose_name="使用用户的唯一id编号")
    android_device_info = models.IntegerField(verbose_name="Build.BRAND + Build.DEVICE + Build.MODEL")
    android_os_ver = models.IntegerField(verbose_name="操作系统版本")
    lib_version = models.IntegerField(verbose_name="所使用的库的版本")
    sync_trigger_mode = models.IntegerField(verbose_name="所使用的同步触发模式", null=True)
    sync_mode = models.IntegerField(verbose_name="同步模式", null=True)
    sync_record_mode = models.IntegerField(verbose_name="同步记录模式", null=True)
    exception = models.TextField(verbose_name="异常名称", null=True)
    traceback = models.TextField(verbose_name="调用堆栈", null=True)
    fileinfo = models.TextField(verbose_name="文件信息", null=True)
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

class IuDeviceInfoTracker(models.Model):

    id = models.IntegerField(primary_key=True)
    vender_id = models.IntegerField(verbose_name="厂商id")
    device_id = models.IntegerField(verbose_name="设备id")
    serial = models.CharField(max_length=255, verbose_name="设备串号")
    android_device_unique_id = models.CharField(max_length=255, verbose_name="安卓设备唯一编号")
    android_user_unique_id = models.IntegerField(verbose_name="使用用户的唯一id编号")
    android_device_info = models.IntegerField(verbose_name="Build.BRAND + Build.DEVICE + Build.MODEL")
    android_os_ver = models.IntegerField(verbose_name="操作系统版本")
    lib_version = models.IntegerField(verbose_name="所使用的库的版本")
    device_info = models.TextField(verbose_name="设备信息")
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
