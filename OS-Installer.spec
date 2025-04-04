%undefine _debugsource_packages
Name:           os-installer
Version:        0.4.3
Release:        1
Group:          System/Configuration/Other
Summary:        A generic OS-Installer that can be customized by distributions
License:        GPL-3.0
URL:            https://gitlab.gnome.org/p3732/os-installer/
Source0:        https://gitlab.gnome.org/p3732/os-installer/-/archive/%{version}/os-installer-%{version}.tar.bz2

BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gweather4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(vte-2.91-gtk4)
BuildRequires: python-gi
BuildRequires: python-gobject3
BuildRequires: gettext

Requires: gtk4
Requires: gnome-disk-utility
Requires: gnome-control-center
Requires: systemd


#epiphany

%description
A simple operating system installer, intended to be used with live install systems.
Provides bootstrapping through language, keyboard, internet connection and disk selection.
Allows defining of optional additional software to be installed.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/os-installer
%{_datadir}/appdata/com.github.p3732.OS-Installer.appdata.xml
%{_datadir}/applications/com.github.p3732.OS-Installer.desktop
%{_datadir}/glib-2.0/schemas/com.github.p3732.OS-Installer.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.p3732.OS-Installer.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.p3732.OS-Installer-symbolic.svg
%{_datadir}/os-installer/
