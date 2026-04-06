import platform
import psutil

soft_info = platform.uname()
distro = platform.freedesktop_os_release()
spacer_total = psutil.disk_usage("/").total/(1024**3)
spacer_used = psutil.disk_usage("/").used/(1024**3)
spaceh_total = psutil.disk_usage("/home").total/(1024**3)
spaceh_used = psutil.disk_usage("/home").used/(1024**3)
ram_total = psutil.virtual_memory().total/(1024**3)
ram_used = psutil.virtual_memory().used/(1024**3)

print(f"Distro > {distro["PRETTY_NAME"]} {soft_info.machine}")
print(f"Kernel > {soft_info.system} {soft_info.release}")
print(f"Rootdisk > {spacer_used:.2f} GiB / {spacer_total:.2f} GiB")
print(f"Homedisk > {spaceh_used:.2f} GiB / {spaceh_total:.2f} GiB")
print(f"RAM > {ram_used:.2f} GiB / {ram_total:.2f} GiB")
