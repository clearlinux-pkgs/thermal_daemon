#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thermal_daemon
Version  : 1.8
Release  : 21
URL      : https://github.com/intel/thermal_daemon/archive/v1.8.tar.gz
Source0  : https://github.com/intel/thermal_daemon/archive/v1.8.tar.gz
Summary  : The "Linux Thermal Daemon" program from 01.org
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0
Requires: thermal_daemon-bin
Requires: thermal_daemon-autostart
Requires: thermal_daemon-config
Requires: thermal_daemon-data
Requires: thermal_daemon-license
Requires: thermal_daemon-man
BuildRequires : buildreq-qmake
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev
Patch1: 0001-start-the-service-if-battery-exists.patch

%description
Thermal Daemon monitors and controls platform temperature.

%package autostart
Summary: autostart components for the thermal_daemon package.
Group: Default

%description autostart
autostart components for the thermal_daemon package.


%package bin
Summary: bin components for the thermal_daemon package.
Group: Binaries
Requires: thermal_daemon-data
Requires: thermal_daemon-config
Requires: thermal_daemon-license
Requires: thermal_daemon-man

%description bin
bin components for the thermal_daemon package.


%package config
Summary: config components for the thermal_daemon package.
Group: Default

%description config
config components for the thermal_daemon package.


%package data
Summary: data components for the thermal_daemon package.
Group: Data

%description data
data components for the thermal_daemon package.


%package license
Summary: license components for the thermal_daemon package.
Group: Default

%description license
license components for the thermal_daemon package.


%package man
Summary: man components for the thermal_daemon package.
Group: Default

%description man
man components for the thermal_daemon package.


%prep
%setup -q -n thermal_daemon-1.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536793463
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536793463
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/thermal_daemon
cp COPYING %{buildroot}/usr/share/doc/thermal_daemon/COPYING
cp tools/thermal_monitor/qcustomplot/GPL.txt %{buildroot}/usr/share/doc/thermal_daemon/tools_thermal_monitor_qcustomplot_GPL.txt
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d
install -p -D -m 644 data/org.freedesktop.thermald.conf %{buildroot}/usr/share/dbus-1/system.d/org.freedesktop.thermald.conf
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sf ../thermald.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/thermald.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/thermald.service

%files bin
%defattr(-,root,root,-)
/usr/bin/thermald

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/thermald.service
/usr/lib/systemd/system/thermald.service

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.freedesktop.thermald.service
/usr/share/dbus-1/system.d/org.freedesktop.thermald.conf

%files license
%defattr(-,root,root,-)
/usr/share/doc/thermal_daemon/COPYING
/usr/share/doc/thermal_daemon/tools_thermal_monitor_qcustomplot_GPL.txt

%files man
%defattr(-,root,root,-)
/usr/share/man/man5/thermal-conf.xml.5
/usr/share/man/man8/thermald.8
