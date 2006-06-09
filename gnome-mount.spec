Summary:	Programs for mounting, unmounting and ejecting storage devices
Summary(pl):	Programy do montowania, odmontowywania i wysuwania urz�dze� do przechowywania danych
Name:		gnome-mount
Version:	0.4
Release:	5
License:	GPL v.2
Group:		Applications
Source0:	http://freedesktop.org/~david/dist/%{name}-%{version}.tar.gz
# Source0-md5:	75f260ea6b0ec3c5e0af3c722fbd9568
Patch0:		%{name}-shortname.patch
Patch1:		%{name}-drive_mount.patch
Patch2:		%{name}-no_media.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gnome-keyring-devel >= 0.4.9
BuildRequires:	gtk+2-devel >= 2:2.9.2
BuildRequires:	hal-devel >= 0.5.7
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.15.1
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.15.1
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	nautilus >= 2.15.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Programs for mounting, unmounting and ejecting storage devices.

%description -l pl
Programy do montowania, odmontowywania i wysuwania urz�dze� do
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
%patch1	-p0
%patch2 -p0

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
%{_sysconfdir}/gconf/schemas/gnome-mount.schemas

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
