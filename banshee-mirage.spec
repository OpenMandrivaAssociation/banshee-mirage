%define name banshee-mirage
%define oname mirage
%define version 0.2
%define release %mkrel 1

Summary: Automatic playlist generator for Banshee based on similarity
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}_%{version}.tar.gz
License: GPLv2+
Group: Sound
Url: http://hop.at/mirage/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: banshee
BuildRequires: mono-devel
BuildRequires: libfftw-devel
BuildRequires: sqlite3-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libsamplerate-devel
Suggests: gstreamer0.10-faad
Suggests: gstreamer0.10-plugins-ugly
Suggests: gstreamer0.10-flac
Suggests: gstreamer0.10-plugins-good

%description
Mirage is a ready-to-try implementation of the latest reseach in
automatic playlist generation and music similarity. Mirage analyzes
your music collection and computes similarity models for each song, so
it is then able to automatically compute playlists. Playlist
generation was implemented as a plugin for the popular GNOME audio
player Banshee. 

%prep
%setup -q -n %oname

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
#gw wrong dir
%if %_lib != lib
mv  %buildroot%_prefix/lib/banshee/*  %buildroot%_libdir/banshee/
%endif
rm -f %buildroot%_libdir/banshee/libmirageaudio.*a
%find_lang Mirage

%clean
rm -rf $RPM_BUILD_ROOT

%files -f Mirage.lang
%defattr(-,root,root)
%_libdir/banshee/Banshee.Plugins/Banshee.Plugins.Mirage.dll*
%_libdir/banshee/Mirage.dll*
%_libdir/banshee/libmirageaudio.so
