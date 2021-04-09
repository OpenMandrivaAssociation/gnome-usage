%define url_ver	%%(echo %{version}|cut -d. -f1,2)

Name:		gnome-usage
Version:	3.38.1
Release:	2
Summary:	A GNOME app to view information about use of system resources
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Usage
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(accountsservice)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  tracker-vala


%description
gnome-usage lets you easily visualize the use of system resources such as
CPU, memory, and storage.

%prep
%setup -q

%build
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
%{_datadir}/metainfo/org.gnome.Usage.appdata.xml
