%define name banshee-mirage
%define oname mirage
%define version 0.1
%define release %mkrel 2

Summary: Automatic playlist generator for Banshee based on similarity
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}_%{version}-1.tar.bz2
Source1: Banshee.Plugins.Mirage.dll.config
Patch: mirage-flac.patch
License: GPLv2
Group: Sound
Url: http://hop.at/mirage/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: banshee
BuildRequires: mono-devel
BuildRequires: libfftw-devel
BuildRequires: sqlite3-devel
Requires: sox
Requires: mpg123
Requires: vorbis-tools
Suggests: flac
Suggests: faad2


%description

Mirage is a ready-to-try implementation of the latest reseach in
automatic playlist generation and music similarity. Mirage analyzes
your music collection and computes similarity models for each song, so
it is then able to automatically compute playlists. Playlist
generation was implemented as a plugin for the popular GNOME audio
player Banshee. 

%prep
%setup -q -n %oname
%patch -p1 -b .flac

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cp %SOURCE1 %buildroot%_libdir/banshee/Banshee.Plugins/Banshee.Plugins.Mirage.dll.config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/mirage-decoder
%_libdir/banshee/Banshee.Plugins/Banshee.Plugins.Mirage.dll*
