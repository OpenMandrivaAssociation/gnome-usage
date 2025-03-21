%define url_ver	%%(echo %{version}|cut -d. -f1,2)

Name:		gnome-usage
Version:	48.rc
Release:	1
Summary:	A GNOME app to view information about use of system resources
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Usage
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(tinysparql-3.0)
BuildRequires:  tinysparql-vala


%description
gnome-usage lets you easily visualize the use of system resources such as
CPU, memory, and storage.

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS README.md NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Usage.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Usage.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Usage.svg
%{_datadir}/metainfo/org.gnome.Usage.metainfo.xml
