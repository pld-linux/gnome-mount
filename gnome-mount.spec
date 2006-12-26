Summary:	Programs for mounting, unmounting and ejecting storage devices
Summary(pl):	Programy do montowania, odmontowywania i wysuwania urz±dzeñ do przechowywania danych
Name:		gnome-mount
Version:	0.5
Release:	1
License:	GPL v.2
Group:		Applications
Source0:	http://freedesktop.org/~david/dist/%{name}-%{version}.tar.gz
# Source0-md5:	76622ff9af0131fc44687aed7204f84f
Patch0:		%{name}-shortname.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	gnome-keyring-devel >= 0.5.1
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	hal-devel >= 0.5.8.1
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.16.0
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	nautilus >= 2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Programs for mounting, unmounting and ejecting storage devices.

%description -l pl
Programy do montowania, odmontowywania i wysuwania urz±dzeñ do
przechowywania danych.

%package devel
Summary:	gnome-mount development files
Summary(pl):	Pliki programistyczne gnome-mount
Group:		Development
Requires:	pkgconfig

%description devel
This is the package containing gnome-mount development files.

%description devel -l pl
Ten pakiet zawiera pliki programistyczne gnome-mount.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nautilus-extension
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-mount.schemas

%preun
%gconf_schema_uninstall gnome-mount.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/gnome-mount.schemas

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
