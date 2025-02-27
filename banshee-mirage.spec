%define name banshee-mirage
%define oname mirage
%define version 0.6.0
%define release %mkrel 2

Summary: Automatic playlist generator for Banshee based on similarity
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://hop.at/mirage/download/%{oname}-%{version}.tar.gz
License: GPLv2+
Group: Sound
Url: https://hop.at/mirage/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: banshee >= 1.4
BuildRequires: gnome-sharp2-devel
BuildRequires: mono-devel
BuildRequires: libfftw-devel
BuildRequires: sqlite3-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libsamplerate-devel
BuildRequires: libtool
BuildRequires: intltool
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
%setup -q -n %oname-%version

%build
%configure2_5x --disable-dependency-tracking
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/libmirageaudio.*a
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%_libdir/banshee-1/Extensions/Banshee.Mirage.dll*
%_libdir/banshee-1/Extensions/Mirage.dll*
%_libdir/libmirageaudio.so
