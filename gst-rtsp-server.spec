%define api 0.10
%define major 0
%define libname %mklibname gstrtspserver %{api} %{major}
%define develname %mklibname -d gstrtspserver
%define oname gst-rtsp

Summary:	RTSP server library for the GStreamer framework
Name:		gst-rtsp-server
Version:	0.10.8
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://people.freedesktop.org/~wtay/
Source0:  	http://people.freedesktop.org/~wtay/%{oname}-%{version}.tar.bz2
Patch0:		gst-rtsp-pygobject.patch
Patch1:		gst-rtsp-0.10.6-py-link.patch

BuildRequires:	gtk-doc
BuildRequires:	gettext-devel
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gst-python-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(python)

%description
RTSP server based on GStreamer.

%package -n %{libname}
Summary:	RTSP server library for the GStreamer framework
Group:		System/Libraries

%description -n %{libname}
RTSP server based on GStreamer.

%package -n %develname
Summary:	RTSP server library for the GStreamer framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}
Provides:	libgstrtspserver-devel = %{version}-%{release}

%description -n %{develname}
RTSP server based on GStreamer.

%package -n python-rtspserver
Group: Development/Python
Summary: Python bindings for the RTSP-Server
Requires: gstreamer0.10-python

%description -n python-rtspserver
This is the Python binding for GStreamer's RTSP Server.

%prep
%setup -qn %oname-%{version}
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--with-pic \
	--enable-maintainer-mode \
	--enable-gtk-doc 
%make

%install
%makeinstall_std

%files -n %{libname}
%doc README AUTHORS
%{_libdir}/libgstrtspserver-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/GstRtspServer-%{api}.typelib

%files -n %{develname}
%{_libdir}/libgstrtspserver-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/gstreamer-%{api}/gst/rtsp-server
%{_datadir}/gir-1.0/GstRtspServer-%{api}.gir
%{_datadir}/gtk-doc/html/gst-rtsp-server-0.10
%{_datadir}/vala/vapi/%{name}-%{api}.deps
%{_datadir}/vala/vapi/%{name}-%{api}.vapi

%files -n python-rtspserver
%{py_platsitedir}/gst-%{api}/gst/rtspserver.so
%{_datadir}/gst-rtsp



%changelog
* Tue May 22 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.10.8-1
+ Revision: 800109
- new version 0.10.8
- cleaned up spec

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2011.0
+ Revision: 622535
- new version
- bump vala and gst deps
- enable introspection
- update file list

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 0.10.6-2mdv2011.0
+ Revision: 599416
- fix py linking

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2011.0
+ Revision: 581244
- new version
- patch for new vala
- update file list for new vala

* Fri Nov 06 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.5-1mdv2010.1
+ Revision: 462059
- update to new version 0.10.5

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2010.0
+ Revision: 410207
- update to new version 0.10.4

* Sun May 17 2009 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdv2010.0
+ Revision: 376631
- new version
- remove pkgconfig workaround

* Sat May 16 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-2mdv2010.0
+ Revision: 376451
- fix version in pkgconfig file

* Fri May 15 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2010.0
+ Revision: 376212
- update build deps
- update to new version 0.10.2

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 0.10.1.0-1mdv2009.1
+ Revision: 336579
- new version
- fix URL

* Mon Jan 26 2009 Götz Waschk <waschk@mandriva.org> 0.10.0.1-0.20090124.1mdv2009.1
+ Revision: 333758
- new snapshot
- remove binary, add library and python packages
- update build deps
- fix version number

* Sat Jan 03 2009 Emmanuel Andry <eandry@mandriva.org> 0.20090103-0.1mdv2009.1
+ Revision: 323881
- BR gettext-devel
- import gst-rtsp-server


