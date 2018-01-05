Name     : pygobject
Version  : 3.26.1
Release  : 9
URL      : https://download.gnome.org/sources/pygobject/3.26/pygobject-3.26.1.tar.xz
Source0  : https://download.gnome.org/sources/pygobject/3.26/pygobject-3.26.1.tar.xz
Summary  : Python bindings for GObject
Group    : Development/Tools
License  : LGPL-2.1
Requires: pygobject-python3
Requires: pygobject-python
Requires: pygobject-legacypython
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : py2cairo
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
PyGObject
=====
Original authors:   James Henstridge <james@daa.com.au>
Johan Dahlin <johan@gnome.org>

%package dev
Summary: dev components for the pygobject package.
Group: Development
Provides: pygobject-devel

%description dev
dev components for the pygobject package.

%package legacypython
Summary: legacypython components for the pygobject package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pygobject package.


%package python
Summary: python components for the pygobject package.
Group: Default
Requires: pygobject-python3
Requires: pygobject-legacypython

%description python
python components for the pygobject package.


%package python3
Summary: python3 components for the pygobject package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pygobject package.


%prep
%setup -q -n pygobject-3.26.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509104350

mkdir python2
pushd python2
CFLAGS="${CFLAGS:--O2 -fPIC -g -feliminate-unused-debug-types  -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wl,--copy-dt-needed-entries -Wno-error -Wl,-z -Wl,now -Wl,-z -Wl,relro -Wl,-z,max-page-size=0x1000 -ftree-vectorize -m64 -mtune=skylake -fasynchronous-unwind-tables -fno-omit-frame-pointer -Wp,-D_REENTRANT }" ; export CFLAGS ;
../configure --build=x86_64-generic-linux-gnu --host=x86_64-generic-linux-gnu \
        --target=x86_64-clr-linux-gnu \
        --program-prefix= \
        --prefix=/usr \
        --exec-prefix=/usr \
        --bindir=/usr/bin \
        --sbindir=/usr/bin \
        --sysconfdir=/etc \
        --datadir=/usr/share \
        --includedir=/usr/include \
        --libdir=/usr/lib64 \
        --libexecdir=/usr/libexec \
        --localstatedir=/var \
        --sharedstatedir=/usr/com \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --disable-static --disable-cairo --with-python=python2
make V=1  %{?_smp_mflags}
popd

mkdir python3
pushd python3
CFLAGS="${CFLAGS:--O2 -fPIC -g -feliminate-unused-debug-types  -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wl,--copy-dt-needed-entries -Wno-error -Wl,-z -Wl,now -Wl,-z -Wl,relro -Wl,-z,max-page-size=0x1000 -ftree-vectorize -m64 -mtune=skylake -fasynchronous-unwind-tables -fno-omit-frame-pointer -Wp,-D_REENTRANT }" ; export CFLAGS ;
../configure --build=x86_64-generic-linux-gnu --host=x86_64-generic-linux-gnu \
        --target=x86_64-clr-linux-gnu \
        --program-prefix= \
        --prefix=/usr \
        --exec-prefix=/usr \
        --bindir=/usr/bin \
        --sbindir=/usr/bin \
        --sysconfdir=/etc \
        --datadir=/usr/share \
        --includedir=/usr/include \
        --libdir=/usr/lib64 \
        --libexecdir=/usr/libexec \
        --localstatedir=/var \
        --sharedstatedir=/usr/com \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --disable-static --disable-cairo --with-python=python3
make  V=1  %{?_smp_mflags}
popd


%install
export SOURCE_DATE_EPOCH=1509104350
rm -rf %{buildroot}
pushd python2
%make_install
popd

pushd python3
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pygobject-3.0/pygobject.h
/usr/lib64/pkgconfig/pygobject-3.0.pc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
