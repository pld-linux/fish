Summary:	fish - A friendly interactive shell
Summary(pl):	fish - przyjazna interaktywna pow³oka
Name:		fish
Version:	1.21.12
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://roo.no-ip.org/fish/files/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	77fb4fd2ff5043acf6935f079250ba60
URL:		http://roo.no-ip.org/fish/
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendlieness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%description -l pl
fish jest pow³ok± nastawion± na interaktywne u¿ywanie. Jego cech± jest
przyjazne nastawienie dla u¿ytkownika. Sk³adnia jêzyka jest prosta ale
nie jest zgodna z innymi jêzykami pow³oki.

%prep
%setup -q

%build
CFLAGS="-I /usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%doc %{_docdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish_inputrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fish.d/*.fish
%{_mandir}/man1/*.1*
