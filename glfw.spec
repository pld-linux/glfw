Summary:	Free, portable framework for OpenGL application development
Summary(pl):	Wolnodostêpny, przeno¶ny szkielet do tworzenia aplikacji OpenGL
Name:		glfw
Version:	2.5.0
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/glfw/%{name}-%{version}.tar.bz2
# Source0-md5:	c6dffefbfbe4415c915851b09e76edd9
Patch0:		%{name}-opt.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-pic.patch
URL:		http://glfw.sourceforge.net/
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

%description -l pl
GLFW to wolnodostêpny, maj±cy otwarte ¼ród³a, przeno¶ny szkielet do
tworzenia aplikacji OpenGL. W skrócie jest to pojedyncza biblioteka
udostêpniaj±ca potê¿ne, przeno¶ne API do zadañ zale¿nych od systemu
operacyjnego, takich jak otwieranie okna OpenGL, odczyt wej¶cia z
klawiatury, myszy i joysticka.

Zawiera tak¿e funkcje do odczytu zegara o wysokiej rozdzielczo¶ci,
dostêpu do rozszerzeñ OpenGL, tworzenia i synchronizowania w±tków,
odczytu tekstur z plików i innych zadañ.

GLFW jest dostêpny dla Windows, MacOS X, systemów uniksowych takich
jak Linux czy FreeBSD oraz dla AmigaOS i DOS-a.

%package devel
Summary:	Header files for GLFW library
Summary(pl):	Pliki nag³ówkowe biblioteki GLFW
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLX-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXxf86vm-devel

%description devel
Header files for GLFW library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GLFW.

%package static
Summary:	Static GLFW library
Summary(pl):	Statyczna biblioteka GLFW
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GLFW library.

%description static -l pl
Statyczna biblioteka GLFW.

%prep
%setup -q -n %{name}-2.5
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CC="%{__cc}" \
LFLAGS="%{rpmldflags}" \
INCS= \
OPT="%{rpmcflags}" \
./compile.sh

%{__make} -C lib/x11 -f Makefile.x11 \
	LFLAGS_LINK="%{rpmldflags} -lGL -lXxf86vm -lX11 -lpthread" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/GL,%{_examplesdir}/%{name}-%{version}}

libtool --mode=install install lib/x11/libglfw.la $RPM_BUILD_ROOT%{_libdir}
install include/GL/glfw.h $RPM_BUILD_ROOT%{_includedir}/GL
install examples/{*.c,*.tga,Makefile.x11} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.txt readme.html images
%attr(755,root,root) %{_libdir}/libglfw.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/*.pdf
%attr(755,root,root) %{_libdir}/libglfw.so
%{_libdir}/libglfw.la
%{_includedir}/GL/glfw.h
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libglfw.a
