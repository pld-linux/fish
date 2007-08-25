Summary:	fish - A friendly interactive shell
Summary(pl.UTF-8):	fish - przyjazna interaktywna powłoka
Name:		fish
Version:	1.22.3
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.fishshell.org/files/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	016a5944861ea48e363521c240834415
Patch0:		%{name}-link.patch
URL:		http://fishshell.org/
BuildRequires:	autoconf
BuildRequires:	doxygen
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	man-whatis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendlieness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%description -l pl.UTF-8
fish jest powłoką nastawioną na interaktywne używanie. Jego cechą jest
przyjazne nastawienie dla użytkownika. Składnia języka jest prosta ale
nie jest zgodna z innymi językami powłoki.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="-I/usr/include/ncurses"
%{__autoconf}
%{__autoheader}
%configure \
	--docdir=/docs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT/docs docs

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_sysconfdir}/fish
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish/config.fish
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish/fish_inputrc
%{_mandir}/man1/*.1*
