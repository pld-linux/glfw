Summary:	Free, portable framework for OpenGL application development
Summary(pl.UTF-8):	Wolnodostępny, przenośny szkielet do tworzenia aplikacji OpenGL
Name:		glfw
Version:	3.0.4
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/glfw/%{name}-%{version}.tar.bz2
# Source0-md5:	133a9faed6f1fbd527551a7e42aeb4f9
URL:		http://glfw.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	doxygen
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLFW is a free, Open Source, portable framework for OpenGL application
development. In short, it is a single library providing a powerful,
portable API for otherwise operating system specific tasks such as
opening an OpenGL window, and reading keyboard, mouse and joystick
input.

It also provides functions for reading a high precision timer,
accessing OpenGL extensions, creating and synchronizing threads,
reading textures from files and more.

GLFW is available for Windows, MacOS X, Unix-like systems such as
Linux and FreeBSD, and for AmigaOS and DOS.

%description -l pl.UTF-8
GLFW to wolnodostępny, mający otwarte źródła, przenośny szkielet do
tworzenia aplikacji OpenGL. W skrócie jest to pojedyncza biblioteka
udostępniająca potężne, przenośne API do zadań zależnych od systemu
operacyjnego, takich jak otwieranie okna OpenGL, odczyt wejścia z
klawiatury, myszy i joysticka.

Zawiera także funkcje do odczytu zegara o wysokiej rozdzielczości,
dostępu do rozszerzeń OpenGL, tworzenia i synchronizowania wątków,
odczytu tekstur z plików i innych zadań.

GLFW jest dostępny dla Windows, MacOS X, systemów uniksowych takich
jak Linux czy FreeBSD oraz dla AmigaOS i DOS-a.

%package devel
Summary:	Header files for GLFW library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GLFW
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLX-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXxf86vm-devel
Obsoletes:	glfw-static

%description devel
Header files for GLFW library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GLFW.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/{*.c,CMakeLists.txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING.txt README.md
%attr(755,root,root) %{_libdir}/libglfw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libglfw.so.3

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%attr(755,root,root) %{_libdir}/libglfw.so
%dir %{_includedir}/GLFW
%{_includedir}/GLFW/glfw3*.h
%{_pkgconfigdir}/glfw3.pc
%{_libdir}/cmake/glfw
%{_examplesdir}/%{name}-%{version}
