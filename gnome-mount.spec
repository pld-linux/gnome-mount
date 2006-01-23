%define		snap	20060122
Summary:	Programs for mounting, unmounting and ejecting storage devices
Name:		gnome-mount
Version:	0.4
Release:	1
License:	GPL v.2
Group:		Applications
#Source0:	http://freedesktop.org/~david/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	3106ee5ae8640d82a805cb0f9c5bf34d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.31
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	hal-devel >= 0.5.5
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libtool
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Programs for mounting, unmounting and ejecting storage devices.

%package devel
Summary:	gnome-mount development files
Group:		Development
Requires:	pkgconfig

%description devel
This is the package containing gnome-mount development files.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
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
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/gnome-mount.schemas

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
