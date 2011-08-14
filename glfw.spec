Summary:	Free, portable framework for OpenGL application development
Summary(pl.UTF-8):	Wolnodostępny, przenośny szkielet do tworzenia aplikacji OpenGL
Name:		glfw
Version:	2.7.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/glfw/%{name}-%{version}.tar.bz2
# Source0-md5:	bb4f33b43e40f8cd3015a653dca02ed1
Patch0:		%{name}-opt.patch
Patch1:		%{name}-libdir.patch
URL:		http://glfw.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
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
Requires:	xorg-lib-libXxf86vm-devel

%description devel
Header files for GLFW library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GLFW.

%package static
Summary:	Static GLFW library
Summary(pl.UTF-8):	Statyczna biblioteka GLFW
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GLFW library.

%description static -l pl.UTF-8
Statyczna biblioteka GLFW.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CC="%{__cc}" \
LFLAGS="%{rpmldflags}" \
CFLAGS="%{rpmcflags}" \
sh ./compile.sh

%{__make} -C lib/x11 -f Makefile.x11 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C lib/x11 -f Makefile.x11 dist-install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

install examples/{*.c,*.tga,Makefile.x11} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING.txt readme.html
%attr(755,root,root) %{_libdir}/libglfw.so

%files devel
%defattr(644,root,root,755)
%doc docs/{Reference,UsersGuide}.pdf
%{_includedir}/GL/glfw.h
%{_pkgconfigdir}/libglfw.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libglfw.a
