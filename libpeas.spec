%define api 1.0
%define major 0
%define libname %mklibname peas %major
%define libnamegtk %mklibname peas-gtk %major
%define develname %mklibname -d peas

%define build_gtk3 1

Name:           libpeas
Version:        0.9.0
Release:        %mkrel 2
Summary:        Library for plugin handling
Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.gnome.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0: libpeas-0.9.0-new-seed.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
%if %build_gtk3
BuildRequires:  gtk+3-devel
%endif
BuildRequires:  gobject-introspection-devel >= 0.10.1
BuildRequires:  python-gobject-devel >= 2.28
BuildRequires:  seed-devel >= 2.28.0
BuildRequires:  vala-devel >= 0.11.1
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

%package -n %{libnamegtk}
Summary:	Library plugin handling UI part
Group:		System/Libraries
Requires: %name-data >= %version

%description -n %{libnamegtk}
This is GNOME's plugin handling library - user interface part.

%package -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libnamegtk} = %{version}-%{release}
Provides:	%name-devel = %version-%release

%description -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files data -f %name.lang
%defattr(-,root,root,-)
%_datadir/icons/hicolor/*/actions/*

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS
%{_libdir}/libpeas-%api.so.%{major}*
%{_libdir}/girepository-1.0/Peas-%api.typelib
%_libdir/%name-%api/loaders/libcloader.*
%_libdir/%name-%api/loaders/libpythonloader.*
%_libdir/%name-%api/loaders/libseedloader.*

%files -n %libnamegtk
%defattr(-,root,root,-)
%{_libdir}/libpeas-gtk-%api.so.%{major}*
%{_libdir}/girepository-1.0/PeasGtk-%api.typelib

%files -n %develname
%defattr(-,root,root,-)
%doc ChangeLog
%_bindir/peas-demo
%_libdir/peas-demo
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}-%api.pc
%{_libdir}/pkgconfig/%{name}-gtk-%api.pc
%{_datadir}/gtk-doc/html/%name
%{_datadir}/gir-1.0/Peas-%api.gir
%{_datadir}/gir-1.0/PeasGtk-%api.gir
