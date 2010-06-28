%define api 1.0
%define major 0
%define libname %mklibname peas %major
%define libnameui %mklibname peasui %major
%define develname %mklibname -d peas

%define build_gtk3 1

Name:           libpeas
Version:        0.5.1
Release:        %mkrel 1
Summary:        Library for plugin handling

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.gnome.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
%if %build_gtk3
BuildRequires:  gtk+3-devel
%else
BuildRequires:  gtk+2-devel
%endif
BuildRequires:  gobject-introspection-devel
BuildRequires:  python-gobject-devel
BuildRequires:  seed-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool

%description
This is GNOME's plugin handling library.

%package data
Summary:	Library for plugin handling - data files
Group:		System/Libraries

%description data
This is GNOME's plugin handling library - data files

%package -n %{libname}
Summary:	Library plugin handling
Group:		System/Libraries
Requires: %name-data >= %version

%description -n %{libname}
This is GNOME's plugin handling library.

%package -n %{libnameui}
Summary:	Library plugin handling UI part
Group:		System/Libraries
Requires: %name-data >= %version

%description -n %{libnameui}
This is GNOME's plugin handling library - user interface part.

%package -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libnameui} = %{version}-%{release}
Provides:	%name-devel = %version-%release

%description -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%check

%files data -f %name.lang
%defattr(-,root,root,-)
%_datadir/icons/hicolor/*/actions/*

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS
#NEWS README
%{_libdir}/libpeas-%api.so.%{major}*
%{_libdir}/girepository-1.0/Peas-%api.typelib
%_libdir/%name-%api/loaders/libcloader.*
%_libdir/%name-%api/loaders/libpythonloader.*
%_libdir/%name-%api/loaders/libseedloader.*

%files -n %libnameui
%defattr(-,root,root,-)
%{_libdir}/libpeasui-%api.so.%{major}*
%{_libdir}/girepository-1.0/PeasUI-%api.typelib

%files -n %develname
%defattr(-,root,root,-)
%doc ChangeLog
%_bindir/peas-demo
%_libdir/peas-demo
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}-%api.pc
%{_libdir}/pkgconfig/%{name}ui-%api.pc
%{_datadir}/gtk-doc/html/%name
%{_datadir}/gir-1.0/Peas-%api.gir
%{_datadir}/gir-1.0/PeasUI-%api.gir
