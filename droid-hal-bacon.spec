# These and other macros are documented in dhd/droid-hal-device.inc
%define device bacon
%define vendor oneplus
%define vendor_pretty OnePlus
%define device_pretty One
%define installable_zip 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
