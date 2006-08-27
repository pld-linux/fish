Summary:	fish - A friendly interactive shell
Summary(pl):	fish - przyjazna interaktywna pow�oka
Name:		fish
Version:	1.6
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://roo.no-ip.org/fish/files/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	089cb13572deeac26c7d217ad75384e7
Patch0:		%{name}-Makefile.patch
URL:		http://roo.no-ip.org/fish/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendlieness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%description -l pl
fish jest pow�ok� nastawion� na interaktywne u�ywanie. Jego cech� jest
przyjazne nastawienie dla u�ytkownika. Sk�adnia j�zyka jest prosta ale
nie jest zgodna z innymi j�zykami pow�oki.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="-I /usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%doc %{_docdir}/%{name}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
